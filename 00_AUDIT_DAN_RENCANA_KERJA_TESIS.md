# AUDIT DIAGNOSTIK & RENCANA KERJA TESIS

**Judul:** Pengaruh Upah Tenaga Kerja terhadap Kinerja Ekspor Industri Manufaktur di Indonesia
**Mahasiswa:** Satria Dwi Saputra (1306418013) — Magister Ilmu Ekonomi, FEB Universitas Indonesia
**Berkas yang diaudit:** `draftp Proposal tesis rev4b.docx` (492 paragraf, 4 tabel)
**Tanggal audit:** 27 Juli 2026
**Target:** Sidang tesis
**Keputusan desain:** periode data 2007–2012 dipertahankan; literatur dimutakhirkan

---

## RINGKASAN PENILAIAN

Kerangka penelitian Anda **kuat dan layak dipertahankan**. Model penawaran ekspor Riveros (1992)
yang diturunkan dari maksimisasi profit dan Hotelling's Lemma adalah landasan teoretis yang sah,
struktur BAB I–V sudah lengkap, dan data mikro BPS Survei Industri yang Anda pakai adalah aset
yang tidak dimiliki banyak tesis.

Masalahnya bukan pada ide, melainkan pada **eksekusi empiris dan konsistensi internal**.
Dalam kondisi sekarang, draft ini akan gagal di meja sidang bukan karena penguji tidak setuju
dengan argumen Anda, tetapi karena angka di Tabel 4.2 tidak bisa dipertanggungjawabkan secara
aritmetik. Kabar baiknya: karena data mentah dan file Stata masih ada, **semua temuan di bawah
dapat diperbaiki**.

Penilaian kesiapan sidang saat ini: **kira-kira 45%**.

---

## A. TEMUAN KRITIS (harus selesai sebelum sidang)

### A1. Tabel 4.2 tidak konsisten secara aritmetik — ini temuan paling berbahaya

Saya menghitung ulang `t = koefisien / standard error` untuk setiap baris Tabel 4.2.
Tujuh dari sepuluh baris tidak cocok:

| Variabel | Koef. | Std. Err. | t seharusnya | t dilaporkan | Status |
|---|---|---|---|---|---|
| lnPx | 0,196 | 0,0401 | **4,89** | 1,85 | Tidak cocok |
| lnPm | −0,001 | 0,0018 | **−0,56** | 0,70 | Tidak cocok |
| lnWPekerja | 0,174 | 0,0350 | **4,97** | 2,21 | Tidak cocok |
| lnRer | 0,096 | 0,1182 | **0,81** | 2,99 | Tidak cocok |
| lnTotPekerja | −0,491 | 0,1321 | **−3,72** | −0,21 | Tidak cocok |
| lnTotPlain | −0,2550 | 0,1491 | **−1,71** | 0,71 | Tidak cocok |
| lnCapital | 0,0424 | 0,0627 | 0,68 | 0,68 | Cocok |
| Asing | 3,996 | 6,923 | **0,58** | 5,77 | Tidak cocok (kemungkinan SE seharusnya 0,6923) |
| LaborIntensive | −0,1015 | 0,2193 | −0,46 | 0,46 | Cocok (tanda hilang) |
| CapitalIntensive | −1,188 | 0,2401 | −4,95 | −4,95 | Cocok |

**Konsekuensinya serius.** Variabel `lnRer` dan `lnTotPlain` yang Anda klaim signifikan
(p = 0,003 dan p = 0,091) sesungguhnya **tidak signifikan** bila dihitung dari koefisien dan
standard error yang Anda cantumkan sendiri. Sebaliknya `lnTotPekerja` yang Anda tulis "tidak
signifikan (p = 0,833)" justru punya t = −3,72. Sebagian narasi BAB IV berdiri di atas angka
yang keliru.

Tambahan: statistik model tertulis `F(11,107)` dan `R² = 0,4146`. Derajat bebas penyebut 107
mengimplikasikan N ≈ 119 observasi, padahal panel Anda 643 observasi dan output Stata di
lampiran menunjukkan `F(8,634)` serta `R² = 0,5541`. **Tabel 4.2 tidak berasal dari satu pun
regresi yang ada di lampiran.** Kemungkinan besar angkanya disalin manual dari beberapa
output berbeda.

*Tindakan:* jalankan ulang seluruh estimasi, lalu **generate tabel secara otomatis dari output**,
tidak pernah menyalin manual.

### A2. Spesifikasi model berbeda-beda di tiga tempat

| Sumber | Variabel |
|---|---|
| BAB III (persamaan 3.1) | lnPx, lnPm, lnW, lnTotTK, **lnRer**, lnCapital, Asing, DSektor |
| Output Stata (lampiran) | lnPx, lnPm, lnWPekerja, lnTotTK, lnCapital, asing, dummy — **tanpa lnRer** |
| Tabel 4.2 (BAB IV) | ditambah **lnTotPlain** yang tidak pernah didefinisikan di BAB III |

Penguji akan langsung menanyakan: "Model mana yang sebenarnya Anda estimasi?" Ini harus
diseragamkan menjadi satu spesifikasi utama plus beberapa spesifikasi robustness yang
dinyatakan eksplisit.

### A3. Level agregasi ISIC bertentangan

- BAB III baris "i : industry berdasarkan ISIC rev.3 (**4 digit**)"
- Tabel 3.2 "Berdasarkan ISIC Rev. 3 **2 Digit**"
- Variabel panel di Stata bernama `isic3`, dengan **108 grup**

Ketiganya tidak mungkin benar bersamaan. Perlu ditetapkan dan dikonsistenkan di seluruh naskah.

### A4. Hausman menolak RE, tetapi FE membunuh tujuan penelitian kedua

Hausman: χ²(6) = 35,80; Prob > χ² = 0,0000 → **fixed effects yang konsisten**.
Namun pada FE, `laborIntensive` dan `capitalIntensive` **omitted because of collinearity** —
wajar, karena klasifikasi sektor tidak berubah antarwaktu (time-invariant).

Akibatnya **Tujuan Penelitian #2** (membandingkan kinerja ekspor antar klasifikasi sektor)
secara metodologis tidak terjawab oleh model utama Anda. Namun BAB IV bagian 4.2.5 dan BAB V
tetap menarik kesimpulan tentang perbedaan antar sektor. Ini kontradiksi yang pasti dikejar penguji.

**Tiga jalan keluar (saya sarankan gabungan 1 + 2):**
1. **Interaksi sektor × upah** dalam FE — `lnW × laborIntensive`, `lnW × capitalIntensive`.
   Efek utama dummy tetap ter-absorb, tetapi *slope* upah antar sektor dapat diidentifikasi.
   Ini justru pertanyaan yang lebih menarik: "apakah dampak upah terhadap ekspor berbeda
   antar sektor?" — dan sepenuhnya menjawab tujuan #2.
2. **Prosedur Mundlak / Hausman–Taylor** untuk mempertahankan regresor time-invariant
   sekaligus mengendalikan efek individu.
3. Pooled OLS dengan cluster-robust standard error di level industri, disajikan sebagai
   pembanding — bukan sebagai model utama.

### A5. Endogenitas upah tidak ditangani

Upah dan ekspor ditentukan bersama-sama: industri yang ekspornya tumbuh membayar upah lebih
tinggi (*exporter wage premium*), sekaligus upah tinggi memengaruhi daya saing. Koefisien OLS/FE
pada `lnW` karena itu **bias**, dan kemungkinan besar inilah sebab tanda positif yang berlawanan
dengan hipotesis Anda.

2SLS yang ada di lampiran tidak menyelesaikan masalah ini: yang di-instrumen justru `lnPx`,
bukan `lnW`; sampelnya hanya 105 observasi (bukan 643); variabel terikatnya `lnVolume`
(bukan `lnEkspor`); dan `lnGdp` gugur karena kolinearitas sehingga tinggal satu instrumen —
tidak ada uji over-identifikasi yang mungkin dilakukan.

*Rekomendasi instrumen untuk `lnW`:* upah minimum provinsi tertimbang berdasarkan sebaran
geografis tenaga kerja tiap industri (variasi kebijakan yang eksogen terhadap permintaan ekspor
industri tertentu), atau upah tertinggal (lag) dengan pendekatan Arellano–Bond bila panelnya
memadai. Alternatif yang lebih realistis untuk T = 6: sistem GMM ringkas atau, minimal,
**pengakuan eksplisit atas keterbatasan identifikasi** di BAB III dan BAB V — jauh lebih baik
diakui sendiri daripada dibongkar penguji.

### A6. Tidak ada satu pun uji diagnostik

Belum ada: heteroskedastisitas (Modified Wald untuk FE), autokorelasi (Wooldridge),
multikolinearitas (VIF — perhatikan korelasi `lnAsing`–`lnavgWPekerja` = 0,48 dan
`capitalIntensive`–`lnAsing` = 0,49), *cross-sectional dependence* (Pesaran CD), serta
normalitas residual. Untuk tesis magister ekonometrika terapan, ini bagian yang wajib ada.

### A7. Daftar pustaka tidak lengkap dan sebagian rusak

**Dikutip di naskah tetapi tidak ada di daftar pustaka:**
Riveros (1992) — *ini kerangka utama seluruh tesis Anda*; Bernard & Jensen (1997, 1999);
Nicholson (2010); Acemoglu (2002); Narjoko & Hill (2007); Suharyadi (2001).

**Entri yang malformed:** "Khan, M. &." (seharusnya Goldstein & Khan), "Amiti, M. &."
(seharusnya Amiti & Davis).

**Inkonsistensi nama:** teks menulis "Amirti dan Davis", "Surhayadi", "Thorbecker" —
daftar pustaka menulis Amiti, Thorbecke.

Total hanya 13 entri; untuk tesis magister, wajar 35–50 entri.

---

## B. TEMUAN SEDANG

- **B1. Koefisien upah positif belum dijelaskan secara ekonomi.** Saat ini hanya dikutip
  Bernard & Jensen. Perlu mekanisme eksplisit: *exporter wage premium*, *efficiency wage*,
  upah sebagai proksi produktivitas/kualitas tenaga kerja, *skill upgrading*, dan simultanitas.
  Jelaskan juga mengapa spesifikasi log-log dalam level upah **nominal per pekerja** kemungkinan
  menangkap komposisi keterampilan, bukan biaya kompetitif murni — indikator yang tepat untuk
  daya saing biaya sebenarnya **Unit Labour Cost** (upah dibagi produktivitas), sebagaimana
  dipakai Golub & Edwards (2004) yang sudah Anda kutip. Menambahkan spesifikasi ULC akan
  menjadi kontribusi kuat sekaligus menjawab keberatan penguji sebelum diajukan.
- **B2. Narasi BAB IV menyebut dua hasil regresi upah** (tenaga kerja produksi dan non-produksi),
  tetapi Tabel 4.2 hanya memuat satu kolom. Tabel hasil harus disajikan berdampingan.
- **B3. Penomoran gambar rusak.** Teks merujuk "Gambar 1.3", caption tertulis "Gambar 1. 2".
  Tabel 4.1 memuat salah ketik angka: `1.0764.57` (2008, capital intensive).
- **B4. BAB V terlalu tipis** — hanya dua paragraf pendek. Untuk tesis magister diperlukan
  kesimpulan yang menjawab tiap tujuan penelitian satu per satu, implikasi kebijakan yang
  operasional (khususnya terkait kebijakan upah minimum), keterbatasan, dan agenda riset lanjutan.
- **B5. Tinjauan pustaka berhenti di 2011.** Perlu tambahan literatur 2015–2025 mengenai
  daya saing ekspor Indonesia, deindustrialisasi dini, dampak upah minimum di Indonesia,
  dan integrasi rantai nilai global.
- **B6. Justifikasi periode 2007–2012 harus diperkuat**, mengingat jarak waktu. Bingkai secara
  positif: periode pasca-krisis global dengan ketersediaan data mikro industri BPS yang lengkap
  dan konsisten pada ISIC Rev.3 — bukan sekadar "keterbatasan data".

---

## C. TEMUAN RINGAN (redaksional)

Ejaan nama teori tidak konsisten dalam satu dokumen: "Heckser-Ohlin", "Hecksker-Ohlin",
"Hecsker–Ohlin", "Heckshcer-Ohlin" (yang benar: **Heckscher–Ohlin**).
Salah ketik lain: "dirasarkan", "regeresi", "signfikan", "relative" (→ relatif),
"endownment", "kelompokkan" ("mengkelompokkan"), "Instrumented", "peneltian", "Penelitan".
Penomoran subbab tidak konsisten (BAB I–II tanpa nomor, BAB III memakai 3.3/3.4).

---

## D. RENCANA KERJA

### Tahap 0 — Kesiapan alat ✅ SELESAI
Lingkungan analisis sudah siap: `pandas`, `numpy`, `scipy`, `statsmodels`,
`linearmodels` (PanelOLS, RandomEffects, IV2SLS, panel comparison), `pyreadstat`
(pembacaan file `.dta` Stata), `matplotlib`, `python-docx`.
Konteks tesis juga sudah disimpan sebagai skill permanen `tesis-ui-ekonomi`, sehingga
seluruh temuan dan keputusan desain di atas otomatis termuat di sesi-sesi berikutnya.

### Tahap 1 — Rekonstruksi data *(butuh input Anda)*
Silakan letakkan ke folder ini: file `.dta` panel final, seluruh `.do` file, dan bila ada
data mentah BPS/WITS/Kemenperin. Saya akan mereplikasi panel 643 observasi / 108 industri,
memverifikasi konstruksi tiap variabel, dan mengonfirmasi level ISIC yang sesungguhnya.

### Tahap 2 — Re-estimasi menyeluruh
Pooled OLS, FE, RE, uji Hausman, FE dengan interaksi sektor × upah, spesifikasi ULC,
strategi instrumen untuk upah, dan paket lengkap uji diagnostik. Seluruh tabel di-generate
langsung dari output estimasi.

### Tahap 3 — Perbaikan BAB I–III
Penajaman *research gap*, perapian penurunan kerangka Riveros, penyeragaman spesifikasi model,
justifikasi periode data, dan penambahan literatur 2015–2025.

### Tahap 4 — Penulisan ulang BAB IV–V
Berbasis hasil estimasi yang benar, dengan interpretasi ekonomi koefisien upah positif,
analisis robustness, dan kesimpulan serta implikasi kebijakan yang tajam.

### Tahap 5 — Finalisasi & persiapan sidang
Format sesuai Pedoman Penulisan Tugas Akhir UI, daftar pustaka lengkap dan konsisten,
abstrak Indonesia–Inggris, lampiran, lalu simulasi tanya jawab penguji.

---

## E. YANG SAYA BUTUHKAN DARI ANDA SEKARANG

1. **File data:** `.dta` panel final + seluruh `.do` file → letakkan di folder ini.
2. **Kepastian ISIC:** 2, 3, atau 4 digit? (Cek `codebook isic3` di Stata bila ragu.)
3. **Tenggat waktu sidang** — menentukan seberapa ambisius Tahap 2 dapat dijalankan.
4. **Catatan pembimbing** (jika ada) — komentar terakhir dari dosen pembimbing.

Tanpa file data, saya masih bisa mengerjakan Tahap 3, 4 sebagian, dan 5 — tetapi Tabel 4.2
tidak dapat diperbaiki, dan itu adalah masalah nomor satu.
