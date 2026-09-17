"""
Ekstraksi harga produsen domestik (Pd) dari publikasi BPS
"Statistik Industri Manufaktur - Produksi 2012" (Katalog 6103014, Buku III).

Menghasilkan data/Pd_2012_KBLI5.csv berisi harga per kilogram tingkat KBLI 5 digit,
lengkap dengan dua kolom diagnostik kualitas:
  - cakupan_nilai_terbit : nilai barang yang terbit / total produksi KBLI
                           (< 1 karena BPS menyensor sebagian jenis barang dengan '*')
  - pangsa_item_kg       : porsi nilai yang berasal dari barang bersatuan KG

Saring dengan cakupan >= 0,70 dan pangsa_item_kg >= 0,50 sebelum dipakai dalam regresi.

Jalankan:  pdftotext -layout <publikasi>.pdf prod.txt  lalu  python3 extract_pd.py prod.txt
"""
import re, csv, sys, collections, statistics as st

SRC = sys.argv[1] if len(sys.argv) > 1 else "prod.txt"
OUT = sys.argv[2] if len(sys.argv) > 2 else "Pd_2012_KBLI5.csv"
NOISE = re.compile(r'^[ht tps:/w.bgoid]+$')

kbli, items, totals = None, [], {}
for page in open(SRC, encoding='utf-8', errors='replace').read().split('\f'):
    for line in page.split('\n'):
        t = line.strip()
        if not t or NOISE.fullmatch(t):
            continue
        m = re.match(r'^(\d{5})\s+(\S.*)$', t)
        if m and not re.match(r'^\d{6}', t):
            kbli = m.group(1); continue
        if kbli and t.startswith('Jumlah - Total'):
            v = re.findall(r'[\d][\d ]*\d|\d', t)
            if v: totals[kbli] = int(v[-1].replace(' ', ''))
            continue
        mi = re.match(r'^(\d{9})\s+(.*)$', t)
        if mi and kbli:
            toks = [x.strip() for x in re.split(r'\s{2,}', mi.group(2)) if x.strip()]
            nums = [x for x in toks if re.fullmatch(r'[\d][\d ]*\d|\d', x)]
            if len(nums) < 2:
                continue                      # baris disensor '*' -> dilewati
            qty = int(nums[-2].replace(' ', '')); val = int(nums[-1].replace(' ', ''))
            unit = ''
            for i, x in enumerate(toks):
                if x == nums[-2] and i > 0:
                    unit = toks[i-1].upper(); break
            if not re.fullmatch(r'[A-Z0-9/ ]{1,12}', unit):
                unit = ''
            items.append(dict(kbli=kbli, deskripsi=toks[0][:70], satuan=unit,
                              banyaknya=qty, nilai=val))

by = collections.defaultdict(list)
for it in items:
    by[it['kbli']].append(it)

rows = []
for k, its in by.items():
    tot = totals.get(k)
    vis = sum(i['nilai'] for i in its)
    kg = [i for i in its if i['satuan'] == 'KG' and i['banyaknya'] > 0]
    if not kg:
        continue
    kgv = sum(i['nilai'] for i in kg); kgq = sum(i['banyaknya'] for i in kg)
    dom = max(kg, key=lambda i: i['nilai'])
    rows.append(dict(
        kbli=k, n_item=len(its), n_item_kg=len(kg),
        cakupan_nilai_terbit=round(vis/tot, 3) if tot else None,
        pangsa_item_kg=round(kgv/vis, 3) if vis else None,
        Pd_rp_per_kg=round(kgv*1000/kgq, 1),
        Pd_item_dominan_rp_per_kg=round(dom['nilai']*1000/dom['banyaknya'], 1),
        item_dominan=dom['deskripsi'],
        nilai_produksi_kg_000rp=kgv))
rows.sort(key=lambda r: r['kbli'])

with open(OUT, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

covs = [r['cakupan_nilai_terbit'] for r in rows if r['cakupan_nilai_terbit']]
good = [r for r in rows if (r['cakupan_nilai_terbit'] or 0) >= .7 and (r['pangsa_item_kg'] or 0) >= .5]
print(f"jenis barang terbaca      : {len(items):,}")
print(f"KBLI dengan harga per kg  : {len(rows)}")
print(f"cakupan nilai median      : {st.median(covs):.0%}")
print(f"lolos saringan kualitas   : {len(good)}")
