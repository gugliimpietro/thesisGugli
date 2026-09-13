# HASIL PEMERIKSAAN DATA 2012 — JAWABAN: TIDAK PERLU MINTA KE BPS

**Tanggal:** 13 September 2026
**Sumber:** `statistik-industri-manufaktur-indonesia-2012.pdf` (BPS, Katalog 6103019, 616 halaman)
**Lokasi:** `bahan tesis\data\data IBS 1990-2013\Data industri manufaktur\PDF file`

---

## JAWABAN SINGKAT

> **Publikasi yang Anda unduh sudah cukup. Tidak perlu meminta mikrodata ke BPS.**

Publikasi ini memuat **409 jenis industri KBLI 5 digit**, dan — yang menentukan — **nilai tambah
diterbitkan langsung**, tidak perlu dihitung sendiri. Unit Labour Cost bisa dibangun sepenuhnya
dari tabel-tabel di dalamnya.

Saya sudah mengekstraksi seluruh datanya dan menghasilkan berkas siap pakai:
**`data/SI2012_KBLI5.csv` — 398 baris industri, 357 di antaranya lengkap dengan ULC terhitung.**

Bandingkan dengan N = 100 pada draft 4c: **jumlah observasi naik tiga setengah kali lipat.**

---

## APA YANG ADA DI DALAM PUBLIKASI

| Tabel | Isi | Kegunaan |
|---|---|---|
| **Tabel 3** | Jumlah perusahaan; tenaga kerja **produksi** dan **lainnya**, dirinci laki-laki/perempuan | Skala industri, penyebut upah per pekerja |
| **Tabel 4** | Pengeluaran untuk pekerja **produksi** dan **lainnya** secara terpisah — upah/gaji, lembur, bonus, pensiun, tunjangan kecelakaan | **Arahan pembimbing terpenuhi**; pembilang ULC |
| **Tabel 7** | Biaya input: bahan baku & penolong, bahan bakar/listrik/gas, sewa | Biaya antara |
| **Tabel 8** | Nilai output: barang dihasilkan, listrik dijual, jasa industri | Output |
| **Tabel 9** | **Nilai output, biaya input, nilai tambah (harga pasar), pajak tak langsung, nilai tambah (biaya faktor produksi)** | **Penyebut ULC — tersedia langsung** |
| Tabel 11–20 | Seluruh variabel di atas **menurut provinsi** | Konteks; bukan silang industri × provinsi |
| Lampiran 2 | Kuesioner Survei 2012 | Verifikasi definisi variabel |

Catatan penting dari BPS: setiap kode industri disajikan dalam **dua baris** — angka tebal
adalah total industri besar dan sedang, angka miring hanya industri besar. Tanda `*` berarti
**tidak dipublikasikan** karena alasan kerahasiaan (jumlah perusahaan terlalu sedikit). Saya
mengambil baris total IBS.

---

## VERIFIKASI YANG SUDAH SAYA JALANKAN

Bukan sekadar menyalin — saya uji identitas akuntansinya di seluruh 398 baris:

| Identitas | Hasil |
|---|---|
| Nilai tambah = nilai output − biaya input | **357 cocok, 0 tidak cocok** |
| NT biaya faktor = NT harga pasar − pajak tak langsung | **355 cocok, 0 tidak cocok** |
| Upah total = upah produksi + upah non-produksi | **352 cocok, 0 tidak cocok** |
| Tenaga kerja produksi + lainnya ≤ total | **0 pelanggaran** |

Nol ketidakcocokan di ketiga identitas. Ekstraksinya bersih, dan penamaan kolom sudah benar —
ini penting, karena urutan header pada teks PDF sempat menyesatkan dan hanya ketahuan lewat uji
aritmetik silang dengan Tabel 7 dan Tabel 8.

---

## HASIL AWAL — ULC INDUSTRI MANUFAKTUR INDONESIA 2012

Sebaran ULC pada 357 industri KBLI 5 digit:

| | Nilai |
|---|---|
| Minimum | 0,008 |
| Persentil 25 | 0,112 |
| **Median** | **0,229** |
| Persentil 75 | 0,406 |
| Maksimum | 5,510 |

Median 0,229 berarti: dari setiap Rp 1 nilai tambah yang dihasilkan industri manufaktur
Indonesia, sekitar **Rp 0,23 mengalir ke tenaga kerja**. Angka ini masuk akal dan sebanding
dengan pangsa upah dalam nilai tambah manufaktur negara berkembang.

Ekor atas (maksimum 5,5) berasal dari industri dengan nilai tambah sangat kecil — akan
ditangani dengan winsorisasi persentil 1 dan 99.

**Pemeriksaan kewajaran lain:**

| Indikator | Median |
|---|---|
| Upah per pekerja produksi | Rp 23,7 juta/tahun (≈ Rp 2,0 juta/bulan) |
| Upah per pekerja non-produksi | Rp 34,7 juta/tahun (≈ Rp 2,9 juta/bulan) |
| Nilai tambah per pekerja | Rp 113,8 juta/tahun |

Rasio upah non-produksi terhadap produksi sekitar 1,46 — inilah **proksi intensitas
keterampilan** (Teknik D) yang sudah bisa langsung dipakai.

---

## BERKAS YANG DIHASILKAN

**`data/SI2012_KBLI5.csv`** — 398 baris, kolom:

`kbli` · `n_perusahaan` · `tk_produksi` · `tk_lainnya` · `tk_total` · `upah_produksi` ·
`upah_lainnya` · `upah_total` · `biaya_input` · `nilai_output` · `nt_harga_pasar` ·
`pajak_tak_lgsg` · `nt_biaya_faktor` · `ULC` · `upah_per_pekerja_produksi` ·
`upah_per_pekerja_lainnya` · `produktivitas_per_pekerja`

Seluruh nilai rupiah dalam **ribuan rupiah**, sesuai satuan publikasi BPS. Kolom turunan
(`upah_per_pekerja_*`, `produktivitas_*`) sudah dikonversi ke rupiah penuh.

**`scripts/extract_si2012.py`** — skrip ekstraksi, bisa dijalankan ulang kapan saja. Ia membaca
PDF, mendeteksi batas kolom dari pola spasi, dan menjalankan ketiga uji identitas di atas.
Tidak ada satu angka pun yang diketik manual.

---

## YANG BISA DAN TIDAK BISA DILAKUKAN DENGAN DATA INI

### ✅ Bisa

| Teknik | Status |
|---|---|
| **A — Unit Labour Cost** | **Siap, sudah terhitung** |
| **D — Upah produksi/non-produksi terpisah + rasio keterampilan** | **Siap** |
| **E — Interaksi ULC × sektor** | Siap, tinggal bentuk dummy sektor |
| F — Kontrol skala, kapital, produktivitas | Siap |
| Statistik deskriptif lengkap | Siap — permintaan pembimbing yang paling belum tergarap |

### ⚠️ Perlu pekerjaan tambahan

**Konkordansi klasifikasi.** Publikasi 2012 memakai **KBLI 2009 = ISIC Rev.4**, sedangkan tesis
Anda dan data ekspor Comtrade Anda memakai **ISIC Rev.3**. Keduanya harus dijembatani sebelum
digabungkan. Tabel korespondensi Rev.4 ↔ Rev.3 tersedia resmi dari UNSD, dan folder
`table hs code dan sitc` Anda sudah memuat sebagian bahannya. Ini pekerjaan teknis yang jelas,
bukan hambatan.

**Pangsa bahan baku impor** tidak ada di Buku I. Ia ada di **Buku II (Bahan Baku)** — publikasi
terpisah, juga gratis di situs BPS. Kalau ingin memakai kontrol Amiti & Konings, unduh buku itu.

### ❌ Tidak bisa dari publikasi ini

**Silang industri × provinsi.** Publikasi menyajikan data menurut industri (Tabel 1–10) dan
menurut provinsi (Tabel 11–20), tetapi tidak menyilangkan keduanya. Padahal instrumen upah
minimum (Teknik B) membutuhkan pangsa tenaga kerja tiap industri di tiap provinsi.

**Jalan keluarnya:** ambil bobot provinsi dari **Sakernas**, yang memuat kode industri dan
provinsi sekaligus. Berkas `sakernas.zip` ada di Drive Anda tetapi **belum ada di folder lokal**
— perlu diunduh, dan perlu dipastikan tahun berapa isinya.

---

## LANGKAH BERIKUTNYA

| # | Pekerjaan | Butuh apa |
|---|---|---|
| 1 | Konkordansi KBLI 2009 / ISIC Rev.4 → ISIC Rev.3 | Tabel UNSD |
| 2 | Gabungkan `SI2012_KBLI5.csv` dengan data ekspor Comtrade | Data ekspor Anda |
| 3 | Bentuk dummy sektor menurut Narjoko & Putra (2014) | — |
| 4 | Statistik deskriptif lengkap BAB IV | Siap dikerjakan |
| 5 | Estimasi enam spesifikasi, tabel digenerate otomatis | Setelah 1–3 |
| 6 | Unduh Buku II (Bahan Baku) bila ingin kontrol pangsa impor | Situs BPS |
| 7 | Unduh `sakernas.zip` bila ingin instrumen upah minimum | Drive Anda |

Nomor 1 adalah pintu gerbangnya — tanpa konkordansi, data industri dan data ekspor tidak bisa
disatukan. Itu yang saya sarankan dikerjakan berikutnya.

---

## CATATAN UNTUK BAB III

Justifikasi periode yang sekarang ada di draft 4c perlu diperbarui. Kalimat yang akurat:

> Penelitian ini menggunakan data tahun 2012 yang bersumber dari publikasi *Statistik Industri
> Manufaktur Indonesia 2012* (BPS, Katalog 6103019). Publikasi tersebut mengelompokkan industri
> manufaktur besar dan sedang ke dalam 409 kelompok KBLI 2009 lima digit, yang merupakan adaptasi
> ISIC Rev.4 untuk kondisi Indonesia. Data yang tersedia mencakup jumlah perusahaan, tenaga kerja
> produksi dan non-produksi, pengeluaran untuk masing-masing kelompok pekerja, biaya input, nilai
> output, dan nilai tambah — seluruhnya pada tingkat industri lima digit.

Perhatikan: **cakupan survei adalah perusahaan dengan 20 pekerja atau lebih**. Itu harus
dinyatakan sebagai keterbatasan di subbab 3.7, karena industri kecil dan mikro tidak tercakup.
