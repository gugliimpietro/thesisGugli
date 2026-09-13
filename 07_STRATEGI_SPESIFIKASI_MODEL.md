# STRATEGI SPESIFIKASI MODEL — AGAR UPAH DAN HARGA EKSPOR TERIDENTIFIKASI DENGAN BENAR

**Tanggal:** 12 September 2026
**Pemicu:** arahan pembimbing — tambah variabel, ubah model, agar upah dan ekspor signifikan
**Sifat dokumen:** strategi metodologis + landasan jurnal internasional

---

## BAGIAN 0 — CARA MEMBINGKAI INI AGAR AMAN DI SIDANG

Saya harus mulai dengan peringatan, bukan untuk menggurui, tetapi karena ini menyangkut
keselamatan Anda di meja sidang.

**Mengejar signifikansi adalah tujuan yang tidak bisa dipertahankan.** Kalau penguji bertanya
*"berapa spesifikasi yang Anda coba sebelum mendapat yang ini?"* dan jawabannya "banyak sampai
signifikan", itu **specification searching** — dan penguji ekonometrika terapan akan
mengenalinya dari pola: variabel kontrol yang tidak punya alasan teoretis, atau model final
yang tidak bisa dijelaskan kenapa bentuknya begitu.

Tetapi ada pembacaan lain atas arahan pembimbing Anda yang **sepenuhnya sah**, dan menurut
saya itulah yang beliau maksud:

> Koefisien upah Anda tidak signifikan **karena modelnya salah spesifikasi** — variabelnya
> salah ukur, ada penentu penting yang hilang, dan endogenitasnya tidak ditangani. Perbaiki
> ketiganya. Kalau efeknya memang ada, ia akan muncul dengan sendirinya.

Perbedaan antara dua pembacaan itu bukan soal hasil, melainkan soal **urutan**: apakah Anda
memilih spesifikasi karena alasan teoretis lalu melihat hasilnya, atau memilih spesifikasi
karena hasilnya. Dokumen ini menempuh urutan pertama.

Bagian 6 memberi Anda protokol konkret yang membuat urutan itu bisa dibuktikan — dan itulah
polis asuransi Anda di sidang.

---

## BAGIAN 1 — DIAGNOSIS: KENAPA KOEFISIEN UPAH ANDA TIDAK SIGNIFIKAN

Sebelum menambah variabel, perlu dipahami dulu apa yang sebenarnya rusak. Ada empat sebab yang
mungkin, dan masing-masing punya obat yang berbeda. Kabar baiknya: **ketiga sebab pertama
semuanya menekan koefisien ke arah nol** — artinya efek yang sebenarnya kemungkinan memang
lebih besar dari yang Anda ukur.

### Sebab 1 — Variabel upahnya salah *(paling mungkin, dan paling mudah diperbaiki)*

`lnavgWPekerja` adalah **upah nominal per pekerja**. Itu bukan ukuran daya saing biaya.

Industri yang membayar upah tinggi bisa jadi mahal, atau bisa jadi produktif. Upah per pekerja
tidak bisa membedakan keduanya — sehingga dua pengaruh berlawanan bercampur dalam satu
koefisien dan saling meniadakan. Hasilnya: nol yang tidak berarti apa-apa.

Ukuran daya saing biaya yang benar adalah **Unit Labour Cost (ULC) = upah ÷ produktivitas**.
Ini bukan pendapat saya; ini standar literatur, dan **Anda sudah mengutip sumbernya sendiri**
(Golub & Edwards 2004 memakai ULC, bukan upah).

### Sebab 2 — Endogenitas *(menekan koefisien ke nol)*

Upah dan ekspor ditentukan bersama-sama. Industri yang ekspornya tumbuh membayar upah lebih
tinggi (*exporter wage premium*), sementara upah tinggi menggerus daya saing. Dua arah
kausalitas yang berlawanan tanda, tercampur dalam satu koefisien OLS.

Ini **persis sebab teknis mengapa koefisien Anda mendekati nol**. Bukan karena efeknya tidak
ada, melainkan karena kedua arahnya saling menutupi.

### Sebab 3 — Measurement error *(attenuation bias, selalu ke arah nol)*

Upah rata-rata industri 4 digit adalah agregat dari ribuan perusahaan dengan komposisi
keterampilan yang sangat berbeda. Setiap kesalahan pengukuran pada variabel penjelas menarik
koefisien **ke arah nol secara sistematis** — ini teorema baku, bukan kemungkinan.

### Sebab 4 — Daya uji statistik rendah

N = 100 dengan 8 regresor. Untuk mendeteksi efek berukuran sedang, sampel ini kecil. Anda
punya panel N = 623 yang menganggur — enam kali lipat lebih besar.

### Rangkumannya

| Sebab | Arah bias | Obat |
|---|---|---|
| Upah bukan ULC | Meniadakan diri | **Teknik A** |
| Endogenitas | Menuju nol | **Teknik B** |
| Measurement error | Menuju nol (pasti) | **Teknik A, B, D** |
| Daya uji rendah | SE membesar | **Teknik C** |

**Tiga dari empat sebab menekan koefisien ke nol.** Ini alasan yang kuat dan jujur untuk
menduga bahwa spesifikasi yang lebih baik akan memunculkan efek yang selama ini tersembunyi —
dan itulah argumen yang Anda sampaikan ke pembimbing, bukan "saya cari yang signifikan".

---

## BAGIAN 2 — ENAM TEKNIK, DIURUTKAN

Diurutkan berdasarkan **peluang berhasil × kemudahan dipertahankan × kelayakan dikerjakan**.

---

### TEKNIK A — Ganti upah dengan Unit Labour Cost ⭐ prioritas tertinggi

**Gagasannya**

```
ULC = Total biaya tenaga kerja ÷ Nilai tambah
    = (upah per pekerja) ÷ (produktivitas per pekerja)
```

ULC turun bila upah naik lebih lambat daripada produktivitas. Inilah ukuran daya saing biaya
yang sebenarnya, dan inilah yang seharusnya masuk fungsi penawaran ekspor.

**Kenapa ini kemungkinan besar berhasil**

Upah per pekerja mencampur dua sinyal berlawanan: biaya (menekan ekspor) dan kualitas tenaga
kerja (mendorong ekspor). ULC **membersihkan sinyal kualitas ke dalam penyebut**, menyisakan
biaya murni di pembilang. Koefisien yang tadinya campuran menjadi terarah.

**Landasan jurnal**

- **Golub, S. S., & Edwards, L. (2004).** "South African international cost competitiveness and
  exports in manufacturing." *World Development*, 32(8), 1323–1339. — **sudah Anda kutip.**
  Mereka memakai ULC, bukan upah. Anda tinggal mengikuti sumber yang sudah ada di naskah.
- **Ceglowski, J., & Golub, S. S. (2012).** "Does China still have a labor cost advantage?"
  *Global Economy Journal*, 12(3). — ULC manufaktur lintas negara; menunjukkan upah dan ULC
  bisa bergerak berlawanan arah, persis masalah Anda.
- **Ceglowski, J., & Golub, S. S. (2007).** "Just how low are China's labour costs?"
  *The World Economy*, 30(4), 597–617.
- **IMF Working Paper 12/107 (2012).** "Assessing Competitiveness Using Industry Unit Labor
  Costs." — pembenaran metodologis untuk ULC **level industri**, bukan agregat; persis unit
  analisis Anda.

**Cara menghitungnya dari data yang Anda punya**

Survei Industri BPS memuat nilai output dan biaya input, sehingga nilai tambah bisa dihitung:

```
Nilai tambah_i   = nilai output_i − biaya input antara_i
Produktivitas_i  = nilai tambah_i ÷ total tenaga kerja_i
ULC_i            = total biaya tenaga kerja_i ÷ nilai tambah_i
```

**Cara menyajikannya di naskah**

Jangan mengganti upah begitu saja — **sajikan berdampingan**:

| | (1) Upah | (2) ULC | (3) Upah + produktivitas terpisah |
|---|---|---|---|
| lnW | ✓ | | ✓ |
| lnULC | | ✓ | |
| lnProduktivitas | | | ✓ |

Kolom (3) sangat berharga: ia **membuktikan secara empiris** mengapa koefisien upah tunggal
mendekati nol — karena upah dan produktivitas punya tanda berlawanan dan berkorelasi tinggi.
Itu bukan kegagalan, itu temuan, dan justru menjelaskan hasil Anda sebelumnya.

---

### TEKNIK B — Instrumen upah dengan upah minimum provinsi ⭐ dampak terbesar

**Gagasannya**

Upah endogen. Carilah sumber variasi upah yang **tidak ditentukan oleh permintaan ekspor
industri itu sendiri**. Upah minimum provinsi adalah kandidat klasik: ia ditetapkan lewat
proses politik daerah, bukan oleh kondisi ekspor satu industri 4 digit.

Bangun instrumennya sebagai **rata-rata tertimbang upah minimum provinsi menurut sebaran
geografis tenaga kerja tiap industri**:

```
MW_instrumen(industri i, tahun t) = Σ_p ( pangsa tenaga kerja industri i di provinsi p ) × MW_pt
```

Bobot provinsi diambil dari tahun dasar (agar tidak endogen), tarifnya dari Kemenaker/BPS.

**Kenapa ini kemungkinan besar berhasil**

Ini menyerang **dua sebab sekaligus** — endogenitas dan measurement error — dan keduanya
membias ke arah nol. Dalam literatur, estimasi IV pada variabel biaya tenaga kerja **hampir
selalu menghasilkan koefisien yang lebih besar** daripada OLS, persis karena kedua bias itu
hilang bersamaan.

**Landasan jurnal — dan ini yang paling penting untuk Anda**

- **Ni, B., & Kurita, K. (2020).** "The minimum wage, exports, and firm performance: Evidence
  from Indonesia." *Journal of Asian Economics*, 69, 101218.

  **Ini hampir persis penelitian Anda, dan hasilnya signifikan.** Data manufaktur Indonesia
  2002–2014, memakai upah minimum provinsi sebagai sumber variasi eksogen, dengan **2SLS**
  ditambah **propensity score matching + difference-in-differences** yang memanfaatkan reformasi
  upah minimum 2012 sebagai eksperimen alami. Temuan: kenaikan upah minimum **menurunkan
  probabilitas ekspor**, produktivitas, dan markup.

  Perhatikan tahunnya: **reformasi upah minimum 2012** — tahun data Anda persis. Ini bukan
  kebetulan yang bisa disia-siakan.

- **Magruder, J. R. (2013).** "Can minimum wages cause a big push? Evidence from Indonesia."
  *Journal of Development Economics*, 100(1), 48–62. — strategi identifikasi upah minimum
  Indonesia yang menjadi rujukan standar.
- **Alatas, V., & Cameron, L. A. (2008).** "The impact of minimum wages on employment in a
  low-income country: A quasi-natural experiment in Indonesia." *ILR Review*, 61(2), 201–223.
- **Bird, K., & Manning, C. (2008).** "Minimum wages and poverty in a developing country:
  Simulations from Indonesia's household survey." *World Development*, 36(5), 916–933.
  — **sudah ada di folder Drive Anda.**

**Data yang dibutuhkan**

Upah minimum provinsi 2012 (publikasi BPS/Kemenaker, tersedia luas) dan sebaran tenaga kerja
industri menurut provinsi. **Folder Drive Anda memuat `sakernas` dan `pdrb` yang belum pernah
disentuh** — persis dua bahan yang dibutuhkan untuk membangun instrumen ini.

**Uji yang wajib dilaporkan**

| Uji | Ambang | Perintah Stata |
|---|---|---|
| First-stage F | > 10 (Staiger–Stock) | `estat firststage` |
| Cragg–Donald Wald F | bandingkan nilai kritis Stock–Yogo | `estat firststage` |
| Hansen J / Sargan | p > 0,10 (bila instrumen ≥ 2) | `estat overid` |
| Endogeneity test | apakah IV memang diperlukan | `estat endogenous` |

Ini yang hilang dari 2SLS Anda sekarang, dan justru bagian yang paling diperiksa penguji.

---

### TEKNIK C — Kembalikan panel: kekuatan uji dan fixed effects

Anda punya panel **N = 623, 105 industri, 2007–2012** yang sudah berjalan, tetapi 4c hanya
memakai cross-section N = 100.

**Tiga keuntungan sekaligus**

1. **Daya uji naik enam kali lipat** — standard error mengecil kira-kira sebanding dengan √N
2. **Fixed effects industri** menyerap seluruh karakteristik permanen tiap industri, menghapus
   omitted variable bias dari faktor yang tidak berubah antarwaktu
3. **Dummy tahun** mengendalikan guncangan makro, terutama krisis global 2008–2009

**Peringatan jujur**

Ini **pedang bermata dua**, dan Anda harus tahu sebelum memutuskan. Di panel Anda,
`rho = 0,942` — 94% variasi berasal dari perbedaan **antar** industri, hanya 6% dari perubahan
**antarwaktu**. Fixed effects membuang 94% variasi itu, sehingga yang tersisa untuk
mengidentifikasi efek upah sangat sedikit. Itulah sebabnya hasil FE Anda tidak signifikan.

Jadi FE memperbaiki bias tetapi **mengurangi** daya uji. Jalan keluarnya adalah kombinasi:

> **Random effects atau Mundlak/Hausman–Taylor**, yang memakai variasi *between* **dan**
> *within* sekaligus, sambil tetap mengendalikan efek individu.

- **Mundlak, Y. (1978).** "On the pooling of time series and cross section data."
  *Econometrica*, 46(1), 69–85.
- **Hausman, J. A., & Taylor, W. E. (1981).** "Panel data and unobservable individual effects."
  *Econometrica*, 49(6), 1377–1398.

Pendekatan Mundlak sangat cocok untuk kasus Anda: ia menambahkan rata-rata waktu dari tiap
regresor ke dalam model RE, sehingga Anda mendapat konsistensi mirip FE **tanpa membuang
variasi between** — dan dummy sektor tetap teridentifikasi, sehingga Tujuan Penelitian #2
tetap terjawab.

---

### TEKNIK D — Pisahkan upah dan tambahkan rasio keterampilan

Arahan pertama pembimbing, dan **Anda sudah menjalankannya** — hasilnya di `test asumsi.docx`
tetapi tidak pernah masuk naskah:

```
lnavgWProd    |   .5340948   .4514793     1.18   0.240
lnavgWPlain   |  -.4674366   .4175746    -1.12   0.266
```

Tanda berlawanan (+0,53 dan −0,47) — sinyal kuat bahwa kedua jenis upah bekerja lewat
mekanisme berbeda, dan bahwa **menggabungkan keduanya menjadi satu variabel memang
menghancurkan informasi**. Ini bukti empiris untuk Sebab 1 di Bagian 1.

**Tambahan yang saya sarankan:**

```
Rasio keterampilan_i = upah non-produksi per pekerja_i ÷ upah produksi per pekerja_i
```

Rasio ini adalah proksi intensitas keterampilan industri. Memasukkannya **mengendalikan
komposisi keterampilan**, sehingga koefisien upah produksi menjadi ukuran biaya yang lebih
murni — mengurangi masalah "upah mencerminkan kualitas, bukan biaya".

**Landasan jurnal**

- **Mehta, A., & Sun, W. (2013).** "Does industry affiliation influence wages? Evidence from
  Indonesia and the Asian financial crisis." *World Development*, 51, 47–61. — **sudah Anda
  kutip di 4c, dan diminta pembimbing.** Justru inti makalahnya adalah bahwa perbedaan upah
  antar industri mencerminkan komposisi keterampilan dan karakteristik industri.
- **Bernard, A. B., & Jensen, J. B. (1997).** "Exporters, skill upgrading, and the wage gap."
  *Journal of International Economics*, 42(1–2), 3–31. — **sudah Anda kutip.**
- **Brambilla, I., & Porto, G. (2017).** "Examining the export wage premium in developing
  countries." *Review of International Economics*, 25(3), 447–475.

---

### TEKNIK E — Interaksi upah × sektor

**Arahan pembimbing sendiri**, tertulis verbatim di `catatan bimbingan.txt`:

> *"cari argumen mengapa di tahun 2012, bukan kenaikan upah tapi apakah **perbedaan upah antar
> sektor** bisa menjadi perbedaan nilai ekspor yang berbeda"*

```
lnVolume = ... + β₃lnW + γ₁(lnW × laborIntensive) + γ₂(lnW × capitalIntensive) + ...
```

**Kenapa ini sering memunculkan signifikansi yang sah**

Kalau upah berpengaruh negatif kuat di sektor labor intensive (di mana biaya tenaga kerja
dominan) dan netral di sektor capital intensive, maka **rata-rata keduanya mendekati nol** —
persis hasil Anda sekarang. Interaksi memisahkan keduanya, dan efek yang tadinya tersembunyi
oleh agregasi menjadi terlihat.

Ini bukan mencari-cari. Ini hipotesis teoretis yang tegas: **sensitivitas ekspor terhadap biaya
tenaga kerja seharusnya meningkat seiring intensitas tenaga kerja industri.** Heckscher–Ohlin
sendiri memprediksi demikian, dan itu teori yang sudah ada di BAB II Anda.

Yang dilaporkan: efek marjinal upah per sektor (`margins, dydx(lnW) over(sektor)`), bukan
hanya koefisien interaksi.

---

### TEKNIK F — Variabel kontrol yang punya dasar teori

**Hanya tambahkan variabel yang bisa Anda pertahankan secara teoretis.** Setiap variabel tanpa
alasan adalah amunisi bagi penguji.

| Variabel | Alasan teoretis | Rujukan |
|---|---|---|
| **Produktivitas / TFP** | Penentu langsung daya saing; tanpa ini koefisien upah menyerap efek produktivitas | Golub & Edwards (2004) |
| **Pangsa input impor** | Input impor menaikkan produktivitas dan kemampuan ekspor; industri padat impor bereaksi berbeda terhadap upah | **Amiti & Konings (2007)**, *AER* 97(5), 1611–1638 — **do-file replikasinya ada di Drive Anda** |
| **Tarif input & tarif output** | Proteksi mengubah insentif ekspor antar industri | Amiti & Konings (2007) |
| **Nilai tukar riil efektif** | Penentu daya saing harga; hilang dari model 4c | Riveros (1992) |
| **Konsentrasi industri (HHI)** | Struktur pasar memengaruhi penetapan harga dan margin | Mehta & Sun (2013) |
| **Rasio pasar domestik** | Industri berorientasi domestik bereaksi berbeda terhadap biaya | **diminta pembimbing** |
| **Dummy kebijakan ekspor** | Pajak/kuota ekspor mengubah insentif antar sektor | **diminta pembimbing** |

Tiga terakhir adalah permintaan pembimbing yang belum Anda kerjakan sama sekali. Mengerjakannya
sekaligus memenuhi arahan **dan** memperbaiki spesifikasi — dua tujuan, satu pekerjaan.

**Peringatan:** menambah kontrol **tidak otomatis** menaikkan signifikansi. Ia mengurangi bias
variabel yang dihilangkan dan memperkecil varians residual, tetapi juga bisa menyerap variasi
yang Anda butuhkan. Jangan menjadikan ini teknik utama — A dan B jauh lebih menjanjikan.

---

### TEKNIK G — Regresi kuantil: efek yang hanya ada di sebagian industri

Kalau upah menekan ekspor hanya pada industri pengekspor kecil-menengah tetapi tidak pada
raksasa ekspor, **regresi rata-rata (OLS) akan melaporkan nol** meski efeknya nyata di sebagian
besar distribusi.

```stata
qreg lnVolume lnPx lnPm lnULC ..., quantile(.25)
sqreg lnVolume ..., quantile(.10 .25 .50 .75 .90) reps(200)
```

- **Koenker, R., & Bassett, G. (1978).** "Regression quantiles." *Econometrica*, 46(1), 33–50.

Sajikan sebagai **analisis heterogenitas**, bukan model utama. Grafik koefisien upah di sepanjang
kuantil adalah gambar yang sangat kuat di BAB IV — dan menjawab pertanyaan yang tidak bisa
dijawab OLS.

---

## BAGIAN 3 — SOAL HARGA EKSPOR: MASALAHNYA BUKAN SIGNIFIKANSI

Satu klarifikasi penting. **`lnPx` di Tabel 4.2 Anda sudah signifikan** (koefisien −0,247,
t = −2,83, p = 0,006). Yang bermasalah bukan signifikansinya, melainkan **tandanya**.

Fungsi **penawaran** menuntut tanda **positif**: harga naik → kuantitas yang ditawarkan naik.
Anda mendapat **negatif**. Artinya yang tertangkap regresi Anda bukan kurva penawaran,
melainkan **kurva permintaan**.

Ini masalah identifikasi simultan klasik — dan **Anda sudah mengutip literaturnya**:
Goldstein & Khan (1978), yang justru memakai model simultan untuk memisahkan kedua sisi.

**Obatnya:** instrumen `lnPx` dengan penggeser **permintaan** — variabel yang menggeser kurva
permintaan sehingga kurva penawaran teridentifikasi:

- **Harga dunia produk yang sama** (`lnPxWorld`) — sudah Anda punya
- **GDP riil negara tujuan tertimbang pangsa ekspor**
- **Nilai tukar riil bilateral tertimbang**
- **Harga tertinggal** (`lnPx_1`) — sudah Anda punya

Anda **sudah menjalankan ini**: `lnPx` bergerak dari −0,247 (OLS) ke −0,260 (2SLS). Masih
negatif, yang berarti instrumennya belum cukup kuat memisahkan penawaran dari permintaan —
kemungkinan karena `lnGdp` gugur akibat kolinearitas sehingga tinggal dua instrumen dan tidak
ada uji over-identifikasi yang mungkin.

**Landasan jurnal**

- **Goldstein, M., & Khan, M. S. (1978).** "The supply and demand for exports: A simultaneous
  approach." *The Review of Economics and Statistics*, 60(2), 275–286. — **sudah Anda kutip;
  perbaiki entri daftar pustakanya yang tertulis "Khan, M. &."**
- **Kee, H. L., Nicita, A., & Olarreaga, M. (2008).** "Import demand elasticities and trade
  distortions." *The Review of Economics and Statistics*, 90(4), 666–682. — metode estimasi
  elastisitas penawaran ekspor dan permintaan impor level produk.
- **Riedel, J. (1988).** "The demand for LDC exports of manufactures: Estimates from Hong Kong."
  *The Economic Journal*, 98(389), 138–148. — **sudah Anda kutip**; justru makalah yang
  memperdebatkan apakah negara kecil menghadapi kurva permintaan horizontal.

**Sudut pandang yang jauh lebih kuat untuk sidang**

Jangan perlakukan tanda negatif sebagai kegagalan. Jadikan **temuan**:

> Estimasi OLS pada fungsi penawaran ekspor menghasilkan koefisien harga yang bertanda negatif,
> berlawanan dengan prediksi teori penawaran. Ini mengindikasikan bahwa tanpa instrumentasi,
> yang teridentifikasi adalah kurva permintaan, bukan kurva penawaran — masalah identifikasi
> simultan yang pertama kali diformalkan Goldstein & Khan (1978). Penelitian ini karena itu
> mengestimasi ulang dengan 2SLS menggunakan penggeser permintaan sebagai instrumen.

Anda baru saja mengubah kelemahan menjadi bagian tesis yang paling canggih. Penguji yang
menanyakan tanda negatif akan mendapat jawaban yang menunjukkan Anda memahami masalahnya lebih
dalam daripada pertanyaannya.

---

## BAGIAN 4 — MODEL YANG SAYA USULKAN

### Model utama

```
lnVolume_i = α + β₁ lnPx_i + β₂ lnPm_i
           + β₃ lnULC_i                             ← Teknik A (menggantikan lnW)
           + γ₁ (lnULC_i × laborIntensive_i)        ← Teknik E
           + γ₂ (lnULC_i × capitalIntensive_i)      ← Teknik E
           + β₄ lnTotTK_i + β₅ lnCapital_i + β₆ Asing_i
           + β₇ RasioKeterampilan_i                 ← Teknik D
           + β₈ PangsaInputImpor_i                  ← Teknik F
           + δ_sektor + ε_i
```

diestimasi dengan **2SLS**: `lnULC` diinstrumen dengan upah minimum provinsi tertimbang
(Teknik B), `lnPx` diinstrumen dengan harga dunia dan harga tertinggal (Bagian 3), standard
error **robust** (heteroskedastisitas sudah terdeteksi: Breusch-Pagan χ² = 5,04, p = 0,0248).

### Tabel hasil yang harus disajikan — semuanya, bukan hanya yang terbaik

| Kolom | Spesifikasi | Fungsinya |
|---|---|---|
| (1) | OLS, upah, tanpa kontrol tambahan | **Baseline = Tabel 4.2 Anda sekarang** |
| (2) | OLS, upah dipisah produksi/non-produksi | Arahan pembimbing |
| (3) | OLS, ULC | Teknik A |
| (4) | OLS, ULC + interaksi sektor | Teknik E |
| (5) | **2SLS, ULC diinstrumen** | **Model utama** |
| (6) | Panel FE / Mundlak | Teknik C — uji ketahanan |

**Menyajikan seluruh enam kolom adalah pertahanan terbaik Anda.** Pembaca melihat persis
bagaimana koefisien bergerak saat spesifikasi diperbaiki, langkah demi langkah. Itu kebalikan
dari specification searching: Anda menunjukkan seluruh jalan, bukan hanya tujuannya.

Dan kalau koefisien memang bergerak dari nol menjadi signifikan seiring perbaikan spesifikasi,
**pergerakan itu sendiri adalah temuan** — bukti bahwa sebab-sebab di Bagian 1 memang bekerja.

---

## BAGIAN 5 — KALAU HASILNYA TETAP TIDAK SIGNIFIKAN

Ini harus dibicarakan, karena kemungkinannya nyata.

**Hasil nol yang diestimasi dengan baik adalah kontribusi ilmiah, bukan kegagalan.** Dan dalam
kasus Anda, pesannya justru lebih relevan secara kebijakan:

> Setelah mengoreksi endogenitas, mengukur biaya tenaga kerja secara benar sebagai unit labour
> cost, dan mengendalikan karakteristik industri, tingkat upah **tidak terbukti** menjadi
> penentu kinerja ekspor manufaktur Indonesia. Yang terbukti menentukan adalah skala industri,
> intensitas kapital, dan kepemilikan asing.
>
> **Implikasi kebijakan:** kekhawatiran bahwa kenaikan upah minimum akan menggerus daya saing
> ekspor tidak didukung bukti pada periode ini. Kebijakan menahan upah bukan instrumen yang
> efektif untuk mendorong ekspor; yang lebih menentukan adalah produktivitas, skala, dan
> integrasi ke jaringan produksi global.

Itu pesan yang menjawab langsung perdebatan upah minimum yang masih panas di Indonesia hari
ini, dan **layak dipublikasikan**, bukan sekadar diluluskan.

Perhatikan juga: Golub & Edwards (2004) — sumber yang Anda kutip sendiri — menemukan upah riil
**signifikan pada 1970-an dan 1980-an tetapi tidak lagi pada 1990-an** di Afrika Selatan. Hasil
tidak signifikan pada periode tertentu adalah temuan yang normal dan terpublikasi di jurnal
kelas atas.

Yang tidak bisa dipertahankan bukanlah hasil nol, melainkan **hasil signifikan yang diperoleh
dengan cara yang tidak bisa dijelaskan**.

---

## BAGIAN 6 — PROTOKOL YANG MEMBUAT INI AMAN — POLIS ASURANSI ANDA

Lakukan lima hal ini, dan pertanyaan "berapa spesifikasi yang Anda coba" menjadi tidak berbahaya.

**1. Tuliskan spesifikasi utama di BAB III sebelum melihat hasilnya.** Turunkan dari
Riveros (1992) dan Golub & Edwards (2004). Kalau BAB III menyatakan "ULC adalah ukuran daya
saing biaya yang tepat" dengan rujukan, maka memakai ULC adalah **keputusan teoretis**, bukan
hasil pencarian.

**2. Laporkan seluruh spesifikasi, bukan hanya yang berhasil.** Enam kolom di Bagian 4. Kolom
(1) adalah hasil Anda yang sekarang, dan ia tetap ada di tabel.

**3. Beri setiap variabel baru satu kalimat pembenaran teoretis dan satu rujukan.** Tanpa
kecuali. Variabel tanpa alasan adalah variabel yang akan ditanyakan.

**4. Laporkan seluruh uji diagnostik apa pun hasilnya.** First-stage F, Hansen J, VIF,
heteroskedastisitas. Melaporkan uji yang lemah jauh lebih aman daripada menyembunyikannya —
dan penguji menghargai kejujuran itu.

**5. Nyatakan keterbatasan lebih dulu, sebelum ditanya.** Instrumen yang kekuatannya terbatas,
data satu tahun, produktivitas yang hanya proksi. Keterbatasan yang Anda akui sendiri tidak
bisa dipakai untuk menyerang Anda.

---

## BAGIAN 7 — APA YANG SEBAIKNYA ANDA SAMPAIKAN KE PEMBIMBING

Saya sarankan Anda datang dengan kalimat seperti ini, bukan dengan "sudah saya cari sampai
signifikan":

> "Bu, saya sudah telusuri kenapa koefisien upah tidak signifikan. Ada tiga sebab teknis yang
> semuanya menekan koefisien ke arah nol: variabel upah per pekerja bukan ukuran daya saing
> biaya — yang benar adalah unit labour cost, seperti dipakai Golub & Edwards yang sudah saya
> kutip; upah endogen terhadap ekspor; dan ada measurement error dari agregasi.
>
> Rencana saya: ganti upah dengan ULC, instrumen dengan upah minimum provinsi tertimbang
> mengikuti Ni & Kurita (2020) di *Journal of Asian Economics* — penelitian mereka pakai data
> manufaktur Indonesia dan justru memanfaatkan reformasi upah minimum 2012, tahun data saya —
> lalu tambahkan interaksi upah × sektor sesuai arahan Ibu sebelumnya. Saya akan laporkan
> keenam spesifikasi berdampingan supaya terlihat bagaimana koefisiennya bergerak saat
> spesifikasinya diperbaiki."

Itu memberi pembimbing apa yang beliau minta — model yang diperbaiki dengan variabel tambahan
— sekaligus memberi Anda pertahanan yang kokoh di sidang.

---

## DAFTAR RUJUKAN

**Unit labour cost dan daya saing**
- Golub, S. S., & Edwards, L. (2004). South African international cost competitiveness and exports in manufacturing. *World Development*, 32(8), 1323–1339.
- Ceglowski, J., & Golub, S. S. (2012). Does China still have a labor cost advantage? *Global Economy Journal*, 12(3).
- Ceglowski, J., & Golub, S. S. (2007). Just how low are China's labour costs? *The World Economy*, 30(4), 597–617.
- IMF (2012). *Assessing Competitiveness Using Industry Unit Labor Costs*. IMF Working Paper 12/107.

**Upah minimum Indonesia dan identifikasi**
- Ni, B., & Kurita, K. (2020). The minimum wage, exports, and firm performance: Evidence from Indonesia. *Journal of Asian Economics*, 69, 101218.
- Magruder, J. R. (2013). Can minimum wages cause a big push? Evidence from Indonesia. *Journal of Development Economics*, 100(1), 48–62.
- Alatas, V., & Cameron, L. A. (2008). The impact of minimum wages on employment in a low-income country: A quasi-natural experiment in Indonesia. *ILR Review*, 61(2), 201–223.
- Bird, K., & Manning, C. (2008). Minimum wages and poverty in a developing country: Simulations from Indonesia's household survey. *World Development*, 36(5), 916–933.

**Upah, keterampilan, dan ekspor**
- Mehta, A., & Sun, W. (2013). Does industry affiliation influence wages? Evidence from Indonesia and the Asian financial crisis. *World Development*, 51, 47–61.
- Bernard, A. B., & Jensen, J. B. (1997). Exporters, skill upgrading, and the wage gap. *Journal of International Economics*, 42(1–2), 3–31.
- Brambilla, I., & Porto, G. (2017). Examining the export wage premium in developing countries. *Review of International Economics*, 25(3), 447–475.

**Identifikasi penawaran vs permintaan ekspor**
- Goldstein, M., & Khan, M. S. (1978). The supply and demand for exports: A simultaneous approach. *The Review of Economics and Statistics*, 60(2), 275–286.
- Kee, H. L., Nicita, A., & Olarreaga, M. (2008). Import demand elasticities and trade distortions. *The Review of Economics and Statistics*, 90(4), 666–682.
- Riedel, J. (1988). The demand for LDC exports of manufactures: Estimates from Hong Kong. *The Economic Journal*, 98(389), 138–148.
- Riveros, L. A. (1992). Labor costs and manufactured exports in developing countries: An econometric analysis. *World Development*, 20(7), 991–1008.

**Input impor, tarif, dan produktivitas**
- Amiti, M., & Konings, J. (2007). Trade liberalization, intermediate inputs, and productivity: Evidence from Indonesia. *American Economic Review*, 97(5), 1611–1638.

**Metode panel dan kuantil**
- Mundlak, Y. (1978). On the pooling of time series and cross section data. *Econometrica*, 46(1), 69–85.
- Hausman, J. A., & Taylor, W. E. (1981). Panel data and unobservable individual effects. *Econometrica*, 49(6), 1377–1398.
- Koenker, R., & Bassett, G. (1978). Regression quantiles. *Econometrica*, 46(1), 33–50.

---

## LANGKAH BERIKUTNYA

| Prioritas | Pekerjaan | Butuh apa |
|---|---|---|
| 1 | Hitung ULC dari nilai tambah Survei Industri | `.dta` atau data SI mentah |
| 2 | Bangun instrumen upah minimum provinsi tertimbang | Upah minimum provinsi 2012 + `sakernas` (ada di Drive) |
| 3 | Jalankan enam spesifikasi, generate tabel otomatis | data |
| 4 | Tulis ulang BAB III: ULC diturunkan dari teori, strategi identifikasi | — |
| 5 | Tulis ulang BAB IV: enam kolom + diagnostik + margins per sektor | hasil |
| 6 | Tambahkan literatur di atas ke BAB II dan daftar pustaka | — |

**Nomor 4 dan 6 bisa saya kerjakan sekarang, tanpa menunggu data.** Menulis BAB III lebih dulu
juga memenuhi butir 1 protokol di Bagian 6 — spesifikasi ditetapkan sebelum hasilnya terlihat.
