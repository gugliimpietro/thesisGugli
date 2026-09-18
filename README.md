# Tesis — Pengaruh Upah Tenaga Kerja terhadap Kinerja Ekspor Industri Manufaktur di Indonesia

Magister Ilmu Ekonomi, FEB Universitas Indonesia
Satria Dwi Saputra — NPM 1306418013

**Repo ini private.** Berisi naskah tesis yang belum disidangkan, catatan bimbingan, dan data
olahan. Jangan diubah menjadi public.

---

## Status saat ini

Draft lengkap BAB I–V, dalam tahap perbaikan menuju sidang. Naskah kerja: **`draftp Proposal
tesis 4c.docx`** (bukan rev4b — lihat catatan di bawah).

Kesiapan sidang diperkirakan **sekitar 65%**.

### Desain penelitian

| | |
|---|---|
| Variabel terikat | Volume ekspor (`lnVolume`), bukan nilai — sesuai fungsi penawaran Riveros (1992) |
| Desain | Cross-section tahun 2012 |
| Unit analisis | KBLI 2009 / ISIC Rev.4, 5 digit |
| Kerangka | Riveros (1992), fungsi penawaran ekspor *small country* |

### Dua keputusan besar yang sudah diambil

**1. Biaya tenaga kerja diukur sebagai Unit Labour Cost, bukan upah per pekerja.**
Upah per pekerja mencampur dua sinyal berlawanan — biaya (menekan ekspor) dan produktivitas
(mendorong ekspor) — yang saling meniadakan. Itu sebab koefisien upah di draft lama tidak
signifikan (+0,074; p = 0,855). Bukti empirisnya ada di `11_ULC_DAN_DESKRIPTIF_2012.md`.

**2. Analisis memakai ISIC Rev.4, bukan Rev.3.**
Publikasi BPS 2012 memakai KBLI 2009 (= ISIC Rev.4). Mengonversinya ke Rev.3 bersifat
banyak-ke-banyak dan menyuntikkan kesalahan pengukuran. Yang dikonversi justru data ekspornya:
HS → ISIC Rev.4.

---

## Peta berkas

### Dokumen analisis (urut nomor = urut pengerjaan)

| Berkas | Isi |
|---|---|
| `00_AUDIT_DAN_RENCANA_KERJA_TESIS.md` | Audit awal draft rev4b |
| `01_KELAS_STATISTIK_UNTUK_TESIS.md` | Materi ekonometrika panel, ditulis dari model tesis ini |
| `02_TEMUAN_FOLDER_DRIVE_DAN_STRATEGI_BARU.md` | Temuan dari folder Drive; koreksi atas audit pertama |
| `03_SPEK_BAB_IV_DESKRIPTIF.md` | Rancangan BAB IV deskriptif sesuai arahan pembimbing |
| `04_OUTPUT_STATA_ASLI.md` | **Salinan verbatim 11 regresi Stata asli**, terverifikasi 48/48 baris |
| `05_INVENTARIS_DRIVE.md` | Audit ketersediaan data |
| `06_REVIEW_DRAFT_4C.md` | **Review lengkap draft 4c** — 6 temuan kritis, 10 sedang |
| `07_STRATEGI_SPESIFIKASI_MODEL.md` | **Strategi ULC + instrumen upah minimum**, dengan rujukan jurnal |
| `08_PANDUAN_MEMBANGUN_ULC.md` | Cara menghitung ULC + kode variabel BPS |
| `09_BAB_III_REVISI.md` | **Naskah BAB III revisi**, siap disisipkan; + tambahan BAB II dan daftar pustaka |
| `10_HASIL_CEK_DATA_2012.md` | Hasil ekstraksi publikasi BPS 2012 |
| `11_ULC_DAN_DESKRIPTIF_2012.md` | **ULC per sektor dan per divisi** + klasifikasi sektor Rev.4 |
| `12_CATATAN_Pd_DAN_MDB.md` | Harga domestik `Pd` dari Buku Produksi; catatan `ImporIndonesia.mdb` |
| `13_CEK_BUKU_BAHAN_BAKU.md` | Buku Bahan Baku Bagian A — cakupan median 45%, butuh Bagian B |
| `14_PM_DARI_BEA_CUKAI.md` | **Pm dari Bea Cukai 2012** — metode, hasil, beda dengan Buku Bahan Baku |
| `14_VERIFIKASI_DATA_IMPOR.md` | `Imporberat2012.csv` terpotong di HS 38; korelasi Pm Bea Cukai vs BPS ≈ 0 |
| `15_CEK_PUBLIKASI_MANUFAKTUR_2012.md` | Proxy modal: energi per pekerja (stok modal tidak ada di publikasi) |
| `16_PANDUAN_DATA_EKSPOR_IMPOR.md` | Mengapa Comtrade, bukan Trade Map; Px dan Pm dari sumber yang sama |
| `17_HASIL_UJI_COMTRADE_LEWAT_BROWSER.md` | Resep unduhan Comtrade + rekonsiliasi per bab HS |

### Data

| Berkas | Isi |
|---|---|
| `data/SI2012_KBLI5.csv` | 398 industri KBLI 5 digit — tenaga kerja, upah, nilai tambah, ULC, sektor |
| `data/SI2012_KBLI5_with_prices.csv` | **Master kerja** — SI2012 + `lnPm` Bea Cukai + `lnPd` + `lnULC` |
| `data/Pm_2012_KBLI5_beacukai.csv` | Harga impor unit value, 377 KBLI (proksi; bukan harga input pabrik) |
| `data/ImporNilai2012.csv` / `Imporberat2012.csv` | **Impor** 2012 dari `ImporIndonesia.mdb` (nilai lengkap via LFS; berat terpotong di HS 38) |
| `data/comtrade_2012_X_HS6.csv` | Ekspor Indonesia 2012, HS 6-digit: nilai USD + berat kg (cakupan 100%) |
| `data/comtrade_2012_M_HS6.csv` | Impor, format sama (cakupan 100%) |
| `data/HS2012_ISIC4.csv` | Konkordans HS 2012 → ISIC Rev.4 lewat CPC Ver. 2.1 (5.205 pasangan) |
| `data/trade_2012_ISIC4.csv` | Agregat per ISIC: `X_usd, X_kg, M_usd, M_kg, Px, Pm` — siap digabung dengan SI2012 |
| `data/tabel_sektor.csv` | Agregat per sektor — siap menjadi Tabel 4.1 BAB IV |
| `data/tabel_divisi.csv` | Agregat per divisi, 24 baris |

Seluruh nilai rupiah dalam **ribuan rupiah** (satuan publikasi BPS), kecuali kolom turunan
`upah_per_pekerja_*` dan `produktivitas_per_pekerja` yang sudah dalam rupiah penuh.

### Skrip

| Berkas | Fungsi |
|---|---|
| `scripts/extract_si2012.py` | Ekstraksi publikasi BPS 2012 dari PDF; menjalankan 3 uji identitas akuntansi |
| `scripts/klasifikasi_sektor.py` | Pemetaan divisi Rev.4 → sektor; agregasi ULC |
| `scripts/00_inspeksi_data.py` | Inspeksi berkas data apa pun yang masuk folder |
| `scripts/build_pm_from_customs.py` | HS-10 → ISIC Rev.4 → `Pm` / `lnPm` dari Bea Cukai 2012 |
| `scripts/fetch_comtrade_2012.py` | Unduh Comtrade 2012 tanpa API key; rekonsiliasi per bab HS |

**Aturan kerja:** seluruh tabel hasil di-*generate* dari skrip, tidak pernah diketik manual.
Inilah cara Tabel 4.2 di rev4b rusak — gabungan dari tiga regresi berbeda.

---

## Temuan yang perlu diketahui siapa pun yang melanjutkan

**Tabel 4.2 di `rev4b` rusak.** Statistiknya (F = 4,89; R² = 0,4146) berasal dari regresi
cross-section 2012 N = 88, bukan panel. Tujuh dari sepuluh t-statistiknya tidak sama dengan
koefisien ÷ SE. Jangan pakai rev4b.

**Tabel 4.2 di `4c` bersih.** Sembilan dari sembilan baris konsisten. N = 100 berhasil dibalik
dari R² dan adjusted R², tervalidasi oleh F = 15,65.

**BAB V di 4c bertentangan dengan tabelnya sendiri** — menulis pengaruh upah "negatif" padahal
tabel menunjukkan +0,074. Dan koefisien tidak signifikan tidak punya arah.

**Tabel 4.1 di 4c salah.** Jumlah perusahaan tertulis 147.582; angka BPS 2012 yang benar
**23.592**.

**Upah tidak signifikan di ketiga estimator** (FE, RE, 2SLS) pada berkas lama — kesimpulan itu
kokoh terhadap pilihan estimator.

---

## Bukti utama yang sudah dihasilkan

| Sektor | Upah/pekerja produksi | ULC | Produktivitas/pekerja |
|---|---:|---:|---:|
| Resource Intensive | Rp 28,6 jt | 0,114 | Rp 252,7 jt |
| Labor Intensive | Rp 23,7 jt | **0,190** | Rp 136,6 jt |
| Capital Intensive | **Rp 44,0 jt** | **0,105** | Rp 432,1 jt |

Sektor yang upahnya tertinggi justru punya biaya tenaga kerja per unit output terendah.
Tingkat upah dan daya saing biaya bergerak berlawanan — inilah alasan variabel upah per pekerja
gagal menangkap apa pun.

---

## Yang belum selesai

| # | Pekerjaan | Kebutuhan |
|---|---|---|
| 1 | Unduh data **ekspor** Comtrade 2012, konkordansi HS → ISIC Rev.4 | **selesai** — ekspor dan impor 100% nilai 2012; lihat `17_` dan `data/verifikasi_comtrade.txt` |
| 2 | `Pm` proksi dari Bea Cukai | **selesai** (377 KBLI). Bukan harga bahan baku pabrik — lihat `14_`. Comtrade kini sumber utama `Px`/`Pm`; Bea Cukai jadi uji silang |
| 3 | Gabungkan industri dan ekspor pada KBLI 5 digit | **siap** — potong KBLI 5 digit jadi ISIC 4 digit, gabung dengan `trade_2012_ISIC4.csv` |
| 4 | Estimasi enam spesifikasi (OLS → ULC → interaksi → 2SLS) | setelah 1–3 |
| 5 | Sisipkan BAB III revisi ke naskah, buat versi `4d.docx` | siap |
| 6 | Tulis ulang BAB IV–V | setelah 4 |
| 7 | Instrumen upah minimum provinsi (perlu Sakernas untuk bobot provinsi) | opsional |
| 8 | Bahan Baku Bagian B + Produksi Bagian A | menyempurnakan `Pm` input dan `Pd` |

---

## Catatan untuk sesi/LLM lain

Konteks lengkap ada di dua tempat: dokumen bernomor di repo ini, dan skill `tesis-ui-ekonomi`.
Bila memulai dari nol, baca berurutan: `06` (apa yang salah) → `07` (strategi) →
`11` (data dan bukti) → `09` (naskah BAB III baru).

Bahan mentah tidak ada di repo ini — ada di `D:\kuliah s2\1. tesis\bahan tesis\`
(publikasi BPS 2012, data IBS 1990–2011, `ImporIndonesia.mdb`, catatan bimbingan).
