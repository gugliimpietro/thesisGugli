# INVENTARIS FOLDER DRIVE — APA YANG ADA, APA YANG TIDAK

**Tanggal:** 11 September 2026
**Cakupan:** penelusuran menyeluruh Drive `gugliimpietro@gmail.com` untuk berkas `.dta` dan `.do`

---

## JAWABAN SINGKAT ATAS PERTANYAAN ANDA

Folder `1gRoYhEayS5qGk9beaWTsAdb36yB0CARu` berisi **34 berkas `indus90`–`indus04`** dalam
format `.accdb` (Access), `.sd2` (SAS versi lama), dan satu `.dta`.

**Itu bukan berkas yang kita cari.**

Dua alasan yang menentukan:

1. **Periodenya salah.** Isinya 1990–2004. Tesis Anda memakai 2007–2012.
2. **Tingkatannya salah.** Ukuran 13–47 MB per tahun menunjukkan ini **data mentah
   Survei Industri Besar Sedang pada level perusahaan** — puluhan ribu baris per tahun.
   Panel tesis Anda adalah data **agregat per industri**: 623 baris, 105 industri, 6 tahun.
   Berkasnya seharusnya hanya beberapa ratus kilobyte.

Yang ada di folder itu adalah **bahan baku**, bukan hasil olahan. Berguna suatu saat —
tetapi bukan panel yang menghasilkan angka di BAB IV.

---

## HASIL PENELUSURAN `.dta` DI SELURUH DRIVE

Hanya **lima** berkas `.dta` di seluruh Drive Anda:

| Berkas | Ukuran | Isi sebenarnya |
|---|---|---|
| `indus01.dta` | 12 MB | Data mentah SI level perusahaan, 2001 |
| `indus07.dta` | 16,6 MB | Data mentah SI level perusahaan, 2007 |
| `recoding_temp.dta` | 3 KB | Berkas sementara milik paket replikasi peneliti lain |
| `inputtariffs5d.dta` | 55 KB | Data tarif input — paket replikasi peneliti lain |
| `prod5dtariffs.dta` | 39 KB | Data tarif produk — paket replikasi peneliti lain |

**Tidak satu pun merupakan panel tesis Anda.**

## HASIL PENELUSURAN `.do`

Seluruh `.do` yang ada (`aer_Table4.do`, `final_Table5.do` s.d. `final_Table10skilled.do`,
`estimatingtfp.do`, `correspondencetable.do`) berasal dari **paket replikasi jurnal peneliti
lain** — kemungkinan besar Amiti & Konings (AER), yang memang Anda kutip. Penanggalannya
2006–2007, jauh sebelum tesis Anda dikerjakan.

**Do-file tesis Anda sendiri tidak ada di Drive.**

---

## KESIMPULAN SOAL DATA

> **File `.dta` panel final dan do-file tesis Anda tidak ada di Google Drive.**

Kemungkinan lokasinya, urut dari yang paling mungkin:

1. **Hard disk atau laptop lama** yang dipakai pada 2015–2016 — ini yang paling mungkin
2. Media penyimpanan eksternal dari masa itu
3. Folder lokal di komputer sekarang yang belum tersambung ke sesi ini
4. Alamat email atau akun Drive lain (`satriodwisaputra@gmail.com`)

Perlu dikatakan terus terang: ada kemungkinan nyata berkas itu **memang sudah hilang**.
Bagian berikutnya menjelaskan mengapa itu bukan akhir dari pekerjaan ini.

---

## YANG BERHASIL DISELAMATKAN HARI INI

Ini kabar baiknya, dan cukup besar.

| Berkas | Isi | Nilainya |
|---|---|---|
| `catatan bimbingan.txt` | Arahan pembimbing, verbatim | Daftar tugas yang harus dipenuhi |
| `komparasi hasil regresi.docx` | 7 regresi: CS 2012, pooled, FE robust, RE, 2SLS, OLS, dekomposisi | Seluruh hasil empiris inti |
| `test asumsi.docx` | 4 regresi + korelasi + VIF + Breusch-Pagan | Uji asumsi lengkap |

Isinya sudah saya rekam verbatim ke `04_OUTPUT_STATA_ASLI.md`, lengkap dengan verifikasi
aritmetik: **48 dari 48 baris cocok**.

**Konsekuensinya penting:** untuk lima spesifikasi utama, koefisien, standard error, t, p, N,
jumlah grup, R² within/between/overall, sigma_u, sigma_e, dan rho semuanya tersedia. Itu
cukup untuk **membangun ulang seluruh tabel hasil BAB IV dengan benar** — tanpa menyentuh
file `.dta` sama sekali.

Yang tidak bisa dikerjakan tanpa `.dta` hanyalah spesifikasi **baru**: interaksi upah × sektor,
dummy tahun, Unit Labour Cost, uji autokorelasi, dan statistik deskriptif.

---

## BERKAS LAIN YANG TERSEDIA DI `ketikan tesis`

Kelengkapan dokumen sidang Anda ternyata nyaris penuh:

| Kategori | Berkas |
|---|---|
| **Naskah terbaru** | `draftp Proposal tesis 4c.docx` (24 Feb 2016, 304 KB) |
| Riwayat draft | rev1, rev2, rev3, rev4, rev4a, rev4b |
| Bab terpisah | BAB I, BAB II, BAB IIa, BAB III |
| Abstrak | versi Indonesia & Inggris (docx + pdf) — sudah jadi |
| Administratif | Cover, Daftar Isi, Surat Pernyataan |
| Presentasi sidang | `presentasi tesis rev.1.ppt` + pdf |
| Lain-lain | kerangka konseptual, ringkasan naskah |
| **Dua foto (10 Feb 2016)** | `IMG_6901.JPG`, `IMG_6902.JPG` |

Dua foto itu bertanggal 10 Februari 2016 — dua minggu sebelum draft 4c dibuat, tepat di
tengah masa bimbingan terakhir. Besar kemungkinan isinya catatan tulisan tangan pembimbing
atau papan tulis diskusi. Layak dibuka.

---

## LANGKAH YANG SAYA SARANKAN

**Yang perlu Anda lakukan — dua hal:**

1. **Unduh `draftp Proposal tesis 4c.docx` ke folder tesis.** Berkasnya 304 KB, terlalu besar
   untuk saya tarik lewat jalur ini. Satu klik dari Drive. Setelah itu saya bandingkan 4c
   dengan rev4b baris per baris dan seluruh revisi berpindah ke 4c.

2. **Cari `.dta` di hard disk atau laptop lama.** Kata kunci pencarian: `*.dta`, `*.do`,
   dan nama berkas yang mungkin dipakai — `panel`, `ekspor`, `tesis`, `olah`. Bila ketemu,
   taruh di folder tesis.

**Yang saya kerjakan sementara itu, tanpa menunggu apa pun:**

- Membangun ulang seluruh tabel hasil BAB IV dari `04_OUTPUT_STATA_ASLI.md` — termasuk
  mengganti Tabel 4.2 yang rusak dengan tabel FE cluster-robust yang sah
- Menyusun tabel perbandingan estimator (pooled / FE / RE / 2SLS) berdampingan
- Menyiapkan tabel `lnEkspor` vs `lnVolume` yang membuktikan pentingnya pemilihan variabel
  terikat
- Menulis ulang BAB V dengan kesimpulan baru
- Merapikan BAB I–III, memutakhirkan literatur, dan melengkapi daftar pustaka

Dengan kata lain: **tidak adanya file `.dta` memperlambat pekerjaan, tetapi tidak
menghentikannya.** Bagian terbesar dari perbaikan yang tesis ini butuhkan justru berupa
perakitan ulang naskah dari hasil yang sudah ada.
