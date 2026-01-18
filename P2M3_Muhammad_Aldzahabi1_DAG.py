from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2
from elasticsearch import Elasticsearch, helpers
import re


# Default Arguments 
default_args = {
    'owner': 'Aldza',
    'start_date': datetime(2024, 11, 1),
    'retries': 1
}

# EXTRACT
def extract():
    conn = psycopg2.connect(
        host="postgres",
        port="5432",
        database="database", 
        user="airflow",
        password="airflow"
    )

    df_raw = pd.read_sql("SELECT * FROM table_m3", conn)
    df_raw.to_csv(
        '/opt/airflow/dags/P2M3_Muhammad_Aldzahabi_data_raw.csv',
        index=False
    )

    conn.close()
    print(f"Berhasil extract {len(df_raw)} rows dari PostgreSQL")

# TRANSFORM 
def transform():
    df = pd.read_csv('/opt/airflow/dags/P2M3_Muhammad_Aldzahabi_data_raw.csv')

    # 1. REMOVE DUPLICATES
    initial_count = len(df)
    df = df.drop_duplicates()
    print(f"Duplicates removed: {initial_count - len(df)}")

    # 2. COLUMN NAME NORMALIZATION 
    def normalize_column_name(col):
        col = col.lower()   
        # 1. Ganti karakter non-alfanumerik dengan underscore
        col = re.sub(r'[^\w]', '_', col)
        
        # 2. PERBAIKAN DI SINI: Ganti underscore berlebih (_+) menjadi satu underscore saja (_)
        col = re.sub(r'_+', '_', col).strip('_')
        
        return col
    # menerapkan ke semua kolom
    df.columns = [normalize_column_name(c) for c in df.columns]

    print("Normalized columns:", df.columns.tolist())

    # 3. HANDLE MISSING VALUES
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('Unknown')
        else:
            df[col] = df[col].fillna(0)

    # 4. DATE PARSING & SORTING
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')

        # saya menambahkan @timestamp karena jika ingin ke elasticsearch dan kibana ketika date sudah di ganti ke datetime, akan masih object tipe datanya
        df['@timestamp'] = df['date']

        df = df.sort_values(by='@timestamp', ascending=True)
        df = df.reset_index(drop=True)

    df.to_csv(
        '/opt/airflow/dags/P2M3_Muhammad_Aldzahabi_data_clean.csv',
        index=False
    )

    print("Data clean berhasil disimpan")

# LOAD 
def load():
    df = pd.read_csv('/opt/airflow/dags/P2M3_Muhammad_Aldzahabi_data_clean.csv')
    es = Elasticsearch("http://elasticsearch:9200")

    if not es.indices.exists(index="aldzahabi"):
        es.indices.create(
            index="aldzahabi",
            body={
                "mappings": {
                    "properties": {
                        "@timestamp": {"type": "date"}
                    }
                }
            }
        )

    actions = []

    for _, r in df.iterrows():
        actions.append({
            "_index": "aldzahabi",
            "_source": r.to_dict()
        })


    helpers.bulk(es, actions)
    print("Data berhasil dikirim ke Elasticsearch")

# DAG
with DAG(
    dag_id='aldzahabi',
    default_args=default_args,
    description='ETL Pipeline PostgreSQL to Elasticsearch',
    schedule_interval='@daily',
    catchup=False
) as dag:

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load
    )

    extract_task >> transform_task >> load_task