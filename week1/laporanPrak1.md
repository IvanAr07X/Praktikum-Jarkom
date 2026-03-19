# Laporan Praktikum Week 1

<pre>
Nama        : Ivan Radithya Tanaya Ardianto<br>
NIM         : 103072430005<br>
Kelas       : IF-04-05<br>
Mata Kuliah : Jaringan Komputer
</pre>
__________________________________________

<br>

## Instalasi Wireshark (modul 1)

### Langkah-langkah instalasi Wireshark:
1. Pergi ke website www.wireshark.org atau buka link ini https://www.wireshark.org/download.html
2. Pilih sesuai dengan OS (Operating System) masing-masing, kemudian download (pilih yang stable version atau versi terbaru)
3. Setelah file didownload klik open file
4. Lakukan installation setup mulai dari peletakan direktori instalasi sampai proses instalasi selesai<br>

### Lampiran
- Download page
![Wireshark Website](../assets/image/fromWeb/wiresharkWebsite.png)
- Installation Part 1<br>
![install setup part 1](../assets/image/fromDesktop/installationSetupPart1.png)
- Installation Part 2<br>
![install setup part 2](../assets/image/fromDesktop/installationSetupPart2.png)
- Installation Part 3<br>
![install setup part 3](../assets/image/fromDesktop/installationSetupPart3.png)
- Installation Part 4<br>
![install setup part 4](../assets/image/fromDesktop/installationSetupPart4.png)
- Installation Part 5<br>
![install setup part 5](../assets/image/fromDesktop/installationSetupPart5.png)
- Installation Part 6<br>
![install setup part 6](../assets/image/fromDesktop/installationSetupPart6.png)
- Installation Part 7<br>
![install setup part 7](../assets/image/fromDesktop/installationSetupPart7.png)
- Installation Part 8<br>
![install setup part 8](../assets/image/fromDesktop/installationSetupPart8.png)
- Installation Part 9<br>
![install setup part 9](../assets/image/fromDesktop/installationSetupPart9.png)
- Installation Part 10<br>
![install setup part 10](../assets/image/fromDesktop/installationSetupPart10.png)
- Installation Done<br>
![install setup done](../assets/image/fromDesktop/installationSetupDone.png)<br><br>

## Tugas Praktikum week 1 (modul 2)

### Langkah-langkah basic HTTP GET atau response interaction:
1. Buka Wireshark terlebih dahulu
2. Untuk capture bisa pilih wifi (matikan **VPN** jika menggunakan) dengan cara double klik tulisan wifi
3. Buka link ini http://gaia.cs.umass.edu/wireshark-labs/INTRO-wireshark-file1.html (pastikan di browser *pakai http*, jika belum bisa coba pakai *browse as guest*)
4. Browser akan menampilkan html sederhana dalam 1 baris "Congratulations! You've downloaded the first Wireshark lab file!"
5. Ketik pada bagian filter di wireshark "http" (tanpa tanda kutip)
6. pilih yang ada tulisan "(text/html)"
7. klik panah pada tulisan "Line-based text data", akan menampilkan: 
```
<html>\n 
Congratulations! You've download the first Wireshark lab file!
</html>\n
```

**Untuk keluar bisa klik stop capture pada menu, kemudian close this capture file**<br>

### Lampiran
- Tampilan Wireshark
![Tampilan Wireshark](../assets/image/fromWireshark/tampilanWireshark.png)
- Tampilan Capture from Wi-Fi
![Tampilan Capture from Wi-Fi](../assets/image/fromWireshark/tampilanCaptureFromWifi.png)
- Tampilan Browser pada link html
![Tampilan Browser pada link html](../assets/image/fromWeb/tampilanBrowserPadaLinkHtml.png)
- Tampilan Capture from Wi-Fi With Filter HTTP
![Tampilan Capture from Wi-Fi With Filter HTTP](../assets/image/fromWireshark/tampilanCaptureFromWifiWithFilterHTTP.png)
- Line-Based Text Data: text/html from GET html
![Line-Based Text Data: text/html](../assets/image/fromWireshark/lineBasedTextDataHtmlVer.png)