# ULC 2012, KLASIFIKASI SEKTOR, DAN STATISTIK DESKRIPTIF

**Tanggal:** 13 September 2026
**Sumber:** `data/SI2012_KBLI5.csv` (hasil ekstraksi publikasi BPS 2012, 398 KBLI 5 digit)
**Berkas baru:** `data/tabel_sektor.csv`, `data/tabel_divisi.csv`

---

## 1. TEMUAN UTAMA — INILAH BUKTI YANG MEMBENARKAN SELURUH STRATEGI ULC

Satu tabel ini, menurut saya, adalah tabel terpenting yang akan masuk BAB IV Anda.

| Sektor | KBLI | Perusahaan | Tenaga kerja | Nilai tambah (T Rp) | **Upah/pekerja produksi** | **ULC** | Produktivitas/pekerja |
|---|---:|---:|---:|---:|---:|---:|---:|
| Resource Intensive | 123 | 9.088 | 1.738.858 | 439,3 | Rp 28,6 jt | **0,114** | Rp 252,7 jt |
| Labor Intensive | 127 | 10.044 | 2.212.732 | 302,2 | Rp 23,7 jt | **0,190** | Rp 136,6 jt |
| Capital Intensive | 137 | 4.375 | 929.575 | 401,6 | **Rp 44,0 jt** | **0,105** | Rp 432,1 jt |
| **Total** | **387** | **23.507** | **4.881.165** | **1.143,2** | **Rp 29,1 jt** | **0,130** | **Rp 234,2 jt** |

**Perhatikan dua kolom yang saya tebalkan.**

Sektor *capital intensive* membayar upah **hampir dua kali lipat** sektor *labor intensive*
(Rp 44,0 juta versus Rp 23,7 juta per pekerja produksi per tahun). Bila diukur dengan tingkat
upah, sektor ini tampak paling mahal dan paling tidak kompetitif.

Tetapi unit labour cost-nya justru **paling rendah dari ketiganya** — 0,105 versus 0,190.
Sebabnya ada di kolom terakhir: produktivitasnya lebih dari tiga kali lipat (Rp 432,1 juta
versus Rp 136,6 juta per pekerja).

> **Tingkat upah dan daya saing biaya bergerak ke arah yang berlawanan antar sektor.**
>
> Sektor yang upahnya tertinggi justru yang biaya tenaga kerja per unit outputnya terendah.

Inilah penjelasan empiris mengapa koefisien `lnavgWPekerja` di Tabel 4.2 Anda bernilai +0,074
dengan p = 0,855. Variabel upah per pekerja mencampur dua sinyal yang saling meniadakan, dan
regresi tidak punya cara untuk memisahkannya. Bukan karena efeknya tidak ada — karena alat
ukurnya salah.

Anda sekarang punya bukti angkanya, dari data resmi BPS, bukan sekadar argumen teoretis.

---

## 2. BUKTI YANG SAMA DI TINGKAT DIVISI — LEBIH TAJAM LAGI

**Lima divisi dengan ULC tertinggi:**

| Divisi | Nama | ULC | Upah/pekerja produksi |
|---|---|---:|---:|
| 31 | Furnitur | **0,599** | Rp 24,6 jt |
| 32 | Pengolahan lainnya | 0,403 | Rp 21,2 jt |
| 14 | Pakaian jadi | 0,276 | **Rp 18,5 jt** |
| 16 | Kayu dan barang dari kayu | 0,263 | Rp 22,1 jt |
| 15 | Kulit, barang kulit dan alas kaki | 0,259 | Rp 25,8 jt |

**Lima divisi dengan ULC terendah:**

| Divisi | Nama | ULC | Upah/pekerja produksi |
|---|---|---:|---:|
| 30 | Alat angkutan lainnya | **0,040** | Rp 27,7 jt |
| 29 | Kendaraan bermotor | 0,052 | **Rp 53,5 jt** |
| 17 | Kertas dan barang dari kertas | 0,073 | Rp 29,9 jt |
| 20 | Bahan kimia dan barang kimia | 0,074 | Rp 49,1 jt |
| 12 | Pengolahan tembakau | 0,076 | Rp 19,5 jt |

Bandingkan dua baris ini:

| | Upah/pekerja | ULC |
|---|---|---|
| **Pakaian jadi** | Rp 18,5 juta — **terendah** | 0,276 — ketiga **tertinggi** |
| **Kendaraan bermotor** | Rp 53,5 juta — **tertinggi** | 0,052 — kedua **terendah** |

Industri dengan upah tertinggi punya biaya tenaga kerja per unit output **lima kali lebih
rendah** daripada industri dengan upah terendah. Kalau ada satu perbandingan yang bisa Anda
bawa ke meja sidang untuk menjelaskan mengapa Anda beralih ke ULC, ini dia.

Pola sektoralnya juga konsisten: kelima divisi ULC tertinggi seluruhnya padat karya (furnitur,
pakaian, kayu, kulit/alas kaki), kelima yang terendah didominasi padat modal dan berbasis
sumber daya. Artinya ULC yang terhitung **berperilaku sebagaimana diprediksi teori** — ini uji
kewajaran yang penting sebelum variabel dipakai dalam regresi.

---

## 3. TEMUAN BARU: TABEL 4.1 DI DRAFT 4C SALAH BESAR

Saat membandingkan hasil ekstraksi dengan naskah, muncul satu kekeliruan yang belum tertangkap
di review sebelumnya.

| | Draft 4c (Tabel karakteristik) | Data BPS 2012 | |
|---|---:|---:|---|
| Jumlah perusahaan | **147.582** | **23.592** | ❌ selisih 6,3 kali |
| Total tenaga kerja | 4.899.328 | 4.881.165 | ✅ cocok |
| Biaya tenaga kerja produksi | Rp 88,24 T | Rp 114,45 T | ❌ tidak cocok |

Jumlah perusahaan industri besar dan sedang Indonesia tahun 2012 menurut BPS adalah **23.592
unit**. Angka 147.582 di naskah Anda lebih dari enam kali lipat — itu besaran industri mikro
dan kecil, bukan industri besar dan sedang yang menjadi cakupan survei ini.

Angka tenaga kerja di naskah justru **cocok** (4,90 juta versus 4,88 juta; selisih kecil berasal
dari divisi 33 yang saya keluarkan dan beberapa sel yang dirahasiakan BPS). Jadi bukan seluruh
tabel yang salah — hanya baris jumlah perusahaan dan biaya tenaga kerja produksi.

Ini juga menjelaskan temuan A5 pada review sebelumnya: upah rata-rata pekerja produksi di
naskah tidak bisa direproduksi dari Tabel 4.1, sementara upah non-produksi cocok sempurna.
Penyebabnya memang ada di baris biaya tenaga kerja produksi.

**Seluruh Tabel 4.1 sekarang dapat diregenerasi dari `tabel_sektor.csv`.**

---

## 4. KLASIFIKASI SEKTOR — JEMBATAN ISIC REV.3 KE REV.4

Publikasi 2012 memakai KBLI 2009 (= ISIC Rev.4), sedangkan Tabel 3.1 naskah Anda menyusun
klasifikasi sektor pada ISIC Rev.3 2 digit mengikuti Narjoko & Putra (2014). Keduanya saya
jembatani pada tingkat **divisi**, karena pada tingkat itu korespondensinya tegas dan
terdokumentasi.

| Divisi Rev.4 | Nama | Asal Rev.3 | Sektor |
|---|---|---|---|
| 10, 11 | Makanan, Minuman | 15 | Resource Intensive |
| 12 | Pengolahan tembakau | 16 | Resource Intensive |
| 13 | Tekstil | 17 | Labor Intensive |
| 14 | Pakaian jadi | 18 | Labor Intensive |
| 15 | Kulit dan alas kaki | 19 | Labor Intensive |
| 16 | Kayu | 20 | Labor Intensive |
| 17 | Kertas | 21 | Resource Intensive |
| 18 | Percetakan | 22 | Labor Intensive |
| 19 | Batubara dan pengilangan migas | 23 | Resource Intensive |
| 20, 21 | Kimia, Farmasi | 24 | Labor Intensive |
| 22 | Karet dan plastik | 25 | Resource Intensive |
| 23 | Galian bukan logam | 26 | Capital Intensive |
| 24 | Logam dasar | 27 | Capital Intensive |
| 25 | Barang logam bukan mesin | 28 | Capital Intensive |
| 26 | Komputer, elektronik dan optik | 30, 32, 33 | Capital Intensive |
| 27 | Peralatan listrik | 31 | Capital Intensive |
| 28 | Mesin dan perlengkapan | 29 | Capital Intensive |
| 29 | Kendaraan bermotor | 34 | Capital Intensive |
| 30 | Alat angkutan lainnya | 35 | Capital Intensive |
| 31 | Furnitur | 36 | Labor Intensive |
| ⚠️ 32 | Pengolahan lainnya | 36 + sebagian 33 | Labor Intensive *(perlu dicek)* |
| ⛔ 33 | Jasa reparasi dan pemasangan mesin | tidak ada padanan | **dikeluarkan** |

**Dua puluh satu dari dua puluh empat divisi terpetakan tanpa ambiguitas.** Dua kasus yang
perlu dicatat:

**Divisi 32 (Pengolahan lainnya)** sebagian besar berasal dari Rev.3 divisi 36 (industri
pengolahan ytdl, diklasifikasikan *labor intensive* dalam Tabel 3.1 Anda), tetapi juga menerima
sebagian dari Rev.3 divisi 33 (instrumen kedokteran dan optik, *capital intensive*). Saya
menempatkannya sebagai *labor intensive* mengikuti asal yang dominan, dan menandainya di kolom
`status_pemetaan` agar bisa Anda uji sebagai bagian dari analisis ketahanan.

**Divisi 33 (Jasa reparasi dan pemasangan mesin)** tidak punya padanan di divisi manufaktur
ISIC Rev.3 — kegiatan ini dulu tersebar di sektor jasa. Saya mengeluarkannya, dan ini juga
tepat secara substantif: jasa reparasi tidak menghasilkan barang yang dapat diekspor, sehingga
tidak relevan untuk fungsi penawaran ekspor. Sebelas kode KBLI dan 85 perusahaan keluar dari
sampel.

Sampel setelah penyaringan: **387 KBLI 5 digit**, dari 398.

---

## 5. KEPUTUSAN YANG SAYA SARANKAN SOAL KONKORDANSI

Awalnya saya berencana mengonversi data industri dari ISIC Rev.4 ke Rev.3 agar cocok dengan
naskah lama. **Setelah melihat datanya, saya menyarankan arah sebaliknya.**

**Jangan konversi data industri ke Rev.3. Konversi data ekspornya ke Rev.4.**

Empat alasan:

1. **Konversi Rev.4 → Rev.3 pada tingkat 4–5 digit bersifat banyak-ke-banyak.** Satu kelas Rev.4
   bisa terpecah ke beberapa kelas Rev.3 dan sebaliknya. Setiap pemecahan membutuhkan asumsi
   pembagian yang tidak dapat diverifikasi, dan itu menyuntikkan kesalahan pengukuran ke dalam
   variabel utama Anda — persis masalah yang sedang kita coba hilangkan.

2. **Data ekspor Anda harus dibangun ulang.** Berkas Comtrade tidak ada di komputer maupun
   Drive Anda; yang tersimpan hanya `ImporIndonesia.mdb`. Karena tetap harus diunduh ulang,
   tidak ada biaya tambahan untuk mengunduhnya dalam konkordansi Rev.4.

3. **Konkordansi HS → ISIC Rev.4 tersedia resmi** dari UN Comtrade dan WITS, dan justru lebih
   mutakhir serta lebih terawat daripada jalur HS → Rev.3.

4. **Data industri tetap utuh** pada klasifikasi aslinya, tanpa satu pun asumsi pembagian.

Konsekuensinya terhadap naskah kecil dan mudah dipertahankan: BAB III menyatakan unit analisis
sebagai **KBLI 2009 / ISIC Rev.4 lima digit**, Tabel 3.1 diganti dengan tabel pemetaan di
bagian 4 dokumen ini, dan justifikasinya satu kalimat — klasifikasi mengikuti publikasi sumber
data agar tidak ada kesalahan konversi.

Ini juga **memperbaiki temuan B8 pada review sebelumnya**, yaitu level agregasi ISIC yang
bertabrakan di tiga tempat dalam naskah. Sekarang hanya ada satu klasifikasi di seluruh tesis.

---

## 6. BERKAS YANG DIHASILKAN

**`data/SI2012_KBLI5.csv`** — 398 baris, kini dengan lima kolom tambahan:
`divisi` · `divisi_nama` · `isic_rev3_asal` · `sektor` · `status_pemetaan`

**`data/tabel_sektor.csv`** — agregat per sektor, siap menjadi **Tabel 4.1 BAB IV**

**`data/tabel_divisi.csv`** — agregat per divisi, 24 baris, bahan untuk pembahasan dan grafik

Catatan metodologis: ULC agregat dihitung sebagai `Σ biaya tenaga kerja ÷ Σ nilai tambah`,
bukan rata-rata ULC antar industri. Pembobotan ini yang benar — industri besar memang seharusnya
lebih menentukan ULC kelompok — dan menghindari distorsi dari industri bernilai tambah sangat
kecil. Kolom `ULC_median` disediakan sebagai pembanding tak tertimbang.

---

## 7. LANGKAH BERIKUTNYA

| # | Pekerjaan | Status |
|---|---|---|
| 1 | Unduh data ekspor Comtrade 2012 dengan konkordansi HS → ISIC Rev.4 | **butuh Anda** |
| 2 | Gabungkan dengan `SI2012_KBLI5.csv` pada KBLI 5 digit | setelah 1 |
| 3 | Hitung `Px` (unit value) dan variabel ekspor | setelah 1 |
| 4 | Harga bahan baku impor — dari `ImporIndonesia.mdb` yang sudah ada | bisa dikerjakan |
| 5 | Statistik deskriptif lengkap BAB IV | sebagian **sudah jadi** |
| 6 | Estimasi enam spesifikasi | setelah 1–4 |
| 7 | Unduh Buku II (Bahan Baku) untuk pangsa input impor | opsional |

**Nomor 4 bisa saya kerjakan sekarang** — `ImporIndonesia.mdb` ada di folder Anda dan memuat
data impor yang dibutuhkan untuk membangun `Pm`. Itu satu variabel utama lagi yang bisa
diselesaikan tanpa menunggu apa pun.
