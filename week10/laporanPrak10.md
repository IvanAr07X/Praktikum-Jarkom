# Laporan Praktikum Week 10

<pre>
Nama        : Ivan Radithya Tanaya Ardianto
NIM         : 103072430005
Kelas       : IF-04-05
Mata Kuliah : Jaringan Komputer
</pre>
__________________________________________

<br>

## ICMP (modul 12)
<p>
Apa itu ICMP? ICMP (Internet Control Message Protocol) adalah protokol pendukung IP yang digunakan untuk komunikasi kontrol.
</p>

Fungsi ICMP:
<ul>
    <li>
    <p>
    Error reporting &rarr; Memberitahu pengirim jika paket gagal dikirim (contoh: host unreachable, port unreachable).
    </p> 
    </li>
    <li>
    <p>
    Diagnostics &rarr; Digunakan oleh ping dan traceroute untuk cek konektivitas dan jalur.
    </p>
    </li>
    <li>
    <p>
    Routing support &rarr; Pesan Redirect memberi tahu host agar menggunakan rute lain yang lebih efisien.
    </p>
    </li>
    <li>
    <p>
    Congestion feedback &rarr; Memberikan sinyal jika terjadi masalah seperti TTL (Time To Live) habis.
    </p>
    </li>
</ul>

Mekanisme kerja ICMP:
<ol>
    <li>
    <p>
    Encapsulation &rarr; Pesan ICMP dikirim dalam bentuk paket IP (IP header + ICMP header + data).
    </p>
    </li>
    <li>
    <p>
    Message types &rarr; Ada beberapa pesan, misalnya:
        <ul>
            <li>
            <p>
            Echo Request/Reply &rarr; Dipakai oleh ping.
            </p>
            </li>
            <li>
            <p>
            Destination Unreachable &rarr; Host atau port tidak bisa dijangkau.
            </p>
            </li>
            <li>
            <p>
            Time Exceeded &rarr; TTL habis, apket dibuang.
            </p>
            </li>
            <li>
            <p>
            Redirect &rarr; Router menyarankan jalur lain.
            </p>
            </li>
        </ul>
    </p>
    </li>
    <li>
    <p>
    Checksum &rarr; Memastikan integritas pesan ICMP.
    </p>
    </li>
    <li>
    <p>
    Connections &rarr; Tidak ada sesi atau handshake, hanya kirim pesan langsung.
    </p>
    </li>
</ol>

### ICMP & Ping
Menangkap paket yang dihasilkan oleh program Ping (paket ICMP).

#### Melakukan Percobaan atau Test dengan Melakukan Ping ke www.ust\.hk
<ol>
    <li>Pertama buka wireshark, lalu pilih capture pada Wi-Fi.</li>
    <li>
    Kemudian, buka CMD. Lalu ketik <kbd>ping -n 10 www.ust.hk</kbd>.c                                                                                                                                   
    <img src="../assets/image/fromCMD/ping.png" alt="Tampilan ping pada CMD"><br>
    </li>
    <li>Lalu stop capturing pada Wi-Fi.</li>
    <li>
    Ketik <kbd>icmp</kbd> pada kolom filter.
    <img src="../assets/image/fromWireshark/wiresharkFilter23Crop.png" alt="Tampilan filter icmp pada wireshark"><br>
    </li>
    <li>
    Kemudian, pilih salah satu paket ICMP (termasuk Echo Reply dan Echo Request).
    <img src="../assets/image/fromWireshark/wiresharkFilter23Crop5.png" alt="Tampilan icmp dari ping sebanyak sepuluh kali pada wireshark"><br>
    <img src="../assets/image/fromWireshark/wiresharkFilter23Crop1.png" alt="Tampilan Echo request pada wireshark"><br>
    <img src="../assets/image/fromWireshark/wiresharkFilter23Crop2.png" alt="Tampilan Echo reply pada wireshark"><br>
    </li>
    </li>
    <li>
    Lalu pada bagian packet detail dan expand pada bagian <kbd>Internet Control Message Protocol</kbd>.
    <img src="../assets/imagE/fromWireshark/wiresharkFilter23Crop3.png" alt="Tampilan deskripsi dari Internet Control Message Protocol (Echo request)"><br>
    dengan isi pesan
    <pre><code>
        Type: Echo (ping) request (8)
        Code: 0
        Checksum: 0x4d4c [correct]
        ...
        Identifier (BE): 1 (0x0001)
        Identifier (LE): 256 (0x0100)
        Sequence Number (BE): 15 (0x000f)
        Sequence Number (LE): 3840 (0x0f00)
        [Response frame: 6317]
    </code></pre>
    <img src="../assets/image/fromWireshark/wiresharkFilter23Crop4.png" alt="Tampilan deskripsi dari Internet Control Message Protocol (Echo Reply)"><br>
    dengan isi pesan
    <pre><code>
        Type: Echo (ping) reply (0)
        Code: 0
        Checksum: 0x554c [correct]
        ...
        Identifier (BE): 1 (0x001)
        Identifier (LE): 256 (0x0100)
        Sequence Number (BE): 15 (0x000f)
        Sequence Number (LE): 3840 (0x0f00)
        [Request frame: 6298]
        [Response time: 90.215 ms]
    </code></pre>
    </li>
</ol>

#### Berdasarkan analisis saya:
<p align="justify">
Dari hasil pengamatan saya, saat menjalankan perintah <kbd>ping -n 10 www.ust.hk</kbd> yang akan melakukan uji konektivitas sebanyak 10 kali ke server atau host www.ust.hk, didapatkan paket ICMP sebanyak 20 (10 Request, 10 Reply) dengan paket <kbd>Echo Request (Type 8, Code 0)</kbd> yang dikirimkan oleh komputer yang kemudian memperoleh balasan berupa paket <kbd>Echo Reply (Type 0, Code 0)</kbd> dari server.
</p>

### ICMP & Traceroute
Menangkap paket yang dihasilkan oleh program Traceroute (paket ICMP).

#### Melakukan Percobaan atau Test dengan Melakukan Traceroute ke www.ust\.hk
<ol>
    <li>Pertama buka wireshark, lalu pilih capture pada Wi-Fi.</li>
    <li>
    Kemudian, buka CMD. Lalu ketik <kbd>tracert www.ust.hk</kbd>.
    <img src="../assets/image/fromCMD/tracert.png" alt="Tampilan tracert pada CMD"><br>
    </li>
    <li>Lalu stop capturing pada Wi-Fi.</li>
    <li>
    Ketik <kbd>icmp</kbd> pada kolom filter.
    <img src="../assets/image/fromWireshark/wiresharkFilter24.png" alt="Tampilan filter icmp pada wireshark"><br>
    </li>
    <li>
    Kemudian, pilih salah satu paket ICMP. Lalu pada bagian packet detail dan expand pada bagian <kbd>Internet Control Message Protocol</kbd>.
    <img src="../assets/image/fromWireshark/wiresharkFilter24Crop.png" alt="Tampilan Rime to live exceeded pada wireshark"><br>
    dengan pesan
    <pre><code>
        Type: Time-to-live exceeded (11)
        Code: 0 (Time to live exceed in transit)
        Checksum: 0xf4ff [correct]
        ...
        Unused: 00000000
    </code></pre>
    <img src="../assets/image/fromWireshark/wiresharkFilter24Crop1.png" alt="Tampilan Echo request pada wireshark"><br>
    dengan pesan
    <pre><code>
        Type: Echo (ping) request (8)
        Code: 0
        Checksum: 0xf7e1 [correct]
        ...
        Identifier (BE): 1 (0x001)
        Identifier (LE): 256 (0x0100)
        Sequence Number (BE): 29 (0x001d)
        Sequence Number (LE): 7424 (0x1d00)
        [No response seen]
    </code></pre>
    <img src="../assets/image/fromWireshark/wiresharkFilter24Crop2.png" alt="Tampilan Echo request pada wireshark"><br>
    dengan pesan
    <pre><code>
        Type: Echo (ping) request (8)
        Code: 0
        Checksum: 0xf7b0 [correct]
        ...
        Identifier (BE): 1 (0x001)
        Identifier (LE): 256 (0x0100)
        Sequence Number (BE): 78 (0x004e)
        Sequence Number (LE): 19968 (0x4e00)
        [Response frame: 745]
    </code></pre>
    <img src="../assets/image/fromWireshark/wiresharkFilter24Crop3.png" alt="Tampilan Echo reply pada wireshark"><br>
    dengan pesan
    <pre><code>
        Type: Echo (ping) reply (0)
        Code: 0
        Checksum: 0xffb0 [correct]
        ...
        Identifier (BE): 1 (0x001)
        Identifier (LE): 256 (0x0100)
        Sequence Number (BE): 78 (0x004e)
        Sequence Number (LE): 19968 (0x4e00)
        [Request frame: 744]
        [Response time: 68.468 ms]
    </code></pre>
    </li>
</ol>

#### Berdasarkan analisis saya:
<p align="justify">
Dari hasil pengamatan saya, saat menjalankan perintah <kbd>tracert www.ust.hk</kbd> terlihat ada paket ICMP yang bertipe <kbd>Time-to-live-exceeded (Type 11, Code 0)</kbd>. Cara kerjanya dengan mengirim paket dengan TTL (Time To Live) secara bertahap, kemudian mencatat router (hop) yang dilewati.
</p>

### Kesimpulan
<p align="justify">
Berdasarkan hasil analisis tadi, dapat diamati bahwa struktur dan isi paket ICMP, seperti Type, Code, Checksum, Identifier, dan Sequence Number memilki peran penting dalam proses pemeantauan, troubleshooting, dan analisis performa dalam jaringan komputer.
</p>