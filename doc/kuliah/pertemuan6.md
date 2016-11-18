**Rangkuman Pertemuan 6 Sistem Informasi Geografis**

<p align="center">
  <img src="../../img/shapes.png" width="400px">
</p>

Latar Belakang Masalah

Pada sistem informasi geografis terdapat shapefile, shapefile disini kita berupa data geometri yang dapat ditambahkan, diedit, dihapus dan dilihat

1. Bagaimana cara create shapefile?
2. Bagaimana cara edit shapefile?
3. Bagaimana cara hapus shapefile?
4. Bagaimana cara menampilkan shapefile?

Cara membuat data geometri shapefile adalah sebagai berikut:

- --Buka python di command prompt
- --import shapefile
- --sf = shapefile.Writer(shapeType=1)
- --sf.shapeType -&gt; untuk mengecek
- --sf.field(&#39;NAMA&#39;,&#39;C&#39;,&#39;40&#39;)
- --sf.field(&#39;PEMILIK&#39;,&#39;C&#39;,&#39;40&#39;)
- --sf.record(&#39;WARTEG&#39;,&#39;Jajang Kusendar&#39;)
- --sf.point(10,10,0,0) -&gt; disini point bisa diganti line atau polygon sesuai keinginan
- --sf.save(&#39;warteg.shp&#39;) -&gt; untuk menyimpan

Cara Mengedit data geometri shapefile adalah sebagai berikut:

- --Buka python di command prompt
- --import shapefile
- --sf = shapefile.Editor(shapefile=&#39;warteg.shp&#39;)
- --sf.point(19,19,0,0)
- --sf.record(&#39;Warung Padang&#39;,&#39;Ucok&#39;)
- --sf.save(&#39;warteg&#39;)

Cara menghapus data geometri shapefile adalah sebagai berikut:

- --Buka python di command prompt
- --import shapefile
- --e = shapefile.Editor(&#39;warteg.shp&#39;)
- --e.shape(1) -&gt; record ke berapa
- --e.delete(1)
- --e.save(&#39;warteg&#39;)

Cara menampilkan data geometri shapefile adalah sebagai berikut:

- --Buka python di command prompt
- --import shapefile
- --sf = shapefile.Reader(&#39;warteg.shp&#39;)
- --sf.record() -&gt; semua record
- --sf.record(0) -&gt; record ke 1
- --sf.record(1) -&gt; record ke 2
- --sf.shapes()(0).points -&gt; menampilkan

Penutup

Kesimpulan
Dari pernyataan diatas dapat disimpulkan bahwa dalam data geometri shapefile dapat melakukan penambahan , pengeditan, penghapusan dan penampilan data geometri shapefile dengan mudah menggunakan python

Saran
Sebaiknya kita mempelajari cara membuat, mengedit, menghapus dan menampilkan data shapefile karena mudah dan hanya menggunakan pemrograman python

* Nama : Gilang Romadhanu Tartila
* NPM : 1144033
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Mata Kuliah : Sistem Informasi Geografis

Link Github : https://github.com/gilangtartila99/SistemInformasiGeografis2016

Referensi : 
1. https://en.wikipedia.org/wiki/Shapefile

Scan Plagiarisme
1. smallseotools - Link https://drive.google.com/open?id=0B5gySyqZ4GGodEZpS2UtOVNESGM
2. searchenginereport - Link https://drive.google.com/open?id=0B5gySyqZ4GGoRXpsaTdCSld5YW8