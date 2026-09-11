# OUTPUT STATA ASLI — SUMBER TUNGGAL UNTUK REGENERASI TABEL

**Tanggal:** 11 September 2026
**Sumber:** `komparasi hasil regresi.docx` (24 Feb 2016) dan `test asumsi.docx` (24 Jan 2016),
folder Drive `bahan tesis` → `ketikan tesis`
**Status:** salinan verbatim, sudah diverifikasi secara aritmetik

> **Aturan kerja:** seluruh tabel di naskah harus bersumber dari dokumen ini atau dari
> estimasi ulang, tidak pernah diketik manual dari ingatan. Inilah cara Tabel 4.2 rusak.

---

## VERIFIKASI ARITMETIK

Saya menghitung ulang `t = koefisien ÷ standard error` untuk **48 baris** di seluruh
regresi di bawah ini, mencakup lima spesifikasi utama.

**Hasil: 48 dari 48 cocok.** Tidak ada satu pun ketidaksesuaian.

Bandingkan dengan Tabel 4.2 di naskah, yang tujuh dari sepuluh barisnya tidak cocok.
Kesimpulannya tegas dan melegakan: **output Stata Anda bersih.** Kerusakan terjadi
sepenuhnya pada saat pengetikan ulang ke dalam naskah.

---

## DAFTAR SPESIFIKASI YANG TERSEDIA

| # | Spesifikasi | Var. terikat | N | Grup | Sumber |
|---|---|---|---|---|---|
| 1 | OLS cross-section 2012 | lnEkspor | 88 | — | komparasi |
| 2 | Pooled OLS panel | lnVolume | 623 | — | komparasi |
| 3 | **FE cluster-robust** | lnVolume | 623 | 105 | komparasi |
| 4 | Random effects | lnVolume | 623 | 105 | komparasi |
| 5 | 2SLS (instrumen lnPx) | lnVolume | 100 | — | komparasi |
| 6 | OLS pembanding 2SLS | lnVolume | 100 | — | komparasi |
| 7 | OLS dekomposisi asing | lnVolume | 50 | — | komparasi |
| 8 | OLS robust | lnEkspor | 105 | — | test asumsi |
| 9 | OLS | lnVolume | 105 | — | test asumsi |
| 10 | OLS upah dipisah | lnVolume | 105 | — | test asumsi |
| 11 | OLS dekomposisi asing (10 var) | lnVolume | 50 | — | test asumsi |

Ditambah uji: matriks korelasi (N=105), VIF, dan Breusch-Pagan/Cook-Weisberg.

---

## 1. OLS CROSS-SECTION 2012 — `lnEkspor`, N = 88

```
reg lnEkspor lnPx lnPm lnWTotProd lnWTotPlain Pd lnTotProd lnTotPlain ///
    lnCapital asing laborIntensive capitalIntensive

Number of obs =      88        F( 11,    76) =    4.89
Prob > F      =  0.0000        R-squared     =  0.4146
Adj R-squared =  0.3298        Root MSE      =  1.1606

lnEkspor         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |   .1754241   .0775793     2.26   0.027
lnPm             |   .0047371   .0540093     0.09   0.930
lnWTotProd       |   .1317629   .2726465     0.48   0.630
lnWTotPlain      |    .288121   .2976389     0.97   0.336
Pd               |  -.0258222   .0263172    -0.98   0.330
lnTotProd        |   .7697409   .3600977     2.14   0.036
lnTotPlain       |   -.304098    .366592    -0.83   0.409
lnCapital        |   .0634836    .096405     0.66   0.512
asing            |   2.373266   1.396228     1.70   0.093
laborIntensive   |  -.4438214    .408452    -1.09   0.281
capitalIntensive |  -.9648887   .3780738    -2.55   0.013
_cons            |   18.49414   3.489921     5.30   0.000
```

> **INILAH SUMBER STATISTIK TABEL 4.2.** `F = 4,89` dan `R² = 0,4146` cocok persis, dan
> jumlah regresor sama-sama 11. Derajat bebas penyebut yang benar adalah 88 − 11 − 1 = **76**;
> naskah menulis **107**. Sebuah regresi cross-section satu tahun dilaporkan sebagai hasil
> panel 2007–2012. Ini temuan paling berbahaya di meja sidang.

---

## 2. POOLED OLS PANEL — `lnVolume`, N = 623

```
reg lnVolume lnPx lnPm lnWTotProd lnWTotPlain lnTotProd lnTotPlain ///
    lnCapital asing laborIntensive capitalIntensive

Number of obs =     623        F( 10,   612) =   89.91
Prob > F      =  0.0000        R-squared     =  0.5950
Adj R-squared =  0.5884        Root MSE      =  1.3671

lnVolume         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |  -.5771609   .0332002   -17.38   0.000
lnPm             |  -.0276682   .0169949    -1.63   0.104
lnWTotProd       |   .1748921   .0718641     2.43   0.015
lnWTotPlain      |   .0456556   .0930535     0.49   0.624
lnTotProd        |  -.0072814   .0869084    -0.08   0.933
lnTotPlain       |   .5991548   .1121307     5.34   0.000
lnCapital        |   .0571087   .0440181     1.30   0.195
asing            |   3.131901   .5265358     5.95   0.000
laborIntensive   |   .2754575   .1652405     1.67   0.096
capitalIntensive |  -.0781124   .1518984    -0.51   0.607
_cons            |   5.445793   .6756874     8.06   0.000
```

> `lnWTotProd = 0,1749` — angka inilah yang muncul di Tabel 4.2 sebagai `lnWPekerja = 0,174`.
> Berasal dari regresi yang **berbeda lagi** dari sumber statistik modelnya. Tabel 4.2
> terbukti merupakan gabungan sedikitnya tiga regresi.

---

## 3. FIXED EFFECTS CLUSTER-ROBUST — `lnVolume`, N = 623, 105 industri

**Spesifikasi paling kredibel di seluruh berkas.**

```
xtreg lnVolume lnPx lnPm lnWTotProd lnWTotPlain lnTotProd lnTotPlain ///
      lnCapital asing laborIntensive capitalIntensive, fe ro

note: laborIntensive omitted because of collinearity
note: capitalIntensive omitted because of collinearity

Fixed-effects (within) regression      Number of obs      =       623
Group variable: isic3                  Number of groups   =       105
R-sq:  within  = 0.1980                Obs per group: min =         3
       between = 0.3711                               avg =       5.9
       overall = 0.3604                               max =         6
                                       F(8,104)           =      1.72
corr(u_i, Xb)  = 0.2342                Prob > F           =    0.1026

(Std. Err. adjusted for 105 clusters in isic3)

                 |             Robust
lnVolume         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |  -.4347619   .2569842    -1.69   0.094
lnPm             |  -.0229101   .0121482    -1.89   0.062
lnWTotProd       |   .0264388    .021861     1.21   0.229
lnWTotPlain      |  -.0008355   .0251332    -0.03   0.974
lnTotProd        |   .0064099   .0388974     0.16   0.869
lnTotPlain       |   .0367968   .0470078     0.78   0.436
lnCapital        |  -.0127703   .0167899    -0.76   0.449
asing            |  -.3792002   .2804264    -1.35   0.179
laborIntensive   |          0  (omitted)
capitalIntensive |          0  (omitted)
_cons            |   13.52078   .6831427    19.79   0.000
-----------------+--------------------------------------
sigma_u          |  1.7361735
sigma_e          |  .43127177
rho              |  .94188179   (fraction of variance due to u_i)
```

**Tiga hal yang harus dibaca dari output ini:**

1. **Upah tidak signifikan.** Baik upah produksi (p = 0,229) maupun non-produksi (p = 0,974).
   Ini membalik kesimpulan yang tertulis di naskah.
2. **rho = 0,942.** 94,2% variasi berasal dari perbedaan permanen antar industri. Cerita
   substantif tesis ini ada di dimensi antar-industri, bukan antarwaktu — dan FE justru
   membuang dimensi itu. Inilah pembenaran metodologis mengapa BAB IV deskriptif harus kaya.
3. **F(8,104) = 1,72; Prob > F = 0,1026** — model secara keseluruhan tidak signifikan pada 5%.
   Harus dibahas terbuka, bukan disembunyikan. Penjelasan yang jujur dan masuk akal: variasi
   *within* hanya sekitar 6% dari total, sehingga enam tahun terlalu pendek untuk
   mengidentifikasi efek upah. Keterbatasan itu sendiri adalah temuan yang layak dilaporkan.

Catatan: kedua dummy sektor ter-drop karena time-invariant. Tujuan Penelitian #2 karena itu
tidak dapat dijawab oleh model ini — jawabannya harus melalui interaksi upah × sektor dan
melalui analisis deskriptif.

---

## 4. RANDOM EFFECTS — `lnVolume`, N = 623, 105 industri

```
xtreg lnVolume lnPx lnPm lnWTotProd lnWTotPlain lnTotProd lnTotPlain ///
      lnCapital asing laborIntensive capitalIntensive, re

Number of obs = 623      Number of groups = 105
R-sq:  within = 0.1878   between = 0.4448   overall = 0.4287
Wald chi2(10) = 219.80   Prob > chi2 = 0.0000

lnVolume         |      Coef.   Std. Err.      z    P>|z|
-----------------+--------------------------------------
lnPx             |   -.473591   .0373192   -12.69   0.000
lnPm             |  -.0239666   .0072727    -3.30   0.001
lnWTotProd       |   .0234169   .0284796     0.82   0.411
lnWTotPlain      |  -.0037901    .037313    -0.10   0.919
lnTotProd        |  -.0023699   .0372115    -0.06   0.949
lnTotPlain       |   .1467755   .0619361     2.37   0.018
lnCapital        |  -.0128304   .0190877    -0.67   0.501
asing            |  -.1395046    .353462    -0.39   0.693
laborIntensive   |  -.4568326   .3537942    -1.29   0.197
capitalIntensive |  -.7397005   .3085591    -2.40   0.017
_cons            |   12.99714   .4569859    28.44   0.000
-----------------+--------------------------------------
sigma_u          |  1.2167102
sigma_e          |  .43127177
rho              |  .88838353
```

> Upah tetap tidak signifikan di RE (p = 0,411 dan 0,919). Kesimpulan "upah tidak berpengaruh"
> karena itu **kokoh terhadap pilihan estimator** — bukan artefak fixed effects. Ini poin
> pertahanan yang kuat di sidang.

---

## 5. 2SLS — `lnVolume` diinstrumen `lnPx`, N = 100

```
ivregress 2sls lnVolume (lnPx = lnPxWorld lnGdp lnPx_1) lnPm lnAvgWProd ///
          lnAvgWPlain lnTotTK lnCapital lnAsing laborIntensive capitalIntensive

note: lnGdp omitted because of collinearity

Number of obs = 100      Wald chi2(9) = 147.97
Prob > chi2 = 0.0000     R-squared = 0.5904     Root MSE = 1.2677

lnVolume         |      Coef.   Std. Err.      z    P>|z|
-----------------+--------------------------------------
lnPx             |  -.2598802   .0898666    -2.89   0.004
lnPm             |   .0663174    .039052     1.70   0.089
lnAvgWProd       |  -.0997223   .4416864    -0.23   0.821
lnAvgWPlain      |   .1180165   .4324608     0.27   0.785
lnTotTK          |   .5458313   .1526288     3.58   0.000
lnCapital        |    .238466   .0931863     2.56   0.010
lnAsing          |   .4117241   .1682607     2.45   0.014
laborIntensive   |  -.8100707   .4214221    -1.92   0.055
capitalIntensive |  -.5341407   .3685076    -1.45   0.147
_cons            |   9.271376    4.74987     1.95   0.051

Instrumented:  lnPx
Instruments:   lnPm lnAvgWProd lnAvgWPlain lnTotTK lnCapital lnAsing
               laborIntensive capitalIntensive lnPxWorld lnPx_1
```

**Upah tetap tidak signifikan juga di sini** (p = 0,821 dan 0,785). Tiga estimator, satu
kesimpulan yang sama.

Yang perlu diperbaiki pada 2SLS ini: `lnGdp` gugur karena kolinearitas sehingga tersisa dua
instrumen untuk satu regresor endogen — over-identifikasi minimal dan belum pernah diuji.
Belum ada uji kekuatan instrumen (first-stage F / Cragg-Donald) maupun uji Sargan-Hansen.
Sampelnya juga hanya 100, bukan 623.

---

## 6. OLS PEMBANDING 2SLS — `lnVolume`, N = 100

```
reg lnVolume lnPx lnPm lnavgWPekerja lnTotTK lnCapital lnAsing ///
    laborIntensive capitalIntensive

Number of obs = 100    F( 8, 91) = 16.55    Prob > F = 0.0000
R-squared = 0.5926     Adj R-squared = 0.5568     Root MSE = 1.3254

lnVolume         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |  -.1927321   .0890756    -2.16   0.033
lnPm             |   .0676693   .0408409     1.66   0.101
lnavgWPekerja    |   .0317212   .3907575     0.08   0.935
lnTotTK          |   .5287484   .1585607     3.33   0.001
lnCapital        |   .2560294   .0974947     2.63   0.010
lnAsing          |   .3702774   .1746292     2.12   0.037
laborIntensive   |  -.9087475   .4412149    -2.06   0.042
capitalIntensive |  -.6009611   .3831295    -1.57   0.120
_cons            |   8.335457   4.809215     1.73   0.086
```

> Perbandingan langsung OLS vs 2SLS pada sampel yang sama: koefisien `lnPx` bergerak dari
> −0,193 ke −0,260 setelah instrumentasi. Tabel berdampingan OLS/2SLS ini layak masuk naskah
> sebagai bukti bahwa endogenitas harga ditangani, bukan diabaikan.

---

## 7. OLS DEKOMPOSISI KEPEMILIKAN ASING — `lnVolume`, N = 50

```
reg lnVolume lnPx lnPm lnavgWPekerja lnTotTK lnCapital ///
    lnAsing lnDominanAsing lnMajoritasAsing lnMinoritasAsing

Number of obs = 50     F( 9, 40) = 4.48     Prob > F = 0.0004
R-squared = 0.5022     Adj R-squared = 0.3902     Root MSE = 1.4462

lnVolume         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |  -.1405694   .1315003    -1.07   0.291
lnPm             |   .1198776   .0612915     1.96   0.057
lnavgWPekerja    |  -.0408193     .62117    -0.07   0.948
lnTotTK          |   .6341818   .3097577     2.05   0.047
lnCapital        |   .3132158   .1656814     1.89   0.066
lnAsing          |  -.1504049   2.146709    -0.07   0.944
lnDominanAsing   |  -.2926022   1.260361    -0.23   0.818
lnMajoritasAsing |   .1629987   .6515781     0.25   0.804
lnMinoritasAsing |   .4756106   .4805222     0.99   0.328
_cons            |   7.191102   7.400436     0.97   0.337
```

> N = 50 dengan 9 regresor; `lnAsing` punya SE 2,15 — pertanda kolinearitas berat dengan
> ketiga variabel turunannya. Sebaiknya **tidak** dijadikan hasil utama; paling jauh
> disebut sebagai eksplorasi yang tidak konklusif karena keterbatasan sampel.

---

## 8. OLS ROBUST — `lnEkspor`, N = 105 (`test asumsi.docx`)

```
reg lnEkspor lnPx lnPm lnavgWPekerja lnTotTK lnAsing ///
    laborIntensive capitalIntensive, robust

Number of obs = 105    F( 7, 97) = 21.18    Prob > F = 0.0000
R-squared = 0.5773     Root MSE = 1.2336

                 |             Robust
lnEkspor         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |   .1709589   .0768276     2.23   0.028
lnPm             |   .0796695   .0475829     1.67   0.097
lnavgWPekerja    |  -.0036912   .3614143    -0.01   0.992
lnTotTK          |   .9354539   .1090634     8.58   0.000
lnAsing          |    .775872   .1275552     6.08   0.000
laborIntensive   |  -.2446284   .3364004    -0.73   0.469
capitalIntensive |  -.4264454   .3538955    -1.21   0.231
_cons            |   13.05748   4.626362     2.82   0.006
```

---

## 9. OLS — `lnVolume`, N = 105 (`test asumsi.docx`)

```
reg lnVolume lnPx lnPm lnavgWPekerja lnTotTK lnAsing ///
    laborIntensive capitalIntensive

Number of obs = 105    F( 7, 97) = 18.48    Prob > F = 0.0000
R-squared = 0.5715     Adj R-squared = 0.5406     Root MSE = 1.4612

lnVolume         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |  -.3527208   .0883284    -3.99   0.000
lnPm             |   .0748192   .0573102     1.31   0.195
lnavgWPekerja    |   .2143366    .413353     0.52   0.605
lnTotTK          |   .9959661   .1179865     8.44   0.000
lnAsing          |   .6165649   .1765676     3.49   0.001
laborIntensive   |  -.4549791   .4552644    -1.00   0.320
capitalIntensive |  -.5965204   .3936745    -1.52   0.133
_cons            |   8.950488   5.464793     1.64   0.105
```

> **Pasangan nomor 8 dan 9 adalah bukti terbersih dari masalah variabel terikat.** Regresor
> identik, sampel identik (N = 105), hanya ruas kirinya berbeda. `lnPx` berubah dari
> **+0,171 (t = 2,23, signifikan)** menjadi **−0,353 (t = −3,99, signifikan)**.
>
> Tanda berbalik total dan keduanya signifikan. Penyebabnya mekanis: nilai ekspor =
> harga × kuantitas, sehingga menaruh nilai di ruas kiri dan harga di ruas kanan membuat
> harga muncul di kedua sisi persamaan. Kerangka penawaran Riveros (Qx^s) menuntut
> **kuantitas** sebagai variabel terikat. Kedua regresi ini layak disajikan berdampingan
> di naskah sebagai justifikasi pemilihan `lnVolume`.

---

## 10. OLS UPAH DIPISAH — `lnVolume`, N = 105 (`test asumsi.docx`)

```
reg lnVolume lnPx lnPm lnavgWProd lnavgWPlain lnTotTK ///
    lnAsing laborIntensive capitalIntensive

Number of obs = 105    F( 8, 96) = 16.44    Prob > F = 0.0000
R-squared = 0.5780     Adj R-squared = 0.5429     Root MSE = 1.4576

lnVolume         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |   -.333974   .0894488    -3.73   0.000
lnPm             |   .0763081   .0571848     1.33   0.185
lnavgWProd       |   .5340948   .4514793     1.18   0.240
lnavgWPlain      |  -.4674366   .4175746    -1.12   0.266
lnTotTK          |   .9950752   .1181141     8.42   0.000
lnAsing          |   .6311298   .1751242     3.60   0.000
laborIntensive   |  -.4695163   .4478698    -1.05   0.297
capitalIntensive |  -.6380084   .3946009    -1.62   0.109
_cons            |   11.03259   5.626539     1.96   0.053
```

> Menjawab arahan pembimbing untuk memisahkan upah produksi dan non-produksi. Pola tandanya
> menarik meski tidak signifikan: upah produksi positif (+0,53), upah non-produksi negatif
> (−0,47). Layak dibahas sebagai indikasi awal, dengan kejujuran bahwa keduanya tidak signifikan.

---

## 11. OLS DEKOMPOSISI ASING (10 regresor) — `lnVolume`, N = 50 (`test asumsi.docx`)

```
reg lnVolume lnPx lnPm lnavgWPekerja lnTotTK lnCapital ///
    lnDominanAsing lnMajoritasAsing lnMinoritasAsing laborIntensive capitalIntensive

Number of obs = 50     F( 10, 39) = 4.01    Prob > F = 0.0008
R-squared = 0.5068     Adj R-squared = 0.3804     Root MSE = 1.4579

lnVolume         |      Coef.   Std. Err.      t    P>|t|
-----------------+--------------------------------------
lnPx             |  -.1213867   .1360146    -0.89   0.378
lnPm             |   .1086142   .0652893     1.66   0.104
lnavgWPekerja    |   .0788637   .6210337     0.13   0.900
lnTotTK          |   .6181991   .3050836     2.03   0.050
lnCapital        |   .3164016   .1672052     1.89   0.066
lnDominanAsing   |  -.3907446   .3578469    -1.09   0.282
lnMajoritasAsing |   .1416758   .3539147     0.40   0.691
lnMinoritasAsing |    .475684   .3497579     1.36   0.182
laborIntensive   |   .2071412   .6778789     0.31   0.762
capitalIntensive |  -.2530009   .5894353    -0.43   0.670
_cons            |   4.481905   7.443345     0.60   0.551
```

---

## UJI ASUMSI

### Matriks korelasi (obs = 105)

```
               | lnEkspor    lnPx     lnPm  lnavgW~a  lnTotTK  lnAsing  laborI~e  capita~e
---------------+--------------------------------------------------------------------------
lnEkspor       |   1.0000
lnPx           |   0.1734   1.0000
lnPm           |   0.1110  -0.0999   1.0000
lnavgWPekerja  |   0.1652   0.0207  -0.0055    1.0000
lnTotTK        |   0.5633  -0.1866  -0.0087   -0.0647   1.0000
lnAsing        |   0.2814   0.3860   0.0436    0.4834  -0.3023   1.0000
laborIntensive |   0.0779   0.1245   0.0836   -0.4152   0.1881  -0.1838    1.0000
capitalIntens~ |  -0.1137   0.3176  -0.0710    0.3351  -0.4230   0.4851   -0.4537    1.0000
```

Korelasi tertinggi: `lnAsing`–`lnavgWPekerja` = 0,483 dan `capitalIntensive`–`lnAsing` = 0,485.
Cukup tinggi untuk disebutkan, tetapi tidak mengkhawatirkan — dikonfirmasi oleh VIF di bawah.

### Multikolinearitas (VIF)

```
Variable         |       VIF       1/VIF
-----------------+----------------------
capitalIntensive |      1.90    0.527147
lnAsing          |      1.84    0.542876
lnavgWPekerja    |      1.59    0.627277
laborIntensive   |      1.57    0.636231
lnPx             |      1.39    0.718151
lnTotTK          |      1.27    0.786437
lnPm             |      1.04    0.964523
-----------------+----------------------
Mean VIF         |      1.52
```

**Aman.** Maksimum 1,90, jauh di bawah ambang lazim 10. Multikolinearitas bukan masalah
pada tesis ini, dan itu dapat dinyatakan dengan percaya diri.

### Heteroskedastisitas

```
Breusch-Pagan / Cook-Weisberg test for heteroskedasticity
Ho: Constant variance
Variables: fitted values of lnEkspor

chi2(1)      =     5.04
Prob > chi2  =   0.0248
```

**Terdeteksi heteroskedastisitas** pada taraf 5%. Ini justru pembenaran empiris untuk memakai
cluster-robust standard error di model utama — jadi bukan kelemahan, melainkan alasan yang
bisa dikutip untuk pilihan metode.

### Catatan penamaan di berkas asli

Judul di `test asumsi.docx` tertulis "test autokorelasi" tetapi isinya perintah `vif`
(multikolinearitas). **Uji autokorelasi sesungguhnya belum pernah dijalankan.**

---

## YANG MASIH HARUS DIJALANKAN

| Uji / spesifikasi | Status |
|---|---|
| Uji Hausman FE vs RE | Disebut di lampiran naskah (χ²(6) = 35,80; p = 0,0000), tidak ada di dua berkas ini |
| Uji autokorelasi Wooldridge | **Belum** |
| Uji cross-sectional dependence (Pesaran CD) | **Belum** |
| Uji kekuatan instrumen 2SLS (first-stage F) | **Belum** |
| Uji over-identifikasi (Sargan-Hansen) | **Belum** — dan hanya mungkin bila instrumen ≥ 2 |
| FE + interaksi upah × sektor | **Belum** — kunci untuk Tujuan Penelitian #2 |
| FE + dummy tahun | **Belum** — untuk mengendalikan krisis 2008–2009 |
| Spesifikasi Unit Labour Cost | **Belum** |
| Statistik deskriptif lengkap | **Belum** — lihat `03_SPEK_BAB_IV_DESKRIPTIF.md` |

Seluruhnya membutuhkan file `.dta`, yang sampai sekarang belum ditemukan.

---

## DUA VERSI DATASET — HARUS DIPUTUSKAN

| Panel | N | Grup | Muncul di |
|---|---|---|---|
| A | 623 | 105 | `komparasi hasil regresi.docx` (FE, RE, pooled) |
| B | 643 | 108 | lampiran `rev4b.docx` |

Sub-sampel lain yang beredar: 50, 88, 100, 105.

Panel A didukung output lengkap dan konsisten untuk tiga estimator sekaligus. Selama file
`.dta` belum ditemukan, **Panel A (N = 623, 105 industri) adalah kandidat dataset master
yang paling dapat dipertanggungjawabkan**, dan satu-satunya angka N yang boleh muncul di
naskah sampai ada keputusan lain.
