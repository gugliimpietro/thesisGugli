#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch_comtrade_2012.py  (versi 2 — sudah diuji langsung lewat browser)

Mengunduh ekspor & impor Indonesia 2012 pada level HS 6-digit dari UN Comtrade,
membangun konkordans HS2012 -> ISIC Rev.4 lewat CPC Ver.2.1, lalu mengagregasi
ke level industri.

TIDAK PERLU API KEY.

Versi ini memakai endpoint "preview" yang gratis, dengan tiga pengaman yang
ditemukan lewat percobaan langsung pada 18 September 2026:

  1. Permintaan banyak kode sekaligus kadang dijawab 200 OK tetapi KOSONG
     (pembatasan laju tersembunyi). Respons kosong diulang, bukan diterima.
  2. Hasil diverifikasi per bab HS terhadap total resmi (cmdCode=AG2).
     Bab yang kurang dari 99,9% disapu ulang dengan enumerasi kode.
  3. Total akhir dibandingkan dengan angka kontrol yang sudah terbukti:
        Ekspor 2012 = USD 190.031.839.234
        Impor  2012 = USD 191.690.908.079

CARA PAKAI
----------
    python fetch_comtrade_2012.py

HASIL (folder data/ di akar repo, satu tingkat di atas scripts/)
----------------------------------------------------------------
    data/comtrade_2012_X_HS6.csv    ekspor per HS6  (nilai USD, berat kg, kuantitas)
    data/comtrade_2012_M_HS6.csv    impor  per HS6
    data/HS2012_ISIC4.csv           konkordans HS6 -> ISIC Rev.4 (4 digit)
    data/trade_2012_ISIC4.csv       agregasi: X_usd, X_kg, M_usd, M_kg, Px, Pm
    data/verifikasi_comtrade.txt    laporan rekonsiliasi per bab
"""

import csv, json, os, re, sys, time
import urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT  = os.path.join(ROOT, "data")
os.makedirs(OUT, exist_ok=True)

REPORTER, YEAR = 360, 2012
UA = {"User-Agent": "Mozilla/5.0 (academic thesis data collection)"}

PREVIEW = "https://comtradeapi.un.org/public/v1/preview/C/A/HS"
REFH4   = "https://comtradeapi.un.org/files/v1/app/reference/H4.json"
CONC_HS_CPC   = "https://unstats.un.org/unsd/classifications/Econ/tables/CPC/CPCv21_HS12/cpc21-hs2012.txt"
CONC_CPC_ISIC = "https://unstats.un.org/unsd/classifications/Econ/tables/CPC/CPCv21_ISIC4/CPC21-ISIC4.txt"

KONTROL = {"X": 190031839234, "M": 191690908079}

DELAY, BATCH, RETRY = 2.5, 200, 4
LOG = []


def say(s):
    print(s, flush=True)
    LOG.append(s)


def get(url, timeout=120):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def q(flow, cmd):
    return PREVIEW + "?" + urllib.parse.urlencode({
        "reporterCode": REPORTER, "period": YEAR, "partnerCode": 0,
        "partner2Code": 0, "customsCode": "C00", "motCode": 0,
        "flowCode": flow, "cmdCode": cmd})


def ask(flow, cmd, allow_empty=False):
    """Satu permintaan, diulang bila jawabannya kosong (rate limit tersembunyi)."""
    for _ in range(RETRY):
        try:
            j = json.loads(get(q(flow, cmd)))
            d = j.get("data") or []
            time.sleep(DELAY)
            if d or allow_empty:
                return d
        except Exception:
            time.sleep(DELAY)
    return []


# ---------------------------------------------------------------- 1. panen
def rows_of(d):
    out = []
    for x in d:
        c = str(x.get("cmdCode", ""))
        if re.fullmatch(r"\d{6}", c):
            out.append([c, x.get("primaryValue"), x.get("netWgt"),
                        x.get("qty"), x.get("qtyUnitAbbr")])
    return out


def panen(flow, codes, store):
    have = {r[0] for r in store}
    todo = [c for c in codes if c not in have]
    for i in range(0, len(todo), BATCH):
        b = todo[i:i + BATCH]
        for r in rows_of(ask(flow, ",".join(b))):
            if r[0] not in have:
                have.add(r[0]); store.append(r)
        say(f"    {flow} {i + len(b):5d}/{len(todo)}  terkumpul {len(store)}")
    return store


def bab_resmi(flow):
    return {str(x["cmdCode"]): x["primaryValue"] for x in ask(flow, "AG2")}


def bab_kita(store):
    m = {}
    for r in store:
        m[r[0][:2]] = m.get(r[0][:2], 0) + (r[1] or 0)
    return m


def kurang(resmi, kita, amb=0.999):
    return [c for c, v in resmi.items() if v and kita.get(c, 0) / v < amb]


def sapu_bab(flow, babs, headings, store):
    """Enumerasi pos 4-digit + 00..99 untuk bab yang belum cocok."""
    have = {r[0] for r in store}
    cand = [h + f"{s:02d}" for h in headings if h[:2] in babs
            for s in range(100) if h + f"{s:02d}" not in have]
    say(f"    sapu ulang bab {','.join(babs)}: {len(cand)} kode kandidat")
    for i in range(0, len(cand), BATCH):
        for r in rows_of(ask(flow, ",".join(cand[i:i + BATCH]), allow_empty=True)):
            if r[0] not in have:
                have.add(r[0]); store.append(r)
    return store


def tulis(store, path):
    store.sort(key=lambda r: r[0])
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["cmdCode", "primaryValue", "netWgt", "qty", "qtyUnitAbbr"])
        for r in store:
            w.writerow(["" if v is None else v for v in r])


# ---------------------------------------------------------- 2. konkordans
def konkordans():
    dest = os.path.join(OUT, "HS2012_ISIC4.csv")

    def baca(url):
        t = get(url)
        out = []
        for line in t.strip().splitlines()[1:]:
            out.append([c.strip().strip('"') for c in line.split(",")])
        return out

    hs_cpc = baca(CONC_HS_CPC)      # CPC21code, CPC21partial, HS12code, HS12partial
    cpc_is = baca(CONC_CPC_ISIC)    # CPC21code, CPC21partial, ISIC4code, ISIC4partial

    c2i = {}
    for r in cpc_is:
        if len(r) >= 3 and r[0] not in c2i:
            c2i[r[0]] = r[2]

    m = {}
    for r in hs_cpc:
        if len(r) < 3:
            continue
        hs = r[2].replace(".", "")
        isic = c2i.get(r[0])
        if len(hs) == 6 and isic and hs not in m:
            m[hs] = isic

    with open(dest, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["hs6", "isic4"])
        for k in sorted(m):
            w.writerow([k, m[k]])
    say(f"  konkordans: {len(m)} pasangan HS6 -> ISIC Rev.4")
    return m


# ------------------------------------------------------------ 3. agregasi
def agregasi(conc):
    agg = {}
    for flow, fn in (("X", "comtrade_2012_X_HS6.csv"), ("M", "comtrade_2012_M_HS6.csv")):
        p = os.path.join(OUT, fn)
        if not os.path.exists(p):
            continue
        for r in csv.DictReader(open(p, encoding="utf-8")):
            isic = conc.get(r["cmdCode"])
            if not isic:
                continue
            a = agg.setdefault(isic, dict(isic4=isic, X_usd=0.0, X_kg=0.0,
                                          M_usd=0.0, M_kg=0.0, n_hs_X=0, n_hs_M=0))
            a[flow + "_usd"] += float(r["primaryValue"] or 0)
            a[flow + "_kg"]  += float(r["netWgt"] or 0)
            a["n_hs_" + flow] += 1

    rows = []
    for a in sorted(agg.values(), key=lambda x: x["isic4"]):
        a["Px_usd_per_kg"] = round(a["X_usd"] / a["X_kg"], 4) if a["X_kg"] else ""
        a["Pm_usd_per_kg"] = round(a["M_usd"] / a["M_kg"], 4) if a["M_kg"] else ""
        rows.append(a)
    if rows:
        p = os.path.join(OUT, "trade_2012_ISIC4.csv")
        with open(p, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
        man = [r for r in rows if r["isic4"][:2].isdigit() and 10 <= int(r["isic4"][:2]) <= 33]
        say(f"  agregasi: {len(rows)} industri ISIC Rev.4, {len(man)} di antaranya manufaktur (10-33)")


# ------------------------------------------------------------------ main
def main():
    say("=" * 66)
    say("UNDUH DATA PERDAGANGAN INDONESIA 2012 — UN COMTRADE (tanpa API key)")
    say("=" * 66)

    say("\n[1/4] Daftar kode HS 6-digit")
    ref = json.loads(get(REFH4))
    ref = ref.get("results", ref)
    HS6 = sorted({str(x["id"]) for x in ref if re.fullmatch(r"\d{6}", str(x["id"]))})
    HEAD = sorted({c[:4] for c in HS6})
    say(f"  {len(HS6)} kode HS6, {len(HEAD)} pos 4-digit")

    for flow, fn in (("X", "comtrade_2012_X_HS6.csv"), ("M", "comtrade_2012_M_HS6.csv")):
        say(f"\n[2/4] Panen arus {flow}")
        store = []
        panen(flow, HS6, store)

        resmi = bab_resmi(flow)
        for putaran in range(3):
            b = kurang(resmi, bab_kita(store))
            if not b:
                break
            say(f"  putaran {putaran + 1}: bab belum cocok -> {','.join(b)}")
            sapu_bab(flow, set(b), HEAD, store)

        tot = sum(r[1] or 0 for r in store)
        b = kurang(resmi, bab_kita(store))
        say(f"  {flow}: {len(store)} baris | total USD {tot:,.0f} "
            f"| kontrol USD {KONTROL[flow]:,} | cakupan {tot / KONTROL[flow] * 100:.3f}%")
        say(f"  bab yang masih < 99,9%: {','.join(b) if b else 'TIDAK ADA'}")
        tulis(store, os.path.join(OUT, fn))

    say("\n[3/4] Konkordans HS2012 -> CPC 2.1 -> ISIC Rev.4")
    conc = konkordans()

    say("\n[4/4] Agregasi ke ISIC Rev.4")
    agregasi(conc)

    with open(os.path.join(OUT, "verifikasi_comtrade.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(LOG))
    say("\nSelesai. Commit & push, lalu beri tahu Claude.")


if __name__ == "__main__":
    main()
