# PANDUAN MENGAMBIL DATA EKSPOR (Qx, Px) DAN IMPOR (Pm)

**Tanggal:** 18 September 2026
**Pertanyaan Anda:** bisakah pakai trademap.org atau Comtrade?

---

## VONIS SINGKAT

| Sumber | Untuk tesis ini | Alasan |
|---|---|---|
| **UN Comtrade** | **PAKAI INI** | Gratis, HS 6-digit, ada nilai *dan* berat, bisa diunduh otomatis lewat API, mudah disitasi |
| Trade Map (ITC) | **Jangan** | Perlu login, unduhan dibatasi beberapa ratus baris per query pada akun gratis, dan **datanya sendiri berasal dari Comtrade** |
| Bea Cukai (`ImporIndonesia.mdb`) | Tetap dipakai sebagai pembanding | Sumber nasional, bagus untuk uji silang Pm |

Trade Map itu **etalase** Comtrade, bukan sumber terpisah. Mengambil dari Trade Map
berarti mengambil angka yang sama lewat jalan yang lebih sempit dan lebih sulit
direplikasi penguji. Jadi: langsung ke Comtrade.

---

## SATU KEPUTUSAN YANG MENYEDERHANAKAN BANYAK HAL

Comtrade memberi **ekspor dan impor sekaligus** dalam satu format yang sama.
Artinya:

- **Qx** (variabel terikat) = `netWgt` arus ekspor → berat ekspor dalam kg
- **Px** = nilai ekspor ÷ berat ekspor → USD per kg
- **Pm** = nilai impor ÷ berat impor → USD per kg

Kalau Pm diambil dari Comtrade juga, maka:

1. **Kita tidak lagi tergantung pada ekspor ulang tabel "Impor (Berat) KG"** dari
   `ImporIndonesia.mdb` yang kemarin terpotong di bab HS 38. Beban itu hilang.
2. **Px dan Pm terdefinisi dengan cara yang persis sama.** Ini penting secara
   metodologis — rasio harga `Px/Pm` di fungsi penawaran ekspor jadi konsisten,
   bukan campuran dua definisi yang berbeda.
3. Data Bea Cukai berubah peran: dari sumber utama menjadi **uji silang**. Kalau Pm
   Comtrade dan Pm Bea Cukai berkorelasi tinggi, itu satu paragraf validasi yang enak
   dituliskan di BAB III.

Jadi jawaban untuk pertanyaan kedua Anda: **ya, impor pun sebaiknya dari Comtrade** —
bukan karena Bea Cukai jelek, tapi karena konsistensi definisi lebih berharga daripada
sumber nasional yang formatnya berbeda.

---

## YANG HARUS ANDA LAKUKAN — 10 MENIT

### Langkah 1 — ambil API key gratis (disarankan, bukan wajib)

1. Buka **https://comtradedeveloper.un.org**
2. **Sign up** dengan email Anda → konfirmasi lewat email
3. Masuk ke menu **Products** → pilih **"Comtrade - v1"** → klik **Subscribe**
4. Buka **Profile** → salin **Primary key** (deretan huruf-angka panjang)

Key gratis memberi 500 panggilan per hari dan 100.000 baris per panggilan — jauh lebih
dari cukup, karena kita hanya perlu 2 panggilan.

> Tanpa key skrip tetap jalan, tapi lewat endpoint *preview* yang dibatasi 500 baris
> per panggilan, sehingga harus mengambil per bab HS satu per satu (± 3–4 menit dan
> ada risiko bab besar seperti 84/85 terpotong). Skrip akan memberi peringatan
> `<-- MENYENTUH BATAS 500` kalau itu terjadi.

### Langkah 2 — jalankan skrip

Simpan `fetch_comtrade_2012.py` di folder repo tesis (`D:\kuliah s2\1. tesis\thesisGugli\scripts\`),
lalu di Command Prompt:

```
cd "D:\kuliah s2\1. tesis\thesisGugli\scripts"
pip install requests
python fetch_comtrade_2012.py --key KUNCI_ANDA
```

atau tanpa key:

```
python fetch_comtrade_2012.py
```

### Langkah 3 — commit & push

```
cd "D:\kuliah s2\1. tesis\thesisGugli"
git add data scripts
git commit -m "data: ekspor-impor Comtrade 2012 HS6 + konkordans ISIC Rev.4"
git push
```

Lalu beri tahu saya. Saya lanjut menggabungkannya dengan `SI2012_KBLI5.csv`.

---

## APA YANG DIHASILKAN

| Berkas | Isi |
|---|---|
| `data/comtrade_2012_X_HS6.csv` | Ekspor Indonesia 2012 ke dunia, per kode HS 6-digit: nilai USD, berat kg, kuantitas |
| `data/comtrade_2012_M_HS6.csv` | Impor, format sama |
| `data/HS2012_ISIC4.csv` | Konkordans HS 2012 → ISIC Rev.4 |
| `data/trade_2012_ISIC4.csv` | Sudah diagregasi per industri: `X_usd, X_kg, M_usd, M_kg, Px_usd_per_kg, Pm_usd_per_kg` |

Berkas terakhir itulah yang langsung bisa saya gabungkan dengan data industri, karena
KBLI 2009 = ISIC Rev.4. Penyambungannya tinggal memotong KBLI 5-digit menjadi 4-digit.

---

## CATATAN JUJUR TENTANG KETERBATASANNYA

Ini harus Anda ketahui sebelum penguji menanyakannya.

**1. Berat bukan kuantitas fisik yang sempurna.**
`netWgt` adalah berat bersih dalam kg. Untuk industri seperti garmen atau elektronik,
kg bukan satuan yang paling bermakna — satu kilogram kaus tidak sebanding dengan satu
kilogram semikonduktor. Konsekuensinya, `Px = USD/kg` adalah **unit value**, bukan
indeks harga murni; ia ikut bergerak kalau komposisi produk di dalam satu industri
berubah. Ini keterbatasan standar dalam literatur unit-value dan sudah lazim diakui.
Tulis satu paragraf tentang ini di BAB III, jangan tunggu ditanya.

**2. Sebagian baris tidak punya berat.**
Comtrade kadang melaporkan nilai tanpa `netWgt`. Setelah data turun, saya akan hitung
berapa persen nilai ekspor yang punya berat. Kalau cakupannya di bawah ~85 % untuk
sebuah industri, industri itu perlu ditandai atau dikeluarkan.

**3. Pemetaan HS → ISIC tidak satu-ke-satu.**
Satu kode HS bisa jatuh ke lebih dari satu ISIC. Konkordans UNSD memilih satu pasangan
dominan, jadi ada sedikit kesalahan pengukuran di batas industri. Sama seperti poin 1:
akui, jangan sembunyikan.

**4. Ekspor Comtrade adalah ekspor *negara*, bukan ekspor *perusahaan disurvei BPS*.**
Penyebut dan pembilang berasal dari dua sistem statistik berbeda. Rasio seperti
"ekspor per output" bisa melebihi 1 pada beberapa industri karena re-ekspor dan karena
BPS hanya mencakup perusahaan ≥20 pekerja. Ini persis alasan mengapa model memakai
`lnQx` sebagai variabel terikat, bukan rasio ekspor terhadap output.

---

## KENAPA BUKAN WITS ATAU BACI

Dua alternatif yang sering disarankan:

- **WITS (Bank Dunia)** — datanya juga dari Comtrade, tapi API-nya SDMX/XML yang jauh
  lebih merepotkan dan cakupan kuantitasnya lebih tipis.
- **BACI (CEPII)** — sangat bagus (nilai dan kuantitas sudah direkonsiliasi antara
  pelapor dan mitra), tapi perlu registrasi, unduhannya besar, dan karena sudah
  "dibersihkan" CEPII, angkanya tidak persis sama dengan Comtrade — penguji bisa
  menanyakan mengapa berbeda dari sumber resmi.

Untuk tesis level S2 dengan satu tahun data, Comtrade langsung adalah pilihan yang
paling mudah dipertahankan.

---

## SATU HAL LAGI: REPO DI LAPTOP INI TERTINGGAL

Folder `thesisGugli` di laptop rumah masih berhenti di catatan nomor 11. Catatan 12–15
dan berkas `Pd_2012_KBLI5.csv`, `struktur_biaya_2012.csv`, `T7_biaya_input.csv` dibuat
di PC kantor. Sebelum mulai, jalankan:

```
cd "D:\kuliah s2\1. tesis\thesisGugli"
git pull
```

Kalau ternyata PC kantor belum sempat push, berkasnya tetap ada di riwayat percakapan
ini dan bisa saya kirim ulang.
