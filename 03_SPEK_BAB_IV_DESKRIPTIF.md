# SPESIFIKASI BAB IV — ANALISIS DESKRIPTIF

**Tanggal:** 11 September 2026
**Dasar:** arahan pembimbing di `catatan bimbingan.txt` (diminta dua kali, paling belum digarap)
**Status:** spesifikasi kerja — menunggu file `.dta` untuk dieksekusi

---

## KENAPA BAGIAN INI YANG DIDAHULUKAN

Dari tujuh arahan pembimbing, yang paling tegas dan paling belum dipenuhi adalah permintaan
statistik deskriptif. Ia disebut dua kali dalam satu catatan, dengan daftar rinci, dan BAB IV
sekarang hanya memuat sekitar empat paragraf deskriptif. Besar kemungkinan di sinilah tesis
tersendat pada 2016.

Ada alasan metodologis yang lebih dalam. Hasil FE menunjukkan `rho = 0,942` — 94,2% variasi
ekspor berasal dari perbedaan permanen antar industri, hanya 6% dari perubahan antarwaktu.
Artinya **cerita utama tesis ini sesungguhnya ada di dimensi antar-industri**, bukan di dimensi
waktu. Statistik deskriptif yang kaya bukan pelengkap basa-basi; ia adalah tempat temuan
substantif tesis ini berada. Regresi FE justru membuang 94% variasi itu.

Ini juga yang membuat kesimpulan "upah tidak signifikan" dapat dipertahankan dengan percaya
diri: bukan karena tidak ada yang ditemukan, melainkan karena yang menentukan ekspor adalah
struktur industri — dan struktur itu kita tunjukkan secara deskriptif.

---

## STRUKTUR YANG DIUSULKAN

BAB IV dipecah menjadi dua bagian besar:

- **4.1 Gambaran Umum Data** (baru, isi dokumen ini)
- **4.2 Hasil Estimasi dan Pembahasan** (yang sekarang ada, akan ditulis ulang terpisah)

---

## 4.1.1 — Deskripsi Sampel dan Konstruksi Panel

Wajib tuntas lebih dulu karena seluruh angka berikutnya bergantung padanya.

| Yang harus dinyatakan | Catatan |
|---|---|
| Jumlah observasi final | **Satu angka saja.** Saat ini beredar 50 / 88 / 100 / 105 / 623 / 643 |
| Jumlah industri (grup) | 105 atau 108 — tetapkan |
| Level agregasi ISIC | 2, 3, atau 4 digit — naskah sekarang menyebut ketiganya |
| Rentang tahun | 2007–2012 (T = 6) |
| Sifat panel | Seimbang atau tidak; bila tidak, berapa industri yang tidak lengkap dan mengapa |
| Alur penyaringan | Dari populasi awal Survei Industri sampai panel final, per tahap, dengan jumlah yang gugur di tiap tahap |

**Tabel 4.1 (baru) — Alur konstruksi sampel.** Format: tahap | kriteria | observasi tersisa.
Penguji hampir pasti menanyakan asal-usul N; tabel ini menjawabnya sebelum ditanya.

---

## 4.1.2 — Statistik Deskriptif Variabel

**Tabel 4.2 (baru) — Ringkasan seluruh variabel.**
Kolom: variabel | satuan | N | rata-rata | median | std. dev. | min | maks.

Disajikan dalam **level (satuan asli)**, bukan logaritma. Alasannya: pembaca dan penguji
berpikir dalam rupiah dan ton, bukan dalam log. Logaritma adalah alat estimasi, bukan alat
deskripsi. Kolom tambahan berisi rata-rata bentuk log untuk menjembatani ke BAB berikutnya.

**Tabel 4.3 (baru) — Dekomposisi variasi: within vs between.**
Untuk tiap variabel, tampilkan standar deviasi overall, between (antar industri), dan
within (dalam industri antarwaktu), lengkap dengan proporsinya.

Ini tabel yang **paling penting di seluruh BAB IV** dan belum pernah ada di naskah mana pun.
Ia menjelaskan sebelum regresi dijalankan mengapa fixed effects menyerap hampir segalanya, dan
mengapa enam tahun terlalu pendek untuk mengidentifikasi efek upah. Bila nanti penguji bertanya
"kenapa hasil Anda tidak signifikan", jawabannya sudah tersaji di tabel ini, bukan dicari-cari
saat sidang.

**Tabel 4.4 — Matriks korelasi.** Sudah ada di `test asumsi.docx`, tinggal dirapikan.
Sertakan VIF (mean 1,52; maks 1,90 — aman) pada catatan kaki tabel.

---

## 4.1.3 — Pola Ekspor Manufaktur Indonesia

Menjawab langsung permintaan pembimbing: *"pola ekspor Indonesia, sektor pengekspor terbesar,
pangsa pasar"*.

- **Tabel 4.5** — Sepuluh industri pengekspor terbesar (rata-rata 2007–2012): nilai, volume,
  pangsa terhadap total ekspor manufaktur, dan pangsa kumulatif sepuluh besar.
  Indikator konsentrasi: rasio konsentrasi CR4/CR10 dan indeks Herfindahl.
- **Tabel 4.6** — Sepuluh industri dengan pertumbuhan ekspor tertinggi dan terendah.
- **Gambar 4.1** — Tren nilai dan volume ekspor agregat 2007–2012, dua sumbu.
  Grafik ini harus memperlihatkan dampak krisis global 2008–2009; bila terlihat, ia sekaligus
  menjadi justifikasi empiris pemakaian dummy tahun dalam model.
- **Gambar 4.2** — Tren terpisah kelompok labor intensive vs capital intensive.
  Ini memperbaiki sekaligus memperluas Gambar 1.1 yang judulnya salah di rev4b.

---

## 4.1.4 — Struktur Upah: Produksi vs Non-Produksi

Permintaan pembimbing yang paling eksplisit dan sudah setengah dikerjakan
(variabel `lnWTotProd` dan `lnWTotPlain` sudah dibentuk, tetapi tidak pernah dideskripsikan).

- **Tabel 4.7** — Upah rata-rata per pekerja produksi dan non-produksi, per tahun,
  beserta rasionya. Sajikan nominal dan riil (dideflasi dengan IHK) berdampingan.
- **Tabel 4.8** — Rasio upah non-produksi terhadap produksi menurut kelompok sektor.
  Rasio ini adalah **proksi intensitas keterampilan**, dan di sinilah argumen kunci tesis
  dibangun: bila koefisien upah positif, kemungkinan besar upah menangkap kualitas tenaga kerja,
  bukan biaya kompetitif. Deskriptif inilah yang memberi bukti untuk klaim tersebut.
- **Gambar 4.3** — Sebaran upah per pekerja antar industri (box plot per tahun), untuk
  memperlihatkan bahwa ragam antar industri jauh melampaui ragam antarwaktu.

---

## 4.1.5 — Perbandingan Antar Klasifikasi Sektor

Menjawab arahan pembimbing yang mengalihkan fokus dari *"kenaikan upah"* ke
*"perbedaan upah antar sektor"* — dan menjawab **Tujuan Penelitian #2**, yang secara
metodologis tidak dapat dijawab oleh model FE karena dummy sektor terserap.

Perlu ditegaskan dalam naskah: bagian deskriptif inilah, bersama variabel interaksi
upah × sektor dalam model utama, yang menjawab Tujuan Penelitian #2. Bukan koefisien dummy
sektor, yang memang tidak teridentifikasi dalam FE. Menyatakan hal ini lebih dulu jauh lebih
baik daripada dibongkar penguji.

- **Tabel 4.9** — Perbandingan seluruh variabel kunci antara kelompok labor intensive,
  capital intensive, dan sisanya: ekspor, upah produksi, upah non-produksi, jumlah tenaga kerja,
  kapital, kepemilikan asing.
- **Uji beda rata-rata** antar kelompok (uji t dan Kruskal-Wallis) dengan signifikansinya.
  Ini membuat "perbedaan antar sektor" menjadi klaim statistik, bukan kesan visual.
- **Gambar 4.4** — Diagram sebar upah per pekerja terhadap ekspor per pekerja, titik diwarnai
  menurut kelompok sektor. Satu gambar yang merangkum seluruh tesis.

---

## 4.1.6 — Harga Ekspor Antar Industri

Permintaan pembimbing: *"perbedaan harga ekspor antar industri, komoditas berharga relatif tinggi"*.
Sekaligus menyiapkan pembaca untuk masalah identifikasi nilai vs volume.

- **Tabel 4.10** — Harga ekspor rata-rata per unit (nilai ÷ volume) menurut industri,
  sepuluh tertinggi dan sepuluh terendah.
- **Gambar 4.5** — Perbandingan tren indeks nilai dan indeks volume ekspor (2007 = 100).
  **Gambar ini memikul beban argumentasi penting**: bila nilai dan volume bergerak berbeda,
  ia membuktikan secara visual bahwa pemilihan variabel terikat bukan soal selera, melainkan
  menentukan hasil — dan menyiapkan pembaca untuk keputusan memakai `lnVolume` sesuai kerangka
  penawaran Riveros.

---

## DATA YANG DIBUTUHKAN

Untuk mengeksekusi seluruh spesifikasi di atas, panel harus memuat — dalam **level, bukan log**:

| Kebutuhan | Keterangan |
|---|---|
| Pengenal industri + tahun | `isic3`, `tahun` |
| Nilai ekspor | US$ |
| Volume ekspor | kuantitas |
| Harga ekspor | atau dapat dihitung dari nilai ÷ volume |
| Harga bahan baku impor | `Pm` |
| Upah tenaga kerja produksi | total dan/atau per pekerja |
| Upah tenaga kerja non-produksi | total dan/atau per pekerja |
| Jumlah tenaga kerja produksi | |
| Jumlah tenaga kerja non-produksi | |
| Kapital | |
| Kepemilikan asing | |
| Dummy sektor | `laborIntensive`, `capitalIntensive` |

Bila sebagian variabel hanya tersedia dalam bentuk log, transformasi balik dapat dilakukan —
tetapi **file asli dalam level jauh lebih disukai** karena statistik deskriptif dalam log
tidak dapat dibaca oleh penguji.

Bila tersedia, tambahan yang berguna: IHK/deflator untuk upah riil, dan data `sakernas`
untuk proksi produktivitas guna menghitung **Unit Labour Cost**.

---

## LANGKAH SETELAH DATA MASUK

1. Verifikasi konstruksi tiap variabel terhadap definisi di BAB III
2. Tetapkan dataset master dan kunci angka N
3. Jalankan seluruh tabel dan gambar di atas, **digenerate langsung dari data** — tidak ada
   satu angka pun yang diketik manual
4. Tulis narasi BAB IV bagian 4.1 berdasarkan angka yang keluar
5. Baru setelah itu masuk ke re-estimasi model dan penulisan ulang 4.2
