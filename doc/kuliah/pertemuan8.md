**Rangkuman Pertemuan 8 Sistem Informasi Geografis**

<p align="center">
  <img src="../../img/mapproxy.png" width="400px">
</p>

Latar Belakang
MAP PROXY ,berfungsi untuk menampung hasil gambar dari mapserver agar konsumsi komputasi bisa direduksi.

Pembahasan
**Pengertian MapProxy**

MapProxy (mapproxy.org) adalah open source ubin geospasial proxy yang mendukung proyeksi ulang. Awalnya dikembangkan oleh Omniscale Mapproxy adalah server proxy python untuk gambar geospasial. Hal ini dapat membaca data dari WMS, ubin, mapserver dan mapnik, dan cache dan melayani data bahwa sebagai WMS, WMTS, TMS dan KML. Hal ini juga dapat melakukan reprojections antara berbagai sistem koordinat referensi

**Install MapProxy**

- Ketikkan &quot;#install python-pip dan python-dev&quot;

- Lalu &quot;#pip install mapproxy&quot;

- Setelah itu ketikkan &quot;#install Vwsqi&quot;

- Tunggu hingga proses selesai.

**Konfigurasi MapProxy**  Ada dua file konfigurasi yang digunakan oleh MapProxy.

mappproxy.yaml

Ini adalah konfigurasi utama MapProxy. Ini mengkonfigurasi semua aspek server: Yang server harus dimulai, di mana berasal data dari, apa yang harus di-cache.

seed.yaml

File ini adalah konfigurasi untuk alat mapproxy-benih. Lihat penyemaian dokumentasi untuk informasi lebih lanjut.

Konfigurasi ini menggunakan format YAML. Wikipedia berisi pengenalan yang baik untuk YAML. Konfigurasi MapProxy dikelompokkan menjadi beberapa bagian, masing-masing mengkonfigurasi aspek yang berbeda dari MapProxy. Ini adalah bagian berikut:

• GLOBALS: Internal dari MapProxy dan nilai-nilai default yang digunakan dalam bagian konfigurasi lainnya.

• Layanan: Layanan MapProxy penawaran, misalnya WMS atau TMS.

• sumber: Tentukan mana MapProxy dapat mengambil data baru.

• cache: Konfigurasi cache internal.

• lapisan: Konfigurasi lapisan yang MapProxy menawarkan. Setiap lapisan dapat terdiri dari beberapa sumber dan cache.

• grid: Tentukan grid yang menggunakan MapProxy untuk menyelaraskan gambar cache.

Urutan bagian tidak penting, sehingga Anda dapat mengatur dengan cara Anda.

Untuk membuat satu set baru file konfigurasi untuk MapProxy panggilan:

mapproxy-util create -t base-config mymapproxy

Ini akan membuat direktori mymapproxy dengan contoh konfigurasi minimal (mapproxy.yaml dan seed.yaml) dan dua file konfigurasi contoh lengkap (full\_example.yaml dan full\_seed\_example.yaml).

Lihat dokumentasi konfigurasi untuk informasi lebih lanjut. Dengan konfigurasi default data cache akan ditempatkan di subdirektori cache\_data.

**Untuk memulai server tes:**

cd mymapproxy mapproxy-util serve-develop mapproxy.yaml

Sudah ada lapisan tes dikonfigurasi yang mendapatkan data dari Omniscale OpenStreetMap WMS. Jangan ragu untuk menggunakan layanan ini untuk pengujian. MapProxy dilengkapi dengan layanan demo yang berisi daftar WMS semua dikonfigurasi dan lapisan TMS. Anda dapat mengakses layanan yang di http: // localhost: 8080 / demo /.

Penutup

Kesimpulan
MAP PROXY ,berfungsi untuk menampung hasil gambar dari mapserver agar konsumsi komputasi bisa direduksi, mappproxy.yaml Ini adalah konfigurasi utama MapProxy. Ini mengkonfigurasi semua aspek server: Yang server harus dimulai, di mana berasal data dari, apa yang harus di-cache.
Saran
Selanjutnya untuk mendalami materi Konfigurasi Map Proxy dengan membaca sumber-sumber yang tersedia di buku maupun internet, dan melakukan praktikum mandiri.

* Nama : Gilang Romadhanu Tartila
* NPM : 1144033
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Mata Kuliah : Sistem Informasi Geografis

Link Github : https://github.com/gilangtartila99/SistemInformasiGeografis2016

Referensi : 
1. https://id.wikipedia.org/wiki/MapProxy

Scan Plagiarisme
1. smallseotools - Link https://drive.google.com/open?id=0B5gySyqZ4GGoeGh6MG44UTVldFE
2. searchenginereport - Link https://drive.google.com/open?id=0B5gySyqZ4GGoblNYVk9GWF9MTzQ