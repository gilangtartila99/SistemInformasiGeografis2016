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

| &lt;!DOCTYPE html&gt;&lt;html&gt;  &lt;head&gt;    &lt;title&gt;Overlay&lt;/title&gt;    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://openlayers.org/en/v3.20.1/css/ol.css&quot; type=&quot;text/css&quot;&gt;    &lt;!-- The line below is only needed for old environments like Internet Explorer and Android 4.x --&gt;    &lt;script src=&quot;https://cdn.polyfill.io/v2/polyfill.min.js?features=requestAnimationFrame,Element.prototype.classList,URL&quot;&gt;&lt;/script&gt;    &lt;script src=&quot;https://openlayers.org/en/v3.20.1/build/ol.js&quot;&gt;&lt;/script&gt;    &lt;script src=&quot;https://code.jquery.com/jquery-2.2.3.min.js&quot;&gt;&lt;/script&gt;    &lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css&quot;&gt;    &lt;script src=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js&quot;&gt;&lt;/script&gt;    &lt;style&gt;      #marker {        width: 30px;        height: 30px;        border: 7px solid #088;        border-radius: 60px;        background-color: #0000CD;        opacity: 3.0;       }      #bandung {        text-decoration: none;        color: #FF0000;        font-size: 11pt;        font-weight: bold;      }      #marker1 {        width: 30px;        height: 30px;        border: 7px solid #088;        border-radius: 60px;        background-color: #0000CD;        opacity: 3.0;      }      #pamekasan {        text-decoration: none;        color: #FF0000;        font-size: 11pt;        font-weight: bold;      }      .popover-content {        min-width: 180px;      }    &lt;/style&gt;  &lt;/head&gt;  &lt;body&gt;    &lt;div id=&quot;map&quot; class=&quot;map&quot;&gt;&lt;/div&gt;    &lt;div style=&quot;display: none;&quot;&gt;      &lt;!-- Clickable label for Vienna --&gt;      &lt;a class=&quot;overlay&quot; id=&quot;bandung&quot; target=&quot;\_blank&quot; href=&quot;https://id.wikipedia.org/wiki/Kota\_Bandung&quot;&gt;Bandung&lt;/a&gt;      &lt;div id=&quot;marker&quot; title=&quot;Marker&quot;&gt;&lt;/div&gt;      &lt;!-- Clickable label for Vienna --&gt;      &lt;a class=&quot;overlay&quot; id=&quot;pamekasan&quot; target=&quot;\_blank&quot; href=&quot;https://id.wikipedia.org/wiki/Kabupaten\_Pamekasan&quot;&gt;Pamekasan&lt;/a&gt;      &lt;div id=&quot;marker1&quot; title=&quot;Marker&quot;&gt;&lt;/div&gt;      &lt;!-- Popup --&gt;      &lt;div id=&quot;popup&quot; title=&quot;Welcome to My Maps&quot;&gt;&lt;/div&gt;    &lt;/div&gt;    &lt;script&gt;       var map = new ol.Map({        layers: [          new ol.layer.Tile({            source: new ol.source.XYZ({              url: &#39;https://map.vas.web.id/wmts/agm/webmercator/{z}/{x}/{y}.png&#39;            })          })       ],        target: &#39;map&#39;,        view: new ol.View({          center: ol.proj.transform([118.015776, -2.6000285], &#39;EPSG:4326&#39;, &#39;EPSG:3857&#39;),          zoom: 5        })      });       var pos = ol.proj.fromLonLat([107.609810,-6.914744]);       // Vienna marker      var marker = new ol.Overlay({        position: pos,        positioning: &#39;center-center&#39;,        element: document.getElementById(&#39;marker&#39;),        stopEvent: false      });      map.addOverlay(marker);       // Vienna label      var bandung = new ol.Overlay({        position: pos,        element: document.getElementById(&#39;bandung&#39;)      });      map.addOverlay(bandung);       var pos1 = ol.proj.fromLonLat([113.4739,-7.1542]);       // Vienna marker      var marker1 = new ol.Overlay({        position: pos1,        positioning: &#39;center-center&#39;,        element: document.getElementById(&#39;marker1&#39;),        stopEvent: false      });      map.addOverlay(marker1);       // Vienna label      var pamekasan = new ol.Overlay({        position: pos1,        element: document.getElementById(&#39;pamekasan&#39;)      });      map.addOverlay(pamekasan);       // Popup showing the position the user clicked      var popup = new ol.Overlay({        element: document.getElementById(&#39;popup&#39;)      });      map.addOverlay(popup);       map.on(&#39;click&#39;, function(evt) {        var element = popup.getElement();        var coordinate = evt.coordinate;        var hdms = ol.coordinate.toStringHDMS(ol.proj.transform(            coordinate, &#39;EPSG:3857&#39;, &#39;EPSG:4326&#39;));         $(element).popover(&#39;destroy&#39;);        popup.setPosition(coordinate);        // the keys are quoted to prevent renaming in ADVANCED mode.        $(element).popover({          &#39;placement&#39;: &#39;top&#39;,          &#39;animation&#39;: false,          &#39;html&#39;: true,          &#39;content&#39;: &#39;&lt;p&gt;The location you clicked was:&lt;/p&gt;&lt;code&gt;&#39; + hdms + &#39;&lt;/code&gt;&#39;        });        $(element).popover(&#39;show&#39;);      });    &lt;/script&gt;  &lt;/body&gt;&lt;/html&gt; |
| --- |

- --Kemudian simpan sebagai file .html
- --Setelah itu buka file .html tersebut, maka hasilnya akan seperti dibawah ini:
<p align="center">
  <img src="../../img/overlayy.png" width="400px">
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