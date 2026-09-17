import csv, statistics
si={r['kbli']:r for r in csv.DictReader(open('SI2012_KBLI5.csv'))}
t7=list(csv.DictReader(open('T7_biaya_input.csv')))
def n(x):
    return float(x) if x not in ('',None) else None
out=[]; ident_ok=0; ident_bad=0
for r in t7:
    k=r['kbli']; s=si.get(k)
    comp=[n(r[c]) for c in ('bahan_baku','energi','sewa','jasa','repres','lainnya')]
    tot=n(r['jumlah_T7'])
    if tot is not None and all(c is not None for c in comp):
        if abs(sum(comp)-tot)<=2: ident_ok+=1
        else: ident_bad+=1
    e=n(r['energi']); tk=float(s['tk_total']) if s and s['tk_total'] else None
    out.append(dict(kbli=k, sektor=s['sektor'] if s else '', divisi=s['divisi'] if s else '',
        bahan_baku_penolong=r['bahan_baku'], biaya_energi=r['energi'], sewa=r['sewa'],
        jasa_pihak_lain=r['jasa'], representasi_royalti=r['repres'], pengeluaran_lainnya=r['lainnya'],
        biaya_input_T7=r['jumlah_T7'], biaya_input_T9=r['biaya_input_T9'],
        energi_per_pekerja_rp=round(e*1000/tk) if (e and tk) else '',
        pangsa_energi=round(e/tot,4) if (e and tot) else '',
        pangsa_bahan_baku=round(n(r['bahan_baku'])/tot,4) if (n(r['bahan_baku']) and tot) else ''))
print(f"identitas komponen = jumlah -> cocok {ident_ok}, tidak {ident_bad}")
vals=[float(o['energi_per_pekerja_rp']) for o in out if o['energi_per_pekerja_rp']!='']
print("KBLI dgn energi/pekerja:",len(vals),"median Rp",format(round(statistics.median(vals)),',d'))
ps=[float(o['pangsa_energi']) for o in out if o['pangsa_energi']!='']
print("pangsa energi: n",len(ps),"median",round(statistics.median(ps),4))
w=csv.DictWriter(open('/mnt/user-data/outputs/struktur_biaya_2012.csv','w',newline=''),fieldnames=list(out[0]));w.writeheader();w.writerows(out)
# ringkas per sektor
import collections
g=collections.defaultdict(lambda:[0,0,0])
for o in out:
    if o['sektor'] and o['biaya_energi'] and o['biaya_input_T7']:
        g[o['sektor']][0]+=float(o['biaya_energi']); g[o['sektor']][1]+=float(o['biaya_input_T7']); g[o['sektor']][2]+=1
print("\nSektor | n | pangsa energi thd biaya input")
for k,v in sorted(g.items(), key=lambda x:-x[1][0]/x[1][1]):
    print(f"{k:22s} {v[2]:4d}  {v[0]/v[1]*100:5.2f}%")
