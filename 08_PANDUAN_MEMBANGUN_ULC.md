# PANDUAN MEMBANGUN VARIABEL UNIT LABOUR COST (ULC)

**Tanggal:** 12 September 2026
**Untuk:** Teknik A pada `07_STRATEGI_SPESIFIKASI_MODEL.md`
**Isi:** apa itu ULC, rumusnya, kode variabel BPS yang persis, dan audit ketersediaan data di Drive Anda

---

# BAGIAN 1 — ULC ITU APA, DALAM BAHASA SEDERHANA

## Masalah dengan variabel upah Anda sekarang

Bayangkan dua industri:

| | Industri A (tekstil) | Industri B (mesin) |
|---|---|---|
| Upah per pekerja per tahun | Rp 20 juta | Rp 60 juta |
| Output per pekerja per tahun | Rp 100 juta | Rp 400 juta |

Kalau Anda hanya melihat **upah**, Industri B tampak tiga kali lebih mahal. Kesimpulannya: B
pasti kalah bersaing.

Tetapi hitung berapa biaya tenaga kerja untuk menghasilkan **satu rupiah output**:

| | Industri A | Industri B |
|---|---|---|
| ULC = upah ÷ output per pekerja | 20 ÷ 100 = **0,20** | 60 ÷ 400 = **0,15** |

**Industri B justru lebih murah.** Ia membayar upah tiga kali lipat, tetapi pekerjanya
menghasilkan empat kali lipat. Untuk setiap rupiah barang yang diekspor, B mengeluarkan
Rp 0,15 untuk tenaga kerja, sementara A mengeluarkan Rp 0,20.

**Itulah inti persoalan tesis Anda.** Upah tinggi bisa berarti dua hal yang berlawanan:

- **mahal** → menekan ekspor
- **produktif** → mendorong ekspor

Variabel `lnavgWPekerja` Anda mencampur keduanya dalam satu angka. Keduanya saling meniadakan,
dan yang keluar adalah koefisien +0,074 dengan p = 0,855 — nol yang tidak berarti apa-apa.

ULC memisahkan keduanya: **produktivitas masuk ke penyebut**, sehingga yang tersisa di
pembilang adalah biaya murni. Itulah ukuran daya saing biaya yang sebenarnya.

## Rumusnya

```
                  Total biaya tenaga kerja
      ULC   =   ─────────────────────────────
                       Nilai tambah
```

Atau, bentuk yang sama tetapi lebih mudah dijelaskan ke penguji:

```
                  Upah per pekerja
      ULC   =   ───────────────────────────
                Produktivitas per pekerja
```

**Cara membacanya:** ULC = 0,20 berarti dari setiap Rp 1 nilai tambah yang dihasilkan industri
itu, Rp 0,20 mengalir ke tenaga kerja.

**ULC turun** bila produktivitas naik lebih cepat daripada upah → daya saing membaik.
**ULC naik** bila upah naik lebih cepat daripada produktivitas → daya saing memburuk.

Karena ULC adalah rasio (tanpa satuan), ia bisa dibandingkan antar industri dan antar negara —
dan itulah sebabnya menjadi standar literatur.

## Kenapa "nilai tambah", bukan "nilai output"?

Nilai output memuat harga bahan baku. Industri yang bahan bakunya mahal akan terlihat sangat
produktif padahal sebagian besar nilainya hanya "lewat" saja.

**Nilai tambah** = nilai output − biaya bahan antara. Inilah nilai yang benar-benar diciptakan
oleh tenaga kerja dan kapital di dalam pabrik itu. Ini juga definisi yang dipakai BPS,
BLS Amerika, OECD, dan IMF — jadi Anda mengikuti standar internasional, bukan mengarang.

---

# BAGIAN 2 — TEMUAN PENTING DARI KUESIONER BPS DI DRIVE ANDA

Saya membaca `VARQues2009.pdf` di folder Drive Anda — kuesioner resmi Survei Tahunan
Perusahaan Industri Pengolahan. Isinya jauh lebih berguna dari dugaan saya.

## BPS sudah menghitung nilai tambah untuk Anda

Di **Bagian VII (Ringkasan)** kuesioner, ada rumus resmi BPS:

```
Nilai Tambah  =  (24) Pendapatan  −  (23) Pengeluaran  +  (23.1) Biaya pekerja
                 +  (25.a) Komponen nilai tambah lainnya
```

Perhatikan bagian **`+ (23.1) Biaya pekerja`**. Biaya tenaga kerja dikurangkan dulu sebagai
pengeluaran, lalu **ditambahkan kembali** — karena upah adalah bagian dari nilai tambah, bukan
biaya antara. Ini persis konsep yang Anda butuhkan.

## Kode variabel yang persis Anda perlukan

Ini yang membuat pekerjaan jadi jauh lebih ringan — nama variabelnya sudah pasti:

### Pembilang: biaya tenaga kerja

| Kode | Isi |
|---|---|
| `ZPZVCU` | **Total pengeluaran pekerja produksi** (upah + insentif) |
| `ZNZVCU` | **Total pengeluaran pekerja lainnya / non-produksi** |
| `ZPSVCU` | Upah/gaji pokok pekerja produksi |
| `ZPXVCU` | Insentif lainnya pekerja produksi |
| `ZNSVCU` / `ZNXVCU` | Idem untuk pekerja non-produksi |

> **Ini langsung memenuhi arahan pertama pembimbing Anda** — memisahkan total pengeluaran
> menjadi upah produksi dan non-produksi. Variabelnya memang sudah terpisah di sumbernya.

### Penyebut: komponen nilai tambah

**Pendapatan (Bagian 24):**

| Kode | Isi |
|---|---|
| `YPRVCU` | Nilai barang yang dihasilkan |
| `YISVCU` | Pendapatan jasa industri (makloon) |
| `YRNVCU` | Pendapatan lainnya |
| `YELVCU` | Listrik yang dijual |
| `SFNVCU`, `STJVCU` | Selisih nilai stok barang setengah jadi dan barang jadi |

**Pengeluaran antara (Bagian 23) — yang dikurangkan:**

| Kode | Isi |
|---|---|
| `RTLVCU` | **Total bahan baku dan penolong** |
| `EFUVCU` | Total bahan bakar dan pelumas |
| `EPLVCU` + `ENPVCU` | Listrik yang dibeli (PLN + non-PLN) |
| `IT1VCU` | Total pengeluaran lainnya |

**Komponen nilai tambah lain yang ditambahkan kembali (25.a):**

| Kode | Isi |
|---|---|
| `ILRVCU` | Sewa tanah |
| `ITXVCU` | Pajak (bukan pajak penghasilan) |
| `IINVCU` | Bunga atas pinjaman |

### Jumlah pekerja

| Kode | Isi |
|---|---|
| `LPRNOU` | Total pekerja produksi |
| `LNPNOU` | Total pekerja non-produksi |
| `LTLNOU` | Total seluruh pekerja |

### Bonus — empat variabel yang belum pernah Anda pakai

| Kode | Isi | Kegunaannya |
|---|---|---|
| `RIMVCU` / `RTLVCU` | **Pangsa bahan baku impor** | Kontrol Amiti & Konings (2007) — dasar teorinya kuat |
| `DPROVI` | **Kode provinsi perusahaan** | **Kunci instrumen upah minimum provinsi** (Teknik B) |
| `DASING` | Persentase kepemilikan asing | Lebih baik daripada dummy 10% yang Anda pakai sekarang |
| Pertanyaan 15.a & 15.b kol (6) | **Status ekspor & persentase diekspor per produk** | Ekspor di level perusahaan, langsung dari BPS |
| `DISIC` | Kode ISIC **5 digit** | Bisa diagregasi ke 4, 3, atau 2 digit sesuai kebutuhan |
| `CTTTCU` | Nilai seluruh barang modal tetap | Variabel `Capital` Anda |

**`DPROVI` adalah temuan terpenting di sini.** Tanpa kode provinsi, instrumen upah minimum
provinsi tidak mungkin dibangun. Dengan `DPROVI`, Anda bisa menghitung persis berapa pangsa
tenaga kerja tiap industri di tiap provinsi — itulah bobot yang dibutuhkan Teknik B.

### Satu catatan teknis yang mudah terlewat

Kuesioner menyatakan: **seluruh nilai dilaporkan dalam ribuan rupiah**. Jangan lupa dikalikan
1.000 saat menghitung nilai absolut. Untuk ULC ini tidak berpengaruh (rasio), tetapi untuk
statistik deskriptif upah per pekerja, ini menentukan apakah angka Anda masuk akal atau
meleset seribu kali lipat.

---

# BAGIAN 3 — LANGKAH-LANGKAH MEMBANGUN ULC

## Langkah 1 — Hitung di level perusahaan

```
biaya_TK      = ZPZVCU + ZNZVCU

output        = YPRVCU + YISVCU + YRNVCU + YELVCU
                + (perubahan stok barang setengah jadi & barang jadi)

biaya_antara  = RTLVCU + EFUVCU + EPLVCU + ENPVCU + IT1VCU

komponen_NT   = ILRVCU + ITXVCU + IINVCU

nilai_tambah  = output − biaya_antara + biaya_TK + komponen_NT
```

## Langkah 2 — Agregasi ke industri ISIC 4 digit

**Jangan merata-ratakan ULC antar perusahaan.** Jumlahkan dulu pembilang dan penyebutnya,
baru dibagi:

```
ULC_industri  =  Σ biaya_TK_perusahaan  ÷  Σ nilai_tambah_perusahaan
```

Ini disebut agregasi **weighted**, dan ini yang benar — perusahaan besar memang seharusnya
lebih menentukan ULC industri daripada perusahaan kecil. Kalau Anda merata-ratakan ULC tiap
perusahaan, satu perusahaan kecil dengan nilai tambah hampir nol bisa menghasilkan ULC
raksasa yang merusak seluruh angka industri.

## Langkah 3 — Bersihkan

Ini bukan opsional. ULC punya penyebut yang bisa mendekati nol atau negatif.

| Masalah | Perlakuan |
|---|---|
| Nilai tambah ≤ 0 | Buang perusahaan tersebut, catat berapa banyak yang dibuang |
| Biaya tenaga kerja = 0 atau kosong | Buang |
| Jumlah pekerja = 0 | Buang |
| ULC ekstrem | Winsorisasi pada persentil 1 dan 99 |

**Laporkan jumlah yang dibuang di setiap tahap** di BAB III. Penguji akan menanyakan asal-usul
N, dan tabel penyaringan menjawabnya sebelum ditanya.

## Langkah 4 — Variabel turunan yang sekalian dihitung

```
produktivitas       = nilai_tambah ÷ LTLNOU              (nilai tambah per pekerja)
upah_prod           = ZPZVCU ÷ LPRNOU                    (upah per pekerja produksi)
upah_nonprod        = ZNZVCU ÷ LNPNOU                    (upah per pekerja non-produksi)
rasio_keterampilan  = upah_nonprod ÷ upah_prod           (proksi intensitas keterampilan)
pangsa_impor        = RIMVCU ÷ RTLVCU                    (kontrol Amiti-Konings)
pangsa_asing        = rata-rata DASING tertimbang
```

`rasio_keterampilan` adalah Teknik D. `pangsa_impor` adalah Teknik F. Sekali jalan, tiga teknik
sekaligus.

## Langkah 5 — Uji kewajaran sebelum dipakai

Jangan langsung meregresi. Periksa dulu:

| Pemeriksaan | Yang diharapkan |
|---|---|
| Sebaran ULC | Sebagian besar antara 0,1 dan 0,6 |
| Sektor capital intensive | ULC **lebih rendah** dari labor intensive |
| Korelasi ULC dengan upah per pekerja | Positif tetapi **jauh di bawah 1** — kalau mendekati 1, produktivitas tidak menambah informasi apa pun dan ULC tidak akan menolong |
| Rata-rata tertimbang seluruh manufaktur | Bandingkan dengan pangsa upah dalam PDB sektor industri (BPS) |

Pemeriksaan ketiga adalah **uji nyala** untuk seluruh strategi ini. Kalau ULC dan upah
berkorelasi 0,95, berarti variasi produktivitas antar industri terlalu kecil untuk membedakan
keduanya, dan Teknik A tidak akan mengubah hasil. Lebih baik tahu itu di awal.

---

# BAGIAN 4 — AUDIT DATA: APA YANG ADA DI DRIVE ANDA

Saya telusuri seluruh Drive untuk setiap bahan yang dibutuhkan.

## ✅ Yang tersedia

| Bahan | Berkas di Drive | Tahun |
|---|---|---|
| **Survei Industri mentah** | `indus90`–`indus04` (.accdb/.sd2), `indus05.accdb`, `indus06.xlsx`, `indus07.dta` + `.xlsx`, `indus08.xlsx`, `indus09.xlsx`, `indus10.xlsx`, `industri_2011.sas7bdat` | **1990–2011** |
| **Kamus variabel** | `VARQues2006.doc`, `VarQues2007.doc`, `VARQues2009.pdf` | 2006, 2007, 2009 |
| **Layout data lama** | `LAY8587.TXT`, `LAY9095.TXT` | 1985–1995 |
| Konkordansi HS↔SITC↔ISIC | folder `table hs code dan sitc`, `correspondencetable.do` | — |
| Klasifikasi industri | `KBLI2005.xlsx`, `KLUI1990.xlsx`, `KLUI1997.xlsx` | — |
| Sakernas | `sakernas.zip` (4 MB), `Kode Wilayah Sakernas.xlsx` | tahun perlu dicek |
| PDRB kabupaten/kota | 5 buku PDF | 2009–2012 |
| Alat konversi | `StatTransfer9` | — |

## ❌ Yang tidak ada

| Bahan | Status | Akibatnya |
|---|---|---|
| **Survei Industri 2012** | **Tidak ada di Drive** | **ULC untuk tahun 2012 tidak bisa dibangun** |
| Upah minimum provinsi | Tidak ada | Instrumen Teknik B belum bisa dibangun |
| Panel olahan Anda (`.dta`) | Tidak ada | — |
| Do-file tesis Anda | Tidak ada | — |

## Inilah persoalannya

> **Draft 4c Anda memakai data tahun 2012. Data mentah Survei Industri di Drive berhenti di
> 2011.**

Berkas terbaru adalah `industri_2011.sas7bdat` (21 MB, dimodifikasi Juli 2013). Tidak ada
`indus12` maupun `industri_2012` di mana pun di Drive Anda.

Artinya, dengan bahan yang ada sekarang, **ULC untuk 2012 tidak dapat dihitung.**

Tetapi ada sisi lain yang jauh lebih cerah.

---

# BAGIAN 5 — TEMUAN YANG MENGUBAH GAMBARAN

Perhatikan daftar berkas ini:

| Tahun | Berkas | Format |
|---|---|---|
| 2006 | `indus06.xlsx` | Excel, 27 MB |
| 2007 | `indus07.dta` + `indus07.xlsx` | Stata + Excel |
| 2008 | `indus08.xlsx` | Excel, 11 MB |
| 2009 | `indus09.xlsx` | Excel, 11 MB |
| 2010 | `indus10.xlsx` | Excel, 11 MB |
| 2011 | `industri_2011.sas7bdat` | SAS, 21 MB |

**Ini enam tahun data mentah Survei Industri di level perusahaan, berurutan, 2006–2011.**

Anda mengira kehilangan data. Yang hilang sebenarnya hanya **hasil olahan** Anda. **Bahan
bakunya masih lengkap** — dan bahan baku justru lebih berharga, karena dari situ Anda bisa
membangun apa saja, termasuk variabel-variabel yang dulu tidak Anda punya.

Dari keenam berkas ini Anda dapat membangun:

- ✅ Panel enam tahun (2006–2011) — **N sekitar 600, bukan 100**
- ✅ **ULC** untuk setiap industri setiap tahun
- ✅ Upah produksi dan non-produksi terpisah — arahan pembimbing
- ✅ Rasio keterampilan
- ✅ Pangsa bahan baku impor — kontrol Amiti & Konings
- ✅ **Kode provinsi** — pintu masuk instrumen upah minimum
- ✅ Status ekspor di level perusahaan
- ✅ Kepemilikan asing sebagai persentase, bukan dummy

Dengan kata lain: **hampir seluruh strategi di dokumen 07 bisa dijalankan** dari berkas yang
sudah ada di Drive Anda hari ini.

---

# BAGIAN 6 — TIGA PILIHAN, DAN YANG SAYA SARANKAN

## Pilihan A — Minta ulang data Survei Industri 2012 ke BPS

Pertahankan desain 4c apa adanya, tambahkan ULC.

**Untung:** naskah 4c tidak berubah strukturnya; pekerjaan paling sedikit.
**Rugi:** bergantung pada proses permintaan data ke BPS yang waktunya tidak Anda kendalikan.
N tetap sekitar 100, sehingga masalah daya uji statistik tidak terselesaikan.

## Pilihan B — Geser tahun penelitian ke 2011

Pertahankan desain cross-section, ganti 2012 → 2011 (`industri_2011.sas7bdat`).

**Untung:** bisa dikerjakan hari ini juga; struktur naskah 4c tetap.
**Rugi:** seluruh angka di BAB IV harus dihitung ulang, dan justifikasi "2012 adalah publikasi
terakhir BPS" di BAB III harus ditulis ulang. N tetap kecil.

## Pilihan C — Bangun panel 2007–2011 ⭐ **yang saya sarankan**

Rekonstruksi dari berkas mentah, lima tahun, dengan seluruh variabel baru.

**Untung — dan ini banyak:**

- **N naik sekitar lima kali lipat** → standard error mengecil → Teknik C langsung terpenuhi
- ULC, rasio keterampilan, pangsa impor, provinsi — semuanya sekaligus
- Membuka Teknik B (instrumen upah minimum), yang mustahil pada data satu tahun
- Mengembalikan justifikasi periode pasca-krisis global yang sudah ada di naskah lama Anda
- **Datanya sudah ada di tangan Anda sekarang** — tidak menunggu siapa pun

**Rugi:** pekerjaan rekonstruksi data paling berat dari ketiganya, dan BAB III–IV harus ditulis
ulang cukup banyak.

**Kenapa saya tetap menyarankannya:** pekerjaan berat itu **sekali jalan menyelesaikan hampir
seluruh temuan kritis** dari review saya — N yang tidak jelas, statistik deskriptif yang
kurang, daya uji rendah, endogenitas, dan arahan pembimbing tentang pemisahan upah. Pilihan A
dan B hanya menambahkan satu variabel dan meninggalkan sisanya.

Dan kalau nanti data 2012 datang dari BPS, ia tinggal ditambahkan sebagai tahun keenam —
tidak ada pekerjaan yang terbuang.

---

# BAGIAN 7 — YANG PERLU ANDA LAKUKAN

## Kalau memilih Pilihan C

**1. Unduh enam berkas ini dari Drive ke folder tesis** (total sekitar 90 MB):

- `indus06.xlsx` · `indus07.xlsx` · `indus08.xlsx` · `indus09.xlsx` · `indus10.xlsx`
- `industri_2011.sas7bdat`

Semuanya ada di folder `data` → subfolder `excel complete` dan folder induknya.

**2. Cari upah minimum provinsi 2006–2011.** Ini data publik, tersedia di situs BPS
(Upah Minimum Provinsi menurut Provinsi) atau publikasi Kemenaker. Formatnya cukup satu tabel
kecil: 33 provinsi × 6 tahun. Kalau tidak ketemu, saya bisa carikan.

**3. Cek `sakernas.zip`** — beri tahu saya tahun berapa isinya. Kalau memuat 2006–2011, ia bisa
dipakai untuk proksi pendidikan dan keterampilan tenaga kerja, memperkuat penyebut ULC.

## Yang saya kerjakan setelah berkas masuk

| # | Pekerjaan |
|---|---|
| 1 | Skrip pembaca `.xlsx` dan `.sas7bdat`, verifikasi nama variabel terhadap `VARQues` |
| 2 | Hitung nilai tambah, ULC, dan seluruh variabel turunan di level perusahaan |
| 3 | Agregasi ke ISIC 4 digit, gabungkan enam tahun menjadi panel |
| 4 | Pembersihan dan tabel penyaringan sampel yang bisa dilaporkan |
| 5 | Statistik deskriptif lengkap — permintaan pembimbing yang belum tergarap |
| 6 | Gabungkan dengan data ekspor Comtrade yang sudah Anda punya |
| 7 | Bangun instrumen upah minimum provinsi tertimbang |
| 8 | Jalankan enam spesifikasi, generate seluruh tabel otomatis |

**Catatan teknis:** `pandas` membaca `.xlsx` dan `.sas7bdat` secara native, jadi tidak perlu
Stata maupun StatTransfer untuk tahap ini.

---

# RINGKASAN SATU HALAMAN

**ULC = biaya tenaga kerja ÷ nilai tambah.** Ia memisahkan "mahal" dari "produktif" — dua hal
yang tercampur dan saling meniadakan di variabel upah Anda sekarang, dan itulah sebab paling
mungkin koefisien Anda nol.

**Kabar baik:** kuesioner BPS di Drive Anda memberi kode variabel yang persis, dan BPS sudah
menyediakan rumus nilai tambah resminya. Tidak ada yang perlu dikarang.

**Kabar kurang baik:** data Survei Industri 2012 — tahun yang dipakai draft 4c — tidak ada di
Drive.

**Kabar baik yang lebih besar:** ada enam tahun data mentah level perusahaan, 2006–2011. Yang
hilang hanya hasil olahan Anda, bukan bahan bakunya. Dari situ Anda bisa membangun panel yang
**lebih baik daripada yang dulu Anda punya** — dengan ULC, upah terpisah, pangsa impor, dan
kode provinsi yang membuka jalan ke instrumen upah minimum.

**Keputusan yang perlu Anda ambil:** minta data 2012 ke BPS (A), geser ke 2011 (B), atau bangun
panel 2007–2011 (C). Saya menyarankan C — pekerjaannya paling berat, tetapi sekali jalan
menyelesaikan hampir seluruh masalah yang tersisa di tesis ini, dan datanya sudah ada di tangan
Anda hari ini.
