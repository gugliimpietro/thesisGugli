# TEMUAN DARI FOLDER DRIVE "bahan tesis" — DAN STRATEGI BARU

**Tanggal:** 2 September 2026
**Sumber:** folder Drive `bahan tesis` (pemilik satriodwisaputra@gmail.com)
**Status:** mengoreksi sebagian audit di `00_AUDIT_DAN_RENCANA_KERJA_TESIS.md`

---

## RINGKASAN EKSEKUTIF — tiga kalimat

Anda **sudah mengerjakan jauh lebih banyak analisis daripada yang masuk ke dalam naskah tesis.**
Regresi fixed effects dengan standard error robust-clustered, uji heteroskedastisitas, uji VIF,
2SLS dengan instrumen yang benar, dan pemisahan upah produksi/non-produksi — semuanya ada di
folder Drive, tetapi tidak satu pun dipakai di BAB IV. Masalah utama tesis ini bukan kekurangan
kerja, melainkan **kerja yang sudah ada tidak pernah dirakit menjadi naskah**.

Kabar baiknya: sebagian besar pekerjaan berat sudah selesai sepuluh tahun lalu.

---

## KOREKSI ATAS AUDIT SAYA SEBELUMNYA

Saya perlu meralat dua hal. Audit pertama saya dibuat hanya dari file `rev4b.docx`, dan dua
kesimpulannya ternyata salah:

| Klaim saya sebelumnya | Faktanya |
|---|---|
| "Tidak ada satu pun uji diagnostik" (Temuan A6) | **Salah.** File `test asumsi.docx` berisi uji multikolinearitas (VIF), heteroskedastisitas (Breusch-Pagan/Cook-Weisberg), dan matriks korelasi. Semuanya sudah dijalankan. |
| "Tidak ada standard error robust" | **Salah.** File `komparasi hasil regresi.docx` berisi FE dengan `fe ro` — clustered robust SE pada 105 klaster industri. Persis yang saya rekomendasikan. |

Temuan lain di audit pertama tetap berlaku, dan satu di antaranya justru **jauh lebih serius**
dari dugaan awal saya. Lihat bagian berikutnya.

---

## TEMUAN 1 — Sumber Tabel 4.2 akhirnya ketahuan, dan masalahnya lebih besar

Saya berhasil melacak asal statistik model di Tabel 4.2.

File `komparasi hasil regresi.docx` dibuka dengan baris:

> **"Menggunakan cross section satu tahun (tahun 2012)"**
> `reg lnEkspor lnPx lnPm lnWTotProd lnWTotPlain Pd lnTotProd lnTotPlain lnCapital asing laborIntensive capitalIntensive`
> `Number of obs = 88`, `F(11, 76) = 4.89`, `R-squared = 0.4146`

Bandingkan dengan Tabel 4.2 di naskah Anda: `F(11,107)=4.89`, `R-squared = 0.4146`.

**F dan R² cocok persis.** Jumlah regresornya juga persis 11. Dan derajat bebas penyebut yang
benar adalah 88 − 11 − 1 = **76**, bukan 107.

### Artinya

> **Tabel 4.2 — tabel hasil utama tesis Anda — bukan hasil regresi data panel.
> Statistik modelnya berasal dari regresi cross-section satu tahun (2012) dengan 88 observasi.**

Padahal seluruh BAB III, BAB IV, dan BAB V menyatakan penelitian ini memakai data panel
2007–2012 dengan 643 observasi. Ini bukan sekadar salah ketik — ini **salah tabel**.

Lebih jauh lagi, kolom koefisien dan standard error di Tabel 4.2 juga tidak cocok dengan
regresi cross-section itu (`lnCapital` 0,0424 vs 0,0635; `capitalIntensive` −1,188 vs −0,965),
dan memuat variabel `lnRer` yang tidak ada di regresi mana pun dalam file Anda. Sementara
`lnWPekerja = 0,174` justru cocok dengan `lnWTotProd = 0,1749` dari **regresi pooled panel
N=623** — regresi yang berbeda lagi.

**Kesimpulan: Tabel 4.2 adalah tabel gabungan dari sedikitnya tiga regresi berbeda.**
Ini yang paling berbahaya di meja sidang, dan wajib diregenerasi dari satu regresi tunggal.

### Kontrasnya dengan file Drive Anda

Sebagai pembanding, saya cek konsistensi aritmetik seluruh baris FE-robust di
`komparasi hasil regresi.docx` — `t = koefisien ÷ SE` untuk kedelapan variabel:

| Variabel | koef ÷ SE | t dilaporkan | |
|---|---|---|---|
| lnPx | −1,69 | −1,69 | ✅ |
| lnPm | −1,89 | −1,89 | ✅ |
| lnWTotProd | 1,21 | 1,21 | ✅ |
| lnWTotPlain | −0,03 | −0,03 | ✅ |
| lnTotProd | 0,16 | 0,16 | ✅ |
| lnTotPlain | 0,78 | 0,78 | ✅ |
| lnCapital | −0,76 | −0,76 | ✅ |
| asing | −1,35 | −1,35 | ✅ |

**Delapan dari delapan cocok sempurna.** Output Stata asli Anda bersih. Yang rusak hanyalah
tabel yang diketik ulang secara manual ke dalam naskah — persis seperti yang saya duga.

---

## TEMUAN 2 — Anda mengerjakan draft yang salah

| File | Ukuran | Terakhir diubah |
|---|---|---|
| `draftp Proposal tesis rev4b.docx` (yang kita pakai) | 1,008 KB | Januari 2016 |
| **`draftp Proposal tesis 4c.docx`** | 304 KB | **24 Februari 2016** |

**Versi 4c lebih baru satu bulan** dan isinya sudah direvisi:

- Judul Gambar 1.1 sudah diperbaiki menjadi "Tren Ekspor Industri **Labor Intensive**"
  (di rev4b masih keliru: "Tren Ekspor Industri Manufaktur")
- Sumber Gambar 1.2 diubah dari WITS menjadi **Comtrade**
- Sudah mengutip **Mehta & Sun (2013)** dan **Yeaple (2004)** — literatur yang diminta pembimbing
- Kalimat-kalimatnya lebih rapi dan beberapa salah ketik sudah dibersihkan

**Tindakan wajib:** pastikan versi mana yang terakhir dilihat pembimbing sebelum kita lanjut.
Kalau 4c, seluruh pekerjaan revisi harus berpindah ke 4c, bukan rev4b.

---

## TEMUAN 3 — Ini masalah ilmiah terbesar Anda, dan pembimbing kemungkinan sudah melihatnya

Di seluruh file Anda ada **dua variabel terikat berbeda** yang dipakai bergantian:

- `lnEkspor` — **nilai** ekspor (US$)
- `lnVolume` — **volume/kuantitas** ekspor

Perhatikan apa yang terjadi pada koefisien harga ekspor:

| Spesifikasi | Variabel terikat | Koefisien lnPx |
|---|---|---|
| Cross-section 2012 | lnEkspor (nilai) | **+0,175** |
| OLS robust N=105 | lnEkspor (nilai) | **+0,171** |
| Pooled panel N=623 | lnVolume (kuantitas) | **−0,577** |
| FE robust N=623 | lnVolume (kuantitas) | **−0,435** |
| 2SLS N=100 | lnVolume (kuantitas) | **−0,260** |

**Tandanya berbalik total.** Ini bukan kebetulan, dan penjelasannya sederhana:

> Nilai ekspor = harga × kuantitas. Kalau Anda menaruh **nilai** di ruas kiri dan **harga**
> di ruas kanan, harga muncul di kedua sisi persamaan. Koefisien positif yang Anda dapat
> sebagian bersifat **mekanis**, bukan perilaku ekonomi.

Kerangka Riveros (1992) yang Anda pakai adalah **fungsi penawaran**: `Qx^s = f(Px, w, Pm)`.
Huruf **Q** di situ berarti **kuantitas**. Jadi secara teori, variabel terikat yang benar
adalah `lnVolume`, bukan `lnEkspor`.

### Tapi ada lapisan kedua yang lebih menarik

Setelah beralih ke volume, koefisien harga justru menjadi **negatif**. Untuk fungsi penawaran,
harga naik seharusnya membuat kuantitas yang ditawarkan **naik** — koefisien positif.
Negatif berarti yang tertangkap regresi Anda bukan kurva penawaran, melainkan **kurva permintaan**.

Ini adalah **masalah identifikasi simultan klasik** dalam estimasi ekspor — dan Anda sudah
mengutip literaturnya sendiri: **Goldstein & Khan (1978)**, yang justru memakai model simultan
untuk memisahkan sisi penawaran dari sisi permintaan.

Anda bahkan sudah menjalankan solusinya. Di `komparasi hasil regresi.docx`:

```
ivregress 2sls lnVolume (lnPx = lnPxWorld lnGdp lnPx_1) lnPm lnAvgWProd lnAvgWPlain ...
```

Anda meng-instrumen harga ekspor dengan **harga dunia**, **GDP negara tujuan**, dan
**harga tertinggal (lnPx_1)** — ini instrumen yang secara teori tepat untuk menggeser
kurva permintaan sehingga kurva penawaran teridentifikasi. Pekerjaannya ada. Hanya saja
`lnGdp` gugur karena kolinearitas, dan hasilnya tidak pernah masuk naskah.

**Inilah yang akan mengangkat tesis Anda dari "sekadar lulus" menjadi tesis yang kuat.**

---

## TEMUAN 4 — Kesimpulan tesis Anda kemungkinan besar harus dibalik (dan itu bagus)

Ini hasil FE dengan clustered robust SE, N=623, 105 industri — spesifikasi paling kredibel
yang ada di seluruh file Anda:

| Variabel | Koefisien | Robust SE | t | p | Kesimpulan |
|---|---|---|---|---|---|
| lnWTotProd (upah produksi) | 0,0264 | 0,0219 | 1,21 | 0,229 | **tidak signifikan** |
| lnWTotPlain (upah non-produksi) | −0,0008 | 0,0251 | −0,03 | 0,974 | **tidak signifikan** |
| lnPx | −0,435 | 0,257 | −1,69 | 0,094 | signifikan 10% |
| lnPm | −0,023 | 0,012 | −1,89 | 0,062 | signifikan 10% |

Dan: `rho = 0,942` — **94,2% variasi berasal dari perbedaan permanen antar industri.**

### Bandingkan dengan yang tertulis di tesis Anda

Naskah Anda menyatakan: *"upah tenaga kerja berpengaruh positif dan signifikan terhadap
kinerja ekspor"*. Tetapi begitu Anda (a) memakai volume sebagai variabel terikat, (b) memasang
fixed effects industri, dan (c) mengoreksi standard error dengan clustering —
**pengaruh upah hilang sama sekali.**

### Kenapa ini justru kabar baik

Kesimpulan lama Anda secara teori memang janggal: upah naik menaikkan ekspor, berlawanan
dengan hipotesis sendiri, dan hanya bisa dijelaskan dengan permintaan maaf metodologis.

Kesimpulan baru jauh lebih kuat dan lebih mudah dipertahankan:

> **Setelah mengendalikan karakteristik permanen tiap industri dan mengoreksi standard error,
> tingkat upah tenaga kerja tidak terbukti berpengaruh signifikan terhadap kinerja ekspor
> industri manufaktur Indonesia. Kinerja ekspor jauh lebih ditentukan oleh faktor struktural
> yang melekat pada masing-masing industri — terlihat dari rho sebesar 0,942, yang berarti
> 94% variasi ekspor berasal dari perbedaan antar industri, bukan dari perubahan antarwaktu.**

Implikasi kebijakannya tajam dan relevan sampai hari ini:

> **Kebijakan pengendalian upah bukan instrumen efektif untuk mendorong daya saing ekspor
> manufaktur Indonesia.** Kekhawatiran bahwa kenaikan upah minimum akan menggerus ekspor tidak
> didukung data pada periode 2007–2012. Yang jauh lebih menentukan adalah faktor struktural
> industri: harga bahan baku impor, skala, dan karakteristik sektor.

Ini pesan yang **bisa dipublikasikan**, bukan sekadar diluluskan. Dan ini menjawab langsung
perdebatan upah minimum yang masih panas di Indonesia sampai sekarang.

⚠️ *Satu catatan jujur:* model FE tersebut punya `F(8,104) = 1,72` dengan `Prob > F = 0,1026`
— secara keseluruhan tidak signifikan pada 5%. Ini harus diperiksa dan dibahas terbuka,
bukan disembunyikan. Kemungkinan penyebabnya: variasi *within* memang sangat kecil (hanya 6%
dari total), sehingga enam tahun terlalu pendek untuk mengidentifikasi efek upah. Itu sendiri
merupakan temuan yang layak dilaporkan.

---

## TEMUAN 5 — Pembimbing sudah memberi peta jalan, dan baru separuh dikerjakan

File `catatan bimbingan.txt` berisi arahan pembimbing. Saya bandingkan dengan isi naskah:

| Arahan pembimbing | Status |
|---|---|
| Pisahkan total upah menjadi upah tenaga kerja produksi dan non-produksi | ✅ **Sudah** (lnWTotProd, lnWTotPlain) — tapi tidak masuk Tabel 4.2 dengan benar |
| Cari argumen: bukan *kenaikan* upah, tapi apakah **perbedaan upah antar sektor** menjelaskan perbedaan nilai ekspor | ⚠️ **Separuh** — inilah alasan regresi cross-section 2012 ada |
| Buat dummy kebijakan ekspor (pajak ekspor, kuota ekspor) antar sektor | ❌ **Belum sama sekali** |
| Karakteristik ISIC: nilai produksi tinggi/rendah, rasio produksi domestik vs total, size, penggolongan sektor | ⚠️ Hanya size & penggolongan sektor yang dikerjakan |
| **Buat statistik deskriptif** — pola ekspor Indonesia, sektor pengekspor terbesar, pangsa pasar, perbandingan upah produksi vs non-produksi, komoditas berharga relatif tinggi | ❌ **Sangat kurang** — BAB IV hanya ~4 paragraf deskriptif |
| Analisa deskriptif: perbedaan harga ekspor antar industri, grafik tiap variabel | ❌ **Belum** |
| Baca Mehta & Sun, "Does industry affiliation influence wages" | ✅ Sudah dikutip di draft 4c |

**Pola yang terlihat jelas:** pembimbing meminta analisis deskriptif yang jauh lebih kaya —
disebut dua kali dalam catatan yang sama, dengan daftar rinci. Ini permintaan yang paling
tegas dan paling belum dipenuhi. Kemungkinan besar **di sinilah tesis Anda tersendat pada 2016.**

Dan perhatikan arahan yang kedua: pembimbing mengarahkan Anda dari "dampak *kenaikan* upah"
menuju "**dampak perbedaan upah antar sektor**". Itu persis ide **variabel interaksi
upah × sektor** yang saya usulkan di audit pertama. Pembimbing Anda dan saya sampai pada
kesimpulan yang sama, terpisah sepuluh tahun.

---

## TEMUAN 6 — Jumlah observasi kacau di seluruh dokumen

Saya menemukan enam ukuran sampel berbeda dalam berkas Anda:

| N | Grup | Muncul di |
|---|---|---|
| 50 | — | regresi dekomposisi kepemilikan asing |
| 88 | — | cross-section 2012 (sumber statistik Tabel 4.2) |
| 100 | — | 2SLS versi `komparasi` |
| 105 | — | OLS robust `test asumsi` |
| **623** | **105** | panel di `komparasi hasil regresi.docx` |
| **643** | **108** | panel di lampiran `rev4b.docx` |

Dua panel utama (623/105 vs 643/108) berbeda — artinya ada **dua versi dataset**.
Penguji hampir pasti menanyakan: "Sebenarnya berapa observasi penelitian Anda?"

**Wajib:** tetapkan satu dataset master, jalankan ulang semua spesifikasi di atasnya,
dan laporkan satu angka N yang konsisten di seluruh naskah.

---

## TEMUAN 7 — Aset yang belum Anda manfaatkan

Isi folder Drive jauh lebih kaya dari naskah yang dihasilkan:

- **`data IBS 1990-2013`** — data Survei Industri Besar Sedang **24 tahun**, bukan 6.
  Ada `Statistik Industri Sedang Besar.mdb`, `Stat 1.accdb`, file layout `LAY8587.TXT`,
  `LAY9095.TXT`, dan kuesioner `VARQues2006/2007/2009` untuk kamus variabel.
- `Data_Ekspor-Impor-2015-02-23` — data ekspor-impor
- `table hs code dan sitc` — tabel konkordansi HS↔SITC↔ISIC (aset yang mahal dibuat)
- `pdrb`, `sakernas` — data yang belum dipakai sama sekali.
  **`sakernas` sangat berharga**: bisa dipakai membangun proksi produktivitas atau
  pendidikan/keterampilan tenaga kerja, yang persis dibutuhkan untuk menghitung **ULC** dan
  menjawab masalah variabel produktivitas yang hilang.
- `StatTransfer9` — alat konversi Access/dBase ke Stata
- `presentasi tesis rev.1.ppt` + `.pdf` — bahan presentasi sidang sudah ada
- `abstrak versi Indonesia` & `abstrak versi inggris` (docx + pdf) — abstrak sudah jadi
- `Cover.docx`, `DAFTAR ISI.docx`, `SURAT PERNYATAAN.docx` — kelengkapan administratif sudah ada
- BAB I, BAB II, BAB IIa, BAB III sebagai file terpisah — berguna untuk membandingkan versi

Artinya: **kelengkapan dokumen sidang Anda sesungguhnya sudah hampir penuh.** Yang hilang
hanyaperakitan dan perbaikan BAB IV–V.

---

## STRATEGI YANG SAYA REKOMENDASIKAN

### Prinsip utama
**Jangan mengumpulkan data baru. Jangan mengganti topik. Rakit dan perbaiki yang sudah ada.**
Pekerjaan empiris Anda 70% sudah selesai — ia hanya tersebar di file yang tidak pernah disatukan.

### Model utama yang saya usulkan

```
lnVolume_it = α + β₁lnPx_it + β₂lnPm_it + β₃lnWProd_it + β₄lnWPlain_it
            + β₅lnTotTK_it + β₆lnCapital_it + β₇Asing_it
            + γ₁(lnWProd × laborIntensive) + γ₂(lnWProd × capitalIntensive)
            + δ_t (dummy tahun) + μ_i (fixed effect industri) + ε_it
```

dengan **cluster-robust standard error** pada level industri.

Lima alasan mengapa ini menyelesaikan hampir semua masalah sekaligus:

1. **`lnVolume`** — variabel terikat yang benar untuk fungsi penawaran Riveros
2. **Upah dipisah produksi/non-produksi** — memenuhi arahan pembimbing
3. **Interaksi upah × sektor** — menjawab Tujuan Penelitian #2 meski dummy sektor terserap FE,
   sekaligus menjawab arahan pembimbing tentang perbedaan upah antar sektor
4. **Dummy tahun** — mengendalikan guncangan makro, terutama krisis global 2008–2009
5. **Cluster-robust SE** — mengatasi heteroskedastisitas (yang uji Anda sendiri sudah
   deteksi: Breusch-Pagan chi²=5,04, p=0,0248) dan autokorelasi sekaligus

Ditambah **2SLS** sebagai uji robustness, meng-instrumen `lnPx` dengan `lnPxWorld` dan
`lnPx_1` (versi yang sudah Anda jalankan, tinggal dirapikan dan diuji kekuatan instrumennya).

### Urutan kerja

| Tahap | Pekerjaan | Butuh apa |
|---|---|---|
| **1** | Tetapkan draft mana yang dipakai (4c vs rev4b) & dataset master mana (623 vs 643) | Keputusan Anda |
| **2** | Rekonstruksi & jalankan ulang seluruh spesifikasi dari satu dataset | File `.dta` + `.do` |
| **3** | **Bangun BAB IV deskriptif yang kaya** sesuai daftar pembimbing — ini prioritas tertinggi yang belum dikerjakan | Data |
| **4** | Regenerasi seluruh tabel hasil secara otomatis dari output | — |
| **5** | Tulis ulang BAB IV–V dengan kesimpulan baru | — |
| **6** | Rapikan BAB I–III, mutakhirkan literatur, perbaiki daftar pustaka | — |
| **7** | Format UI, kelengkapan, simulasi sidang | — |

---

## YANG SAYA BUTUHKAN DARI ANDA

Saya bisa membaca folder Drive Anda, tetapi **tidak bisa menjalankan regresi dari sana** —
file Access dan Stata perlu ada di folder kerja lokal agar bisa saya olah.

**Langkah paling penting sekarang:** unduh dua folder ini dari Drive, lalu letakkan di folder
tesis di komputer Anda (folder yang sama dengan tempat file ini berada):

1. Seluruh isi **`ketikan tesis`** — terutama `draftp Proposal tesis 4c.docx`
2. File data Stata (`.dta`) dan do-file (`.do`) — kalau tidak ketemu di Drive, cek folder
   `data` → `Data` → `StatTransfer9`, atau hard disk lama Anda

Setelah itu saya bisa langsung menjalankan seluruh spesifikasi di atas dan menghasilkan
tabel hasil yang bersih dan konsisten.

**Tiga pertanyaan yang perlu Anda jawab:**

1. Versi mana yang terakhir dilihat pembimbing — `rev4b` atau `4c`?
2. Apakah Anda masih punya file `.dta` dan `.do`? (Saya tidak menemukannya di Drive —
   kemungkinan ada di folder lain atau hard disk lama.)
3. Apakah Anda masih terdaftar aktif di UI, atau perlu mengurus aktivasi kembali?
   Ini menentukan realistis tidaknya target waktu.
