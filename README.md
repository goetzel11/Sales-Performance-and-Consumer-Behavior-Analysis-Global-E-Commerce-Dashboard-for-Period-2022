# Judul Project
```
"Sales Performance and Consumer Behavior Analysis: Global E-Commerce Dashboard for Period 2022" 
```
## Repository Outline
`Bagian ini menjelaskan secara singkat konten/isi dari file yang dipush ke repository`

Contoh:
```
1. P2M3_Muhammad_Aldzahabi_Conceptual.txt
    - Basic knowledge NoSQL
2. P2M3_Muhammad_Aldzahabi_DAG_graph.png
    - Berisi alur ETL yang diautomsi dengan airflow 
3. P2M3_Muhammad_Aldzahabi_Ddl.txt
    - QUerry untuk create table dan insert value ke postgreSQL
4. P2M3_Muhammad_Aldzahabi_GX.ipynb
    - great expectation yang berisi validasi data setelah proses ETL
5. P2M3_Muhammad_Aldzahabi1_DAG.py
    - berisi syntax DAG untuk melakukan extraksi data dari data source (postgresSQL) dilanjut dengan transformasi data dan load data ke warehouse data base (elasticsearch)
6. P2M3_Muhammad_Aldzahabi_data_raw.txt
    - MErupakan data mentah dari ekstraksi postgreSQL
7. P2M3_Muhammad_Aldzahabi_clean_raw.txt
    - Merupakan data hasil transformasi yang sudah siap dimasukkan ke server warehouse database
8. Images
    - berisi kumpulan visualisasi untuk analisis
```

## Problem Background
```
Sebuah perusahaan e-commerce fashion global sedang mengevaluasi performa operasional dan profitabilitasnya sepanjang tahun 2022 untuk menentukan strategi ekspansi di tahun berikutnya. Perusahaan memiliki dataset transaksi yang mencakup berbagai atribut seperti brand, kategori produk, gender, lokasi negara, hingga metode pembayaran. Namun, manajemen menghadapi tantangan berupa fluktuasi pendapatan mingguan yang sangat tajam, di mana terdapat kesenjangan besar antara periode puncak di bulan Juli dan titik terendah di bulan Mei. Selain itu, dominasi brand tertentu seperti Nike dan ketergantungan pada metode pembayaran konvensional (COD) di beberapa kategori produk menimbulkan pertanyaan mengenai stabilitas dan efisiensi model bisnis saat ini. Laporan ini disusun untuk memberikan analisis mendalam mengenai kelayakan strategi pasar dan efektivitas operasional perusahaan agar keputusan berbasis data (data-driven) dapat diambil guna meningkatkan ROI dan stabilitas pendapatan global.
```

## Project Output
``` 
Proyek ini menghasilkan dashboard visualisasi komprehensif yang berfungsi sebagai instrumen audit untuk menilai kelayakan investasi perusahaan, dengan capaian sebagai berikut:

Valuasi Performa Finansial: Dashboard menyajikan bukti total pendapatan sebesar $193,103.07 selama tahun 2022 sebagai basis perhitungan potensi imbal hasil investasi (ROI).

Analisis Kekuatan Pasar & Brand: Memberikan gambaran dominasi Nike >$65,000 dan loyalitas tinggi pada segmen Wanita 40.86% sebagai indikator stabilitas pangsa pasar perusahaan.

Pemetaan Risiko Geografis: Menyediakan data sebaran profitabilitas global yang stabil, terutama di Japan 16.36% dan Canada 15.98%, guna meminimalisir risiko ketergantungan pada satu wilayah saja.

Evaluasi Efisiensi Operasional: Mengidentifikasi fluktuasi penjualan mingguan dan efektivitas metode pembayaran digital (Wallet/Card) dibandingkan COD sebagai pertimbangan efisiensi arus kas bagi investor.
```

## Data
```
Dataset berisi data penjualan Penjualan product fashion yang terdiri dari 11 kolom didapatkan dari kaggle dengan
    URL = https://www.kaggle.com/datasets/atharvasoundankar/sneakers-and-streetwear-sales-2022
dengan rincian sebagai berikut:
    Date            : Tanggal dari setiap transaksi
    Product Name    : Nama-nama dari setiap produk
    Product Type    : Tipe-tipe dari produk
    Brand           : Brand yang tersedia/terjual 
    Gender          : Jenis Kelamin pembeli
    Category        : Kategori dari setiap produk dan Brand
    Country         : Asal negara dari setiap transaksi
    Quantity        : Jumlah Unit yang terjual
    Unit Price ($)  : Harga dari setiap unit 
    Amount ($)      : ROI atau jumlah Price x Quantity
    
```

## Method
```
Sebelum dilakukan analisis dilakukan
- extraksi data dari postgree sebagai source  
- transformasi guna membersihkan dari noise dan menyesuaikan tipe data 
- load data ke elasticsearch sebagai data warehouse
- validasi data dengan great expectation untuk QC
- visualisasi data dengan kibana sesuai kebutuhan analisis
```

## Stacks
```
bahasa pemrogaman
    - python
    - SQL
library
    - pandas
    - psycopg2
    - datetime
    - airflow (DAG)
    - airflow.operators.python (PythonOperator)
    - elastchsearch (Elasticsearch, helpers)
    - csv
    - re
container
    - docker
database
    - postgresSQL
    - elasticsearch
orchestractor
    - airflow
visualization
    - kibana
```

## Reference
```
URL dataset = https://www.kaggle.com/datasets/atharvasoundankar/sneakers-and-streetwear-sales-2022
```



