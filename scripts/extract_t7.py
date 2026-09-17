import re, csv, json
exec(open('build.py').read().split('def parse_ordered')[0])

L = parse("Tabel 7 Biaya Input menurut Kode Industri")
R = parse("Table 7 Input Cost by Industrial Code")
print("kiri:", len(L), L.get('10110'))
print("kanan:", len(R), R.get('10110'))

T9 = json.load(open('raw.json'))['T9']

rows=[]; cocok=0; beda=0; kosong=0
for k in sorted(set(L)|set(R)):
    l=L.get(k,{}); r=R.get(k,{})
    rec=dict(kbli=k,
        bahan_baku=num(l.get(2)), energi=num(l.get(3)), sewa=num(l.get(4)),
        jasa=num(r.get(5)), repres=num(r.get(6)), lainnya=num(r.get(7)),
        jumlah_T7=num(r.get(8)))
    bi9 = num(T9.get(k,[None,None])[1]) if k in T9 else None
    rec['biaya_input_T9']=bi9
    if rec['jumlah_T7'] is None or bi9 is None: kosong+=1
    elif rec['jumlah_T7']==bi9: cocok+=1
    else: beda+=1; print("BEDA",k,rec['jumlah_T7'],bi9)
    rows.append(rec)
print(f"VERIFIKASI jumlah T7 vs biaya_input T9 -> cocok {cocok}, beda {beda}, tak terbandingkan {kosong}")
json.dump({'L':L,'R':R}, open('t7_raw.json','w'))
csv.DictWriter(open('T7_biaya_input.csv','w',newline=''), fieldnames=list(rows[0])).writeheader()
w=csv.DictWriter(open('T7_biaya_input.csv','a',newline=''), fieldnames=list(rows[0]))
for r_ in rows: w.writerow(r_)
