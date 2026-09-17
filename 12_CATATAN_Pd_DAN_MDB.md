# CATATAN — HARGA DOMESTIK (Pd) DAN BERKAS ImporIndonesia.mdb

**Tanggal:** 16 September 2026

---

## 1. PDF yang diunduh ternyata Buku III, bukan Buku II

Berkas `49029-ID-statistik-industri-manufaktur-produksi-bagian-b-tahun-2012.pdf` adalah
**Statistik Industri Manufaktur — PRODUKSI** (Katalog BPS 6103014), berisi banyaknya dan nilai
**barang yang dihasilkan** per jenis barang.

Yang dibutuhkan untuk `Pm` (harga bahan baku impor) adalah **Buku II — BAHAN BAKU**, yang
memuat banyaknya dan nilai bahan baku yang **dipakai**, dipisah antara asal dalam negeri dan
impor. Itu publikasi terpisah dan belum ada.

**Tetapi Buku III tetap berguna** — dan untuk variabel yang sebenarnya sudah pernah ada di
pekerjaan Anda sendiri.

---

## 2. Buku III memberi harga domestik (Pd)

Strukturnya: untuk setiap KBLI 5 digit, setiap jenis barang dirinci dengan kode KBKI 9 digit,
satuan, banyaknya, dan nilai. Dari situ harga produsen domestik dihitung sebagai nilai ÷ banyaknya.

**Kenapa ini penting.** Regresi cross-section 2012 Anda yang tersimpan di
`komparasi hasil regresi.docx` memuat variabel `Pd`:

```
reg lnEkspor lnPx lnPm lnWTotProd lnWTotPlain Pd lnTotProd ...
```

Variabel itu hilang dari draft 4c. Dan secara teori ia memang seharusnya ada: Goldstein & Khan
(1978) memasukkan indeks harga domestik ke dalam persamaan penawaran ekspor, karena yang
menentukan keputusan mengekspor adalah **harga ekspor relatif terhadap harga domestik**
(Px/Pd), bukan harga ekspor semata.

**Verifikasi:** total nilai produksi per KBLI di Buku III cocok persis dengan Tabel 8 Buku I
(contoh KBLI 10110: 6.220.937 ribu rupiah di kedua buku). Kedua publikasi konsisten.

### Hasil ekstraksi

`data/Pd_2012_KBLI5.csv` — **270 KBLI** dengan harga per kilogram, 11.385 baris jenis barang
terbaca.

| | Rp/kg |
|---|---|
| Persentil 10 | 1.020 |
| Median | 10.708 |
| Persentil 90 | 73.118 |

### ⚠️ Peringatan kualitas — baca sebelum dipakai

**Jangan langsung masukkan ke regresi.** Ada tiga masalah nyata:

**Penyensoran BPS.** Banyak jenis barang ditandai `*` (tidak dipublikasikan karena kerahasiaan).
Cakupan nilai yang terbit terhadap total produksi: **median 79%**, tetapi sebagian KBLI hanya
sekitar 59%. Kolom `cakupan_nilai_terbit` merekam ini per baris.

**Satuan bercampur.** Dari 11.385 jenis barang: BUAH 3.190, KG 2.385, SET 624, TON 540, METER
422, LUSIN 412, M3 402. Harga per kilogram hanya bisa dihitung untuk barang bersatuan KG,
sehingga banyak industri tidak punya `Pd` yang sebanding dengan `Px` (yang dari Comtrade juga
per kg).

**Sebagian angka tidak masuk akal.** Contoh nyata di KBLI 10110: daging sapi tanpa tulang
Rp 42.077/kg (wajar untuk 2012), tetapi "hasil ikutan/sisa industri pemotongan hewan"
Rp 138.199/kg — limbah pemotongan hewan tidak mungkin lebih mahal daripada daging sapi. Ada
ketidakkonsistenan satuan di sumbernya.

**Yang lolos saringan ketat** (cakupan ≥ 70% dan pangsa barang bersatuan KG ≥ 50%):
**hanya 66 KBLI**. Terlalu sedikit untuk menjadi regresor utama pada 355 industri.

### Rekomendasi

Pakai `Pd` sebagai **variabel uji ketahanan**, bukan regresor utama — dijalankan pada subsampel
yang lolos saringan kualitas, dan dilaporkan apa adanya beserta jumlah observasinya. Menyajikan
`Px/Pd` sebagai harga relatif pada subsampel tersebut justru menjadi nilai tambah, selama
keterbatasannya dinyatakan.

Kolom `cakupan_nilai_terbit` dan `pangsa_item_kg` sudah disediakan supaya penyaringan bisa
dilakukan dan dipertanggungjawabkan.

---

## 3. ImporIndonesia.mdb tidak bisa saya baca dari jarak jauh

Ukurannya **763 MB**, sedangkan batas transfer berkas dari komputer Anda ke sesi ini **400 MB**.
Jembatan Windows juga tidak memberi saya shell untuk menjalankan query di tempat.

Karena itu saya siapkan `scripts/cek_mdb.ps1`. Skrip itu membuka database, mendaftar seluruh
tabel beserta jumlah baris, nama kolom, dan satu baris contoh, lalu menulis hasilnya ke
`data/mdb_struktur.txt`.

**Cara menjalankan:**

```powershell
cd "E:\onedrive\...\10. thesis gugli"
.\scripts\cek_mdb.ps1
```

Kirimkan isi `data\mdb_struktur.txt` ke saya. Dari situ saya bisa menentukan tabel dan kolom
mana yang dibutuhkan, lalu menuliskan query ekspor yang menghasilkan CSV kecil — kemungkinan
hanya baris tahun 2012 dengan kode HS, nilai, dan kuantitas. Ukuran CSV seperti itu wajar di
bawah 100 MB dan bisa saya olah langsung.

Bila skrip gagal karena provider OLEDB tidak tersedia, pasang **Microsoft Access Database
Engine 2016 Redistributable** versi 64-bit, atau buka berkasnya langsung di Microsoft Access
dan salin daftar tabelnya secara manual.

---

## 4. Yang dibutuhkan berikutnya

| # | Bahan | Untuk | Cara |
|---|---|---|---|
| 1 | **Buku II — Bahan Baku 2012** | `Pm` dan pangsa input impor | Unduh gratis di situs BPS |
| 2 | Struktur `ImporIndonesia.mdb` | Alternatif/pembanding `Pm` | Jalankan `scripts\cek_mdb.ps1` |
| 3 | Data ekspor Comtrade 2012 | `lnVolume`, `Px` | Unduh, konkordansi HS → ISIC Rev.4 |

Nomor 1 adalah jalur paling cepat dan paling bersih untuk `Pm` — satu unduhan, formatnya sama
dengan Buku I dan Buku III yang sudah terbukti bisa diekstraksi, dan sekaligus memberi pangsa
bahan baku impor sebagai variabel kontrol.

Nomor 2 berguna sebagai pembanding, dan berpotensi memberi harga impor pada tingkat HS yang
jauh lebih rinci daripada publikasi.
