# KELAS STATISTIK UNTUK TESIS ANDA
### Metode 20/80 — 20% konsep yang menjelaskan 80% isi tesis Anda

**Untuk:** Satria Dwi Saputra
**Materi:** Semua contoh memakai angka asli dari hasil regresi tesis Anda sendiri
**Cara pakai:** Baca berurutan. Jangan lompat. Tiap modul dibangun di atas modul sebelumnya.

---

## PENGANTAR: 9 konsep, itu saja

Tesis Anda terlihat rumit karena penuh istilah asing. Tetapi sesungguhnya seluruh isinya
berdiri di atas **sembilan konsep**. Kalau Anda kuasai sembilan ini, Anda bisa menjelaskan
setiap angka dalam tesis Anda, dan bisa menjawab hampir semua pertanyaan penguji.

| # | Konsep | Menjawab pertanyaan |
|---|---|---|
| 1 | Regresi | Bagaimana kita tahu upah memengaruhi ekspor? |
| 2 | Logaritma & elastisitas | Kenapa semua variabel Anda pakai "ln"? |
| 3 | Koefisien, SE, t, p-value | Angka mana yang boleh dipercaya? |
| 4 | Data panel | Kenapa 108 industri × 6 tahun? |
| 5 | Fixed Effects | Kenapa dummy sektor Anda hilang? |
| 6 | Random Effects & Hausman | Kenapa Anda menjalankan tiga regresi? |
| 7 | Endogenitas | Kenapa koefisien upah Anda positif, bukan negatif? |
| 8 | Variabel Instrumen | Bagaimana cara memperbaikinya? |
| 9 | R² & uji diagnostik | Seberapa bagus model saya? |

Mari mulai.

---

# MODUL 1 — Apa itu regresi?

## Intinya dalam satu kalimat
> **Regresi adalah menarik satu garis lurus terbaik melewati sekumpulan titik, untuk mengukur
> seberapa besar sesuatu berubah ketika sesuatu yang lain berubah.**

## Cerita dulu, rumus belakangan

Bayangkan Anda punya warung kopi. Selama 10 hari Anda mencatat dua hal: berapa jumlah gula
yang Anda beli, dan berapa cangkir kopi yang terjual.

| Hari | Gula (kg) | Kopi terjual (cangkir) |
|---|---|---|
| 1 | 2 | 40 |
| 2 | 3 | 55 |
| 3 | 5 | 95 |
| 4 | 4 | 70 |
| 5 | 6 | 115 |

Kalau titik-titik ini Anda gambar di kertas — gula di sumbu horizontal, kopi di sumbu
vertikal — titiknya akan membentuk pola menanjak. Tidak persis lurus, tapi jelas menanjak.

**Regresi = menarik satu garis lurus yang paling pas melewati titik-titik itu.**

Dari garis itu keluar satu angka penting: **kemiringan garis (slope)**. Misalnya
kemiringannya 19. Artinya: *setiap tambah 1 kg gula, kopi terjual bertambah sekitar 19 cangkir.*

Angka 19 itulah yang di tesis Anda disebut **koefisien**.

## Kenapa "garis terbaik"? Terbaik menurut siapa?

Garis terbaik = garis yang membuat **total jarak titik ke garis sekecil mungkin**.
Jaraknya dikuadratkan dulu (supaya jarak ke atas dan ke bawah tidak saling menghapus),
lalu dijumlahkan. Metode ini namanya **Ordinary Least Squares (OLS)** — "kuadrat terkecil biasa".

Itu sebabnya di Stata Anda mengetik `reg`. Itu singkatan dari regression, dan yang dijalankan
adalah OLS.

## Sekarang ke tesis Anda

Ganti "gula" dengan **upah tenaga kerja**, dan ganti "kopi terjual" dengan **nilai ekspor**.
Setiap titik bukan lagi satu hari, melainkan **satu industri di satu tahun** — misalnya
industri tekstil tahun 2009, industri furnitur tahun 2011, dan seterusnya. Anda punya 643 titik.

Regresi Anda menarik garis melewati 643 titik itu, dan menghasilkan koefisien upah = **0,140**.

Tapi tesis Anda tidak hanya punya satu variabel. Ada upah, harga ekspor, harga bahan baku,
jumlah tenaga kerja, kapital, kepemilikan asing. Ini disebut **regresi berganda** (*multiple
regression*). Bayangkan bukan garis di kertas datar, tapi "garis" di ruang berdimensi banyak.

**Intuisinya tetap sama, dan ini bagian terpenting untuk Anda pahami:**

> Koefisien upah = seberapa besar ekspor berubah ketika upah naik, **sementara semua variabel
> lain ditahan tidak berubah.**

Frasa "**ditahan tidak berubah**" (dalam bahasa Inggris: *ceteris paribus*, atau *holding
other variables constant*) adalah nyawa dari regresi berganda. Regresi berganda memisahkan
pengaruh upah dari pengaruh harga ekspor, dari pengaruh ukuran perusahaan, dan seterusnya —
sehingga Anda dapat efek murni upah saja.

### ✅ Cek pemahaman Modul 1
Tutup catatan, lalu jawab dengan kata-kata sendiri:
1. Regresi itu sebenarnya sedang mencari apa?
2. Apa arti koefisien?
3. Kenapa kita perlu memasukkan banyak variabel sekaligus, tidak cukup upah saja?

---

# MODUL 2 — Kenapa semua variabel Anda pakai "ln"? (Ini kunci emas tesis Anda)

Kalau Anda hanya sempat menguasai **satu** modul sebelum sidang, pilih modul ini.

## Masalah yang diselesaikan logaritma

Lihat persamaan Anda:

```
lnEkspor = a0 + a1·lnPx + a2·lnPm + a3·lnW + ... + e
```

Semua variabel diawali `ln` — itu **logaritma natural**. Kenapa?

Bayangkan Anda melaporkan tanpa log. Koefisien upah misalnya keluar angka 2.500.000.
Artinya: "kalau upah naik Rp 1, ekspor naik US$ 2.500.000." Kalimat itu tidak berguna —
satuannya campur aduk (rupiah vs dolar), dan kenaikan Rp 1 tidak berarti apa-apa.

Lebih parah lagi: skala industri Anda sangat timpang. Ada industri raksasa dengan ekspor
miliaran dolar, ada industri kecil dengan ekspor ratusan ribu dolar. Dalam satuan asli,
industri raksasa akan mendominasi garis regresi dan membuat hasilnya menyesatkan.

## Yang dilakukan logaritma

Logaritma mengubah **satuan** menjadi **persentase**.

Ini keajaibannya, dan konsekuensinya luar biasa penting:

> **Kalau variabel terikat (Y) dan variabel bebas (X) sama-sama di-log, maka koefisiennya
> otomatis menjadi ELASTISITAS.**

**Elastisitas = kalau X naik 1%, Y berubah berapa persen?**

## Terapkan ke angka asli tesis Anda

Hasil Fixed Effects Anda: **koefisien lnWPekerja = 0,140**

Baca begini:

> **Jika upah tenaga kerja naik 1%, nilai ekspor naik 0,140%.**

Atau dengan angka yang lebih mudah dibayangkan:

> **Jika upah naik 10%, ekspor naik sekitar 1,4%.**

Selesai. Itu saja artinya. Tidak ada rumus tambahan, tidak ada konversi.

**Setiap koefisien di tabel Anda dibaca dengan cara yang persis sama:**

| Variabel | Koefisien (FE) | Cara membacanya |
|---|---|---|
| lnPx (harga ekspor) | 0,234 | Harga ekspor naik 10% → ekspor naik 2,34% |
| lnW (upah) | 0,140 | Upah naik 10% → ekspor naik 1,40% |
| lnTotTK (jumlah TK) | 0,218 | Tenaga kerja naik 10% → ekspor naik 2,18% |
| lnCapital (kapital) | 0,038 | Kapital naik 10% → ekspor naik 0,38% |

Sekali Anda paham ini, **Anda bisa membaca seluruh tabel hasil tesis Anda sendiri.**
Ini benar-benar 20% usaha untuk 80% hasil.

## Elastis vs inelastis — istilah yang pasti ditanya penguji

- Koefisien **> 1** = **elastis** → responsnya besar, lebih besar dari pemicunya
- Koefisien **< 1** = **inelastis** → responsnya kecil, teredam
- Koefisien **= 1** = **unit elastis** → satu banding satu

Semua koefisien Anda berada di bawah 1, jadi semuanya **inelastis**.

**Kalimat siap pakai untuk sidang:**
> "Elastisitas upah terhadap penawaran ekspor sebesar 0,140 menunjukkan respons yang
> inelastis. Artinya, perubahan upah memang berpengaruh terhadap kinerja ekspor, namun
> besarannya moderat — kenaikan upah sebesar 10% hanya diikuti perubahan ekspor sebesar 1,4%.
> Ini mengindikasikan bahwa upah bukan penentu tunggal daya saing ekspor industri manufaktur
> Indonesia."

Kalimat itu terdengar seperti kalimat orang yang menguasai bidangnya — dan Anda memang
menguasainya, karena Anda tahu persis dari mana angka 0,140 itu berasal.

## Kenapa dummy TIDAK di-log

Perhatikan `Asing`, `laborIntensive`, `capitalIntensive` — ketiganya tanpa `ln`. Kenapa?

Karena itu **variabel dummy**: isinya hanya 0 atau 1. Tidak ada "naik 1%" untuk sesuatu
yang cuma bisa ya/tidak. Dummy dibaca beda:

> Koefisien `laborIntensive` = perbedaan rata-rata ekspor antara industri labor-intensive
> dibandingkan kelompok pembanding (yaitu resource-based), bukan persentase perubahan.

*(Catatan teknis: karena Y tetap di-log, koefisien dummy dibaca sebagai perbedaan
persentase-log. Untuk dummy dengan koefisien besar, konversi tepatnya adalah
`(e^koef − 1) × 100%`. Untuk koefisien kecil di bawah ±0,2, membacanya langsung sebagai
persen sudah cukup akurat. Sebutkan detail ini bila penguji menanyakan — akan sangat mengesankan.)*

### ✅ Cek pemahaman Modul 2
1. Kenapa semua variabel di-log?
2. Koefisien lnPx = 0,234. Kalau harga ekspor naik 20%, ekspor naik berapa persen?
3. Apakah 0,234 itu elastis atau inelastis? Apa artinya bagi kebijakan?

*(Jawaban nomor 2: 20% × 0,234 = 4,68%)*

---

# MODUL 3 — Angka mana yang boleh dipercaya? (koefisien, SE, t, p-value)

Modul inilah yang membuat Anda bisa **memeriksa pekerjaan Anda sendiri** — dan yang akan
menyelamatkan Anda dari masalah Tabel 4.2.

## Empat kolom yang selalu muncul

Setiap output regresi punya empat kolom yang sama. Ambil satu baris asli dari tesis Anda:

```
lnWPekerja |   .1400161   .0351634     3.98   0.000
              ^koefisien  ^std.error   ^t     ^p-value
```

Mari bedah satu per satu.

### Kolom 1 — Koefisien (0,140): **jawabannya**
Sudah dibahas di Modul 2. Ini elastisitas. Upah naik 1% → ekspor naik 0,140%.

### Kolom 2 — Standard Error (0,035): **seberapa yakin kita**

Ini konsep yang paling sering tidak dipahami, padahal paling penting.

**Analogi menimbang beras.** Anda menimbang sekarung beras dengan timbangan pasar.
Hasilnya 50 kg. Tapi timbangan pasar tidak presisi — kalau ditimbang ulang mungkin
49,8 kg, lalu 50,3 kg, lalu 50,1 kg. **Standard Error adalah ukuran goyangan itu.**

- SE **kecil** → timbangan presisi → estimasi Anda dapat diandalkan
- SE **besar** → timbangan goyang → estimasi Anda meragukan

Kenapa ada goyangan? Karena data Anda hanyalah **sampel** (643 industri-tahun dari periode
tertentu), bukan seluruh kemungkinan kenyataan. Kalau periodenya sedikit berbeda, angkanya
akan sedikit berbeda pula. SE mengukur seberapa besar "sedikit berbeda" itu.

### Kolom 3 — t-statistik (3,98): **sinyal dibagi bising**

Ini rumus terpenting di seluruh tesis Anda. Hafalkan:

```
        koefisien        0,140
t  =  ─────────────  =  ───────  =  3,98
      standard error     0,035
```

**t = sinyal ÷ bising.**

Bayangkan Anda di kafe yang ramai, mencoba mendengar teman bicara.
- Suara teman = **sinyal** (koefisien)
- Keramaian kafe = **bising** (standard error)
- Kalau suara teman jauh lebih keras dari keramaian, Anda yakin dia bicara → **t besar**
- Kalau suaranya setara keramaian, mungkin Anda cuma berhalusinasi → **t kecil**

### Kolom 4 — p-value (0,000): **peluang Anda tertipu keberuntungan**

p-value menjawab pertanyaan spesifik ini:

> "Andaikan upah sesungguhnya **tidak berpengaruh sama sekali** terhadap ekspor
> (koefisien sejatinya nol), berapa peluang saya tetap menemukan angka sebesar 0,140
> ini hanya karena kebetulan?"

p = 0,000 berarti: **peluangnya di bawah 0,1%.** Nyaris mustahil kebetulan.
Kesimpulan: pengaruhnya nyata. Inilah yang disebut **signifikan**.

## Aturan praktis yang wajib Anda hafal

| |t| | p-value | Simbol | Artinya |
|---|---|---|---|
| > 2,58 | < 0,01 | *** | Signifikan pada 1% — sangat kuat |
| > 1,96 | < 0,05 | ** | Signifikan pada 5% — kuat (standar umum) |
| > 1,64 | < 0,10 | * | Signifikan pada 10% — lemah |
| < 1,64 | > 0,10 | (kosong) | **Tidak signifikan** |

**Jalan pintas yang paling berguna: kalau |t| lebih dari 2, biasanya signifikan.**

## ⚠️ Sekarang, kenapa ini menyelamatkan tesis Anda

Karena `t = koefisien ÷ SE`, maka **ketiga angka itu tidak bisa asal-asalan** — mereka
harus konsisten secara matematis. Anda bisa mengeceknya sendiri dengan kalkulator.

Mari cek Tabel 4.2 Anda:

| Variabel | Koef. | SE | Koef ÷ SE | t yang Anda tulis | |
|---|---|---|---|---|---|
| lnRer | 0,096 | 0,1182 | **0,81** | 2,99 | ❌ |
| lnTotPekerja | −0,491 | 0,1321 | **−3,72** | −0,21 | ❌ |
| lnWPekerja | 0,174 | 0,0350 | **4,97** | 2,21 | ❌ |
| lnCapital | 0,0424 | 0,0627 | 0,68 | 0,68 | ✅ |

Tujuh dari sepuluh baris tidak cocok. Sekarang Anda paham **kenapa** itu fatal:
Anda mengklaim `lnRer` signifikan (p = 0,003), padahal dari koefisien dan SE yang Anda
tulis sendiri, t-nya hanya 0,81 — **jauh di bawah 1,64, artinya tidak signifikan sama sekali.**

Seorang penguji yang teliti hanya butuh kalkulator ponsel untuk menemukan ini dalam 30 detik.

**Ini juga alasan saya bersikeras: jangan pernah menyalin angka secara manual.
Tabel harus di-generate langsung dari output.**

## Jebakan p-value yang sering ditanyakan penguji

**"Signifikan" ≠ "besar" ≠ "penting".**

Signifikansi hanya mengatakan: *kami cukup yakin efeknya bukan nol.*
Besarnya efek ada di **koefisien**, bukan di p-value.

Contoh: sebuah koefisien bisa 0,002 dengan p = 0,000 — sangat signifikan secara statistik,
tetapi secara ekonomi nyaris tidak berarti apa-apa.

**Selalu bahas dua hal: signifikansi statistik DAN besaran ekonomi.** Penguji sangat
menyukai mahasiswa yang membedakan keduanya.

### ✅ Cek pemahaman Modul 3
1. Apa arti Standard Error dengan bahasa Anda sendiri?
2. Koefisien = 0,50, SE = 0,10. Berapa t? Signifikan?
3. Apa bedanya "signifikan secara statistik" dan "penting secara ekonomi"?

*(Jawaban 2: t = 5,0 → jauh di atas 2,58 → signifikan pada 1%)*

---

# MODUL 4 — Data panel: kenapa 108 industri × 6 tahun?

## Tiga jenis data

**1. Cross-section — satu foto.**
108 industri, hanya tahun 2012. Anda lihat perbedaan antar industri, tapi tidak tahu apa
yang berubah dari waktu ke waktu.

**2. Time series — satu film tentang satu tokoh.**
Satu industri tekstil, tahun 2007–2012. Anda lihat perubahan waktu, tapi tidak bisa
membandingkan dengan industri lain.

**3. Panel — 108 film sekaligus.** ← *ini data Anda*
108 industri, masing-masing diikuti selama 6 tahun.

```
              2007  2008  2009  2010  2011  2012
Industri 1     ●     ●     ●     ●     ●     ●
Industri 2     ●     ●     ●     ●     ●     ●
Industri 3     ●     ●     ●     ●     ●     ●
   ...
Industri 108   ●     ●     ●     ●     ●     ●

108 × 6 = 648 sel  →  data Anda 643 (5 sel kosong = panel tidak seimbang)
```

Itulah asal angka `Number of obs = 643` dan `Number of groups = 108` di output Stata Anda.
Dan `Obs per group: min = 5, avg = 6.0, max = 6` — artinya ada beberapa industri yang
datanya kurang satu tahun. Ini normal dan namanya **unbalanced panel**.

## Kenapa panel jauh lebih kuat — dan ini kekuatan utama tesis Anda

**Alasan 1: datanya lebih banyak.** 643 observasi jauh lebih informatif daripada 108.

**Alasan 2 (jauh lebih penting): panel bisa menyingkirkan hal-hal yang tidak terukur.**

Setiap industri punya karakter bawaan yang tidak pernah bisa Anda masukkan sebagai variabel:
budaya kerja, kualitas manajemen, jaringan pembeli di luar negeri, teknologi yang mengendap,
reputasi, kedekatan dengan pelabuhan. Anda tidak punya datanya. Tidak akan pernah punya.

Kalau Anda memakai data cross-section, semua faktor tak terukur itu masuk ke error term
dan **mengotori** estimasi Anda.

Panel memberi jalan keluar yang elegan. Itulah Modul 5.

---

# MODUL 5 — Fixed Effects: kenapa dummy sektor Anda hilang?

Modul ini menjelaskan masalah metodologis terbesar di tesis Anda. Pahami betul.

## Intuisinya: bandingkan setiap industri dengan dirinya sendiri

Bayangkan Anda ingin tahu apakah program diet berhasil.

**Cara buruk:** bandingkan berat badan orang yang ikut diet dengan orang yang tidak ikut.
Masalahnya — orang yang ikut diet mungkin memang sudah lebih gemuk sejak awal, atau punya
genetika berbeda, atau pekerjaannya lebih santai. Anda tidak sedang mengukur efek diet;
Anda sedang mengukur campuran diet dan perbedaan bawaan.

**Cara benar:** bandingkan **setiap orang dengan dirinya sendiri**, sebelum dan sesudah diet.
Genetika orang itu tidak berubah. Tinggi badannya tidak berubah. Semua yang bawaan hilang
dengan sendirinya dari perbandingan. Yang tersisa hanyalah efek diet.

**Itulah persis yang dilakukan Fixed Effects.**

> **Fixed Effects tidak membandingkan industri A dengan industri B.
> FE membandingkan industri A tahun ini dengan industri A tahun lalu.**

Semua karakter bawaan tiap industri — budaya, manajemen, lokasi, reputasi — otomatis
tersapu bersih, tanpa Anda perlu mengukurnya. Inilah kenapa FE begitu dihargai
dalam ekonometrika terapan.

## Mekanismenya (sederhana saja)

FE menghitung rata-rata tiap industri selama 6 tahun, lalu mengurangkan rata-rata itu dari
setiap observasi. Yang tersisa hanya **penyimpangan dari rata-rata industri itu sendiri**.

Karena itu FE juga disebut **within estimator** — ia hanya memakai variasi *di dalam*
tiap industri, bukan variasi *antar* industri.

Contoh, industri tekstil:

| Tahun | Upah | Rata-rata 6 tahun | Yang dipakai FE |
|---|---|---|---|
| 2007 | 90 | 100 | −10 |
| 2008 | 95 | 100 | −5 |
| 2009 | 100 | 100 | 0 |
| 2010 | 105 | 100 | +5 |
| 2011 | 110 | 100 | +10 |

FE bertanya: pada tahun ketika upah tekstil **lebih tinggi dari biasanya**, apakah
ekspor tekstil juga **lebih tinggi dari biasanya**?

## 💥 Dan di sinilah masalah tesis Anda muncul

Lihat kembali output Stata Anda:

```
note: laborIntensive omitted because of collinearity
note: capitalIntensive omitted because of collinearity
```

Sekarang Anda pasti bisa menebak alasannya sendiri. Coba pikirkan dulu sebelum membaca lanjut.

...

**Karena klasifikasi sektor tidak pernah berubah.** Industri tekstil adalah labor-intensive
di 2007, dan tetap labor-intensive di 2012. Nilainya 1 sepanjang waktu.

Ketika FE mengurangkan rata-rata industri (yang juga 1), hasilnya **1 − 1 = 0**.
Variabelnya lenyap. Tidak ada yang tersisa untuk diestimasi.

Aturan umumnya:

> **Fixed Effects tidak bisa mengestimasi apa pun yang tidak berubah antarwaktu.**
> Ini bukan kesalahan program. Ini konsekuensi logis dari cara kerja FE.

Hal yang sama berlaku untuk jenis kelamin dalam studi upah individu, atau letak geografis
dalam studi antarnegara — semuanya lenyap di FE.

## Kenapa ini serius bagi tesis Anda

**Tujuan Penelitian #2 Anda** adalah membandingkan kinerja ekspor antar klasifikasi sektor.
Tetapi model utama Anda (FE) **secara struktural tidak bisa menjawab pertanyaan itu**,
karena dummy sektornya menghilang. Sementara BAB IV bagian 4.2.5 dan BAB V tetap menarik
kesimpulan tentang perbedaan antar sektor.

Penguji yang paham FE akan langsung melihat kontradiksi ini.

## ✅ Solusinya justru membuat tesis Anda lebih baik

Kalau **level** sektor tidak bisa diestimasi, estimasi **kemiringannya**. Tambahkan
variabel interaksi:

```
lnW × laborIntensive
lnW × capitalIntensive
```

Efek utama dummy tetap terserap, tapi **interaksinya berubah antarwaktu** (karena `lnW`
berubah tiap tahun), sehingga bisa diestimasi.

Pertanyaan yang dijawab pun berubah menjadi lebih menarik:

- Model lama: "Apakah ekspor sektor labor-intensive lebih tinggi daripada resource-based?"
  → deskriptif, agak dangkal
- Model baru: "**Apakah dampak kenaikan upah terhadap ekspor berbeda antara sektor
  labor-intensive dan sektor lainnya?**" → ini pertanyaan yang jauh lebih tajam,
  dan secara teori jauh lebih relevan

Secara intuisi ekonominya jelas: sektor labor-intensive lebih bergantung pada tenaga kerja,
jadi kenaikan upah semestinya memukul mereka lebih keras. **Itu hipotesis yang bagus,
bisa diuji, dan langsung terhubung ke kebijakan upah minimum.**

Anda mengubah kelemahan metodologis menjadi kontribusi. Ini yang akan saya kerjakan
bersama Anda di tahap re-estimasi.

### ✅ Cek pemahaman Modul 5
1. Jelaskan Fixed Effects dengan analogi diet, pakai kata-kata Anda sendiri.
2. Kenapa dummy sektor hilang di FE?
3. Kenapa variabel interaksi bisa selamat, padahal dummy-nya tidak?

---

# MODUL 6 — Random Effects & uji Hausman

## Kenapa Anda menjalankan tiga regresi?

Anda menjalankan Pooled OLS, Fixed Effects, dan Random Effects. Ini bukan untuk gaya-gayaan —
ada logikanya.

### Pooled OLS — "anggap saja semua sama"
Menumpuk 643 observasi menjadi satu tumpukan, lalu menganggapnya seolah 643 pengamatan
yang tidak berhubungan. Mengabaikan sepenuhnya bahwa observasi tahun 2007–2012 berasal dari
industri yang sama.

*Masalahnya:* karakter bawaan industri diabaikan. Estimasi cenderung bias.
Perhatikan koefisien upah Anda: pooled = 0,376, FE = 0,140. Bedanya hampir tiga kali lipat.
Selisih itu adalah kotoran dari perbedaan bawaan antar industri.

### Fixed Effects — "tiap industri punya karakternya sendiri, dan karakter itu boleh
berhubungan dengan variabel saya"
Sudah dibahas Modul 5. **Paling aman**, tapi harganya: variabel time-invariant hilang.

### Random Effects — "tiap industri punya karakternya sendiri, TAPI karakter itu murni acak
dan tidak berhubungan dengan variabel saya"
RE membuat asumsi tambahan yang lebih longgar. Imbalannya besar: **variabel time-invariant
tetap bisa diestimasi** (lihat output RE Anda — `laborIntensive` dan `capitalIntensive`
muncul dengan angka, tidak omitted!). RE juga lebih efisien (SE lebih kecil).

**Tapi kalau asumsinya salah, hasil RE bias.**

## Uji Hausman: wasit yang memutuskan

Hausman menjawab satu pertanyaan:

> **"Bolehkah saya memakai jalan pintas RE, atau saya harus memakai FE yang lebih aman?"**

Caranya cerdik: bandingkan koefisien FE dan koefisien RE.
- Kalau **mirip** → asumsi RE tampaknya benar → pakai RE (lebih efisien, dapat bonus dummy)
- Kalau **jauh berbeda** → asumsi RE dilanggar → **harus pakai FE**

Lihat hasil Anda:

```
chi2(6) = 35.80
Prob>chi2 = 0.0000
```

Bacanya persis seperti p-value di Modul 3: **p = 0,0000 → tolak hipotesis nol.**
Hipotesis nol Hausman adalah "perbedaan koefisien tidak sistematis" — yaitu "RE boleh dipakai".

**Kesimpulan: RE ditolak. Anda wajib memakai Fixed Effects.**

Lihat sendiri buktinya di tabel Hausman Anda — `lnTotTK` bergerak dari 0,218 (FE)
ke 0,493 (RE), dan `asing` dari 1,353 ke 2,525. Perbedaannya besar sekali.
Wajar Hausman menolak.

**Kalimat siap pakai untuk sidang:**
> "Uji Hausman menghasilkan chi-square sebesar 35,80 dengan probabilitas 0,0000, sehingga
> hipotesis nol ditolak pada tingkat signifikansi 1%. Ini mengindikasikan adanya korelasi
> antara efek individu industri dengan variabel penjelas, sehingga estimator Random Effects
> tidak konsisten. Karena itu model Fixed Effects yang dipilih sebagai model utama."

## Satu catatan jujur

Di output Anda tertulis `(V_b-V_B is not positive definite)`. Ini peringatan teknis
yang lazim muncul. Uji Hausman versi klasik kadang tidak stabil secara numerik.
Solusi standarnya: gunakan **Hausman robust** atau **uji Mundlak** sebagai pembanding.
Akan saya siapkan pada tahap re-estimasi supaya kesimpulan Anda tidak bisa diganggu gugat.

### ✅ Cek pemahaman Modul 6
1. Apa satu asumsi yang membedakan RE dari FE?
2. Apa sebenarnya yang diuji Hausman?
3. Hasil Hausman Anda p = 0,0000. Model mana yang harus dipakai, dan kenapa?

---

# MODUL 7 — Endogenitas: kenapa koefisien upah Anda POSITIF?

Ini pertanyaan yang **hampir pasti** ditanyakan penguji. Siapkan jawabannya sekarang.

## Masalahnya

Hipotesis Anda: upah naik → biaya produksi naik → daya saing turun → **ekspor turun**.
Koefisien seharusnya **negatif**.

Hasil Anda: **+0,140, positif dan signifikan.** Kebalikan dari hipotesis.

Jangan panik. Ini bukan berarti tesis Anda gagal. Ini justru **temuan yang menarik** —
asalkan Anda bisa menjelaskannya. Mahasiswa yang gagal adalah yang tidak bisa menjelaskan.

## Konsep kunci: endogenitas

**Endogenitas** = variabel X Anda "kotor", karena ia berhubungan dengan hal-hal yang tidak
masuk model. Akibatnya, koefisien yang keluar tidak mengukur sebab-akibat murni.

Ada tiga sumber. Semuanya relevan bagi tesis Anda.

### Sumber 1: Kausalitas terbalik (reverse causality) — **ini yang paling kuat**

Anda mengasumsikan: **upah → ekspor**.
Tetapi kenyataannya juga berlaku: **ekspor → upah**.

Industri yang ekspornya sedang bagus punya banyak uang, sehingga membayar pekerjanya lebih
tinggi. Fenomena ini punya nama dalam literatur: **exporter wage premium**, dan Anda
sudah mengutipnya lewat Bernard & Jensen serta Amiti & Davis.

Jadi ketika Anda melihat "upah tinggi berbarengan dengan ekspor tinggi", regresi tidak bisa
membedakan mana yang menyebabkan mana. Ia hanya melihat keduanya bergerak bersama.

**Analogi yang mudah diingat:** Anda mendata kebakaran di sebuah kota, lalu menemukan bahwa
semakin banyak petugas pemadam yang dikirim, semakin besar kerusakannya. Apakah kesimpulannya
petugas pemadam menyebabkan kerusakan? Tentu tidak. Kebakaran besarlah yang memanggil
banyak petugas. **Arah sebab-akibatnya terbalik.**

Upah dan ekspor di tesis Anda persis seperti petugas pemadam dan kerusakan.

### Sumber 2: Variabel penting yang tidak masuk model (omitted variable)

Apa yang membuat suatu industri membayar upah tinggi **sekaligus** mengekspor banyak?
Jawabannya: **produktivitas**.

Industri yang produktif menghasilkan lebih banyak per pekerja. Karena itu ia mampu membayar
upah lebih tinggi, **dan** mampu bersaing di pasar ekspor. Produktivitas mendorong keduanya.

Kalau produktivitas tidak masuk model, koefisien upah akan "menyerap" pengaruh produktivitas
dan menjadi positif secara semu.

*(Catatan: FE Anda sudah menyerap produktivitas yang **konstan** antarwaktu. Yang belum
terkendali adalah produktivitas yang **berubah** antarwaktu. Ini penjelasan bagus untuk
disampaikan di sidang — menunjukkan Anda paham batas kemampuan FE.)*

### Sumber 3: Kesalahan pengukuran

Variabel upah Anda dihitung sebagai **total biaya tenaga kerja ÷ jumlah tenaga kerja**.
Ini bukan murni harga tenaga kerja — ini tercampur **komposisi keterampilan**.

Industri yang mempekerjakan banyak insinyur akan tampak "berupah tinggi", padahal
sebetulnya yang berbeda adalah kualitas tenaga kerjanya, bukan mahalnya tenaga kerja.

## 🎯 Kenapa ini justru peluang emas bagi tesis Anda

Untuk mengukur **daya saing biaya** yang sesungguhnya, ukuran yang tepat bukan upah,
melainkan **Unit Labour Cost (ULC)**:

```
ULC = upah ÷ produktivitas
```

Logikanya jelas: upah naik 10% tapi produktivitas juga naik 10% → biaya per unit output
**tidak berubah** → daya saing tidak terganggu sama sekali. Upah tinggi tidak otomatis
berarti tidak kompetitif.

Dan yang menarik — **Golub & Edwards (2004) yang sudah Anda kutip di BAB II justru memakai
ULC**, bukan upah mentah. Bahan pembelaannya sudah ada di tesis Anda sendiri.

Menambahkan spesifikasi ULC akan sekaligus:
- Menjelaskan koefisien positif Anda secara meyakinkan
- Menunjukkan penguasaan literatur
- Menjawab keberatan penguji **sebelum** diajukan

## Kalimat siap pakai untuk sidang

> "Koefisien upah yang positif dan signifikan tidak menunjukkan bahwa kenaikan upah
> meningkatkan daya saing ekspor. Temuan ini lebih tepat dibaca sebagai indikasi
> **endogenitas**, terutama kausalitas terbalik berupa *exporter wage premium* — industri
> yang berorientasi ekspor cenderung membayar upah lebih tinggi. Selain itu, proksi upah
> yang dihitung dari rata-rata biaya tenaga kerja per pekerja turut menangkap komposisi
> keterampilan, bukan semata harga tenaga kerja. Karena itu penelitian ini juga
> mengestimasi spesifikasi dengan Unit Labour Cost, yang secara teoretis lebih tepat
> merepresentasikan daya saing biaya."

Jawaban seperti ini mengubah sebuah kelemahan menjadi demonstrasi penguasaan.

### ✅ Cek pemahaman Modul 7
1. Jelaskan kausalitas terbalik dengan analogi pemadam kebakaran.
2. Kenapa produktivitas yang hilang bisa membuat koefisien upah jadi positif?
3. Kenapa ULC lebih tepat daripada upah untuk mengukur daya saing?

---

# MODUL 8 — Variabel Instrumen (IV / 2SLS)

## Masalah yang ingin diselesaikan

Modul 7 menunjukkan variabel upah Anda "kotor". Bagaimana membersihkannya?

## Idenya: cari dorongan yang bersih

Anda butuh sesuatu yang **menggerakkan upah**, tetapi **tidak punya jalur lain menuju ekspor**
selain lewat upah. Sesuatu itu disebut **instrumen**.

**Analogi.** Anda ingin tahu apakah minum kopi membuat orang lebih produktif. Anda tidak bisa
sekadar membandingkan peminum kopi dan bukan peminum kopi — orang yang sudah sibuk cenderung
minum lebih banyak kopi (kausalitas terbalik lagi).

Solusinya: cari sesuatu yang memaksa sebagian orang minum lebih banyak kopi, tanpa alasan
yang berkaitan dengan produktivitas mereka. Misalnya **kafe di dekat kantor sedang diskon
besar minggu ini**. Diskon itu mendorong konsumsi kopi, tetapi tidak ada hubungannya dengan
seberapa produktif seseorang. Diskon itulah instrumennya.

## Dua syarat instrumen yang baik

1. **Relevan** — instrumen harus benar-benar menggerakkan X (upah).
   *Bisa diuji:* lihat F-statistik tahap pertama; patokan umum **F > 10**.
2. **Eksogen / valid** — instrumen tidak boleh punya jalur langsung ke Y (ekspor).
   *Ini tidak bisa diuji sepenuhnya* — harus dipertahankan dengan argumen ekonomi yang masuk akal.

## Kenapa disebut 2SLS (Two-Stage Least Squares)

Namanya menjelaskan cara kerjanya — dua tahap regresi:

**Tahap 1:** Regresikan upah pada instrumen.
→ Hasilnya "upah prediksi", yaitu bagian dari upah yang **hanya** dijelaskan oleh instrumen.
Bagian ini bersih dari kausalitas terbalik.

**Tahap 2:** Regresikan ekspor pada **upah prediksi** tadi, bukan pada upah asli.
→ Koefisien yang keluar sekarang mendekati efek kausal murni.

## Instrumen yang saya sarankan untuk tesis Anda

**Upah minimum provinsi, ditimbang menurut sebaran geografis tenaga kerja tiap industri.**

Argumennya kuat:
- **Relevan** — upah minimum jelas mendorong upah aktual di industri padat karya.
- **Eksogen** — upah minimum ditetapkan pemerintah daerah berdasarkan pertimbangan politik,
  inflasi daerah, dan Kebutuhan Hidup Layak — **bukan** berdasarkan prospek ekspor
  industri tertentu.
- **Ada variasi** — tiap provinsi menetapkan angka berbeda tiap tahun, dan tiap industri
  punya sebaran geografis berbeda. Variasi inilah yang dieksploitasi.

## ⚠️ Masalah pada 2SLS Anda saat ini

Perhatikan baris ini di lampiran Anda:

```
ivregress 2sls lnVolume lnPm lnavgWPekerja ... (lnPx = lnGdp lnPxWorld)
```

Yang berada di dalam kurung adalah variabel yang di-instrumen. Anda meng-instrumen **lnPx
(harga ekspor)** — bukan **lnW (upah)**. Padahal upah adalah variabel utama tesis Anda,
dan upahlah yang bermasalah endogenitas.

Tiga masalah lain: sampelnya hanya 105 observasi (bukan 643), variabel terikatnya `lnVolume`
(bukan `lnEkspor`), dan `lnGdp` gugur karena kolinearitas sehingga hanya tersisa satu
instrumen — dengan satu instrumen untuk satu variabel endogen, model *just-identified*
dan **uji over-identifikasi tidak mungkin dilakukan**.

Ini akan kita perbaiki bersama.

### ✅ Cek pemahaman Modul 8
1. Apa dua syarat instrumen yang baik?
2. Kenapa upah minimum provinsi memenuhi kedua syarat itu?
3. Apa yang terjadi di tahap 1 dan tahap 2 pada 2SLS?

---

# MODUL 9 — R² dan uji-uji diagnostik dalam bahasa manusia

## R² (R-squared)

**Artinya:** berapa persen naik-turunnya ekspor yang berhasil dijelaskan oleh model Anda.

R² = 0,55 → model Anda menjelaskan 55% variasi ekspor; 45% sisanya belum terjelaskan.

Di output FE Anda ada tiga jenis R². Ini sering membingungkan, padahal sederhana:

```
R-sq:  within  = 0.1312     ← variasi DI DALAM tiap industri antarwaktu
       between = 0.4187     ← variasi ANTAR industri
       overall = 0.3959     ← gabungan keduanya
```

Untuk model FE, **yang relevan adalah `within`**, karena FE memang hanya memakai variasi
dalam industri. Jangan laporkan `overall` untuk FE — itu kesalahan yang umum.

**Jangan terobsesi pada R².** R² rendah bukan berarti model jelek. Dalam data ekonomi mikro,
R² within sekitar 0,13 itu wajar — perilaku ekspor dipengaruhi ribuan hal yang tidak mungkin
diukur semua. Yang jauh lebih penting adalah apakah **koefisien variabel utama Anda masuk
akal dan teridentifikasi dengan baik**.

## rho = 0,934 — angka yang menarik di output Anda

```
sigma_u |  1.7029205    ← keragaman ANTAR industri
sigma_e |  .45227797    ← keragaman DALAM industri antarwaktu
rho     |  .93410991    ← 93,4% variasi berasal dari perbedaan antar industri
```

**Artinya: 93,4% dari keragaman ekspor berasal dari perbedaan bawaan antar industri,
hanya 6,6% dari perubahan antarwaktu.**

Ini adalah **bukti kuat yang mendukung pilihan Fixed Effects Anda**. Efek individu industri
sangat dominan — mengabaikannya (seperti pada Pooled OLS) akan sangat menyesatkan.
Sebutkan angka ini di sidang; ia memperkuat argumen metodologi Anda secara meyakinkan.

## Empat uji diagnostik yang wajib ada

Anggap ini seperti servis mobil sebelum perjalanan jauh: memastikan tidak ada yang rusak
di bagian yang tidak terlihat.

### 1. Heteroskedastisitas
**Pertanyaan:** apakah besarnya error konsisten di seluruh data?

*Masalahnya:* industri raksasa punya error besar, industri kecil punya error kecil. Kalau
begitu, standard error Anda salah hitung → t dan p-value ikut salah → kesimpulan signifikansi
bisa keliru.

**Uji:** Modified Wald test (`xttest3` di Stata).
**Solusi:** gunakan **robust standard errors** atau **cluster-robust** di level industri.
Solusinya mudah, dan hampir selalu perlu dilakukan.

### 2. Autokorelasi
**Pertanyaan:** apakah error tahun ini berhubungan dengan error tahun lalu?

*Masalahnya:* dalam data panel hampir selalu ada. Industri yang tahun ini di atas prediksi,
tahun depan cenderung tetap di atas prediksi.

**Uji:** Wooldridge test (`xtserial`).
**Solusi:** cluster-robust standard errors — sekaligus menangani masalah nomor 1.

### 3. Multikolinearitas
**Pertanyaan:** apakah ada dua variabel bebas yang terlalu mirip satu sama lain?

*Masalahnya:* kalau dua variabel bergerak nyaris bersamaan, regresi tidak bisa memisahkan
kontribusi masing-masing. Akibatnya SE membengkak dan koefisien jadi tidak stabil.

**Uji:** VIF (`vif` setelah regresi). Patokan: **VIF > 10 = bermasalah**.

*Perhatikan tesis Anda:* dari matriks korelasi di lampiran, `lnAsing` vs `lnavgWPekerja`
= 0,48 dan `capitalIntensive` vs `lnAsing` = 0,49. Belum berbahaya, tapi wajib dilaporkan.

### 4. Cross-sectional dependence
**Pertanyaan:** apakah industri-industri terguncang oleh hal yang sama pada saat bersamaan?

*Masalahnya:* krisis global 2008 memukul semua industri sekaligus. Ini membuat error
antarindustri saling berkorelasi.

**Uji:** Pesaran CD test.
**Solusi:** tambahkan **time dummies** (dummy tahun) ke dalam model. Ini sekaligus
mengendalikan guncangan makro seperti krisis 2008 — sangat relevan untuk periode data
2007–2012 Anda. **Saya sangat menyarankan ini.**

---

# BAGIAN PENUTUP — Simulasi pertanyaan penguji

Latih jawaban Anda dengan suara keras. Bukan dihafal kata per kata — pahami logikanya,
lalu ucapkan dengan bahasa Anda sendiri.

**T: Coba jelaskan, apa arti koefisien 0,140 itu?**
> Itu elastisitas. Kalau upah tenaga kerja naik 1%, nilai ekspor naik 0,140%. Karena nilainya
> di bawah satu, responsnya inelastis — artinya upah berpengaruh, tapi bukan penentu tunggal
> daya saing ekspor.

**T: Kenapa Anda pakai Fixed Effects, bukan Random Effects?**
> Berdasarkan uji Hausman dengan chi-square 35,80 dan probabilitas 0,0000, hipotesis nol
> ditolak. Artinya ada korelasi antara efek individu industri dengan variabel penjelas,
> sehingga Random Effects tidak konsisten. Selain itu nilai rho sebesar 0,934 menunjukkan
> 93,4% variasi berasal dari perbedaan antar industri, sehingga efek individu memang harus
> dikendalikan.

**T: Kenapa dummy sektor Anda hilang?**
> Karena klasifikasi sektor bersifat time-invariant — tidak berubah selama periode penelitian.
> Fixed Effects bekerja dengan mengurangkan rata-rata individu, sehingga variabel yang konstan
> antarwaktu otomatis terserap. Untuk tetap menjawab tujuan penelitian kedua, saya menggunakan
> variabel interaksi antara upah dan klasifikasi sektor, yang memungkinkan saya menguji apakah
> dampak upah berbeda antar sektor.

**T: Kenapa koefisien upah Anda positif, bukankah itu berlawanan dengan teori?**
> Betul, dan itu justru temuan yang menarik. Penjelasan utamanya adalah endogenitas berupa
> kausalitas terbalik — industri berorientasi ekspor cenderung membayar upah lebih tinggi,
> fenomena yang dikenal sebagai exporter wage premium. Selain itu proksi upah saya turut
> menangkap komposisi keterampilan tenaga kerja. Karena itu saya juga mengestimasi
> spesifikasi Unit Labour Cost yang secara teoretis lebih tepat mengukur daya saing biaya.

**T: Apa keterbatasan penelitian Anda?**
> Ada tiga. Pertama, identifikasi kausal masih terbatas karena instrumen untuk upah belum
> sepenuhnya kuat. Kedua, periode enam tahun relatif pendek untuk metode dinamis. Ketiga,
> analisis dilakukan pada level industri, sehingga heterogenitas antar perusahaan di dalam
> industri tidak tertangkap.

**T: R² Anda hanya 0,13, bukankah itu rendah?**
> Itu R² within, yang memang relevan untuk model Fixed Effects. Nilai tersebut wajar untuk
> data mikro industri, karena FE hanya memakai variasi di dalam industri antarwaktu. Fokus
> penelitian ini bukan pada daya prediksi model, melainkan pada identifikasi hubungan antara
> upah dan kinerja ekspor. R² between sebesar 0,42 menunjukkan model menjelaskan perbedaan
> antar industri dengan cukup baik.

---

# LEMBAR CONTEKAN — satu halaman

| Istilah | Artinya dalam satu kalimat |
|---|---|
| **Koefisien** | Kalau X naik 1%, Y berubah berapa % (karena semua di-log) |
| **Standard Error** | Ukuran goyangan estimasi — kecil berarti presisi |
| **t-statistik** | Sinyal ÷ bising. **t = koef ÷ SE**. Lebih dari 2 biasanya signifikan |
| **p-value** | Peluang hasil ini muncul kebetulan padahal efeknya nol. < 0,05 = signifikan |
| **Elastis** | Koefisien > 1, respons besar |
| **Inelastis** | Koefisien < 1, respons teredam |
| **Data panel** | Banyak unit diikuti sepanjang beberapa tahun |
| **Fixed Effects** | Bandingkan tiap industri dengan dirinya sendiri antarwaktu |
| **Random Effects** | Sama, tapi asumsikan karakter industri tidak berkorelasi dengan X |
| **Uji Hausman** | Wasit FE vs RE. p < 0,05 → wajib FE |
| **Time-invariant** | Tidak berubah antarwaktu → pasti hilang di FE |
| **Endogenitas** | Variabel X kotor, sehingga koefisien bukan sebab-akibat murni |
| **Kausalitas terbalik** | Sebenarnya Y yang menyebabkan X, bukan sebaliknya |
| **Instrumen** | Pendorong X yang tidak punya jalur lain ke Y |
| **2SLS** | Tahap 1 bersihkan X, tahap 2 pakai X yang sudah bersih |
| **Heteroskedastisitas** | Besar error tidak konsisten → SE salah → pakai robust SE |
| **Autokorelasi** | Error tahun ini berkaitan dengan tahun lalu |
| **Multikolinearitas** | Dua variabel terlalu mirip → VIF > 10 bermasalah |
| **R² within** | R² yang benar untuk dilaporkan pada model FE |
| **rho** | Proporsi variasi yang berasal dari perbedaan antar individu |
| **ULC** | Upah ÷ produktivitas — ukuran daya saing biaya yang sesungguhnya |

---

## Rumus yang wajib hafal

```
                 koefisien
    t  =  ─────────────────────          |t| > 2  →  biasanya signifikan
            standard error
```

Satu rumus itu saja. Sisanya adalah cara berpikir.
