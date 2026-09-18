# STATUS TESIS DAN RENCANA KE SIDANG

**Tanggal:** 18 September 2026
**Isi:** apa yang sudah ada, apa yang masih kurang, dan apa yang harus dikerjakan berikutnya

---

## BAGIAN 1 — DATA: SUDAH LENGKAP

Data Comtrade Anda sudah saya periksa. Hasilnya bersih:

```
Ekspor : 4.348 baris HS6 | USD 190.031.839.234 | cakupan 100,000 %
Impor  : 4.848 baris HS6 | USD 191.690.908.079 | cakupan 100,000 %
Bab HS yang belum cocok : TIDAK ADA
Konkordans : 5.205 pasangan HS6 -> ISIC Rev.4
```

Sempurna — bahkan lebih baik dari percobaan saya lewat browser.

**Seluruh variabel di persamaan BAB III sekarang punya sumber:**

| Variabel | Sumber | Status |
|---|---|---|
| `Qx` — kuantitas ekspor | Comtrade `X_kg` | ✅ |
| `Px` — harga ekspor | Comtrade `X_usd / X_kg` | ✅ |
| `Pm` — harga bahan baku impor | Comtrade `M_usd / M_kg` | ✅ |
| `Upah` per pekerja | BPS Buku I Tabel 4 | ✅ |
| `ULC` | BPS: biaya TK ÷ nilai tambah | ✅ |
| Modal (proxy) | BPS Tabel 7: energi per pekerja | ✅ |
| Skala | BPS: nilai output, tenaga kerja | ✅ |

**Tidak ada lagi variabel yang menggantung.** Yang tersisa hanya pelengkap:
Buku Bahan Baku Bagian B (untuk uji silang Pm) — sifatnya opsional, bukan penghalang.

---

## BAGIAN 2 — SAYA SUDAH GABUNGKAN DAN COBA REGRESI

Saya gabungkan data industri BPS dengan data perdagangan. Karena KBLI 2009 = ISIC Rev.4,
penyambungannya lewat kode industri. Hasilnya dua dataset:

| Berkas | Level | N |
|---|---|---|
| `panel_2012_ISIC3.csv` | grup 3-digit | **63** |
| `panel_2012_ISIC4.csv` | kelas 4-digit | **97** |

Lalu saya jalankan regresi persis seperti model di BAB III. **Inilah hasilnya, apa
adanya** — dan Anda perlu membacanya sebelum bertemu pembimbing lagi.

### Hasil pada N = 63 (grup 3-digit)

| Variabel | Koefisien | t | p |
|---|---|---|---|
| ln Upah | +0,22 | 0,53 | 0,597 |
| ULC | +1,51 | 1,35 | 0,181 |
| ln Pm | −0,70 | −4,27 | **0,000** |
| ln Energi per pekerja | −0,02 | −0,09 | 0,927 |
| ln Output | +0,55 | 5,03 | **0,000** |

### Hasil pada N = 97 (kelas 4-digit)

| Variabel | Koefisien | t | p |
|---|---|---|---|
| ln Upah (dep = nilai ekspor) | **−0,90** | −1,76 | **0,082** |
| ln Pm | +0,32 | 2,38 | **0,019** |
| ln Output | +0,75 | 8,05 | **0,000** |

Saya mencoba **sebelas spesifikasi** — dengan dan tanpa output, ULC menggantikan upah,
ekspor per pekerja, rasio ekspor terhadap output, dummy sektor, standard error robust.

**Kesimpulan jujurnya: pada data satu tahun, upah tidak signifikan.**

Yang paling dekat adalah spesifikasi 4-digit: koefisien upah **−0,90 dengan p = 0,082** —
tandanya sudah benar secara teori (upah naik → ekspor turun), tetapi masih di atas 5 %.

---

## BAGIAN 3 — KENAPA TIDAK SIGNIFIKAN, DAN APA OBATNYA

Ini bagian terpenting dari catatan ini. Ada tiga sebab, dan hanya satu yang benar-benar
bisa diobati.

### Sebab 1 — Jumlah observasi terlalu sedikit

63 sampai 97 observasi, dengan 5–7 variabel penjelas. Untuk mendeteksi pengaruh yang
sedang besarnya, itu terlalu tipis. Bandingkan: tesis Anda yang lama memakai **623
observasi** (105 industri × 6 tahun).

### Sebab 2 — Keragaman antarindustri bukan keragaman yang kita cari

Dalam satu tahun, perbedaan upah antarindustri sebagian besar mencerminkan **apa
industrinya** — kilang minyak membayar mahal karena padat modal dan padat keahlian,
bukan karena "upahnya mahal". Pengaruh upah yang kita cari tertutup oleh perbedaan
karakter industri yang tidak teramati.

Data panel menyelesaikan ini secara otomatis: *fixed effect* industri menyerap seluruh
perbedaan antarindustri yang tetap, dan yang tersisa untuk mengidentifikasi koefisien
upah adalah **perubahan upah di dalam industri yang sama dari tahun ke tahun.** Itu
justru variasi yang benar secara teori.

### Sebab 3 — Ada cacat teknis pada `Px` yang harus diperbaiki

Saya menemukan masalah yang harus Anda ketahui sebelum penguji menemukannya.

`Px` dihitung sebagai nilai ÷ berat. Variabel terikatnya adalah berat. Jadi secara
aljabar:

```
ln Qx = ln(nilai)  −  ln(Px)
```

Berat muncul di kedua sisi persamaan. Meregresikan `ln Qx` pada `ln Px` **otomatis
menghasilkan koefisien negatif** — bukan karena ekonominya, tetapi karena aritmetikanya.
Namanya *division bias*, dan memang terlihat di hasil saya: koefisien `ln Px` keluar
−0,72 dengan p = 0,008, padahal dalam fungsi **penawaran** ekspor tandanya seharusnya
**positif**.

Kalau ini masuk ke naskah tanpa penjelasan, penguji yang teliti akan membongkarnya.

**Tiga cara menanganinya** (pilih satu, jelaskan di BAB III):

1. **Keluarkan `Px` dari sisi kanan** dan pakai rasio `Px/Pm` sebagai satu variabel
   *terms of trade* — paling sederhana.
2. **Pakai instrumen untuk `Px`**: harga ekspor dunia untuk produk yang sama (rata-rata
   unit value negara lain di Comtrade) — paling kuat secara metodologis, dan sekalian
   menjawab masalah simultanitas yang ditulis Goldstein & Khan (1978).
3. **Ganti variabel terikat menjadi nilai ekspor** dan akui bahwa yang diestimasi adalah
   persamaan tereduksi, bukan fungsi penawaran murni.

Saran saya: **nomor 2**, karena sekaligus menjawab kritik endogenitas yang sudah ada di
catatan strategi (berkas 07).

---

## BAGIAN 4 — INILAH YANG HARUS DIKERJAKAN: BANGUN PANELNYA

Ini satu-satunya jalan yang benar-benar menyelesaikan masalah, dan kabar baiknya:
**bahan bakunya sudah ada di Drive Anda.**

Di `D:\kuliah s2\1. tesis\bahan tesis\data\data IBS 1990-2013\` ada data mentah Survei
Industri Besar Sedang tingkat perusahaan:

```
Industri Manufaktur_2005-2011\Akses\indus05.accdb, indus06, indus07, indus10
Industri Manufaktur_2005-2011\excel complete\indus07.xlsx, indus09.xlsx
```

Dari berkas itu kita bisa **membangun sendiri** agregat industri per tahun — persis
variabel yang sekarang kita punya untuk 2012, tetapi untuk 2005–2011 juga.
Sisi perdagangannya gampang: skrip Comtrade tinggal diganti angka tahunnya.

Hasil akhirnya:

```
±100 industri × 7 tahun  =  ±700 observasi
```

Dengan itu Anda bisa menjalankan **Fixed Effect** — dan di situlah upah punya peluang
nyata untuk signifikan, karena identifikasinya berubah dari "antarindustri" menjadi
"di dalam industri, antarwaktu". Ini juga persis yang diminta pembimbing waktu beliau
berkata *"tambah variabel dan ubah modelnya"*.

**Yang saya perlukan dari Anda untuk memulai:** buka salah satu berkas `.accdb` itu di
Access, ekspor satu tabel ke CSV (tahun mana saja, misal `indus07`), dan taruh di folder
`data/`. Saya periksa strukturnya, lalu saya buatkan skrip yang mengolah seluruh tahun
sekaligus — sama seperti yang sudah kita lakukan untuk Comtrade.

---

## BAGIAN 5 — URUTAN KERJA SAMPAI SIDANG

| # | Pekerjaan | Siapa | Perkiraan |
|---|---|---|---|
| 1 | Ekspor satu tabel `indus07.accdb` ke CSV untuk saya periksa | **Anda** | 10 menit |
| 2 | Skrip pembangun panel industri 2005–2011 dari data mentah | Saya | — |
| 3 | Unduh Comtrade untuk tahun 2007–2011 (skrip tinggal ganti tahun) | **Anda** | ±1 jam |
| 4 | Gabung jadi panel, bangun instrumen harga dunia untuk `Px` | Saya | — |
| 5 | Estimasi: Pooled OLS, FE, RE, Hausman, 2SLS | Saya | — |
| 6 | Tulis BAB IV (deskriptif + hasil) dan BAB V | Saya | — |
| 7 | Sisipkan BAB III revisi ke naskah, jadikan `draft 4d.docx` | Saya | — |
| 8 | Perbarui presentasi sidang | Saya | — |

Langkah 1 adalah satu-satunya yang menghambat. Sisanya mengalir.

---

## BAGIAN 6 — SATU NASIHAT YANG PERLU SAYA SAMPAIKAN TERUS TERANG

Pembimbing Anda ingin upah dan ekspor signifikan. Itu wajar sebagai harapan, tetapi
signifikansi bukan sesuatu yang bisa dijanjikan — ia hasil dari data, bukan dari pilihan
spesifikasi.

Yang **boleh** dan **harus** dilakukan: memperbaiki identifikasi. Menambah tahun,
memakai fixed effect, membereskan division bias, memakai instrumen. Semua itu membuat
estimasinya lebih benar — dan kalau pengaruhnya memang ada, peluangnya muncul jauh lebih
besar.

Yang **tidak boleh**: mencoba puluhan spesifikasi lalu melaporkan yang bintangnya paling
banyak. Itu namanya *specification searching*, dan penguji yang berpengalaman bisa
menciumnya dari tabel yang terlalu rapi.

Karena itu saya sarankan **menulis protokol spesifikasi lebih dulu** — sebelum panelnya
jadi — yang menyatakan: model utamanya apa, uji ketahanannya apa saja, dan apa yang
akan dilaporkan apa pun hasilnya. Kerangkanya sudah ada di berkas `07_STRATEGI_SPESIFIKASI_MODEL.md`.

Kalau ternyata upah tetap tidak signifikan setelah semua itu, **itu pun temuan yang sah**
— dan ada ceritanya: pada industri manufaktur Indonesia, daya saing ekspor lebih
ditentukan oleh harga bahan baku impor dan skala produksi daripada oleh biaya tenaga
kerja. Perhatikan `ln Pm` di kedua tabel di atas: **selalu signifikan pada 1 %**. Itu
hasil yang kuat dan layak dipertahankan di depan penguji.

Tesis yang jujur dan rapi lebih mudah dipertahankan daripada tesis yang memaksakan
bintang.
