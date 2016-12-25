**Rangkuman Pertemuan 7 Sistem Informasi Geografis**

<p align="center">
  <img src="../../img/mapserver.png" width="400px">
</p>

Latar Belakang

1. Apa yang dimaksud dengan Map Server?
2. Bagaimana cara install Map Server?
3. Apa yang dimaksud Map Proxy?
4. Bagaimana cara install Map Proxy?
5. Bagaimana cara testing?

Map Server adalah aplikasi untuk mengubah data vektor geospasial menjadi gambar untuk ditampilkan sebagai web service

Cara install
1. Jika tidak ada centos maka jalankan saja di virtual box, ISO centos dan virtual box ada di halaman download
2. Setelah itu pastikan koneksi jaringan virtual box bisa diakses dari komputer host
3. Dicentos buka terminal, login sebagai root
4. #install mapserver
5. Selesai

Map Proxy adalah program yang berfungsi untuk menampung hasil gambar dari map server agar konsumsi komputer bisa di reduksi

Cara Install
1. Install python-pip dan python-dev
2. #install python-pip dan python-dev
3. pip Install mapproxy
4. #install mapproxy
5. Install Vwsqi
6. #install Vwsqi

Testing
1. Download peta Indonesia beserta map proxy konfigurasinya di Halaman Download simpan di folder/var
2. Jalankan map proxy dengan cara ketik perintah #vwsqi map proxy ini
3. Peta seudah bisa diakses di browser localhost

Penutup
Kesimpulan
Dari pernyataan diatas dapat disimpulkan bahwa dalam konfigurasi map server dan map proxy cukup mudah dengan menggunakan python karena pluginnya sudah tersedia

Saran
Sebaiknya kita sedikit mempelajari lebih dalam tentang map server dan map proxy agar lebih mengerti apa itu map proxy dan map server

* Nama : Gilang Romadhanu Tartila
* NPM : 1144033
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Mata Kuliah : Sistem Informasi Geografis

Link Github : https://github.com/gilangtartila99/SistemInformasiGeografis2016

Referensi : 
1. https://id.wikipedia.org/wiki/MapServer

Scan Plagiarisme
1. smallseotools - Link https://drive.google.com/open?id=0B5gySyqZ4GGoeGh6MG44UTVldFE
2. searchenginereport - Link https://drive.google.com/open?id=0B5gySyqZ4GGoblNYVk9GWF9MTzQ