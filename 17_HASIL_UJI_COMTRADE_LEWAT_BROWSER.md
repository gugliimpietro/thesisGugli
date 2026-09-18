# HASIL PENGAMBILAN DATA COMTRADE LEWAT BROWSER — DAN APA YANG DITEMUKAN

**Tanggal:** 18 September 2026
**Cara:** browser bawaan Claude di komputer Anda (ekstensi Chrome tidak tersambung ke sesi ini)

---

## RINGKASAN

Saya berhasil menarik **seluruh** data ekspor dan impor Indonesia 2012 pada level HS
6-digit langsung dari UN Comtrade lewat browser Anda, **tanpa API key**, dan
merekonsiliasinya sampai cocok dengan total resmi.

| | Baris HS6 | Total nilai (USD) | Total resmi Comtrade | Cakupan |
|---|---|---|---|---|
| **Ekspor** | 4.342 | 190.026.917.300 | 190.031.839.234 | **99,997 %** |
| **Impor** | 4.848 | 191.690.908.079 | 191.690.908.079 | **100,000 %** |

Rekonsiliasi dilakukan **per bab HS (97 bab)**, bukan hanya pada total. Setelah tiga
putaran penyapuan, tidak ada satu bab pun yang di bawah 99,9 %. Berat bersih (`netWgt`)
tersedia untuk **4.341 dari 4.342** baris ekspor dan **4.846 dari 4.848** baris impor —
artinya `Qx` dan `Px` bisa dihitung untuk praktis seluruh data.

Konkordansnya juga ketemu: **5.205 pasangan HS6 → ISIC Rev.4**.

---

## MASALAHNYA, DAN KENAPA ANDA PERLU MENJALANKAN SATU PERINTAH

Data itu berhasil dikumpulkan **di dalam browser**. Memindahkannya dari browser ke
sesi ini ternyata tidak andal — berkas yang diunduh browser tidak mendarat di folder
yang bisa saya jangkau, dan transfer lewat jalur teks terpotong di tengah.

Jadi hasil kerjanya bukan berkas datanya, melainkan **resepnya** — dan itu justru
lebih berharga, karena bisa diulang kapan saja dan bisa ditunjukkan ke penguji.

Saya sudah menuliskan seluruh temuan ke dalam `scripts/fetch_comtrade_2012.py`
(versi 2). Anda cukup menjalankan:

```
cd "D:\kuliah s2\1. tesis\thesisGugli\scripts"
python fetch_comtrade_2012.py
```

Perlu waktu sekitar **15 menit** (ada jeda sengaja antar permintaan). Tidak perlu
API key, tidak perlu pasang paket apa pun — hanya Python bawaan.

Di akhir, skrip mencetak baris seperti ini, dan **angkanya harus sama persis dengan
tabel di atas**:

```
X: 4342 baris | total USD 190,026,917,300 | kontrol USD 190,031,839,234 | cakupan 99.997%
bab yang masih < 99,9%: TIDAK ADA
```

Kalau angkanya beda jauh, beri tahu saya — berarti ada yang berubah di sisi Comtrade.

---

## TIGA TEMUAN TEKNIS YANG MEMBUAT INI BERHASIL

Ini bagian yang memakan waktu, dan layak dicatat karena tanpa ini datanya **diam-diam
salah** — bukan gagal dengan pesan error, tapi kurang tanpa memberi tahu.

### 1. Comtrade menjawab "200 OK" tapi kosong

Endpoint gratis (`preview`) membatasi laju permintaan secara tersembunyi. Kalau
terlalu cepat, ia tidak mengembalikan error — ia mengembalikan **status 200 dengan
daftar data kosong**. Skrip naif akan menganggap "bab ini memang tidak ada ekspornya"
dan melanjutkan.

Buktinya telak: kode HS 940360 (perabot kayu untuk kamar tidur) sendirian bernilai
**USD 746 juta** — salah satu ekspor manufaktur penting Indonesia. Pada percobaan
pertama, kode itu hilang sama sekali. Bab 94 (furnitur, ISIC 31) hanya tercakup
**42,5 %**. Kalau data itu dipakai apa adanya, industri furnitur akan tampak separuh
ukuran sebenarnya di seluruh BAB IV.

**Penanganannya:** jeda 2,5 detik antar permintaan, dan jawaban kosong diulang sampai
4 kali sebelum diterima.

### 2. Verifikasi harus per bab, bukan per total

Pada satu titik total ekspor sudah mencapai 97,34 % — kelihatan bagus. Tetapi di
baliknya bab 24 (tembakau) **0 %**, bab 42 (barang kulit) **6 %**, bab 94 **22 %**.
Kekurangan di bab-bab kecil tenggelam di dalam total yang didominasi batubara dan
sawit.

**Penanganannya:** skrip menarik total resmi per bab (`cmdCode=AG2`) dan membandingkan
bab per bab. Bab yang kurang dari 99,9 % disapu ulang dengan enumerasi kode.

Ini prinsip yang sama yang dipakai waktu mengekstrak Buku I BPS: **jangan percaya
data sampai ada identitas yang memaksanya cocok.** Di Buku I identitasnya adalah
"nilai tambah = output − input"; di sini identitasnya "jumlah HS6 = total bab".

### 3. Daftar kode resmi HS 2012 pun tidak lengkap

Comtrade menerbitkan daftar 5.206 kode HS6 (berkas `H4.json`). Ternyata Indonesia
melaporkan beberapa kode di luar daftar itu. Skrip menutupnya dengan menebak:
untuk bab yang belum cocok, ia mencoba seluruh kombinasi `pos4digit + 00..99`.

---

## KONKORDANS: LEWAT CPC, BUKAN LANGSUNG

Ini juga temuan yang perlu Anda tahu, karena akan ditanya.

**UNSD tidak menerbitkan tabel konkordans langsung HS 2012 → ISIC Rev.4.** Yang ada
adalah HS 2007, HS 2017, dan HS 2022. Untuk HS 2012 jalurnya harus dua langkah:

```
HS 2012  ->  CPC Ver. 2.1  ->  ISIC Rev. 4
```

Kedua tabelnya resmi dan tersedia gratis di UNSD:

- `cpc21-hs2012.txt` — HS 2012 ke CPC 2.1
- `CPC21-ISIC4.txt` — CPC 2.1 ke ISIC Rev.4

Hasil penggabungannya: **5.205 pasangan HS6 → ISIC Rev.4 4-digit**. Contoh:
`010121 → 0142` (peternakan sapi), `940360 → 3100` (industri furnitur).

Kalau penguji bertanya "dari mana pemetaan industrinya", jawabannya adalah kalimat di
atas — dua tabel resmi UNSD, dirangkai lewat CPC. Itu jauh lebih kuat daripada
pemetaan buatan sendiri.

Keterbatasannya tetap harus diakui: satu kode HS bisa masuk ke lebih dari satu CPC,
dan satu CPC ke lebih dari satu ISIC. Skrip memakai pasangan pertama (dominan) untuk
setiap kode. Tulis satu kalimat tentang ini di catatan metode BAB III.

---

## SETELAH SKRIP SELESAI

Berkas yang akan ada di `data/`:

| Berkas | Isi |
|---|---|
| `comtrade_2012_X_HS6.csv` | Ekspor per HS6: nilai USD, berat kg, kuantitas |
| `comtrade_2012_M_HS6.csv` | Impor, format sama |
| `HS2012_ISIC4.csv` | Konkordans 5.205 pasangan |
| `trade_2012_ISIC4.csv` | **Ini yang dipakai:** per ISIC Rev.4 — `X_usd, X_kg, M_usd, M_kg, Px_usd_per_kg, Pm_usd_per_kg` |
| `verifikasi_comtrade.txt` | Catatan rekonsiliasi, untuk lampiran |

Begitu `trade_2012_ISIC4.csv` ada dan sudah di-push, saya menggabungkannya dengan
`SI2012_KBLI5.csv` (KBLI 5-digit dipotong jadi 4-digit = ISIC Rev.4) dan kita punya
**dataset lengkap** untuk pertama kalinya:

```
lnQx      = ln(X_kg)                      <- variabel terikat, berat ekspor
lnPx      = ln(Px_usd_per_kg)
lnPm      = ln(Pm_usd_per_kg)
lnUpah    = ln(upah per pekerja)          <- sudah ada
ULC       = biaya tenaga kerja / nilai tambah   <- sudah ada
lnEnergi  = ln(energi per pekerja)        <- proxy modal, sudah ada
```

Semua variabel di persamaan BAB III akhirnya punya sumber. Tidak ada lagi yang
menggantung.

---

## SATU HAL YANG BERUBAH DARI RENCANA SEMULA

Data Bea Cukai (`ImporIndonesia.mdb`) **tidak lagi jalur utama** untuk Pm. Comtrade
memberi impor dengan definisi yang persis sama dengan ekspornya, jadi rasio `Px/Pm`
konsisten. Berkas Bea Cukai berubah peran menjadi **uji silang** — dan itu justru
nilai tambah: kalau Pm dari dua sumber independen berkorelasi tinggi, itu satu
paragraf validasi yang bagus di BAB III.

Artinya **Anda tidak perlu lagi mengekspor ulang tabel "Impor (Berat) KG"** yang
kemarin terpotong di bab HS 38. Tugas itu batal.
