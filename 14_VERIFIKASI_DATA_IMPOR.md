# VERIFIKASI DATA IMPOR BEA CUKAI — SATU BERKAS TERPOTONG

**Tanggal:** 17 September 2026
**Diperiksa:** `ImporNilai2012.csv`, `Imporberat2012.csv`, dan seluruh berkas turunannya

---

## JAWABAN SINGKAT

Ya, kedua berkas bisa dipakai — **tetapi `Imporberat2012.csv` terpotong dan harus diekspor ulang
sebelum `Pm` dari bea cukai dipercaya.**

---

## 1. Berkas nilai: sempurna

| | |
|---|---|
| Baris | 519.215 |
| Total nilai | **USD 191,69 miliar** |

Angka itu **cocok dengan total impor Indonesia tahun 2012 menurut BPS** (sekitar USD 191,7
miliar). Ekstraksi dari database Access berhasil penuh. Tidak ada yang perlu diperbaiki.

## 2. Berkas berat: terpotong di bab HS 38

| | |
|---|---|
| Baris | 91.901 |
| Cakupan kunci (HS × negara × bulan) | **17,7%** |
| Cakupan nilai impor | **40,1%** |

Setiap baris berat punya pasangan di berkas nilai (100%), jadi penggabungannya bersih. Masalahnya
bukan kualitas, melainkan **kelengkapan**.

Saya periksa bab HS mana saja yang ada di berkas berat:

> **Bab 01 sampai 38 — lengkap. Bab 39 ke atas — tidak ada sama sekali.**

Ekspor dari tabel "Impor (Berat) KG" **berhenti di tengah jalan, tepat setelah bab 38**. Ini juga
konsisten dengan pesan galat di `mdb_struktur.txt`, yang gagal membaca tabel berat
("Unrecognized database format").

### Yang hilang justru yang paling penting

| Bab HS | Isi | Nilai impor 2012 | Punya berat |
|---|---|---:|---|
| 84 | Mesin dan peralatan mekanik | USD 28,4 miliar | **0%** |
| 85 | Mesin dan peralatan listrik | USD 18,9 miliar | **0%** |
| 72 | Besi dan baja | USD 10,1 miliar | **0%** |
| 87 | Kendaraan bermotor | USD 9,8 miliar | **0%** |
| 39 | Plastik | USD 7,1 miliar | **0%** |
| 73 | Barang dari besi/baja | USD 4,9 miliar | **0%** |
| 52 | Kapas | USD 2,5 miliar | **0%** |
| 27 | Bahan bakar mineral | USD 42,8 miliar | 100% |
| 29 | Bahan kimia organik | USD 6,9 miliar | 100% |

Ada **44 bab HS bernilai di atas USD 100 juta yang nyaris tanpa data berat** — termasuk plastik,
kertas, tekstil, alas kaki, mesin, elektronik, dan kendaraan.

Untuk tesis tentang ekspor manufaktur, itu persis industri yang paling penting. `Pm` untuk
sektor *capital intensive* praktis tidak punya dasar data sama sekali.

---

## 3. Akibatnya pada berkas turunan

`Pm_2012_HS6.csv` memuat total CIF USD 76,6 miliar — sama dengan bagian yang beririsan. Jadi
seluruh berkas turunan (`Pm_2012_ISIC4.csv`, `Pm_2012_KBLI5_beacukai.csv`,
`SI2012_KBLI5_with_prices.csv`) dibangun dari **40% impor saja**, dan 40% itu terpilih secara
sistematis — bukan acak.

Pengerjaannya sendiri sudah benar secara mekanis. Yang bermasalah adalah masukannya.

### Dua catatan lain pada berkas turunan

**Pemetaan HS ke ISIC bersifat banyak-ke-banyak.** 70% kode HS6 memetakan ke lebih dari satu
kelas ISIC Rev.4 (kolom `isic4` berisi `0141|0142|0144`). Akibatnya hanya ada **51 nilai `Pm`
unik untuk 398 KBLI** — sebagian besar industri berbagi angka yang sama. Kolom `match_level`
merekam ini dengan jujur: hanya 129 KBLI cocok di tingkat 4 digit, 182 di tingkat 3 digit,
66 hanya di tingkat divisi, dan 21 tidak cocok sama sekali.

**Ada persoalan konsep yang lebih dalam.** Konkordansi HS→ISIC memetakan barang ke industri yang
**memproduksinya**, bukan yang **memakainya**. Jadi `Pm` dari bea cukai sebenarnya mengukur
"harga impor barang sejenis dengan keluaran industri ini", bukan "harga bahan baku yang dipakai
industri ini". Untuk fungsi penawaran Riveros, yang dibutuhkan adalah yang kedua.

Publikasi BPS Bahan Baku memberi yang kedua secara langsung — ia mencatat apa yang benar-benar
dipakai tiap industri.

---

## 4. Koreksi atas pekerjaan saya sendiri

Saya membandingkan `Pm` bea cukai dengan `Pm` dari BPS Bahan Baku Bagian A pada 234 KBLI yang
punya keduanya:

> **Korelasi ln–ln: r = 0,009.** Hanya 10% yang berada dalam rentang dua kali lipat satu sama
> lain; 63% meleset lebih dari sepuluh kali.

Nol korelasi berarti setidaknya satu dari keduanya salah. Setelah menelusuri, **keduanya
bermasalah** — dan sebagian kesalahan ada di pihak saya.

Contoh dari KBLI 27201 (baterai kering) di publikasi BPS:

```
232010507  Wax/lilin        KG  32 338 229 328  3 233 825  32 380 629 301  3 239 065
232030103  Graphite Powder  KG   6 059 981 874  6 059 988   6 139 436 764   6 138 861
```

Baris grafit menunjukkan banyaknya persis 1.000 kali nilainya — pola yang terlalu rapi untuk
kebetulan. Dan 32 juta ton lilin untuk sepuluh pabrik baterai jelas mustahil. Artinya
**pembaca kolom saya salah memisahkan angka pada tabel ini**: kelompok ribuan bisa menyatu
melintasi batas kolom.

Untuk Buku I hal itu tidak terjadi — di sana ada tiga identitas akuntansi yang saya uji dan
semuanya cocok tanpa kecuali. Untuk Buku Bahan Baku tidak ada identitas pembanding, dan saya
melewatkannya. `Pm_2012_KBLI5_bagianA.csv` karena itu **tidak boleh dipakai** sampai pembacanya
diperbaiki.

---

## 5. Yang perlu dilakukan

| # | Pekerjaan | Siapa |
|---|---|---|
| 1 | **Ekspor ulang tabel "Impor (Berat) KG"** — ekspor sekarang berhenti di bab HS 38 | Anda |
| 2 | Perbaiki pembaca tabel Bahan Baku agar kolom tidak menyatu | saya |
| 3 | Unduh Bahan Baku Bagian B dan Produksi Bagian A | Anda |
| 4 | Bandingkan ulang kedua sumber `Pm` setelah 1–3 beres | saya |

**Untuk nomor 1:** kemungkinan besar ekspornya terhenti, bukan tabelnya rusak — berkas nilai
dari database yang sama berhasil penuh. Coba ekspor per rentang bab, misalnya
`WHERE hs07 >= '39'`, lalu gabungkan. Bila Access menolak membuka tabel itu, jalankan
**Compact and Repair Database** dulu.

Perlu diperhatikan juga: ukuran `ImporIndonesia.mdb` berubah dari 763 MB menjadi 922 MB sejak
pemeriksaan terakhir. Bila itu akibat proses repair, pastikan ada salinan cadangan sebelum
mengulang.

---

## 6. Mana yang akhirnya dipakai

Setelah keduanya bersih, saya menyarankan:

**`Pm` utama dari publikasi BPS Bahan Baku** — karena mengukur bahan baku yang benar-benar
dipakai tiap industri, sesuai yang dituntut kerangka Riveros, dan langsung tersedia pada
tingkat KBLI 5 digit.

**`Pm` bea cukai sebagai uji ketahanan** — nilainya justru terletak pada kerincian HS 6 digit
dan pada fakta bahwa ia sumber yang sepenuhnya independen. Bila kesimpulan tesis bertahan pada
kedua ukuran, itu pernyataan yang kuat di sidang.

Data bea cukai juga punya satu kegunaan yang tidak tergantikan: **harga dunia sebagai instrumen**
untuk mengatasi endogenitas harga (Teknik B pada dokumen 07). Untuk keperluan itu,
kerinciannya justru menjadi keunggulan.
