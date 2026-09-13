import re, csv
SRC = "/mnt/user-data/uploads/bahan tesis/data/data IBS 1990-2013/Data industri manufaktur/PDF file/out.txt"
pages = open(SRC, encoding='utf-8', errors='replace').read().split('\f')

def header_marks(page):
    for line in page.split('\n'):
        m=list(re.finditer(r'\((\d{1,2})\)', line))
        if len(m)>=3: return [(int(x.group(1)), (x.start()+x.end())//2) for x in m]
    return None

def data_lines(page):
    out=[]
    for line in page.split('\n'):
        if re.search(r'\(\d{1,2}\)', line): continue
        if not re.search(r'\d', line): continue
        if re.search(r'Catatan|Note:|Tabel|Table', line): continue
        if re.fullmatch(r'[ht tps:/w.bgoid]+', line.strip()): continue
        if not re.search(r'\b\d{5}\b', line): continue
        out.append(line.rstrip())
    return out

def spans_of(lines):
    W=max(len(l) for l in lines); L=[l.ljust(W) for l in lines]
    sep=[all(l[i]==' ' for l in L) for i in range(W)]
    sp=[];i=0
    while i<W:
        if not sep[i]:
            j=i
            while j<W and not sep[j]: j+=1
            sp.append((i,j)); i=j
        else: i+=1
    mg=[]
    for s,e in sp:
        if mg and s-mg[-1][1]<=1: mg[-1]=(mg[-1][0],e)
        else: mg.append((s,e))
    return mg, W

def parse(title, min_page=20):
    idx=[i for i,p in enumerate(pages) if title in p and i>=min_page]
    rows={}
    for i in idx:
        marks=header_marks(pages[i]); dl=data_lines(pages[i])
        if not marks or not dl: continue
        spans,W = spans_of(dl)
        for l in dl:
            l=l.ljust(W)
            raw=[]
            for s,e in spans:
                txt=l[s:e].strip()
                m=re.fullmatch(r'(.+?)\s(\d{5})', txt)
                if m: raw += [(m.group(1).strip(),(s+e)//2-4), (m.group(2), e)]
                else: raw.append((txt,(s+e)//2))
            code=None; rest=[]
            for txt,c in raw:
                if not txt: continue
                if code is None and re.fullmatch(r'\d{5}', txt): code=txt; continue
                rest.append((txt,c))
            avail=[m for m in marks if m[0]!=1]
            cells={}
            for txt,c in rest:
                if not avail: break
                m=min(avail, key=lambda mm: abs(mm[1]-c))
                cells[m[0]]=txt
                avail=[x for x in avail if x[1]>m[1]]
            if not code or code in rows: continue
            rows[code]=cells
    return rows

def num(s):
    s=(s or '').strip()
    if s in ('','*','-'): return None
    s=s.replace(' ','')
    return int(s) if re.fullmatch(r'\d+',s) else None


def parse_ordered(title, min_page=20):
    idx=[i for i,p in enumerate(pages) if title in p and i>=min_page]
    rows={}
    for i in idx:
        dl=data_lines(pages[i])
        if not dl: continue
        spans,W=spans_of(dl)
        for l in dl:
            l=l.ljust(W); seq=[]
            for s,e in spans:
                t=l[s:e].strip()
                m=re.fullmatch(r'(.+?)\s(\d{5})', t)
                if m: seq += [m.group(1).strip(), m.group(2)]
                else: seq.append(t)
            seq=[x for x in seq if x]
            code=next((x for x in seq if re.fullmatch(r'\d{5}',x)), None)
            if not code or code in rows: continue
            rows[code]=[x for x in seq if x!=code]
    return rows

T3Lo=parse_ordered("Jumlah Perusahaan dan Tenaga Kerja menurut Kode Industri")
T3Ro=parse_ordered("Number of Establishments and Labour by Industrial Code")
T3L=parse("Jumlah Perusahaan dan Tenaga Kerja menurut Kode Industri")
T3R=parse("Number of Establishments and Labour by Industrial Code")
T4L=parse("Pengeluaran untuk Pekerja menurut Kode Industri")
T4R=parse("Labour Expendicture by Industrial Code")
T9 =parse("Nilai Tambah menurut Kode Industri")

codes=sorted(set(T9))
rows=[]
for c in codes:
    a,b,d,e,f = T3L.get(c,{}),T3R.get(c,{}),T4L.get(c,{}),T4R.get(c,{}),T9.get(c,{})
    rows.append(dict(
        kbli=c,
        n_perusahaan   = num((T3Lo.get(c) or [None])[0]),
        tk_produksi    = num((T3Lo.get(c) or [None,None,None,None])[3]) if len(T3Lo.get(c,[]))>=4 else None,
        tk_lainnya     = num((T3Ro.get(c) or [None,None])[1]) if len(T3Ro.get(c,[]))>=2 else None,
        tk_total       = num((T3Ro.get(c) or [None])[-1]) if T3Ro.get(c) else None,
        upah_produksi  = num(d.get(7)),
        upah_lainnya   = num(e.get(13)),
        upah_total     = num(e.get(14)),
        biaya_input    = num(f.get(2)),
        nilai_output   = num(f.get(3)),
        nt_harga_pasar = num(f.get(4)),
        pajak_tak_lgsg = num(f.get(5)),
        nt_biaya_faktor= num(f.get(6)),
    ))

# --- verifikasi identitas akuntansi ---
def chk(name, fn):
    ok=bad=0; ex=[]
    for r in rows:
        try:
            v=fn(r)
        except TypeError:
            continue
        if v is None: continue
        if v: ok+=1
        else:
            bad+=1
            if len(ex)<3: ex.append(r['kbli'])
    print(f"  {name}: cocok {ok}, tidak cocok {bad} {ex}")

print("VERIFIKASI:")
chk("nilai tambah = output - input", lambda r: None if None in (r['nilai_output'],r['biaya_input'],r['nt_harga_pasar']) else abs(r['nilai_output']-r['biaya_input']-r['nt_harga_pasar'])<=2)
chk("NT faktor = NT pasar - pajak",  lambda r: None if None in (r['nt_harga_pasar'],r['pajak_tak_lgsg'],r['nt_biaya_faktor']) else abs(r['nt_harga_pasar']-r['pajak_tak_lgsg']-r['nt_biaya_faktor'])<=2)
chk("upah total = produksi + lainnya",lambda r: None if None in (r['upah_produksi'],r['upah_lainnya'],r['upah_total']) else abs(r['upah_produksi']+r['upah_lainnya']-r['upah_total'])<=2)

for r in rows:
    nt=r['nt_harga_pasar']; ut=r['upah_total']
    r['ULC'] = round(ut/nt,4) if (nt and ut and nt>0) else None
    r['upah_per_pekerja_produksi'] = round(r['upah_produksi']*1000/r['tk_produksi'],0) if (r['upah_produksi'] and r['tk_produksi']) else None
    r['upah_per_pekerja_lainnya']  = round(r['upah_lainnya']*1000/r['tk_lainnya'],0) if (r['upah_lainnya'] and r['tk_lainnya']) else None
    r['produktivitas_per_pekerja'] = round(nt*1000/r['tk_total'],0) if (nt and r['tk_total'] and nt>0) else None

with open('SI2012_KBLI5.csv','w',newline='') as fh:
    w=csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

usable=[r for r in rows if r['ULC'] is not None]
print(f"\nBaris total: {len(rows)} | dengan ULC terhitung: {len(usable)}")
import statistics as st
u=sorted(r['ULC'] for r in usable)
print(f"ULC  min {u[0]:.3f} | p25 {u[len(u)//4]:.3f} | median {st.median(u):.3f} | p75 {u[3*len(u)//4]:.3f} | max {u[-1]:.3f}")
print("\ncontoh:")
for r in rows[:4]:
    print(" ", r['kbli'], "ULC",r['ULC'], "| NT",r['nt_harga_pasar'], "| upah",r['upah_total'], "| TK",r['tk_total'])
