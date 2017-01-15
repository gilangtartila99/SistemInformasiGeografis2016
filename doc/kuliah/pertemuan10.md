**Rangkuman Pertemuan 10 Sistem Informasi Geografis**

<p align="center">
  <img src="../../img/overlay1.jpg" width="400px">
</p>

Resume Pertemuan 10 Sistem Informasi Geografis

Latar belakang

1. Apa itu Open Layer?
2. Apa yang dimaksud Marker?
3. Bagaimana cara menampilkan marker menggunakan Open Layer?

Open Layer adalah library javascript murni untuk menampilkan data peta di berbagai browser, tanpa server side dependencies. Open Layer mengimplementasikan javascript API untuk membangun rich web-based geographic application yang mirip dengan Google Maps dan MSN Virtual Earth APIS

Marker atau penanda genetic merupakan penciri individu yang dilihat oleh mata atau terdeteksi dengan alat tertentu yang menunjukkan genotype suatu individu. Di dalam sebuah peta atau maps, marker adalah suatu tanda yang menjelaskan atau memberitahukan suatu tempat atau wilayah agar user mengetahui lokasi yang dimaksud

Cara membuat marker dengan open layer terdiri dari:

- --Buka web [http://openlayers.org/en/latest/examples/overlay.html?q=overlay](http://openlayers.org/en/latest/examples/overlay.html?q=overlay)
- --Copy codenya dan edit seperti dibawah ini:

~~~
<!DOCTYPE html>
<html>
  <head>
    <title>Overlay</title>
    <link rel="stylesheet" href="https://openlayers.org/en/v3.20.1/css/ol.css" type="text/css">
    <!-- The line below is only needed for old environments like Internet Explorer and Android 4.x -->
    <script src="https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL"></script>
    <script src="https://openlayers.org/en/v3.20.1/build/ol.js"></script>
    <script src="https://code.jquery.com/jquery-2.2.3.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
    <style>
      #marker {
        width: 30px;
        height: 30px;
        border: 7px solid #088;
        border-radius: 60px;
        background-color: #0000CD;
        opacity: 3.0;

      }
      #bandung {
        text-decoration: none;
        color: #FF0000;
        font-size: 11pt;
        font-weight: bold;
      }
      #marker1 {
        width: 30px;
        height: 30px;
        border: 7px solid #088;
        border-radius: 60px;
        background-color: #0000CD;
        opacity: 3.0;
      }
      #pamekasan {
        text-decoration: none;
        color: #FF0000;
        font-size: 11pt;
        font-weight: bold;
      }
      .popover-content {
        min-width: 180px;
      }
    </style>
  </head>
  <body>
    <div id="map" class="map"></div>
    <div style="display: none;">
      <!-- Clickable label for Vienna -->
      <a class="overlay" id="bandung" target="_blank" href="https://id.wikipedia.org/wiki/Kota_Bandung">Bandung</a>
      <div id="marker" title="Marker"></div>
      <!-- Clickable label for Vienna -->
      <a class="overlay" id="pamekasan" target="_blank" href="https://id.wikipedia.org/wiki/Kabupaten_Pamekasan">Pamekasan</a>
      <div id="marker1" title="Marker"></div>
      <!-- Popup -->
      <div id="popup" title="Welcome to My Maps"></div>
    </div>
    <script>

      var map = new ol.Map({
        layers: [
          new ol.layer.Tile({
            source: new ol.source.XYZ({
              url: 'https://map.vas.web.id/wmts/agm/webmercator/{z}/{x}/{y}.png'
            })
          })
        ],
        target: 'map',
        view: new ol.View({
          center: ol.proj.transform([118.015776, -2.6000285], 'EPSG:4326', 'EPSG:3857'),
          zoom: 5
        })
      });

      var pos = ol.proj.fromLonLat([107.609810,-6.914744]);

      // Vienna marker
      var marker = new ol.Overlay({
        position: pos,
        positioning: 'center-center',
        element: document.getElementById('marker'),
        stopEvent: false
      });
      map.addOverlay(marker);

      // Vienna label
      var bandung = new ol.Overlay({
        position: pos,
        element: document.getElementById('bandung')
      });
      map.addOverlay(bandung);

      var pos1 = ol.proj.fromLonLat([113.4739,-7.1542]);

      // Vienna marker
      var marker1 = new ol.Overlay({
        position: pos1,
        positioning: 'center-center',
        element: document.getElementById('marker1'),
        stopEvent: false
      });
      map.addOverlay(marker1);

      // Vienna label
      var pamekasan = new ol.Overlay({
        position: pos1,
        element: document.getElementById('pamekasan')
      });
      map.addOverlay(pamekasan);

      // Popup showing the position the user clicked
      var popup = new ol.Overlay({
        element: document.getElementById('popup')
      });
      map.addOverlay(popup);

      map.on('click', function(evt) {
        var element = popup.getElement();
        var coordinate = evt.coordinate;
        var hdms = ol.coordinate.toStringHDMS(ol.proj.transform(
            coordinate, 'EPSG:3857', 'EPSG:4326'));

        $(element).popover('destroy');
        popup.setPosition(coordinate);
        // the keys are quoted to prevent renaming in ADVANCED mode.
        $(element).popover({
          'placement': 'top',
          'animation': false,
          'html': true,
          'content': '<p>The location you clicked was:</p><code>' + hdms + '</code>'
        });
        $(element).popover('show');
      });
    </script>
  </body>
</html>
~~~

- --Kemudian simpan sebagai file .html
- --Setelah itu buka file .html tersebut, maka hasilnya akan seperti dibawah ini:
<p align="center">
  <img src="../../img/overlayy.PNG" width="400px">
</p>

Penutup
Kesimpulan
Dari praktikum diatas dapat disimpulkan bahwa pembuatan marker dengan open layer beda tipis dengan membuat marker di google maps, hanya berbeda beberapa code saja dan cara pemanggilan mapsnya

Saran
Saran saya sebaiknya pembelajaran tentang open layer dapat diperjelas lagi agar mengetahui perbedaan yang signifikan antara google maps dan open layer

* Nama : Gilang Romadhanu Tartila
* NPM : 1144033
* Kelas : 3C
* Prodi : D4 Teknik Informatika
* Mata Kuliah : Sistem Informasi Geografis

Link Github : https://github.com/gilangtartila99/SistemInformasiGeografis2016

Referensi : 
1. https://gedearta83.wordpress.com/2012/11/03/dokumentasi-openlayers/
2. https://id.wikipedia.org/wiki/Penanda_genetik
3. http://openlayers.org/en/latest/examples/overlay.html?q=overlay

Scan Plagiarisme
1. smallseotools - Link https://drive.google.com/open?id=0B5gySyqZ4GGoYVpFVC0tRnl4cEk
2. searchenginereport - Link https://drive.google.com/open?id=0B5gySyqZ4GGoNjRscGwzbkU4YmM