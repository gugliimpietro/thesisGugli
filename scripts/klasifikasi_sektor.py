import csv, collections, statistics as st

# Divisi KBLI 2009 (= ISIC Rev.4) -> nama, asal divisi ISIC Rev.3, klasifikasi sektor
# Klasifikasi sektor mengikuti Tabel 3.1 naskah (Narjoko & Putra 2014) yang disusun
# pada ISIC Rev.3 2 digit, dipetakan ke divisi Rev.4 yang bersesuaian.
MAP = {
 '10': ('Makanan',                          '15', 'Resource Intensive',  'jelas'),
 '11': ('Minuman',                           '15', 'Resource Intensive',  'jelas'),
 '12': ('Pengolahan tembakau',               '16', 'Resource Intensive',  'jelas'),
 '13': ('Tekstil',                           '17', 'Labor Intensive',     'jelas'),
 '14': ('Pakaian jadi',                      '18', 'Labor Intensive',     'jelas'),
 '15': ('Kulit, barang kulit dan alas kaki', '19', 'Labor Intensive',     'jelas'),
 '16': ('Kayu dan barang dari kayu',         '20', 'Labor Intensive',     'jelas'),
 '17': ('Kertas dan barang dari kertas',     '21', 'Resource Intensive',  'jelas'),
 '18': ('Percetakan dan reproduksi media',   '22', 'Labor Intensive',     'jelas'),
 '19': ('Batubara dan pengilangan migas',    '23', 'Resource Intensive',  'jelas'),
 '20': ('Bahan kimia dan barang kimia',      '24', 'Labor Intensive',     'jelas'),
 '21': ('Farmasi dan obat tradisional',      '24', 'Labor Intensive',     'jelas'),
 '22': ('Karet dan plastik',                 '25', 'Resource Intensive',  'jelas'),
 '23': ('Galian bukan logam',                '26', 'Capital Intensive',   'jelas'),
 '24': ('Logam dasar',                       '27', 'Capital Intensive',   'jelas'),
 '25': ('Barang logam, bukan mesin',         '28', 'Capital Intensive',   'jelas'),
 '26': ('Komputer, elektronik dan optik',    '30/32/33', 'Capital Intensive', 'jelas'),
 '27': ('Peralatan listrik',                 '31', 'Capital Intensive',   'jelas'),
 '28': ('Mesin dan perlengkapan ytdl',       '29', 'Capital Intensive',   'jelas'),
 '29': ('Kendaraan bermotor',                '34', 'Capital Intensive',   'jelas'),
 '30': ('Alat angkutan lainnya',             '35', 'Capital Intensive',   'jelas'),
 '31': ('Furnitur',                          '36', 'Labor Intensive',     'jelas'),
 '32': ('Pengolahan lainnya',                '36 + sebagian 33', 'Labor Intensive', 'PERLU DICEK'),
 '33': ('Jasa reparasi dan pemasangan mesin','tidak ada padanan manufaktur', 'DIKELUARKAN', 'DIKELUARKAN'),
}

rows=list(csv.DictReader(open('SI2012_KBLI5.csv')))
def f(x):
    try: return float(x)
    except: return None

for r in rows:
    d=r['kbli'][:2]
    nm,rev3,sek,flag = MAP[d]
    r['divisi']=d; r['divisi_nama']=nm; r['isic_rev3_asal']=rev3
    r['sektor']=sek; r['status_pemetaan']=flag

cols=list(rows[0].keys())
with open('SI2012_KBLI5.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=cols); w.writeheader(); w.writerows(rows)

def agg(rs):
    g=lambda k: [f(r[k]) for r in rs if f(r[k]) is not None]
    S=lambda k: sum(g(k))
    nt=S('nt_harga_pasar'); ut=S('upah_total')
    tkp=S('tk_produksi'); tkl=S('tk_lainnya'); tkt=S('tk_total')
    up=S('upah_produksi'); ul=S('upah_lainnya')
    ulcs=sorted(f(r['ULC']) for r in rs if f(r['ULC']) is not None)
    return dict(
      n_kbli=len(rs),
      n_perusahaan=int(S('n_perusahaan')),
      tk_produksi=int(tkp), tk_lainnya=int(tkl), tk_total=int(tkt),
      upah_produksi_trilyun=round(up/1e9,2), upah_lainnya_trilyun=round(ul/1e9,2),
      nilai_tambah_trilyun=round(nt/1e9,2),
      ULC_agregat=round(ut/nt,4) if nt else None,
      ULC_median=round(st.median(ulcs),4) if ulcs else None,
      upah_pekerja_produksi_juta=round(up*1000/tkp/1e6,2) if tkp else None,
      upah_pekerja_lainnya_juta=round(ul*1000/tkl/1e6,2) if tkl else None,
      rasio_keterampilan=round((ul/tkl)/(up/tkp),3) if tkp and tkl and up else None,
      produktivitas_juta=round(nt*1000/tkt/1e6,2) if tkt else None,
    )

# per sektor (tanpa divisi 33)
main=[r for r in rows if r['sektor']!='DIKELUARKAN']
out=[]
for sek in ['Resource Intensive','Labor Intensive','Capital Intensive']:
    rs=[r for r in main if r['sektor']==sek]
    out.append(dict(sektor=sek, **agg(rs)))
out.append(dict(sektor='TOTAL (tanpa divisi 33)', **agg(main)))
with open('tabel_sektor.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)

# per divisi
outd=[]
for d in sorted(set(r['divisi'] for r in rows)):
    rs=[r for r in rows if r['divisi']==d]
    outd.append(dict(divisi=d, nama=MAP[d][0], sektor=MAP[d][2], **agg(rs)))
with open('tabel_divisi.csv','w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=list(outd[0].keys())); w.writeheader(); w.writerows(outd)

print(f"{'SEKTOR':24s} {'KBLI':>5} {'Persh':>7} {'TK':>10} {'NT(T Rp)':>10} {'ULC':>7} {'Upah prod':>10} {'Rasio ket':>10} {'Produkt':>9}")
for o in out:
    print(f"{o['sektor']:24s} {o['n_kbli']:5d} {o['n_perusahaan']:7d} {o['tk_total']:10d} {o['nilai_tambah_trilyun']:10.1f} {o['ULC_agregat']:7.3f} {o['upah_pekerja_produksi_juta']:10.1f} {o['rasio_keterampilan']:10.2f} {o['produktivitas_juta']:9.1f}")
