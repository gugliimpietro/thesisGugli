# BAB III REVISI + TAMBAHAN BAB II DAN DAFTAR PUSTAKA

**Tanggal:** 12 September 2026
**Status:** naskah siap disisipkan ke `draftp Proposal tesis 4c.docx`
**Dasar:** strategi di `07_STRATEGI_SPESIFIKASI_MODEL.md`

> **Catatan pemakaian.** Bagian 3.6 (Data dan Sumber Data) ditulis untuk **Pilihan C** — panel
> 2007–2011 — sesuai rekomendasi di `08_PANDUAN_MEMBANGUN_ULC.md`. Bila Anda memilih Pilihan A
> atau B, hanya subbab 3.6 dan beberapa kalimat di 3.5 yang berubah; varian penggantinya saya
> sediakan di akhir dokumen. Seluruh subbab lain berlaku untuk ketiga pilihan.

---

# BAB III — METODOLOGI DAN DATA

## 3.1 Penurunan Model Empiris

Sebagaimana diuraikan pada Bab II, penelitian ini mengadaptasi kerangka penawaran ekspor
Riveros (1992), yang diturunkan dari maksimisasi profit perusahaan pada negara *small country*
dengan penerapan *Hotelling's Lemma*. Fungsi penawaran ekspor yang dihasilkan berbentuk:

$$Q_X^S = f(P_x,\ w,\ P_m) \tag{3.1}$$

dengan $Q_X^S$ sebagai **kuantitas** ekspor yang ditawarkan, $P_x$ harga barang ekspor, $w$
biaya tenaga kerja, dan $P_m$ harga bahan baku impor.

### 3.1.1 Kuantitas, bukan nilai, sebagai variabel terikat

Notasi $Q$ pada persamaan (3.1) menunjuk pada kuantitas, bukan nilai. Perbedaan ini bukan soal
penulisan, melainkan menentukan validitas estimasi.

Nilai ekspor merupakan hasil perkalian harga dengan kuantitas ($V = P_x \cdot Q$). Apabila
nilai ekspor ditempatkan sebagai variabel terikat sementara harga ekspor menjadi variabel
penjelas, maka harga muncul pada kedua ruas persamaan, dan sebagian koefisien harga yang
diperoleh bersifat **mekanis**, bukan mencerminkan perilaku ekonomi. Karena itu penelitian ini
menggunakan **volume ekspor** sebagai variabel terikat, konsisten dengan kerangka Riveros
(1992) serta praktik pada Riedel (1988) dan Golub & Edwards (2004).

### 3.1.2 Biaya tenaga kerja diukur sebagai Unit Labour Cost

Variabel $w$ pada persamaan (3.1) merepresentasikan **biaya tenaga kerja per unit output**,
bukan tingkat upah nominal per pekerja. Pembedaan ini penting secara teoretis maupun empiris.

Tingkat upah per pekerja mengandung dua kandungan informasi yang berlawanan arah. Di satu sisi,
upah yang tinggi meningkatkan biaya produksi dan menurunkan daya saing harga, sehingga
diperkirakan menekan penawaran ekspor. Di sisi lain, upah yang tinggi juga mencerminkan
produktivitas dan kualitas tenaga kerja yang lebih baik (Bernard & Jensen, 1997; Mehta & Sun,
2013), sehingga justru diperkirakan mendorong ekspor. Apabila kedua kandungan tersebut
tercampur dalam satu variabel, koefisien yang diperoleh merupakan resultan dari dua pengaruh
yang saling meniadakan dan tidak dapat diinterpretasikan sebagai ukuran daya saing biaya.

Ukuran yang tepat untuk daya saing biaya tenaga kerja adalah **Unit Labour Cost** (ULC), yaitu
rasio antara total biaya tenaga kerja dengan nilai tambah yang dihasilkan:

$$ULC_i = \frac{\text{Total biaya tenaga kerja}_i}{\text{Nilai tambah}_i}
= \frac{w_i}{\text{Produktivitas}_i} \tag{3.2}$$

ULC menempatkan produktivitas pada penyebut, sehingga kandungan kualitas tenaga kerja
terserap dan yang tersisa pada pembilang adalah komponen biaya. Suatu industri dapat membayar
upah tinggi namun tetap kompetitif apabila produktivitasnya lebih tinggi lagi — kondisi yang
tidak dapat ditangkap oleh tingkat upah semata.

Penggunaan ULC sebagai indikator daya saing biaya mengikuti Golub & Edwards (2004) yang
mengkaji daya saing ekspor manufaktur Afrika Selatan, Ceglowski & Golub (2007, 2012) yang
membandingkan biaya tenaga kerja Tiongkok dengan mitra dagangnya, serta rekomendasi
metodologis IMF (2012) yang secara khusus menganjurkan pengukuran ULC pada **level industri**,
bukan level agregat perekonomian — persis unit analisis penelitian ini.

### 3.1.3 Spesifikasi model

Dengan menambahkan karakteristik industri sebagai variabel kontrol dan interaksi antara biaya
tenaga kerja dengan klasifikasi sektor, model empiris penelitian ini dirumuskan sebagai:

$$
\begin{aligned}
\ln Q_{it} =\ & \alpha + \beta_1 \ln P_{x,it} + \beta_2 \ln P_{m,it} + \beta_3 \ln ULC_{it} \\
& + \gamma_1 (\ln ULC_{it} \times LI_i) + \gamma_2 (\ln ULC_{it} \times CI_i) \\
& + \beta_4 \ln TK_{it} + \beta_5 \ln K_{it} + \beta_6 Asing_{it} \\
& + \beta_7 SkillRatio_{it} + \beta_8 ImpShare_{it} \\
& + \delta_t + \mu_i + \varepsilon_{it}
\end{aligned}
\tag{3.3}
$$

dengan $i$ menunjuk industri (ISIC Rev.3, 4 digit), $t$ menunjuk tahun, $LI$ dan $CI$
masing-masing dummy sektor *labor intensive* dan *capital intensive*, $\delta_t$ dummy tahun,
$\mu_i$ efek individu industri, dan $\varepsilon_{it}$ galat.

Suku interaksi $\gamma_1$ dan $\gamma_2$ merupakan inti dari tujuan penelitian kedua. Secara
teoretis, sensitivitas penawaran ekspor terhadap biaya tenaga kerja diperkirakan meningkat
seiring intensitas penggunaan tenaga kerja dalam produksi — implikasi langsung dari kerangka
Heckscher–Ohlin yang diuraikan pada Bab II. Apabila biaya tenaga kerja berpengaruh kuat pada
sektor *labor intensive* namun netral pada sektor *capital intensive*, maka estimasi tanpa suku
interaksi hanya akan menghasilkan rata-rata dari kedua pengaruh tersebut dan berpotensi
menyimpulkan ketiadaan pengaruh secara keliru.

---

## 3.2 Definisi Operasional Variabel

### 3.2.1 Volume ekspor ($Q$)

Volume ekspor produk manufaktur Indonesia ke seluruh dunia, dalam satuan berat. Data diperoleh
dari UN Comtrade, dikonversi dari HS 6 digit ke ISIC Rev.3 4 digit menggunakan tabel
konkordansi, kemudian diagregasi pada level industri 4 digit.

### 3.2.2 Harga ekspor ($P_x$)

Diperoleh sebagai *unit value*, yaitu nilai ekspor dibagi volume ekspor untuk setiap produk,
kemudian dirata-ratakan tertimbang dengan bobot nilai ekspor pada level industri 4 digit.
Seluruh harga dinyatakan per kilogram untuk menjaga keterbandingan antar produk.

### 3.2.3 Harga bahan baku impor ($P_m$)

Dihitung sebagai nilai impor dibagi volume impor untuk bahan baku yang paling dominan digunakan
pada setiap industri, bersumber dari data Kementerian Perindustrian.

### 3.2.4 Unit Labour Cost ($ULC$) — variabel utama

Dibangun dari data mikro Survei Industri Besar dan Sedang, Badan Pusat Statistik, mengikuti
definisi nilai tambah resmi BPS sebagaimana tercantum pada Bagian VII kuesioner survei:

$$\text{Nilai tambah} = \text{Pendapatan} - \text{Pengeluaran antara}
+ \text{Biaya tenaga kerja} + \text{Komponen nilai tambah lainnya}$$

Komponen pendapatan meliputi nilai barang yang dihasilkan, pendapatan jasa industri, pendapatan
lainnya, penjualan tenaga listrik, serta perubahan nilai stok barang setengah jadi dan barang
jadi. Pengeluaran antara meliputi bahan baku dan penolong, bahan bakar dan pelumas, tenaga
listrik yang dibeli, serta pengeluaran lainnya. Komponen nilai tambah lainnya meliputi sewa
tanah, pajak tidak langsung, dan bunga atas pinjaman. Biaya tenaga kerja ditambahkan kembali
karena merupakan bagian dari nilai tambah, bukan biaya antara.

Agregasi ke level industri dilakukan dengan menjumlahkan pembilang dan penyebut secara terpisah
sebelum dibagi:

$$ULC_i = \frac{\sum_{j \in i} \text{Biaya tenaga kerja}_j}{\sum_{j \in i} \text{Nilai tambah}_j}$$

dengan $j$ menunjuk perusahaan. Prosedur ini memberi bobot lebih besar pada perusahaan berskala
besar, sesuai kontribusinya terhadap daya saing industri secara keseluruhan, dan menghindari
distorsi yang timbul apabila rasio dirata-ratakan antar perusahaan.

### 3.2.5 Upah tenaga kerja produksi dan non-produksi

Sebagai spesifikasi pembanding, total pengeluaran tenaga kerja dipisahkan menjadi pengeluaran
untuk pekerja produksi dan pekerja non-produksi, masing-masing dibagi jumlah pekerja pada
kelompok tersebut. Pemisahan ini dimungkinkan karena kuesioner Survei Industri memang mencatat
kedua komponen secara terpisah.

### 3.2.6 Rasio keterampilan ($SkillRatio$)

Rasio antara upah per pekerja non-produksi dengan upah per pekerja produksi, digunakan sebagai
proksi intensitas keterampilan industri. Variabel ini mengendalikan komposisi keterampilan
tenaga kerja, sehingga koefisien biaya tenaga kerja lebih murni mencerminkan komponen biaya.
Penggunaan struktur upah antar kelompok pekerja sebagai proksi keterampilan mengikuti Mehta &
Sun (2013) dan Bernard & Jensen (1997).

### 3.2.7 Pangsa bahan baku impor ($ImpShare$)

Rasio nilai bahan baku dan penolong yang berasal dari impor terhadap total nilai bahan baku dan
penolong. Amiti & Konings (2007) menunjukkan bahwa akses terhadap bahan baku impor meningkatkan
produktivitas perusahaan manufaktur Indonesia secara substansial, sehingga variabel ini
merupakan penentu kemampuan ekspor yang tidak boleh diabaikan.

### 3.2.8 Total tenaga kerja ($TK$), kapital ($K$), dan kepemilikan asing ($Asing$)

Total tenaga kerja merupakan penjumlahan pekerja produksi dan non-produksi. Kapital diukur dari
nilai taksiran seluruh barang modal tetap menurut harga berlaku. Kepemilikan asing diukur
sebagai persentase permodalan asing, dirata-ratakan tertimbang pada level industri —
penyempurnaan atas penggunaan dummy ambang batas kepemilikan pada versi sebelumnya, karena
persentase memuat informasi yang lebih kaya.

### 3.2.9 Klasifikasi sektor

Industri dikelompokkan menjadi *resource intensive*, *labor intensive*, dan *capital intensive*
mengikuti Narjoko & Putra (2014). Pengelompokan dilakukan pada level ISIC 2 digit, kemudian
klasifikasi tersebut diterapkan pada seluruh industri 4 digit yang berada di bawahnya. **Unit
analisis penelitian ini adalah industri ISIC Rev.3 4 digit**, sedangkan pengelompokan 2 digit
digunakan semata-mata untuk pembentukan dummy sektor. Sektor *resource intensive* digunakan
sebagai kategori acuan.

---

## 3.3 Hipotesis Penelitian

| No | Variabel | Tanda | Landasan |
|---|---|---|---|
| H1 | Harga ekspor ($P_x$) | **+** | Fungsi penawaran: kenaikan harga mendorong kuantitas yang ditawarkan (Riveros, 1992) |
| H2 | Harga bahan baku impor ($P_m$) | **−** | Kenaikan harga input menaikkan biaya produksi dan menekan penawaran ekspor |
| **H3a** | **Unit Labour Cost** | **−** | Kenaikan biaya tenaga kerja per unit output menurunkan daya saing (Riveros, 1992; Golub & Edwards, 2004) |
| **H3b** | **Unit Labour Cost** | **+** | Biaya tenaga kerja yang tinggi dapat mencerminkan produktivitas dan kualitas tenaga kerja (Bernard & Jensen, 1997; Mehta & Sun, 2013) |
| H4 | ULC × *labor intensive* | **−** | Sensitivitas terhadap biaya tenaga kerja lebih besar pada industri padat karya |
| H5 | Total tenaga kerja | **+** | Skala industri memperkuat kemampuan bersaing di pasar internasional (Narjoko & Hill, 2007) |
| H6 | Kapital | **+** | Intensitas kapital meningkatkan kapasitas dan kualitas produksi |
| H7 | Kepemilikan asing | **+** | Transfer teknologi dan keterhubungan dengan jaringan produksi global (Narjoko & Hill, 2007) |
| H8 | Rasio keterampilan | **+** | Intensitas keterampilan yang lebih tinggi menopang daya saing non-harga |
| H9 | Pangsa bahan baku impor | **+** | Akses input impor meningkatkan produktivitas (Amiti & Konings, 2007) |

**Catatan atas H3.** Hipotesis mengenai biaya tenaga kerja sengaja dirumuskan sebagai dua
hipotesis yang saling bersaing, bukan satu hipotesis berarah tunggal. H3a mewakili mekanisme
biaya sebagaimana diajukan Riveros (1992); H3b mewakili mekanisme produktivitas dan kualitas
tenaga kerja sebagaimana ditemukan Bernard & Jensen (1997) serta Mehta & Sun (2013). Penelitian
ini menguji mekanisme mana yang dominan pada industri manufaktur Indonesia. Perumusan semacam
ini menjadikan hasil yang tidak signifikan tetap bermakna, yakni sebagai indikasi bahwa kedua
mekanisme bekerja dengan kekuatan yang berimbang.

---

## 3.4 Strategi Identifikasi

Estimasi kuadrat terkecil biasa (OLS) atas persamaan (3.3) menghadapi dua persoalan
endogenitas yang, apabila diabaikan, menghasilkan koefisien yang bias.

### 3.4.1 Endogenitas biaya tenaga kerja

Biaya tenaga kerja dan kinerja ekspor ditentukan secara simultan. Perusahaan yang berhasil
menembus pasar ekspor cenderung membayar upah lebih tinggi — fenomena *exporter wage premium*
yang terdokumentasi luas (Bernard & Jensen, 1997; Brambilla & Porto, 2017) — sementara pada
saat yang sama biaya tenaga kerja yang tinggi menggerus daya saing. Kedua arah kausalitas
tersebut berlawanan tanda, sehingga koefisien OLS merupakan campuran keduanya dan cenderung
bias menuju nol.

Persoalan ini diperberat oleh kesalahan pengukuran. Biaya tenaga kerja pada level industri 4
digit merupakan agregasi dari ribuan perusahaan dengan komposisi keterampilan yang beragam.
Kesalahan pengukuran pada variabel penjelas menimbulkan *attenuation bias*, yang secara
sistematis juga menarik koefisien ke arah nol.

Untuk mengatasinya, penelitian ini menggunakan **upah minimum provinsi tertimbang** sebagai
variabel instrumen:

$$MW_{it} = \sum_{p} s_{ip}^{0} \cdot MW_{pt} \tag{3.4}$$

dengan $s_{ip}^{0}$ adalah pangsa tenaga kerja industri $i$ yang berada di provinsi $p$ pada
tahun dasar, dan $MW_{pt}$ upah minimum provinsi $p$ pada tahun $t$. Penggunaan bobot tahun
dasar menghindari endogenitas yang timbul apabila sebaran tenaga kerja ikut menyesuaikan diri
terhadap perubahan upah minimum.

Instrumen ini memenuhi kedua syarat yang disyaratkan. **Relevansi**: upah minimum provinsi
merupakan penentu langsung struktur upah industri, khususnya pada industri padat karya yang
sebagian besar pekerjanya berada di sekitar batas upah minimum. **Eksogenitas**: penetapan upah
minimum merupakan hasil proses politik dan negosiasi tripartit di tingkat daerah, yang tidak
ditentukan oleh kondisi permintaan ekspor suatu industri 4 digit tertentu.

Strategi identifikasi ini mengikuti Ni & Kurita (2020), yang memanfaatkan variasi upah minimum
provinsi untuk mengidentifikasi pengaruh biaya tenaga kerja terhadap perilaku ekspor perusahaan
manufaktur Indonesia. Pemanfaatan upah minimum provinsi Indonesia sebagai sumber variasi
eksogen juga telah dilakukan Alatas & Cameron (2008) dan Magruder (2013).

### 3.4.2 Simultanitas harga ekspor

Harga dan kuantitas ekspor ditentukan secara bersamaan oleh perpotongan kurva penawaran dan
kurva permintaan. Estimasi OLS atas persamaan penawaran karenanya tidak mengidentifikasi kurva
penawaran, melainkan campuran dari kedua kurva — persoalan identifikasi simultan klasik yang
diformalkan Goldstein & Khan (1978).

Identifikasi kurva penawaran memerlukan variabel yang menggeser kurva **permintaan** namun
tidak menggeser kurva penawaran. Penelitian ini menggunakan **harga dunia produk sejenis** dan
**harga ekspor tertinggal satu periode** sebagai instrumen bagi $P_x$. Pendekatan ini mengikuti
Goldstein & Khan (1978) dan Kee, Nicita & Olarreaga (2008).

### 3.4.3 Pengujian validitas instrumen

Seluruh pengujian berikut dilaporkan apa pun hasilnya:

| Pengujian | Tujuan | Kriteria |
|---|---|---|
| First-stage $F$ | Kekuatan instrumen | $F > 10$ (Staiger & Stock, 1997) |
| Cragg–Donald Wald $F$ | Instrumen lemah | Dibandingkan nilai kritis Stock–Yogo |
| Hansen $J$ / Sargan | Over-identifikasi | $p > 0{,}10$ |
| Uji endogenitas | Perlu tidaknya IV | Menolak $H_0$ berarti IV diperlukan |

---

## 3.5 Metode Estimasi dan Uji Diagnostik

### 3.5.1 Rangkaian spesifikasi

Untuk menjamin transparansi, penelitian ini melaporkan enam spesifikasi secara berdampingan,
bukan hanya spesifikasi terpilih:

| Spesifikasi | Ukuran biaya tenaga kerja | Estimator |
|---|---|---|
| (1) | Upah rata-rata per pekerja | OLS |
| (2) | Upah produksi & non-produksi terpisah | OLS |
| (3) | Unit Labour Cost | OLS |
| (4) | ULC + interaksi sektor | OLS |
| (5) | **ULC diinstrumen — model utama** | **2SLS** |
| (6) | ULC + efek individu industri | Panel FE / Mundlak |

Penyajian seluruh rangkaian ini memungkinkan pembaca menelusuri bagaimana koefisien bergerak
seiring perbaikan spesifikasi, dan merupakan bentuk pertanggungjawaban atas pilihan model.
Spesifikasi (1) merupakan spesifikasi konvensional yang lazim digunakan penelitian terdahulu
dan disajikan sebagai pembanding dasar.

### 3.5.2 Estimator panel

Uji Hausman digunakan untuk memilih antara *fixed effects* dan *random effects*. Perlu dicatat
bahwa pada data ini sebagian besar variasi bersifat antar-industri dan bukan antarwaktu,
sehingga *fixed effects* menyerap porsi variasi yang besar dan berpotensi menurunkan presisi
estimasi. Sebagai jalan tengah, penelitian ini juga melaporkan estimasi dengan prosedur Mundlak
(1978), yang memasukkan rata-rata waktu dari setiap regresor ke dalam model *random effects*
sehingga konsistensi setara *fixed effects* dapat dicapai tanpa membuang variasi antar-industri.
Prosedur ini sekaligus mempertahankan identifikasi dummy sektor yang bersifat *time-invariant*,
sehingga tujuan penelitian kedua tetap dapat dijawab oleh model utama.

### 3.5.3 Standard error

Seluruh estimasi menggunakan standard error yang robust terhadap heteroskedastisitas, dan pada
spesifikasi panel di-*cluster* pada level industri. Pilihan ini didasarkan pada hasil uji
Breusch-Pagan/Cook-Weisberg yang menolak hipotesis homoskedastisitas.

### 3.5.4 Uji diagnostik

| Uji | Yang diperiksa |
|---|---|
| Variance Inflation Factor | Multikolinearitas |
| Breusch-Pagan / Cook-Weisberg | Heteroskedastisitas |
| Matriks korelasi | Hubungan antar regresor |
| Wooldridge | Autokorelasi (spesifikasi panel) |
| Pesaran CD | Dependensi antar unit (spesifikasi panel) |

---

## 3.6 Data dan Sumber Data

### 3.6.1 Cakupan

Penelitian ini menggunakan data panel industri manufaktur Indonesia pada level ISIC Rev.3
4 digit untuk periode **2007–2011**. Periode ini dipilih atas dua pertimbangan. Pertama,
periode tersebut mencakup masa pasca-krisis keuangan global 2008–2009, sehingga memungkinkan
pengamatan atas respons ekspor manufaktur Indonesia terhadap guncangan permintaan eksternal.
Kedua, pada periode tersebut Survei Industri Besar dan Sedang tersedia secara lengkap dan
konsisten dalam klasifikasi ISIC Rev.3, sehingga variabel dapat dibangun dengan definisi yang
seragam antar tahun.

Penggunaan data panel memberikan dua keunggulan dibandingkan data lintas seksi satu tahun:
jumlah observasi yang jauh lebih besar sehingga presisi estimasi meningkat, serta kemungkinan
mengendalikan karakteristik industri yang tidak teramati namun tetap antarwaktu.

### 3.6.2 Sumber data

| No | Data | Sumber | Keterangan |
|---|---|---|---|
| 1 | Volume dan nilai ekspor | UN Comtrade | Dikonversi dari HS 6 digit ke ISIC Rev.3 4 digit |
| 2 | Harga ekspor | UN Comtrade | *Unit value*, dirata-ratakan tertimbang nilai ekspor |
| 3 | Harga bahan baku impor | Kementerian Perindustrian | Dikonversi dari KBKI 9 digit ke ISIC Rev.3 4 digit |
| 4 | Biaya tenaga kerja, nilai tambah, kapital, kepemilikan asing, bahan baku impor | BPS — Survei Industri Besar dan Sedang | Data mikro level perusahaan, diagregasi ke ISIC 4 digit |
| 5 | Upah minimum provinsi | BPS / Kementerian Ketenagakerjaan | Untuk pembentukan variabel instrumen |
| 6 | Indeks Harga Konsumen | BPS | Deflator nilai nominal |
| 7 | Harga dunia produk sejenis | UN Comtrade | Instrumen bagi harga ekspor |

### 3.6.3 Konstruksi sampel

Sampel akhir diperoleh melalui tahapan penyaringan sebagai berikut:

| Tahap | Kriteria | Observasi tersisa |
|---|---|---|
| 1 | Seluruh industri manufaktur ISIC Rev.3 4 digit, 2007–2011 | *diisi* |
| 2 | Data ekspor tersedia pada Comtrade | *diisi* |
| 3 | Data harga bahan baku impor tersedia | *diisi* |
| 4 | Nilai tambah bernilai positif | *diisi* |
| 5 | Data tenaga kerja dan biaya tenaga kerja lengkap | *diisi* |
| 6 | Setelah winsorisasi persentil 1 dan 99 | **N akhir** |

> **Catatan penulisan:** kolom "observasi tersisa" diisi setelah rekonstruksi data selesai.
> Tabel ini wajib ada — pertanyaan mengenai asal-usul jumlah observasi hampir pasti diajukan
> penguji, dan tabel ini menjawabnya sebelum ditanyakan.

---

## 3.7 Keterbatasan Penelitian

**Pertama, keterbatasan identifikasi.** Meskipun upah minimum provinsi merupakan sumber variasi
yang secara teoretis eksogen terhadap permintaan ekspor industri tertentu, validitas instrumen
tetap bergantung pada asumsi bahwa penetapan upah minimum tidak dipengaruhi oleh kinerja ekspor
industri di provinsi bersangkutan. Asumsi ini tidak dapat diuji secara langsung, dan hasil uji
over-identifikasi dilaporkan sebagai indikasi tidak langsung.

**Kedua, keterbatasan pengukuran produktivitas.** Nilai tambah per pekerja merupakan ukuran
produktivitas tenaga kerja, bukan produktivitas total faktor. Ukuran ini tidak memisahkan
kontribusi kapital dari kontribusi tenaga kerja, sehingga industri padat kapital cenderung
menunjukkan produktivitas tenaga kerja yang lebih tinggi tanpa harus lebih efisien. Masuknya
variabel kapital dan dummy sektor ke dalam model mengurangi, namun tidak menghilangkan,
persoalan ini.

**Ketiga, keterbatasan agregasi.** Analisis dilakukan pada level industri, bukan perusahaan.
Heterogenitas antar perusahaan di dalam satu industri — yang menurut Yeaple (2004) dan Bernard,
Redding & Schott (2007) merupakan penentu penting keputusan ekspor — tidak dapat diamati.

**Keempat, keterbatasan harga.** Harga ekspor dan harga bahan baku impor merupakan rata-rata
tahunan, sehingga variasi harga di dalam tahun tidak tertangkap. Harga bahan baku impor juga
didekati dari bahan baku yang paling dominan pada setiap industri, bukan dari keseluruhan
komposisi input.

**Kelima, cakupan penentu ekspor.** Kinerja ekspor dipengaruhi banyak faktor di luar model ini,
antara lain kebijakan perdagangan negara tujuan, hambatan non-tarif, kualitas infrastruktur,
dan biaya logistik. Model ini berfokus pada penentu dari sisi penawaran sebagaimana dirumuskan
kerangka Riveros (1992).

---

# VARIAN 3.6 UNTUK PILIHAN A ATAU B

Bila desain lintas seksi satu tahun dipertahankan, ganti subbab 3.6.1 dengan teks berikut,
dan hapus $t$, $\delta_t$, serta $\mu_i$ dari persamaan (3.3):

> Penelitian ini menggunakan data lintas seksi industri manufaktur Indonesia pada level ISIC
> Rev.3 4 digit untuk tahun [2012 / 2011]. Tahun tersebut dipilih karena merupakan tahun
> terakhir Survei Industri Besar dan Sedang yang tersedia dalam klasifikasi ISIC Rev.3 secara
> lengkap dan konsisten dengan data ekspor Comtrade, sehingga seluruh variabel dapat dibangun
> dengan definisi yang seragam.
>
> Penggunaan data satu tahun membatasi kemampuan mengendalikan karakteristik industri yang
> tidak teramati. Keterbatasan ini dinyatakan secara eksplisit pada subbab 3.7 dan diatasi
> sebagian melalui strategi variabel instrumen pada subbab 3.4.

Pada Pilihan A atau B, subbab 3.5.2 (estimator panel) dihapus, dan spesifikasi (6) pada tabel
3.5.1 diganti menjadi spesifikasi dengan seluruh variabel kontrol tambahan.

---
---

# TAMBAHAN UNTUK BAB II

Tiga sisipan berikut melengkapi tinjauan pustaka agar sejalan dengan BAB III yang baru.

## Sisipan 1 — pada subbab Tinjauan Teori, setelah pembahasan Heckscher–Ohlin

> **Biaya tenaga kerja dan daya saing: dari tingkat upah menuju unit labour cost**
>
> Literatur daya saing internasional membedakan secara tegas antara tingkat upah dan biaya
> tenaga kerja per unit output. Tingkat upah yang tinggi tidak dengan sendirinya berarti daya
> saing yang rendah, sepanjang diimbangi produktivitas yang lebih tinggi. Landesmann & Poeschl
> (1996) serta Sharpe, Arsenault & Harrison (2008) menegaskan bahwa yang menentukan posisi
> bersaing suatu industri adalah laju pertumbuhan upah relatif terhadap laju pertumbuhan
> produktivitas.
>
> Golub & Edwards (2004) menerapkan kerangka ini pada industri manufaktur Afrika Selatan dan
> menemukan bahwa unit labour cost, bukan tingkat upah, yang berhubungan dengan kinerja ekspor.
> Ceglowski & Golub (2007, 2012) menunjukkan bahwa keunggulan biaya tenaga kerja Tiongkok jauh
> lebih kecil bila diukur dengan unit labour cost dibandingkan dengan tingkat upah, karena
> produktivitas Tiongkok tumbuh berdampingan dengan upahnya. IMF (2012) merekomendasikan
> pengukuran unit labour cost pada level industri karena agregasi pada level perekonomian
> mengaburkan perbedaan struktur produksi antar sektor.

## Sisipan 2 — pada subbab Tinjauan Empiris, setelah pembahasan Goldstein & Khan

> Ni & Kurita (2020) mengkaji hubungan antara upah minimum, ekspor, dan kinerja perusahaan
> manufaktur Indonesia pada periode 2002–2014. Dengan memanfaatkan variasi upah minimum antar
> provinsi sebagai sumber identifikasi, serta mengombinasikan estimasi *two-stage least squares*
> dengan *propensity score matching* dan *difference-in-differences* atas reformasi upah minimum
> 2012, mereka menemukan bahwa kenaikan upah minimum menurunkan probabilitas perusahaan
> melakukan ekspor, serta menurunkan penyerapan tenaga kerja, produktivitas, dan *markup*.
> Temuan tersebut menunjukkan bahwa biaya tenaga kerja berpengaruh terhadap daya saing ekspor
> manufaktur Indonesia apabila endogenitas upah ditangani secara memadai.
>
> Penggunaan upah minimum provinsi sebagai sumber variasi eksogen di Indonesia sebelumnya
> ditempuh Alatas & Cameron (2008) dan Magruder (2013), sedangkan Bird & Manning (2008)
> mengkaji dampaknya terhadap kesejahteraan rumah tangga.

## Sisipan 3 — pada subbab Tinjauan Empiris, di bagian akhir

> Amiti & Konings (2007) menunjukkan bahwa penurunan tarif bahan baku meningkatkan
> produktivitas perusahaan manufaktur Indonesia dua kali lipat lebih besar dibandingkan
> penurunan tarif barang jadi, sehingga akses terhadap bahan baku impor merupakan penentu
> penting kemampuan bersaing. Brambilla & Porto (2017) menemukan adanya *export wage premium*
> yang konsisten di negara berkembang, yang menegaskan bahwa hubungan antara upah dan ekspor
> bersifat dua arah dan tidak dapat diestimasi secara memadai tanpa strategi identifikasi.

---

# TAMBAHAN DAFTAR PUSTAKA

**Entri baru:**

- Alatas, V., & Cameron, L. A. (2008). The impact of minimum wages on employment in a low-income country: A quasi-natural experiment in Indonesia. *Industrial and Labor Relations Review*, 61(2), 201–223.
- Amiti, M., & Konings, J. (2007). Trade liberalization, intermediate inputs, and productivity: Evidence from Indonesia. *American Economic Review*, 97(5), 1611–1638.
- Bird, K., & Manning, C. (2008). Minimum wages and poverty in a developing country: Simulations from Indonesia's household survey. *World Development*, 36(5), 916–933.
- Brambilla, I., & Porto, G. (2017). Examining the export wage premium in developing countries. *Review of International Economics*, 25(3), 447–475.
- Ceglowski, J., & Golub, S. S. (2007). Just how low are China's labour costs? *The World Economy*, 30(4), 597–617.
- Ceglowski, J., & Golub, S. S. (2012). Does China still have a labor cost advantage? *Global Economy Journal*, 12(3).
- Hausman, J. A., & Taylor, W. E. (1981). Panel data and unobservable individual effects. *Econometrica*, 49(6), 1377–1398.
- International Monetary Fund. (2012). *Assessing competitiveness using industry unit labor costs: An application to Slovakia* (IMF Working Paper No. 12/107). Washington, DC: IMF.
- Kee, H. L., Nicita, A., & Olarreaga, M. (2008). Import demand elasticities and trade distortions. *The Review of Economics and Statistics*, 90(4), 666–682.
- Koenker, R., & Bassett, G. (1978). Regression quantiles. *Econometrica*, 46(1), 33–50.
- Landesmann, M., & Poeschl, J. (1996). *Balance-of-payments constrained growth in Central and Eastern Europe*. Vienna Institute for International Economic Studies.
- Magruder, J. R. (2013). Can minimum wages cause a big push? Evidence from Indonesia. *Journal of Development Economics*, 100(1), 48–62.
- Mundlak, Y. (1978). On the pooling of time series and cross section data. *Econometrica*, 46(1), 69–85.
- Ni, B., & Kurita, K. (2020). The minimum wage, exports, and firm performance: Evidence from Indonesia. *Journal of Asian Economics*, 69, 101218.
- Staiger, D., & Stock, J. H. (1997). Instrumental variables regression with weak instruments. *Econometrica*, 65(3), 557–586.

**Perbaikan entri yang rusak** — nama penulis terbalik akibat mesin sitasi:

| Tertulis sekarang | Perbaikan |
|---|---|
| `Amiti, M. &. (2011)` | Amiti, M., & Davis, D. R. (2011). Trade, firms, and wages: Theory and evidence. *Review of Economic Studies*, 79(1), 1–36. |
| `Jensen, B. &. (1997)` | Bernard, A. B., & Jensen, J. B. (1997). Exporters, skill upgrading, and the wage gap. *Journal of International Economics*, 42(1–2), 3–31. |
| `Khan, M. &. (1978)` | Goldstein, M., & Khan, M. S. (1978). The supply and demand for exports: A simultaneous approach. *The Review of Economics and Statistics*, 60(2), 275–286. |
| `Sun, A. M. (2013)` | Mehta, A., & Sun, W. (2013). Does industry affiliation influence wages? Evidence from Indonesia and the Asian financial crisis. *World Development*, 51, 47–61. |
| `Putra, D. N. (2014)` | Narjoko, D., & Putra, C. T. (2014). Industrialization, globalization and labor market regime in Indonesia. *Journal of the Asia Pacific Economy*, 19(1), 57–76. |
| `Hill, D. N. (2007)` | Narjoko, D., & Hill, H. (2007). Winners and losers during a deep economic crisis: Firm-level evidence from Indonesian manufacturing. *Asian Economic Journal*, 21(4), 343–368. |
| `Haryo Aswicahyono, H. H. (2010)` | Aswicahyono, H., Hill, H., & Narjoko, D. (2010). Industrialisation after a deep economic crisis: Indonesia. *The Journal of Development Studies*, 46(6), 1084–1108. |

**Dikutip di naskah tetapi belum ada di daftar pustaka** — perlu dilengkapi:

- Hill, H. (2000). *The Indonesian economy* (2nd ed.). Cambridge University Press.
- Landesmann & Poeschl (1996) — lihat entri baru di atas
- Thorbecke, W. (2006) — dikutip pada perumusan masalah; hanya Thorbecke (2010) yang terdaftar

**Konsistensi yang perlu diperbaiki:** Yeaple dikutip sebagai (2004) di teks namun terdaftar
(2005); Narjoko & Putra dikutip sebagai (2010) dan (2014) pada dua tempat berbeda.

---

# LANGKAH BERIKUTNYA

Naskah di atas siap disisipkan ke `draftp Proposal tesis 4c.docx`. Saya sarankan **tidak
langsung menimpa berkas aslinya** — lebih baik saya buatkan versi baru (`4d.docx`) sehingga
Anda dapat membandingkan keduanya dan membawa perbandingannya ke pembimbing.

Yang saya perlukan dari Anda sebelum penyisipan:

1. **Keputusan Pilihan A, B, atau C** — menentukan subbab 3.6 mana yang dipakai
2. **Persetujuan pembimbing atas arah ULC dan strategi instrumen** — perubahan ini cukup
   mendasar untuk dikonfirmasi lebih dulu, dan Bagian 7 dokumen `07` memuat kalimat yang bisa
   Anda pakai saat menghadap
