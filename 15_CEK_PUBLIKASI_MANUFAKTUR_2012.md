# CEK `statistik-industri-manufaktur-indonesia-2012.pdf` — BISAKAH MENUTUP DATA YANG HILANG?

**Tanggal:** 17 September 2026
**Pertanyaan Anda:** *"can this document fill the missing data?"*

---

## JAWABAN SINGKAT

**Sebagian — dan bagian yang ditutupnya ternyata penting.**

Dokumen itu adalah **Buku I, Katalog 6103019** — publikasi yang sama yang sudah saya
ekstrak pada hari pertama menjadi `data/SI2012_KBLI5.csv`. Jadi tidak ada baris data
*baru* untuk upah, tenaga kerja, output, dan nilai tambah: semuanya sudah ada.

Tetapi ada satu tabel di dalamnya yang **belum pernah kita pakai** — Tabel 7 (Biaya
Input). Tabel itu memecah biaya input menjadi enam komponen, dan salah satunya
menyelamatkan variabel yang sampai kemarin sama sekali tidak punya jalan keluar.

Ringkasnya:

| Variabel yang hilang | Ditutup Buku I? | Keterangan |
|---|---|---|
| **Modal (`lnCapital`)** | **Ya — lewat proxy** | Tabel 7 kolom (3) → intensitas energi per pekerja |
| **Harga bahan baku impor (`Pm`)** | **Tidak** | Tabel 7 tidak memecah domestik/impor |
| **Pangsa bahan baku impor** | **Tidak** | idem — harus dari Buku Bahan Baku |
| **Ekspor (`Qx`, variabel terikat)** | **Tidak** | tidak ada di publikasi mana pun; harus Comtrade |
| Upah, TK, output, nilai tambah, ULC | Sudah ada sejak awal | `SI2012_KBLI5.csv` |

---

## TEMUAN 1 — MODAL: MASALAH YANG BARU KETAHUAN, DAN SOLUSINYA

Waktu memeriksa dokumen ini saya menyadari sesuatu yang sebelumnya luput.

Model di BAB III memakai `lnCapital` (stok modal). Di data mikro BPS, itu variabel
`CTTTCU`. **Variabel itu tidak ada di publikasi mana pun.** Yang ada hanya Tabel 10a
dan 10b: *pembelian/penambahan* dan *penjualan/pengurangan* barang modal tetap —
yaitu **arus (flow)**, bukan **stok (stock)**. Menjumlahkan arus satu tahun tidak
menghasilkan stok modal.

Artinya: dengan Opsi A (pakai publikasi, tidak minta data mikro), `lnCapital`
**tidak bisa dibangun langsung**. Ini lubang yang nyata dan harus diakui di sidang.

**Penggantinya: intensitas energi.**

Tabel 7 kolom (3) adalah *Bahan Bakar, Tenaga Listrik dan Gas*. Dalam literatur
produktivitas industri, pengeluaran energi per pekerja adalah proxy standar untuk
intensitas modal — alasannya sederhana: mesin memakai listrik, tenaga kerja tidak.
Semakin padat modal sebuah industri, semakin besar tagihan energinya per pekerja.

Saya sudah membangunnya dan mengujinya. Hasilnya:

```
korelasi ln(energi per pekerja) vs ln(produktivitas per pekerja) = +0,662
korelasi ln(energi per pekerja) vs ULC                           = −0,403
```

Korelasi +0,66 dengan produktivitas tenaga kerja persis seperti yang diharapkan dari
sebuah proxy intensitas modal: industri padat modal punya produktivitas per pekerja
lebih tinggi. Tanda negatif terhadap ULC juga benar arahnya.

Dan yang paling meyakinkan, urutan antarsektornya benar sendiri tanpa saya atur:

| Sektor | n KBLI | Pangsa energi terhadap biaya input |
|---|---|---|
| **Capital Intensive** | 122 | **13,46 %** |
| Labor Intensive | 117 | 10,53 % |
| Resource Intensive | 111 | 5,62 % |

Sektor yang memang kita namai *Capital Intensive* keluar dengan intensitas energi
tertinggi. Klasifikasi sektor dan proxy modal dibangun dari dua sumber yang sama
sekali terpisah, jadi kecocokan ini adalah validasi silang yang sah — dan enak
diucapkan di depan penguji.

**Rekomendasi:** ganti `lnCapital` menjadi `lnEnergiPerPekerja` di persamaan BAB III,
dan tulis di catatan metode bahwa stok modal tidak tersedia pada level publikasi
sehingga dipakai proxy intensitas energi, dengan rujukan korelasi +0,66 di atas
sebagai pembenarannya. Ini justru lebih jujur daripada memaksakan angka stok modal
yang tidak ada.

---

## TEMUAN 2 — Pm TETAP TIDAK BISA DARI BUKU I

Saya berharap Tabel 7 memecah bahan baku menjadi domestik dan impor. **Tidak.**
Kolomnya adalah:

```
(2) Bahan Baku dan Penolong          (5) Jasa yang Diberikan Pihak Lain
(3) Bahan Bakar, Tenaga Listrik, Gas (6) Biaya representasi dan royalti
(4) Sewa Gedung, Mesin, Alat-alat    (7) Pengeluaran Lainnya
                                     (8) Jumlah
```

Tidak ada pemisahan impor di mana pun. Jadi `Pm` dan pangsa bahan baku impor
**tetap harus** datang dari Buku *Bahan Baku* (Bagian A + B), atau dari data Bea
Cukai yang sudah Anda ekspor dari `ImporIndonesia.mdb`.

---

## VERIFIKASI — SEMUA HIJAU

Standar yang sama seperti waktu membangun `SI2012_KBLI5.csv`: tidak dipakai sebelum
identitas akuntansinya cocok.

```
Jumlah Tabel 7 (kolom 8) = Biaya Input Tabel 9    → cocok 357, beda 0, tak terbanding 41*
Jumlah komponen (2)+(3)+...+(7) = kolom (8)        → cocok 131, beda 0
```

\* 41 KBLI tidak terbandingkan karena BPS menyembunyikan angkanya (tanda `*`,
kerahasiaan responden) — bukan kesalahan ekstraksi.

Dua identitas, nol selisih. Ini berbeda tajam dengan hasil ekstraksi Buku Bahan Baku
yang kemarin saya batalkan sendiri (`Pm_2012_KBLI5_bagianA.csv`) — di sana tidak ada
identitas yang bisa dipakai menguji, dan ternyata memang salah baca kolom. Di sini
ada, dan lulus.

---

## BERKAS BARU

**`data/struktur_biaya_2012.csv`** — 398 KBLI, kolom:

```
kbli, sektor, divisi,
bahan_baku_penolong, biaya_energi, sewa, jasa_pihak_lain,
representasi_royalti, pengeluaran_lainnya,
biaya_input_T7, biaya_input_T9,
energi_per_pekerja_rp, pangsa_energi, pangsa_bahan_baku
```

Median energi per pekerja: **Rp 11.864.187 per tahun** (356 KBLI).
Median pangsa energi terhadap biaya input: **8,0 %**.

---

## SISA PEKERJAAN — TIDAK BERUBAH

Yang masih Anda perlu unduh/ekspor:

1. **Comtrade 2012** + konkordans HS → ISIC Rev.4 — ini variabel terikat, dan
   satu-satunya yang sampai sekarang belum punya jalan sama sekali. **Prioritas 1.**
2. **Bahan Baku 2012 Bagian B** (Katalog 6103002) — untuk melengkapi cakupan Pm.
3. **Ekspor ulang tabel "Impor (Berat) KG"** dari `ImporIndonesia.mdb` — ekspor
   kemarin terpotong di bab HS 38.

Yang saya kerjakan: memperbaiki pembaca kolom Buku Bahan Baku, lalu membandingkan
ulang kedua sumber Pm setelah bersih.
