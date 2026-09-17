# Pm DARI BEA CUKAI 2012 — HASIL STEP 3

**Tanggal:** 17 September 2026
**Skrip:** `scripts/build_pm_from_customs.py`
**Input:** `data/ImporNilai2012.csv`, `data/Imporberat2012.csv`

---

## Apa yang dikerjakan

Harga impor tingkat industri (`Pm`) dihitung dari data kepabeanan yang Anda ekspor dari
`ImporIndonesia.mdb`, lalu dipetakan ke KBLI 2009 / ISIC Rev.4.

### Langkah (yang tadi disebut Step 3)

1. Agregasi ke HS-10 untuk seluruh bulan 2012 (jumlah CIF USD dan jumlah kg, semua negara).
2. Unit value `Pm_hs = CIF / kg`. Nilai ekstrem di bawah persentil 0,5 dan di atas 99,5 dibuang.
3. HS-10 dipotong ke HS-6, dipetakan dengan tabel resmi:
   - **WITS/World Bank:** HS 2007 → ISIC Rev.3
   - **UNSD:** ISIC Rev.3.1 → ISIC Rev.4 (Rev.3 ≈ Rev.3.1 pada 4 digit manufaktur)
   - **WITS:** HS 2007 → BEC (untuk menandai *industrial supplies*)
4. Harga industri = rata-rata tertimbang nilai dari semua HS yang masuk kelas ISIC Rev.4 itu.
5. Setiap KBLI 5 digit mengambil harga dari kelas ISIC yang cocok, urutan:
   - 4 digit (kelas) → 3 digit (grup) → 2 digit (divisi)
6. USD/kg dikalikan kurs IMF/World Bank 2012: **Rp 9.386,63 / USD**.

### Berkas hasil

| Berkas | Isi |
|---|---|
| `data/Pm_2012_HS6.csv` | 1.410 kode HS-6 |
| `data/Pm_2012_ISIC4.csv` | 99 kelas ISIC Rev.4 |
| `data/Pm_2012_KBLI5_beacukai.csv` | 398 KBLI, 377 punya `Pm` |
| `data/SI2012_KBLI5_with_prices.csv` | master industri + `lnPm`, `lnPd`, `lnULC` |

Kolom utama di master: `Pm_rp_per_kg`, `lnPm`, `Pm_intermed_rp_per_kg` (hanya BEC 2),
`Pm_match_level`, `Pd_rp_per_kg`, `lnPd`, `lnULC`, `rasio_keterampilan`.

---

## Angka ringkas

| | |
|---|---|
| Baris nilai 2012 | 519.215 (7.612 HS-10) |
| Baris berat 2012 | 91.901 (2.033 HS-10) |
| HS-10 yang punya nilai **dan** kg | 2.033 |
| Pangsa CIF yang bisa dihitung harganya | **40,1%** |
| KBLI dengan `Pm` | **377 / 398** |
| Median `Pm` | **Rp 25.666 / kg** |
| p10 – p90 | Rp 3.652 – 41.975 / kg |

Pencocokan ke KBLI: 129 di kelas 4 digit, 182 di grup 3 digit, 66 di divisi 2 digit, 21 tidak ketemu.

**21 KBLI tanpa `Pm`:** seluruh pakaian jadi (14), percetakan (18), kendaraan bermotor (29),
dan furnitur (31). Impor golongan itu tidak ada di tabel kilogram — biasanya dicatat dalam
satuan buah/set, bukan kg — jadi unit value per kilogram tidak bisa dihitung.

---

## Ini BUKAN pengganti Buku Bahan Baku BPS

Korelasi `ln Pm` Bea Cukai vs `ln Pm` BPS Bagian A: **0,009 (n = 234)**. Nol.

Itu bukan gagal hitung. Dua angka itu mengukur hal berbeda:

| | Bea Cukai (`ImporIndonesia.mdb`) | BPS Bahan Baku |
|---|---|---|
| Pertanyaan | Berapa harga barang yang **masuk ke Indonesia**, digolongkan menurut jenis barangnya? | Berapa harga bahan baku yang **dipakai pabrik itu**, impor vs total? |
| Unit | HS → ISIC barang | KBLI pemakai |
| Median | Rp 25.666/kg | Rp 1.343/kg (Bagian A, belum lengkap) |

`Pm` Bea Cukai adalah **harga impor barang sejenis** (unit value). Itu proksi yang dipakai
di sebagian literatur perdagangan, dan itu yang bisa dibangun dari mdb. Itu **bukan** harga
bahan baku yang tercatat di kuesioner SI.

Untuk fungsi penawaran ekspor Riveros / Goldstein–Khan, yang lebih tepat tetap **Buku Bahan
Baku A+B**. Pakai hasil Bea Cukai sebagai `lnPm` hanya jika Anda menyatakan di BAB III bahwa
ini unit value impor, bukan harga input pabrik.

`Pm_intermed_*` (BEC 2, industrial supplies) lebih dekat ke input. Itulah kolom yang lebih
aman dipakai kalau jalur Bea Cukai yang dipilih.

---

## Yang sudah bisa dan yang masih tertahan

| Tugas | Status |
|---|---|
| `ULC`, upah produksi/non-produksi, sektor | selesai di `SI2012_KBLI5_with_prices.csv` |
| `Pm` proksi dari Bea Cukai | **selesai**, 377 KBLI |
| `Pd` dari Produksi Bagian B | sementara, 270 KBLI, kualitas rendah |
| Pangsa input impor | **tertahan** — perlu Bahan Baku Bagian B |
| `Pd` lengkap | **tertahan** — perlu Produksi Bagian A |
| `lnVolume`, `Px` | **tertahan** — perlu ekspor Comtrade 2012, HS → ISIC Rev.4 |
| Enam spesifikasi regresi | **tertahan** — tanpa variabel terikat ekspor tidak ada yang diestimasi |

Regresi BAB IV **belum bisa dijalankan**. Yang kurang sekarang hanya data ekspor.

---

## Cara mengulang

```text
python scripts/build_pm_from_customs.py
```

Jika nanti `Imporberat2012.csv` dilengkapi (lebih banyak HS), jalankan ulang skrip itu.
KBLI 14/18/29/31 baru akan terisi jika kilogram untuk golongan itu tersedia.
