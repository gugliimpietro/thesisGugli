# CARA MENGEKSPOR `indus07.accdb` KE CSV

**Dua jalan.** Saya sarankan jalan pertama karena tekniknya sudah terbukti berhasil di
komputer Anda (dipakai waktu membaca `ImporIndonesia.mdb`). Jalan kedua saya siapkan
karena Anda bertanya soal Excel — tapi ada catatan penting di bawah soal mengapa itu
berisiko untuk file sebesar ini.

---

## JALAN 1 — PowerShell (disarankan, tidak perlu Excel sama sekali)

Ini otomatis: membaca semua tabel di dalam `indus07.accdb`, mencatat strukturnya, dan
mengekspor **setiap tabel** langsung ke CSV — tanpa melewati Excel, jadi tidak
terbentur batas baris/kolom lembar kerja atau salah pasang driver 32-bit/64-bit.

1. Simpan `export_indus_accdb.ps1` (terlampir) ke:
   ```
   D:\kuliah s2\1. tesis\thesisGugli\scripts\
   ```
2. Buka **PowerShell biasa** (tidak perlu jadi Administrator):
   ```
   cd "D:\kuliah s2\1. tesis\thesisGugli\scripts"
   .\export_indus_accdb.ps1
   ```
3. Tunggu sampai selesai. Hasilnya di `data\`:
   - `indus_struktur.txt` — daftar tabel, kolom, jumlah baris
   - satu `.csv` untuk setiap tabel di dalam `accdb`

4. Commit & push, lalu beri tahu saya. Kalau ada lebih dari satu tabel, saya baca
   `indus_struktur.txt` dulu untuk menentukan mana tabel data utamanya (biasanya yang
   jumlah barisnya paling banyak, berisi kode industri 5-digit per perusahaan).

**Kalau skrip gagal terhubung** (jarang, karena drivernya sudah pernah jalan untuk
`ImporIndonesia.mdb`): pasang *Microsoft Access Database Engine 2016 Redistributable*
versi 64-bit dari Microsoft, lalu ulangi.

---

## JALAN 2 — Lewat Excel (kalau Anda tetap ingin lewat situ)

**Peringatan dulu:** `indus07.accdb` kemungkinan berisi puluhan ribu baris data tingkat
perusahaan. Memuatnya penuh ke lembar kerja Excel bisa lambat, dan plugin Claude di
Excel bekerja di atas apa yang sudah ada di sel/lembar kerja — ia **tidak bisa membuka
file Access secara langsung**. Jadi urutannya tetap dua tahap: Excel menarik datanya
dulu, baru Claude membantu merapikan/mengekspor.

**Tahap A — tarik tabel dari Access ke Excel (fitur bawaan Excel, bukan plugin):**

1. Buka Excel kosong.
2. Ribbon **Data** → **Get Data** (atau **From Database** di versi lama) →
   **From Microsoft Access Database**.
3. Cari dan pilih file:
   ```
   D:\kuliah s2\1. tesis\bahan tesis\data\data IBS 1990-2013\Data industri manufaktur\Industri Manufaktur_2005-2011\Akses\indus07.accdb
   ```
4. Jendela **Navigator** akan menampilkan daftar tabel di dalamnya. Pilih tabel yang
   jumlah barisnya paling banyak (klik satu-satu, pratinjau muncul di kanan) —
   itu tabel data utama.
5. Klik **Load** (bukan "Transform Data", kecuali Anda ingin membersihkan dulu).

**Tahap B — minta plugin Claude di Excel mengekspornya ke CSV.** Setelah data
termuat di lembar kerja, ketik ini ke plugin Claude di Excel:

```
Data industri manufaktur BPS ada di lembar kerja ini. Simpan seluruh lembar ini
sebagai file CSV bernama indus07.csv, gunakan koma sebagai pemisah dan UTF-8
sebagai enkode karakter, tanpa mengubah nilai apa pun di dalamnya.
```

Kalau plugin tidak punya izin menulis file langsung, Excel juga bisa: **File → Save
As → Comma Separated Values (.csv)**.

---

## SETELAH BERKASNYA ADA

Taruh CSV-nya di `data/`, commit & push, lalu beri tahu saya. Saya akan periksa
kolomnya lebih dulu (mestinya memuat kode industri 5-digit, upah, tenaga kerja, nilai
tambah — persis pola yang sama dengan `SI2012_KBLI5.csv`), lalu saya buatkan satu
skrip yang mengolah **semua tahun sekaligus** (2005–2011) dengan cara yang sama.
