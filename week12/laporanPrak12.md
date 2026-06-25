# Laporan Praktikum Week 12

<pre>
Nama        : Ivan Radithya Tanaya Ardianto
NIM         : 103072430005
Kelas       : IF-04-05
Mata Kuliah : Jaringan Komputer
</pre>
__________________________________________

<br>

## 802.11 WiFi (modul 14)
<p align="justify">
<Strong>802.11</Strong> adalah standar Wi-Fi yang ditetapkan oleh <Strong>IEEE</Strong> (Institute of Electrical and Electronics Engineers) untuk berkomunikasi dengan jaringan nirkabel (WLAN). Standar ini mendefinisikan cara perangkat seperti laptop, smartphone, dan router berkomunikasi menggunakan gelombang radio pada frekuensi 2.4 GHz, 5 GHz, hingga 6 GHz.
</p>

### Percobaan
<p align="justify">
Untuk melakukan pengujian saya mendownload file ini <a href="http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip">http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces.zip</a>. Gunakan file dengan nama <kbd>Wireshark_802_11.pcap</kbd>. Alasan menggunakan file ini, karena komputer saya tidak mendukung mode monitor, sehingga lebih memilih file ini daripada membeli adapternya.
</p>

<ol>
    <li>Buka file tersebut dengan wireshark.</li>
    <li>
    Ketikkan <kbd>wlan.fc.type_subtype == 0</kbd> pada filter.
    <img src="../assets/image/fromWireshark/wiresharkFilter27.png" alt="Tampilan filter wlan.fc.type_subtype == 0 pada wireshark"><br>
    <p align="justify">
    Filter ini digunakan untuk menampilkan paket <i>Association Request</i>, yaitu paket yang dikirim oleh perangkat klien kepada Access Point (AP) ketika ingin bergabung ke dalam jaringan Wi-Fi. Paket ini berisi informasi kemampuan perangkat, seperti data rate yang didukung dan parameter koneksi yang akan digunakan selama proses asosiasi.
    </p> 
    </li>
    <li>
    Ketikkan <kbd>wlan.fc.type_subtype == 1</kbd> pada filter.
    <img src="../assets/image/fromWireshark/wiresharkFilter28.png" alt="Tampilan filter wlan.fc.type_subtype == 1 pada wireshark"><br>
    <p align="justify">
    </p>
    Filter ini digunakan untuk menampilkan paket <i>Association Response</i>, yaitu paket yang dikirm oleh AP sebagai balasan terhadap permintaan (request) asosiasi dari klien. Paket ini berisi informasi apakah proses asosiasi berhasil dilakukan beserta Association ID (AID) yang diberikan kepada perangkat klien.
    </li>
    <li>
    Ketikkan <kbd>wlan.fc.type_subtype == 10</kbd> pada filter.
    <img src="../assets/image/fromWireshark/wiresharkFilter29.png" alt="Tampilan filter wlan.fc.type_subtype == 10 pada wireshark"><br>
    <p align="justify">
    </p>
    Filter ini digunakan untuk menampilkan paket <i>Disassociation</i>, yaitu paket yang menandakan bahwa hubungan antara perangkat klien dan AP telah terputus. Paket ini biasanya muncul ketika perangkat keluar dari jaringan atau ketika Access Point menghentikan koneksi dengan klien. Pada gambaer diatas bisa dilihat bahwa tidak ada koneksi yang terputus antara AP dengan perangkat klien.
    </li>
    <li>
    Ketikkan <kbd>wlan.fc.type == 2</kbd> pada filter.
    <img src="../assets/image/fromWireshark/wiresharkFilter30.png" alt="Tampilan filter wlan.fc.type == 2 pada wireshark"><br>
    <p align="justify">
    Filter ini digunakan untuk menampilkan semua paket <i>Data Frame</i>, yaitu paket yang digunakan untuk mengirimkan data pengguna melalui jaringan Wi-Fi. Setelah proses autentikasi dan asosiasi selesai, sebagian besar komunikasi pada jaringan akan menggunakan frame jenis ini. pada gambaer diatas merupakan contoh data frame yang kosong.
    </p>
    </li>
    <li>
    Ketikkan <kbd>wlan.fc.type_subtype == 8</kbd> pada filter.
    <img src="../assets/image/fromWireshark/wiresharkFilter31.png" alt="Tampilan filter wlan.fc.type_subtype == 8 pada wireshark"><br>
    <p align="justify">
    Filter ini digunakan untuk menampilkan paket <i>Beacon Frame</i> yang dikirimkan secara berkala oleh AP. Beacon Frame berfungsi untuk mengumumkan keberadaan jaringan Wi-Fi serta memberikan informasi penting seperti SSID, channel, kemampuan jaringan, dan parameter lain yang diperlukan agar perangkat klien dapat menemukan serta terhubung ke AP.
    </p><br>
    Isi pada paket:
    <ul>
        <li>Flags: ........C</li>
        <li>Type/Subtype: Beacon frame (0x0008)</li>
        <li>Frame Control Field: 0x8000</li>
        <li>Receiver address: Broadcast (ff:ff:ff:ff:ff:ff)</li>
        <li>Destination address: Broadcast (ff:ff:ff:ff:ff:ff)</li>
        <li>Transmitter address: CiscoLinksys_f7:1d:51 (00:16:b6:f7:1d:51)</li>
        <li>Source address: CiscoLinksys_f7:1d:51 (00:16:b6:f7:1d:51)</li>
        <li>BSS Id: CiscoLinksys_f7:1d:51 (00:16:b6:f7:1d:51)</li>
        <li>...</li>
    </ul>
    </li>
</ol>