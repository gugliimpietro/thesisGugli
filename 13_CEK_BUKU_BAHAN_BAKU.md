# CEK PUBLIKASI BAHAN BAKU 2012 — BENAR, TAPI BARU SEPARUH

**Berkas:** `49027-ID-statistik-industri-besar-dan-sedang-bahan-baku-bagian-a-tahun-2012.pdf`
**Tanggal:** 17 September 2026

---

## 1. Ya, ini publikasi yang benar

**Statistik Industri Manufaktur — BAHAN BAKU, Indonesia 2012**
Katalog BPS 6103002 · No. Publikasi 05310.1404 · 540 halaman · KBLI 2009 (ISIC Rev.4)

Dan strukturnya **persis** yang dibutuhkan:

```
Kode KKI | Deskripsi | Satuan | Impor: Banyaknya, Nilai | Jumlah: Banyaknya, Nilai
```

Kolom **Impor dipisah dari Jumlah**. Dari satu tabel ini keluar dua variabel sekaligus:

- **`Pm`** = nilai bahan baku impor ÷ banyaknya bahan baku impor → harga input impor per kg
- **pangsa input impor** = nilai impor ÷ nilai total → variabel kontrol Amiti & Konings (2007)

Bahan baku domestik pun bisa dihitung sebagai Jumlah − Impor, bila nanti diperlukan.

---

## 2. Masalahnya: ini baru Bagian A

Saya uji setiap KBLI dengan membandingkan penjumlahan jenis barang terhadap baris
"Jumlah - Total" yang tercetak di publikasi itu sendiri.

| Cakupan item terhadap total tercetak | |
|---|---|
| Persentil 25 | 25% |
| **Median** | **45%** |
| Persentil 75 | 68% |
| KBLI dengan cakupan ≥ 95% | **8 dari 299** |

Median 45% bukan efek penyensoran — ini **pemisahan buku**. Daftar jenis barang untuk setiap
KBLI terpotong, dan sisanya ada di **Bagian B**.

Contoh yang jelas: KBLI 10110 (rumah potong hewan) lengkap di Bagian A — tiga jenis barang,
jumlah 4.755.046 ribu rupiah, cocok persis dengan Tabel 7 Buku I. Tetapi KBLI 10213 hanya
4.377.239.561 dari 7.863.366.389 yang seharusnya — sekitar 56%.

### Akibatnya untuk masing-masing variabel

**Pangsa input impor: belum bisa dipakai.** Ia adalah rasio dua penjumlahan, dan kedua
penjumlahan itu belum lengkap. Median pangsa impor yang terhitung sekarang 8,5%, tetapi angka
itu akan berubah setelah Bagian B masuk.

**`Pm`: bisa dipakai sementara, dengan catatan.** Harga adalah rasio nilai terhadap kuantitas,
jadi ia tetap bermakna meski dihitung dari sebagian jenis barang — hanya bobotnya yang belum
mewakili keseluruhan.

---

## 3. Hasil ekstraksi sementara

`data/Pm_2012_KBLI5_bagianA.csv`

| | |
|---|---|
| KBLI terbaca | 349 |
| Jenis bahan baku terbaca | 16.463 |
| KBLI dengan `Pm` per kg | 253 |
| `Pm` median | **Rp 1.343/kg** |

Kolom `cakupan` disertakan di setiap baris supaya kualitas tiap KBLI terlihat, dan supaya nanti
mudah dibandingkan setelah Bagian B digabungkan.

---

## 4. Masalah yang sama terjadi pada Buku Produksi — tapi terbalik

| Publikasi | Yang Anda punya | Yang kurang |
|---|---|---|
| **Bahan Baku** (Katalog 6103002) | **Bagian A** ✅ | **Bagian B** ❌ |
| **Produksi** (Katalog 6103014) | **Bagian B** ✅ | **Bagian A** ❌ |

Kebetulan yang tidak menguntungkan: dari dua publikasi, Anda memegang bagian yang berbeda dari
masing-masing. Cakupan `Pd` dari Buku Produksi yang median 79% kemarin — sebagiannya bukan
penyensoran seperti dugaan saya, melainkan gejala yang sama.

**Dua unduhan lagi dan seluruh variabel harga selesai:**

1. Statistik Industri Manufaktur — **Bahan Baku 2012, Bagian B** (Katalog 6103002)
2. Statistik Industri Manufaktur — **Produksi 2012, Bagian A** (Katalog 6103014)

Setelah keduanya ada, saya gabungkan dan jalankan ulang. Skrip ekstraksinya sudah siap dan
sudah terbukti jalan pada kedua format — tinggal membaca dua berkas tambahan lalu menjumlahkan.

---

## 5. Status variabel model

| Variabel | Status |
|---|---|
| `ULC` — biaya tenaga kerja per unit output | ✅ **selesai**, 357 KBLI |
| Upah produksi & non-produksi terpisah | ✅ selesai |
| Rasio keterampilan | ✅ selesai |
| Tenaga kerja, kapital, kepemilikan asing | ✅ selesai |
| Klasifikasi sektor | ✅ selesai |
| `Pm` — harga bahan baku impor | ⏳ sementara, menunggu Bagian B |
| Pangsa input impor | ⏳ menunggu Bagian B |
| `Pd` — harga domestik | ⏳ sementara, menunggu Produksi Bagian A |
| `lnVolume`, `Px` — ekspor | ❌ menunggu data Comtrade |

Satu-satunya yang belum punya jalur sama sekali adalah **data ekspor Comtrade**. Itu yang
menentukan variabel terikat, jadi cepat atau lambat harus diunduh.
