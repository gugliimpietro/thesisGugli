"""
Ekstraksi harga bahan baku impor (Pm) dan pangsa input impor dari publikasi BPS
"Statistik Industri Manufaktur - Bahan Baku 2012" (Katalog 6103002).

Struktur tabel sumber, per KBLI 5 digit dan per jenis barang (kode KKI 9 digit):
    kode | deskripsi | satuan | Impor: banyaknya, nilai | Jumlah: banyaknya, nilai
Bahan baku domestik = Jumlah - Impor.
"""
import re, csv, sys, collections, statistics as st

SRC = sys.argv[1] if len(sys.argv) > 1 else "bb.txt"
NOISE = re.compile(r'^[ht tps:/w.bgoid]+$')
NUM = re.compile(r'^[\d][\d ]*\d$|^\d$')

def cols(lines):
    W = max(len(l) for l in lines); L = [l.ljust(W) for l in lines]
    sep = [all(l[i] == ' ' for l in L) for i in range(W)]
    sp = []; i = 0
    while i < W:
        if not sep[i]:
            j = i
            while j < W and not sep[j]: j += 1
            sp.append((i, j)); i = j
        else: i += 1
    mg = []
    for s, e in sp:
        if mg and s - mg[-1][1] <= 1: mg[-1] = (mg[-1][0], e)
        else: mg.append((s, e))
    return mg, W

kbli = None; items = []; totals = {}
for page in open(SRC, encoding='utf-8', errors='replace').read().split('\f'):
    raw = []
    for line in page.split('\n'):
        t = line.strip()
        if not t or NOISE.fullmatch(t): continue
        m = re.match(r'^(\d{5})\s+(\S.*)$', t)
        if m and not re.match(r'^\d{6}', t):
            kbli = m.group(1); continue
        if kbli and t.startswith('Jumlah - Total'):
            v = re.findall(r'[\d][\d ]*\d|\d', t)
            if v: totals[kbli] = int(v[-1].replace(' ', ''))
            continue
        if re.match(r'^\d{9}\s', t):
            raw.append((kbli, line.rstrip()))
    if not raw: continue
    spans, W = cols([l for _, l in raw])
    for k, l in raw:
        l = l.ljust(W)
        cells = [l[s:e].strip() for s, e in spans]
        code = cells[0].split()[0] if cells and cells[0] else None
        if not code or not re.fullmatch(r'\d{9}', code): continue
        nums = [c for c in cells if NUM.fullmatch(c)]
        txt = [c for c in cells if not NUM.fullmatch(c)]
        unit = ''
        for c in reversed(txt):
            if re.fullmatch(r'[A-Z0-9/ ]{1,12}', c): unit = c; break
        n = [int(x.replace(' ', '')) for x in nums]
        imp_q = imp_v = None
        if len(n) >= 4: imp_q, imp_v, tot_q, tot_v = n[0], n[1], n[-2], n[-1]
        elif len(n) == 2: tot_q, tot_v = n
        else: continue
        items.append(dict(kbli=k, kki=code, satuan=unit,
                          impor_qty=imp_q, impor_val=imp_v,
                          total_qty=tot_q, total_val=tot_v,
                          deskripsi=(txt[0] if txt else '')[:60]))

by = collections.defaultdict(list)
for it in items: by[it['kbli']].append(it)
print(f"jenis bahan baku terbaca : {len(items):,}")
print(f"KBLI                     : {len(by)}")

ok = bad = 0; ex = []
for k, tv in totals.items():
    s = sum(i['total_val'] for i in by.get(k, []))
    if abs(s - tv) <= max(2, tv * 0.001): ok += 1
    else:
        bad += 1
        if len(ex) < 3: ex.append((k, s, tv))
print(f"VERIFIKASI jumlah item = Jumlah-Total : cocok {ok}, tidak cocok {bad} {ex}")

rows = []
for k, its in by.items():
    tot_v = sum(i['total_val'] for i in its)
    imp_v = sum(i['impor_val'] or 0 for i in its)
    kg = [i for i in its if i['satuan'] == 'KG' and (i['impor_qty'] or 0) > 0 and (i['impor_val'] or 0) > 0]
    pm = (sum(i['impor_val'] for i in kg) * 1000 / sum(i['impor_qty'] for i in kg)) if kg else None
    kgall = [i for i in its if i['satuan'] == 'KG' and i['total_qty'] > 0]
    pin = (sum(i['total_val'] for i in kgall) * 1000 / sum(i['total_qty'] for i in kgall)) if kgall else None
    rows.append(dict(kbli=k, n_item=len(its), n_item_impor_kg=len(kg),
        nilai_bahan_baku_total_000rp=tot_v, nilai_bahan_baku_impor_000rp=imp_v,
        pangsa_impor=round(imp_v / tot_v, 4) if tot_v else None,
        Pm_rp_per_kg=round(pm, 1) if pm else None,
        Pinput_semua_rp_per_kg=round(pin, 1) if pin else None,
        cakupan_nilai_terbit=round(tot_v / totals[k], 3) if totals.get(k) else None))
rows.sort(key=lambda r: r['kbli'])
with open('Pm_2012_KBLI5.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

pm = sorted(r['Pm_rp_per_kg'] for r in rows if r['Pm_rp_per_kg'])
sh = sorted(r['pangsa_impor'] for r in rows if r['pangsa_impor'] is not None)
print(f"\nKBLI dengan Pm (harga impor per kg) : {len(pm)}")
print(f"  Pm  p10 {pm[len(pm)//10]:,.0f} | median {st.median(pm):,.0f} | p90 {pm[9*len(pm)//10]:,.0f} Rp/kg")
print(f"KBLI dengan pangsa impor           : {len(sh)}")
print(f"  pangsa impor  p25 {sh[len(sh)//4]:.1%} | median {st.median(sh):.1%} | p75 {sh[3*len(sh)//4]:.1%}")
