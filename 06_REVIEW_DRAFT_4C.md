# REVIEW DRAFT 4C — TEMUAN DAN PERBAIKAN

**Berkas:** `draftp Proposal tesis 4c.docx` (376 paragraf, 5 tabel, 982 KB)
**Tanggal review:** 11 September 2026
**Pembanding:** `rev4b.docx`, `komparasi hasil regresi.docx`, `test asumsi.docx`, `catatan bimbingan.txt`

---

## RINGKASAN — DAN KOREKSI ATAS AUDIT SAYA SENDIRI

Saya perlu meralat premis dasar dari dua audit saya sebelumnya.

**Draft 4c bukan revisi kecil dari rev4b. Ini penelitian yang berbeda.**

| | rev4b | **4c** |
|---|---|---|
| Desain | Panel 2007–2012 | **Cross-section 2012 saja** |
| Variabel terikat | `lnEkspor` (nilai) | **`lnVolume` (kuantitas)** |
| Metode | Panel (FE/RE, 2SLS) | **OLS** |
| N | 643 / 108 industri | **100** |
| Paragraf | 492 | 376 |

Dua audit saya sebelumnya menilai naskah ini sebagai studi panel yang eksekusinya gagal.
Itu keliru. Anda **memutuskan meninggalkan panel** dan menulis ulang tesis sebagai studi
cross-section 2012 — dan keputusan itu justru mengikuti arahan pembimbing, yang menulis:

> *"cari argumen mengapa di tahun 2012, bukan kenaikan upah tapi apakah perbedaan upah
> antar sektor bisa menjadi perbedaan nilai ekspor yang berbeda"*

Pembimbing mengarahkan Anda ke perbandingan antar sektor pada satu titik waktu. Draft 4c
adalah jawaban atas arahan itu. Rekomendasi saya sebelumnya soal fixed effects dan interaksi
upah × sektor dibangun di atas premis panel, jadi sebagian besar tidak berlaku untuk naskah ini.

### Dan ini kabar baik yang besar

**Tabel 4.2 di draft 4c bersih secara aritmetik.** Saya hitung ulang `t = koef ÷ SE` untuk
sembilan barisnya: **sembilan-sembilannya cocok** (satu selisih 0,008 murni akibat pembulatan
koefisien ke tiga desimal).

Lebih jauh, saya berhasil **membalik jumlah observasi dari R² dan adjusted R²**:

```
(1 − adj R²) = (1 − R²) × (n−1)/(n−k−1)
(1 − 0,5421) = (1 − 0,5791) × (n−1)/(n−9)      →   n = 100,0
Uji silang:  F = (R²/k) / ((1−R²)/(n−k−1)) = 15,65   ← persis seperti dilaporkan
```

**N = 100, k = 8, dan seluruh statistik model saling konsisten.**

Artinya: **temuan paling berbahaya dari audit pertama saya — Tabel 4.2 sebagai gabungan tiga
regresi — sudah Anda perbaiki sendiri di draft 4c.** Anda mengerjakan naskah yang salah selama
ini; kerusakan itu tinggal di rev4b, bukan di sini.

Penilaian kesiapan sidang untuk 4c: **sekitar 65%**, bukan 45%.

Yang tersisa sebagian besar bersifat **konsistensi internal, kelengkapan, dan redaksional** —
bukan kerusakan fundamental. Dua di antaranya tetap serius dan harus diselesaikan.

---

# A. TEMUAN KRITIS

## A1. BAB V bertentangan dengan Tabel 4.2 sendiri — tanda koefisien terbalik

Ini temuan paling berbahaya yang tersisa.

Tabel 4.2 melaporkan `lnavgWPekerja = **+0,074**` — **positif**.

Tetapi BAB V menulis:

> [5.1] *"hasil regresi menunjukkan bahwa **kenaikan upah tenaga kerja akan mengurangi**
> kinerja ekspor industri manufaktur Indonesia"*

> [5.2] *"adanya **pengaruh negatif** namun tidak signifikan antara rata-rata upah tenaga kerja
> dengan kinerja industri manufaktur Indonesia"*

Naskah mengklaim pengaruh negatif dua kali, sementara tabelnya sendiri menunjukkan positif.
Penguji yang membandingkan BAB V dengan Tabel 4.2 akan menemukan ini dalam hitungan detik,
dan pertanyaannya akan tajam: "Anda membaca tabel Anda sendiri, atau menulis apa yang Anda
harapkan?"

**Perbaikan:** hapus seluruh klaim arah negatif. Kalimat yang benar:

> Koefisien upah rata-rata tenaga kerja bertanda positif (0,074) namun **tidak signifikan**
> secara statistik (p = 0,855). Dengan demikian penelitian ini **tidak menemukan bukti** bahwa
> tingkat upah memengaruhi kinerja ekspor industri manufaktur Indonesia pada tahun 2012, baik
> ke arah positif maupun negatif.

Perlu ditegaskan: **koefisien tidak signifikan tidak punya arah.** Menafsirkan tandanya adalah
kesalahan statistik dasar, dan itulah yang sekarang dilakukan BAB V. Justru kalimat "tidak
ditemukan bukti pengaruh" lebih kuat dan lebih aman dipertahankan.

## A2. Narasi BAB IV mengutip angka dari regresi yang berbeda

Tiga angka dalam narasi BAB IV tidak berasal dari Tabel 4.2:

| Kalimat di naskah | Angka disebut | Tabel 4.2 | Asal sebenarnya |
|---|---|---|---|
| [328] *"kenaikan kepemilikan asing 1 persen meningkatkan ekspor rata-rata 0,78 persen"* | **0,78** | `lnAsing = 0,390` | regresi `lnEkspor` N=105 di `test asumsi.docx` (`lnAsing = 0,7759`) |
| [331] labor intensive *"rata-rata sebesar 0,245 lebih rendah"* | **0,245** | `LaborIntensive = −0,341` | regresi `lnEkspor` N=105 (`laborIntensive = −0,2446`) |
| [331] capital intensive *"sebesar 0,43 lebih rendah"* | **0,43** | `CapitalIntensive = −0,433` | kebetulan cocok |

Dua dari tiga angka diambil dari regresi dengan **variabel terikat berbeda** (`lnEkspor`, bukan
`lnVolume`) dan **sampel berbeda** (105, bukan 100). Ini sisa dari kebiasaan menyalin manual
yang merusak Tabel 4.2 di rev4b — polanya sama, hanya skalanya lebih kecil.

**Perbaikan:** ganti 0,78 → 0,390 dan 0,245 → 0,341. Dan pastikan tidak ada satu angka pun di
BAB IV yang tidak bisa ditunjuk langsung ke barisnya di Tabel 4.2.

## A3. Tabel 4.2 tidak mencantumkan jumlah observasi

Tabel melaporkan R², adj R², F, dan Prob > F — tetapi **tidak ada baris "Number of obs"**.

Ini pertanyaan pertama penguji mana pun. Lebih buruk lagi, karena N tidak tercantum, tidak ada
tempat di naskah yang menyatakan berapa industri yang sebenarnya dianalisis. BAB III menyebut
ISIC 1511–3699 (seharusnya sekitar 100–130 industri 4 digit), tetapi angka finalnya tidak
pernah muncul.

**Perbaikan:** tambahkan `Number of obs = 100` ke Tabel 4.2, dan tambahkan satu paragraf di
BAB III yang menjelaskan alur penyaringan: dari sekian industri ISIC 4 digit awal, berapa yang
gugur karena data ekspor tidak tersedia, berapa karena data bahan baku impor tidak tersedia,
sampai tersisa 100.

## A4. Upah dibiarkan satu variabel — arahan pembimbing yang paling tegas belum dijalankan

Judul subbab 4.2.1 berbunyi:

> *"Pengaruh upah tenaga kerja **produksi dan non produksi** terhadap kinerja ekspor"*

dan paragraf [318] menulis *"menunjukan bahwa **kedua variabel** tidak berpengaruh secara
signifikan"*.

Tetapi Tabel 4.2 hanya memuat **satu** variabel upah: `lnavgWPekerja`. Judul dan narasi
menjanjikan dua, tabelnya menyajikan satu. BAB III pun hanya mendefinisikan satu (`w`).

Ini persis arahan pertama pembimbing:

> *"total pengeluaran dibagi 2: (1) total upah tenaga kerja produksi, (2) total upah tenaga
> kerja non produksi"*

**Anda sebenarnya sudah mengerjakannya.** Di `test asumsi.docx` ada regresi yang sudah memisahkan
keduanya, dengan variabel terikat dan sampel yang sesuai:

```
reg lnVolume lnPx lnPm lnavgWProd lnavgWPlain lnTotTK lnAsing laborIntensive capitalIntensive
N = 105    F(8,96) = 16.44    R² = 0.5780    Adj R² = 0.5429

lnavgWProd       |   .5340948   .4514793     1.18   0.240
lnavgWPlain      |  -.4674366   .4175746    -1.12   0.266
```

Hasilnya belum pernah masuk naskah, padahal **pola tandanya menarik**: upah produksi positif
(+0,53), upah non-produksi negatif (−0,47) — meski keduanya tidak signifikan.

**Perbaikan:** jadikan ini **kolom kedua Tabel 4.2**, berdampingan dengan spesifikasi upah
gabungan. Dengan begitu judul subbab menjadi benar, arahan pembimbing terpenuhi, dan naskah
punya satu tabel dengan dua spesifikasi — jauh lebih meyakinkan daripada satu kolom tunggal.

*Catatan:* sampelnya 105, bukan 100. Perbedaan ini harus dijelaskan (kemungkinan karena
`lnCapital` tidak masuk di spesifikasi itu), atau kedua spesifikasi dijalankan ulang pada
sampel yang sama.

## A5. Analisis deskriptif: angka upah produksi tidak bisa direproduksi dari Tabel 4.1

Saya menghitung ulang seluruh angka turunan di bagian deskriptif. Hasilnya terbelah rapi:

**Upah non-produksi — cocok sempurna:**

| Sektor | Biaya ÷ pekerja | Naskah | |
|---|---|---|---|
| Resource | 12,65 T ÷ 327.663 = **38,6 jt** | 38,6 jt | ✅ |
| Labor | 12,34 T ÷ 292.306 = **42,2 jt** | 42,2 jt | ✅ |
| Capital | 9,99 T ÷ 165.868 = **60,2 jt** | 60,2 jt | ✅ |

**Upah produksi — tidak satu pun cocok:**

| Sektor | Biaya ÷ pekerja | Naskah | Selisih |
|---|---|---|---|
| Resource | 29,84 T ÷ 1.441.078 = **20,7 jt** | 25,3 jt | +22% |
| Labor | 34,84 T ÷ 1.879.830 = **18,5 jt** | 21,8 jt | +18% |
| Capital | 23,56 T ÷ 792.583 = **29,7 jt** | 38,7 jt | +30% |

Selisihnya tidak proporsional (22%, 18%, 30%), jadi bukan sekadar salah faktor konversi.
Salah satu dari dua hal terjadi: **baris biaya tenaga kerja produksi di Tabel 4.1 salah**, atau
angka di narasi dihitung dari sumber lain.

Ini berbahaya karena narasi Anda membangun argumen di atasnya — bahwa sektor capital intensive
membayar upah tertinggi. Kesimpulan itu tetap benar dengan angka mana pun (29,7 tetap
tertinggi), tetapi penguji yang membawa kalkulator akan menemukan ketidakcocokannya.

**Perbaikan:** hitung ulang dari data sumber, lalu **tambahkan kolom "rata-rata per pekerja"
langsung ke dalam Tabel 4.1** sehingga angkanya tidak lagi hidup terpisah di narasi.

*Yang lain sudah benar:* rasio kepemilikan asing cocok persis untuk ketiga sektor (1,00%,
1,33%, 2,82%), dan total tenaga kerja labor intensive (2.172.136) cocok dengan penjumlahan.

## A6. Satuan Gambar 4.1 hampir pasti salah — "juta kg" seharusnya "juta ton"

Narasi [285]–[287] menyebut volume dalam **juta kg** dengan nilai dalam triliun rupiah. Saya
hitung harga implisit per kilogram dari setiap pasangan angka:

| Industri | Jika "juta kg" | Jika "juta ton" |
|---|---|---|
| Resource primer | USD **942**/kg | USD 0,94/kg |
| Kertas & minyak bumi | USD **743**/kg | USD 0,74/kg |
| Tekstil, garmen, alas kaki | USD **3.151**/kg | USD 3,15/kg |
| Mesin & transportasi | USD **9.795**/kg | USD 9,79/kg |
| Elektronika | USD **28.365**/kg | USD 28,36/kg |

Kolom "juta kg" absurd — minyak sawit seharga USD 942 per kilogram. Kolom "juta ton"
**seluruhnya masuk akal** dan sesuai harga komoditas 2012: CPO sekitar USD 0,9/kg, tekstil
USD 3/kg, elektronika USD 28/kg.

Perhitungan ini sekaligus memvalidasi dua hal lain: kurs yang Anda pakai (Rp 9.386,63 per USD)
memang rata-rata 2012 yang benar, dan angka nilai perdagangan Anda konsisten.

**Perbaikan:** ganti seluruh "juta kg" menjadi "juta ton" di paragraf [285]–[287] dan pada
sumbu Gambar 4.1. Periksa juga BAB III [214] yang menyatakan volume "dalam kg" — mungkin benar
untuk data mentahnya, tetapi angka agregat di BAB IV jelas dalam ton.

---

# B. TEMUAN SEDANG

## B1. BAB V terlalu tipis dan tidak menjawab tujuan penelitian satu per satu

Kesimpulan hanya empat paragraf, saran dua paragraf. Untuk tesis magister ini kurang.

Yang hilang: jawaban eksplisit terhadap tiap tujuan penelitian, keterbatasan (BAB III punya
bagian keterbatasan, BAB V tidak mengulanginya sebagai kualifikasi kesimpulan), dan agenda
riset lanjutan yang konkret.

Implikasi kebijakannya juga terlalu lembut. Dengan upah tidak signifikan sementara `lnTotTK`,
`lnCapital` dan `lnAsing` semuanya signifikan, pesan yang bisa Anda sampaikan sebenarnya tajam
dan relevan sampai hari ini:

> Pada tahun 2012, tingkat upah tenaga kerja **tidak terbukti** menjadi penentu kinerja ekspor
> industri manufaktur Indonesia. Yang terbukti menentukan adalah **skala industri** (jumlah
> tenaga kerja), **intensitas kapital**, dan **kepemilikan asing**. Implikasinya: kebijakan
> menahan upah bukan instrumen yang efektif untuk mendorong daya saing ekspor; yang lebih
> menentukan adalah skala, akumulasi kapital, dan keterhubungan dengan jaringan produksi global.

Itu pesan yang menjawab langsung perdebatan upah minimum yang masih berlangsung di Indonesia,
dan jauh lebih layak dipertahankan daripada kesimpulan yang sekarang.

## B2. Uji asumsi sudah ada tetapi tidak dilaporkan

`test asumsi.docx` memuat VIF (mean 1,52; maks 1,90 — aman), Breusch-Pagan/Cook-Weisberg
(χ²(1) = 5,04; p = 0,0248 — ada heteroskedastisitas), dan matriks korelasi lengkap. Tidak satu
pun masuk naskah 4c.

Untuk tesis magister ekonometrika terapan, bagian uji asumsi wajib ada. Dan kabar baiknya,
Anda tinggal memindahkannya:

- **VIF aman** → bisa dinyatakan dengan percaya diri bahwa multikolinearitas bukan masalah
- **Heteroskedastisitas terdeteksi** → ini justru **alasan empiris** untuk melaporkan
  standard error robust, bukan kelemahan. Tabel 4.2 sebaiknya memakai SE robust, dan Anda
  sudah punya hasilnya untuk spesifikasi `lnEkspor`

Satu catatan: di `test asumsi.docx`, judul "test autokorelasi" ternyata diikuti perintah `vif`
(multikolinearitas). **Uji autokorelasi tidak pernah dijalankan** — tetapi pada data
cross-section memang tidak relevan, jadi cukup tidak disebut sama sekali.

## B3. Statistik deskriptif variabel belum ada

Pembimbing meminta ini dua kali, dengan daftar rinci. BAB IV punya narasi deskriptif yang cukup
baik tentang pola ekspor dan karakteristik industri, tetapi **tidak ada satu pun tabel
statistik deskriptif variabel** — mean, median, standar deviasi, min, maks untuk setiap
variabel yang masuk regresi.

Ini tabel standar yang ada di hampir semua tesis empiris, dan ketiadaannya akan langsung
terlihat. Tambahkan sebagai Tabel 4.1 (menggeser yang lain), dalam satuan asli — bukan log.

Permintaan pembimbing lain yang masih kosong: perbedaan harga ekspor antar industri, dan
grafik per variabel.

## B4. Tujuan penelitian hanya satu, kesimpulan menjawab empat

Paragraf [89]–[90] menyebut satu tujuan umum dan **satu** tujuan khusus (membandingkan kinerja
ekspor antar klasifikasi sektor). Tetapi BAB V menarik kesimpulan tentang upah, harga ekspor,
harga bahan baku, karakteristik industri, dan perbedaan antar sektor — lima hal.

**Perbaikan:** naikkan tujuan penelitian menjadi dua atau tiga butir yang sejajar dengan isi
BAB IV, misalnya: (1) mengestimasi pengaruh upah terhadap penawaran ekspor; (2) membandingkan
kinerja ekspor antar klasifikasi sektor; (3) mengidentifikasi karakteristik industri yang
menentukan kinerja ekspor. Lalu BAB V menjawab ketiganya, berurutan, satu subbagian masing-masing.

## B5. Endogenitas tidak dibahas, padahal 2SLS-nya sudah ada

Naskah 4c seluruhnya OLS. Tidak ada pembahasan bahwa harga ekspor (`Px`) ditentukan bersama
dengan kuantitas ekspor — masalah identifikasi simultan klasik, yang justru sudah Anda kutip
sendiri lewat **Goldstein & Khan (1978)** di BAB II [195]–[196].

Dan Anda sudah menjalankan solusinya. Di `komparasi hasil regresi.docx`:

```
ivregress 2sls lnVolume (lnPx = lnPxWorld lnGdp lnPx_1) lnPm lnAvgWProd lnAvgWPlain ...
N = 100                   ← sampel yang sama dengan Tabel 4.2

lnPx  |  -.2598802   .0898666   -2.89   0.004
```

Bandingkan dengan OLS di Tabel 4.2: `lnPx = −0,247`. Setelah instrumentasi menjadi **−0,260**.
Bergerak ke arah yang diperkirakan teori, dan tetap signifikan.

**Ini peluang terbesar yang tersisa di naskah Anda.** Menambahkan satu kolom 2SLS ke Tabel 4.2
akan: menunjukkan Anda sadar akan endogenitas, membuktikan hasil Anda robust terhadapnya, dan
menutup satu pertanyaan penguji sebelum ditanyakan. Sampelnya sudah sama (N = 100), jadi
kolomnya tinggal ditempelkan.

Yang perlu diakui jujur: `lnGdp` gugur karena kolinearitas sehingga tersisa dua instrumen, dan
belum ada uji kekuatan instrumen. Nyatakan itu sebagai keterbatasan — jauh lebih baik diakui
sendiri daripada dibongkar.

## B6. `lnCapital` masuk model tetapi tidak pernah didefinisikan

Persamaan model di BAB III [210] memuat `a5Capitali`. Tetapi daftar "Dimana:" [213]–[229]
melompat dari `totTK` langsung ke `Asing` — **definisi `Capital` tidak ada**. Bagian
Definisi Operasional [244]–[263] juga tidak memuatnya. Tabel 3.2 (hipotesis) juga melewatkannya.

Padahal `lnCapital` signifikan pada 5% di Tabel 4.2 (koef 0,231; p = 0,025) dan dibahas di
BAB V. Sebuah variabel yang signifikan tetapi tidak pernah didefinisikan adalah celah yang
mudah sekali ditemukan penguji.

**Perbaikan:** tambahkan definisi `Capital` di ketiga tempat — daftar notasi, Definisi
Operasional (jelaskan sumbernya dari BPS dan cara agregasinya), dan Tabel 3.2 dengan hipotesis
tanda positif.

## B7. Tabel 3.2 (hipotesis) rusak dan tidak lengkap

Tiga masalah dalam satu tabel kecil:

1. Baris "Harga impor bahan baku" — **kolom Pengaruh kosong**, seharusnya bertanda `−`
2. "Upah tenaga kerja" muncul **dua kali, keduanya bernomor 3**, satu dengan `−` dan satu
   dengan `+`, tanpa penjelasan mengapa ada dua hipotesis berlawanan
3. `Capital`, `laborIntensive`, dan `capitalIntensive` **tidak ada sama sekali**

Poin 2 sebenarnya bisa diubah menjadi kekuatan. Dua tanda berlawanan itu bukan kebingungan,
melainkan dua mekanisme teoretis yang bersaing — dan itu justru inti pertanyaan penelitian Anda:

> **H3a (Riveros 1992):** upah ↑ → biaya produksi ↑ → penawaran ekspor ↓ (tanda negatif)
> **H3b (Bernard & Jensen 1997; Amiti & Davis 2011):** upah ↑ mencerminkan produktivitas dan
> kualitas tenaga kerja yang lebih tinggi → penawaran ekspor ↑ (tanda positif)
>
> Penelitian ini menguji mana yang dominan pada industri manufaktur Indonesia.

Dirumuskan begitu, hasil "tidak signifikan" menjadi temuan yang bermakna — kedua mekanisme
kemungkinan saling meniadakan — bukan kegagalan menemukan sesuatu.

## B8. Level agregasi ISIC masih bertabrakan

- BAB III [213]: *"industri berdasarkan ISIC rev.3 (**4 digit**)"*
- Tabel 3.1: kolom berjudul *"**ISIC 2 digit**"*, memuat 22 baris kode 15–36
- Definisi operasional [245]–[260]: konsisten menyebut 4 digit

Tabel 3.1 sebenarnya tidak salah — ia memetakan kelompok 2 digit ke klasifikasi sektor, lalu
klasifikasi itu diturunkan ke industri 4 digit. Tetapi naskah tidak pernah menyatakannya.

**Perbaikan:** satu kalimat setelah Tabel 3.1: *"Pengelompokan sektor dilakukan pada level
ISIC 2 digit, kemudian klasifikasi tersebut diterapkan ke seluruh industri 4 digit yang berada
di bawahnya. Unit analisis penelitian ini adalah industri ISIC Rev.3 4 digit."* Selesai.

## B9. Penomoran tabel dan gambar

- **Dua tabel bernomor 4.2.** Tabel karakteristik industri [305] diberi caption "Tabel 4.2",
  padahal narasi [293]–[294] merujuknya sebagai "Tabel 4.1". Caption harus diperbaiki menjadi
  **Tabel 4.1**.
- Caption ditulis *"Tabel 4.2.karakteristik"* — tanpa spasi, huruf kecil.
- **Gambar 1.3** ditulis *"Gambar 1. 3"* dengan spasi menyimpang.
- **Persamaan (2.7) dipakai dua kali**, di [179] dan [183].
- Persamaan model di BAB III [210] **tidak bernomor**, seharusnya (3.1).
- Gambar 1.3 dirujuk di [75] sebelum muncul di [78] — urutannya benar, tetapi [76] membahas
  isinya sebelum gambarnya muncul. Pindahkan gambar ke atas paragraf [76].

## B10. Daftar pustaka: 20 entri, tujuh di antaranya nama penulisnya rusak

Riveros (1992) sekarang **sudah ada** — perbaikan penting dari rev4b. Tetapi mesin sitasi
membalik nama penulis pada tujuh entri:

| Tertulis | Seharusnya |
|---|---|
| `Amiti, M. &. (2011)` | Amiti, M., & Davis, D. R. |
| `Jensen, B. &. (1997)` | Bernard, A. B., & Jensen, J. B. |
| `Khan, M. &. (1978)` | Goldstein, M., & Khan, M. S. |
| `Sun, A. M. (2013)` | Mehta, A., & Sun, W. |
| `Putra, D. N. (2014)` | Narjoko, D., & Putra, C. T. |
| `Hill, D. N. (2007)` | Narjoko, D., & Hill, H. |
| `Haryo Aswicahyono, H. H. (2010)` | Aswicahyono, H., Hill, H., & Narjoko, D. |

**Dikutip di teks tetapi tidak ada di daftar pustaka:**
Hill (2000) [59] · Landesman & Poessch (1996) [82] · Thorbecke (2006) [85] — hanya Thorbecke
(2010) yang terdaftar

**Ada di daftar pustaka tetapi tidak pernah dikutip:**
Asian Development Bank (2007) · Atukorala (2006) · Farole & Winkler (2012) ·
Aswicahyono, Brooks & Manning (2011)

**Tahun tidak konsisten:** Yeaple dikutip (2004) di [73], terdaftar (2005). Narjoko & Putra
dikutip (2010) di [73] dan (2014) di [231].

**Jumlah:** 20 entri. Untuk tesis magister, wajar 35–50. Perlu tambahan literatur 2015–2025
tentang daya saing ekspor Indonesia, deindustrialisasi dini, dampak upah minimum di Indonesia,
dan integrasi rantai nilai global.

---

# C. TEMUAN RINGAN — REDAKSIONAL

**Ejaan nama teori tidak konsisten dalam satu dokumen:**
"Heckser-Ohlin" [60] · "Heckshcer-Ohlin" [106] · "Heckscher – Ohlin" [107].
Yang benar: **Heckscher–Ohlin**.

**Nama peneliti salah tulis di teks:**
"Metha" → Mehta [73] · "Amirti" → Amiti [74] · "Nardjoko" → Narjoko [73] ·
"Sugiyanto" → Sugiyarto [75] · "Thorbecker" (di rev4b).

**Salah ketik:**
"relative" → relatif [60, 82] · "endownment" → endowment [106] · "pengelompokkan" →
pengelompokan [284] · "resourve" → resource [296] · "mengena" → mengenai [345] ·
"Hasi studi" → Hasil studi [197] · "perode" → periode [195] · "outoput" → output [185] ·
"pernjualan" → penjualan [154] · "negar-negara" → negara-negara [193] ·
"2.172136" → 2.172.136 [297] · "studi literature" → studi literatur [97] ·
"topic penelitian" → topik penelitian [97] · "harga domestic" → harga domestik [197] ·
"negative" → negatif [193, 196].

**Penomoran bab tidak konsisten:** "BAB 1", "BAB 2", "BAB 3", "BAB 4" (angka Arab) versus
"BAB V" (angka Romawi). Pedoman UI menggunakan angka Romawi — seragamkan menjadi BAB I–V.

**Penomoran subbab hilang:** BAB 1 dan BAB 2 memakai judul tanpa nomor ("Latar Belakang",
"Tinjauan Teori") padahal "2.1.1" muncul di [104]; BAB 3 langsung memakai "3.3" dan "3.4"
tanpa 3.1 dan 3.2. Seragamkan seluruhnya.

**Notasi tidak konsisten** dalam satu persamaan [210]: `α0, α1, α2, α3, α4` lalu berganti
menjadi `a5, a6, a7, a8`. Dan `a7DLaborIntensiveo` memuat huruf "o" yang tidak seharusnya ada.

**Angka tidak cocok antara tabel dan teks:** Tabel 4.1 menulis tenaga kerja produksi labor
intensive **1.879.830**, narasi [295] menulis **1.879.839**. Tabel menulis biaya non-produksi
capital intensive **9,99** triliun, narasi [300] membulatkannya menjadi **10** triliun.

**Kesalahan logika di [300]:** *"sektor industri labor intensive memiliki pengeluaran terbesar
sebesar 12,34 triliun"* — padahal kalimat berikutnya menyebut resource intensive **12,65**
triliun, yang lebih besar. Yang terbesar adalah resource intensive.

---

# D. URUTAN KERJA YANG SAYA SARANKAN

Diurutkan berdasarkan dampak terhadap kelulusan sidang dibagi usaha yang diperlukan.

### Tahap 1 — Perbaikan yang tidak butuh data sama sekali *(paling mendesak)*

| # | Pekerjaan | Rujukan |
|---|---|---|
| 1 | Balik arah klaim upah di BAB V — dari "negatif" menjadi "tidak ditemukan bukti pengaruh" | A1 |
| 2 | Ganti 0,78 → 0,390 dan 0,245 → 0,341 di BAB IV | A2 |
| 3 | Tambahkan `Number of obs = 100` ke Tabel 4.2 | A3 |
| 4 | Ganti "juta kg" → "juta ton" di seluruh narasi Gambar 4.1 | A6 |
| 5 | Perbaiki caption Tabel 4.1, penomoran persamaan, penomoran bab | B9, C |
| 6 | Perbaiki tujuh nama penulis yang rusak di daftar pustaka; tambahkan tiga yang hilang | B10 |
| 7 | Seragamkan ejaan Heckscher–Ohlin dan nama peneliti; bersihkan salah ketik | C |
| 8 | Lengkapi Tabel 3.2 dan rumuskan ulang hipotesis upah sebagai H3a vs H3b | B7 |
| 9 | Tambahkan definisi `Capital` di tiga tempat | B6 |
| 10 | Tambahkan satu kalimat penjelas agregasi ISIC setelah Tabel 3.1 | B8 |

Ini semua bisa saya kerjakan langsung pada berkasnya.

### Tahap 2 — Merakit dari hasil yang sudah ada *(tanpa `.dta`)*

| # | Pekerjaan | Sumber |
|---|---|---|
| 11 | Tambahkan kolom upah produksi/non-produksi ke Tabel 4.2 | `test asumsi.docx` |
| 12 | Tambahkan kolom 2SLS ke Tabel 4.2 + pembahasan endogenitas | `komparasi hasil regresi.docx` |
| 13 | Tambahkan subbab uji asumsi: VIF, Breusch-Pagan, matriks korelasi | `test asumsi.docx` |
| 14 | Tulis ulang BAB V — jawab tiap tujuan, implikasi kebijakan yang tajam, keterbatasan, agenda riset | — |
| 15 | Naikkan tujuan penelitian menjadi tiga butir yang sejajar dengan BAB IV | B4 |

### Tahap 3 — Butuh data

| # | Pekerjaan |
|---|---|
| 16 | Rekonsiliasi angka upah produksi di Tabel 4.1 (A5) |
| 17 | Tabel statistik deskriptif seluruh variabel (B3) |
| 18 | Perbedaan harga ekspor antar industri + grafik per variabel — permintaan pembimbing |
| 19 | Alur penyaringan sampel menuju N = 100 (A3) |

### Tahap 4 — Finalisasi

Format Pedoman Penulisan Tugas Akhir UI, pemutakhiran literatur 2015–2025, abstrak
(sudah tersedia di Drive), kelengkapan administratif (Cover, Daftar Isi, Surat Pernyataan —
semua sudah ada), lalu simulasi tanya jawab penguji.

---

## SATU KEPUTUSAN YANG PERLU ANDA AMBIL

Draft 4c adalah studi **cross-section 2012, N = 100, OLS**. Berkas Anda juga memuat panel
lengkap **2007–2012, N = 623, 105 industri** dengan FE, RE, dan uji Hausman — yang tidak
dipakai di 4c.

**Pilihan A — pertahankan cross-section 4c.** Naskahnya sudah utuh dan konsisten, sejalan
dengan arahan pembimbing tentang perbandingan antar sektor pada 2012, dan Tahap 1–2 di atas
bisa membawanya ke kondisi siap sidang relatif cepat. Kelemahannya: tidak bisa mengendalikan
karakteristik permanen tiap industri, sehingga koefisien upah rentan terhadap bias variabel
yang dihilangkan — dan ini pertanyaan yang wajar diajukan penguji.

**Pilihan B — kembalikan panel sebagai model utama, cross-section sebagai pembanding.** Secara
metodologis jauh lebih kuat: fixed effects menyerap seluruh karakteristik industri yang tidak
berubah antarwaktu, dan hasilnya kebetulan mendukung kesimpulan yang sama (upah tidak
signifikan di FE, RE, maupun 2SLS — kokoh terhadap pilihan estimator). Biayanya: BAB III dan
BAB IV harus ditulis ulang cukup banyak, dan dummy sektor akan terserap FE sehingga Tujuan
Penelitian #2 perlu dijawab lewat jalur lain.

Pertimbangan yang menurut saya menentukan: **apa yang terakhir dilihat dan disetujui
pembimbing.** Jika beliau sudah menyetujui arah cross-section 2012, jangan diubah — memutar
balik ke panel berarti memulai negosiasi baru yang bisa memakan berbulan-bulan.

Kalau Anda tidak ingat, Pilihan A adalah taruhan yang lebih aman, dan hasil panel tetap bisa
dimasukkan sebagai **uji robustness satu subbab** di BAB IV. Dengan begitu Anda mendapat
kekuatan metodologis panel tanpa membongkar naskah — dan justru bisa menyatakan bahwa
kesimpulan penelitian ini bertahan pada dua desain data yang berbeda. Itu pernyataan yang
kuat di meja sidang.
