#!/usr/bin/env python3
"""
Bangun harga impor (Pm) tingkat industri dari Bea Cukai 2012.

Sumber:
  data/ImporNilai2012.csv   CIF USD, HS-10 x negara x bulan
  data/Imporberat2012.csv   kilogram, HS-10 x negara x bulan
  WITS HS 2007 (6 digit) -> ISIC Rev.3
  UN ISIC Rev.4 <-> ISIC Rev.3.1

Keluaran:
  data/Pm_2012_HS6.csv
  data/Pm_2012_ISIC4.csv
  data/Pm_2012_KBLI5_beacukai.csv
  data/SI2012_KBLI5_with_prices.csv

Kurs 2012: IMF/World Bank PA.NUS.FCRF Indonesia = 9.386,63 Rp/USD.
"""
from __future__ import annotations

import csv
import math
import statistics as st
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONC = DATA / "concordance"

NILAI = DATA / "ImporNilai2012.csv"
BERAT = DATA / "Imporberat2012.csv"
HS_ISIC3 = CONC / "H3_to_I3" / "JobID-48_Concordance_H3_to_I3.CSV"
ISIC4_31 = CONC / "ISIC4_ISIC31.txt"
HS_BEC = CONC / "H3_to_BE" / "JobID-40_Concordance_H3_to_BE.CSV"
SI = DATA / "SI2012_KBLI5.csv"
PM_BPS = DATA / "Pm_2012_KBLI5_bagianA.csv"
PD = DATA / "Pd_2012_KBLI5.csv"

# IMF/World Bank official exchange rate, Indonesia 2012 (period average)
USDIDR = 9386.63

# BEC 1-digit 2 = industrial supplies n.e.s. (closest to intermediate inputs)
BEC_INTERMEDIATE = {"2"}


def pad(code, n):
    s = "".join(ch for ch in str(code).strip() if ch.isdigit())
    return s.zfill(n) if s else ""


def fnum(x):
    if x is None:
        return None
    s = str(x).strip().replace(",", "")
    if not s:
        return None
    try:
        return float(s)
    except ValueError:
        return None


def load_trade(path, value_name):
    """Aggregate HS-10 x year-month x country to HS-10 annual totals."""
    tot = defaultdict(float)
    n = 0
    with open(path, encoding="utf-8-sig", errors="replace", newline="") as fh:
        for row in csv.reader(fh):
            if len(row) < 6:
                continue
            hs = pad(row[0], 10)
            tahun = row[4].strip()
            val = fnum(row[5])
            if len(hs) != 10 or not tahun.startswith("2012") or val is None or val <= 0:
                continue
            tot[hs] += val
            n += 1
    print(f"  {path.name}: {n:,} baris 2012, {len(tot):,} kode HS-10")
    return tot


def load_hs_isic3():
    m = {}
    with open(HS_ISIC3, encoding="latin-1", newline="") as fh:
        for row in csv.DictReader(fh):
            hs = pad(row["HS 2007 Product Code"], 6)
            isic = pad(row["ISIC Revision 3 Product Code"], 4)
            if hs and isic:
                m[hs] = isic
    print(f"  WITS HS2007->ISIC3: {len(m):,} kode HS-6")
    return m


def load_isic3_to_isic4():
    """Invert UN ISIC4-ISIC3.1 table. ISIC Rev.3 ~ Rev.3.1 at 4 digits for manufacturing."""
    inv = defaultdict(list)
    with open(ISIC4_31, encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            i4 = pad(row["ISIC4code"], 4)
            i3 = pad(row["ISIC31code"], 4)
            if not i4 or not i3:
                continue
            partial4 = row.get("partialISIC4", "1")
            partial3 = row.get("partialISIC31", "1")
            inv[i3].append((i4, partial4 == "0", partial3 == "0"))
    out = {}
    for i3, opts in inv.items():
        mfg = [o for o in opts if 10 <= int(o[0][:2]) <= 33]
        pool = mfg if mfg else opts
        complete = [o for o in pool if o[1] and o[2]]
        chosen = complete if complete else pool
        # unique ISIC4 codes, manufacturing first
        seen = []
        for code, _, _ in chosen:
            if code not in seen:
                seen.append(code)
        out[i3] = seen
    print(f"  UN ISIC3.1->ISIC4: {len(out):,} kode ISIC3")
    return out


def load_bec():
    m = {}
    with open(HS_BEC, encoding="latin-1", newline="") as fh:
        for row in csv.DictReader(fh):
            hs = pad(row["HS 2007 Product Code"], 6)
            bec = str(row["BEC Product Code"]).strip()
            if hs:
                m[hs] = bec[0] if bec else ""
    print(f"  WITS HS2007->BEC: {len(m):,} kode HS-6")
    return m


def pct(xs, p):
    if not xs:
        return None
    ys = sorted(xs)
    i = min(len(ys) - 1, max(0, int(round((p / 100) * (len(ys) - 1)))))
    return ys[i]


def weighted_uv(pairs):
    """pairs = (cif_usd, kg). Returns USD/kg or None."""
    cif = sum(c for c, k in pairs)
    kg = sum(k for c, k in pairs)
    if cif <= 0 or kg <= 0:
        return None
    return cif / kg


def assign_kbli(isic4_map, kbli):
    """
    Return (isic4_list_used, match_level).
    1) exact 4-digit class  kbli[:4] == isic4
    2) group 3-digit        kbli[:3] == isic4[:3]
    3) division 2-digit     kbli[:2] == isic4[:2]
    """
    keys = list(isic4_map.keys())
    hit4 = [k for k in keys if k == kbli[:4]]
    if hit4:
        return hit4, "class_4digit"
    hit3 = [k for k in keys if k[:3] == kbli[:3]]
    if hit3:
        return hit3, "group_3digit"
    hit2 = [k for k in keys if k[:2] == kbli[:2]]
    if hit2:
        return hit2, "division_2digit"
    return [], "unmatched"


def main():
    print("1. Membaca impor 2012...")
    cif = load_trade(NILAI, "cif")
    kg = load_trade(BERAT, "kg")

    hs_both = sorted(set(cif) & set(kg))
    cif_both = sum(cif[h] for h in hs_both)
    cif_all = sum(cif.values())
    print(f"  HS-10 di kedua berkas : {len(hs_both):,}")
    print(f"  Cakupan CIF dengan kg : {cif_both / cif_all:.1%} dari total nilai")

    print("2. Membaca konkordansi resmi...")
    hs_isic3 = load_hs_isic3()
    i3_to_i4 = load_isic3_to_isic4()
    hs_bec = load_bec()

    print("3. Unit value HS-6...")
    hs6_all = defaultdict(list)       # hs6 -> [(cif, kg)]
    hs6_int = defaultdict(list)
    hs6_meta = {}
    n_no_conc = 0
    uv_list = []
    rows_hs10 = []
    for h10 in hs_both:
        c, k = cif[h10], kg[h10]
        if k <= 0 or c <= 0:
            continue
        uv = c / k
        uv_list.append(uv)
        rows_hs10.append((h10, c, k, uv))

    lo, hi = pct(uv_list, 0.5), pct(uv_list, 99.5)
    print(f"  UV USD/kg  p0.5={lo:.4f}  median={pct(uv_list,50):.3f}  p99.5={hi:.1f}")

    n_drop = 0
    for h10, c, k, uv in rows_hs10:
        if uv < lo or uv > hi:
            n_drop += 1
            continue
        hs6 = h10[:6]
        hs6_all[hs6].append((c, k))
        bec = hs_bec.get(hs6, "")
        if bec in BEC_INTERMEDIATE:
            hs6_int[hs6].append((c, k))
        isic3 = hs_isic3.get(hs6)
        if not isic3:
            n_no_conc += 1
        hs6_meta[hs6] = (isic3, bec)
    print(f"  HS-10 dibuang (UV ekstrem): {n_drop:,}")
    print(f"  HS-6 tanpa konkordansi WITS: {n_no_conc:,} (dihitung per HS-10)")

    # write HS-6
    hs6_rows = []
    for hs6, pairs in sorted(hs6_all.items()):
        uv = weighted_uv(pairs)
        if uv is None:
            continue
        isic3, bec = hs6_meta.get(hs6, (None, ""))
        isic4s = i3_to_i4.get(isic3, []) if isic3 else []
        hs6_rows.append({
            "hs6": hs6,
            "cif_usd": round(sum(c for c, _ in pairs), 2),
            "kg": round(sum(k for _, k in pairs), 3),
            "Pm_usd_per_kg": round(uv, 6),
            "Pm_rp_per_kg": round(uv * USDIDR, 2),
            "isic3": isic3 or "",
            "isic4": "|".join(isic4s),
            "bec1": bec,
            "intermediate": int(bec in BEC_INTERMEDIATE),
        })
    write_csv(DATA / "Pm_2012_HS6.csv", hs6_rows)
    print(f"  tulis Pm_2012_HS6.csv  ({len(hs6_rows):,} HS-6)")

    print("4. Agregasi ke ISIC Rev.4 (4 digit)...")
    def to_isic4(hs6_dict):
        bucket = defaultdict(list)
        unmatched_cif = 0.0
        total_cif = 0.0
        for hs6, pairs in hs6_dict.items():
            cif_s = sum(c for c, _ in pairs)
            kg_s = sum(k for _, k in pairs)
            total_cif += cif_s
            isic3, _ = hs6_meta.get(hs6, (None, ""))
            targets = i3_to_i4.get(isic3, []) if isic3 else []
            mfg = [t for t in targets if 10 <= int(t[:2]) <= 33]
            use = mfg if mfg else targets
            if not use:
                unmatched_cif += cif_s
                continue
            share = 1.0 / len(use)
            for t in use:
                bucket[t].append((cif_s * share, kg_s * share))
        return bucket, unmatched_cif, total_cif

    b_all, u_all, t_all = to_isic4(hs6_all)
    b_int, u_int, t_int = to_isic4(hs6_int)
    print(f"  CIF terpetakan ke ISIC4 (semua) : {(t_all-u_all)/t_all:.1%}")
    print(f"  CIF terpetakan (BEC industri)   : {(t_int-u_int)/t_int:.1%}" if t_int else "  BEC industri: 0")

    isic_rows = []
    for code in sorted(set(b_all) | set(b_int)):
        uv_all = weighted_uv(b_all.get(code, []))
        uv_int = weighted_uv(b_int.get(code, []))
        cif_a = sum(c for c, _ in b_all.get(code, []))
        kg_a = sum(k for _, k in b_all.get(code, []))
        cif_i = sum(c for c, _ in b_int.get(code, []))
        isic_rows.append({
            "isic4": code,
            "divisi": code[:2],
            "cif_usd": round(cif_a, 2),
            "kg": round(kg_a, 3),
            "Pm_usd_per_kg": round(uv_all, 6) if uv_all else "",
            "Pm_rp_per_kg": round(uv_all * USDIDR, 2) if uv_all else "",
            "cif_usd_intermediate": round(cif_i, 2),
            "Pm_intermed_usd_per_kg": round(uv_int, 6) if uv_int else "",
            "Pm_intermed_rp_per_kg": round(uv_int * USDIDR, 2) if uv_int else "",
            "manufaktur": int(10 <= int(code[:2]) <= 33),
        })
    write_csv(DATA / "Pm_2012_ISIC4.csv", isic_rows)
    print(f"  tulis Pm_2012_ISIC4.csv ({len(isic_rows)} kelas)")

    isic4_uv = {r["isic4"]: r for r in isic_rows if r["Pm_usd_per_kg"] != ""}

    print("5. Menempelkan ke KBLI 5 digit...")
    si = list(csv.DictReader(open(SI, encoding="utf-8")))
    pm_bps = {r["kbli"]: r for r in csv.DictReader(open(PM_BPS, encoding="utf-8"))}
    pd_map = {r["kbli"]: r for r in csv.DictReader(open(PD, encoding="utf-8"))}

    kbli_rows = []
    merged = []
    n_lvl = defaultdict(int)
    for r in si:
        kbli = r["kbli"].strip()
        used, level = assign_kbli(isic4_uv, kbli)
        n_lvl[level] += 1
        pairs_all = []
        pairs_int = []
        for code in used:
            rec = isic4_uv[code]
            if rec["Pm_usd_per_kg"] != "":
                pairs_all.append((float(rec["cif_usd"]), float(rec["kg"])))
            if rec["Pm_intermed_usd_per_kg"] != "":
                # reconstruct kg from uv if needed
                uv_i = float(rec["Pm_intermed_usd_per_kg"])
                cif_i = float(rec["cif_usd_intermediate"])
                if uv_i > 0:
                    pairs_int.append((cif_i, cif_i / uv_i))
        uv = weighted_uv(pairs_all)
        uv_i = weighted_uv(pairs_int)
        bps = pm_bps.get(kbli, {})
        pdr = pd_map.get(kbli, {})
        row = {
            "kbli": kbli,
            "divisi": r.get("divisi", kbli[:2]),
            "divisi_nama": r.get("divisi_nama", ""),
            "sektor": r.get("sektor", ""),
            "match_level": level,
            "n_isic4_sumber": len(used),
            "Pm_usd_per_kg": round(uv, 6) if uv else "",
            "Pm_rp_per_kg": round(uv * USDIDR, 2) if uv else "",
            "lnPm": round(math.log(uv * USDIDR), 6) if uv and uv > 0 else "",
            "Pm_intermed_rp_per_kg": round(uv_i * USDIDR, 2) if uv_i else "",
            "lnPm_intermed": round(math.log(uv_i * USDIDR), 6) if uv_i and uv_i > 0 else "",
            "cif_usd": round(sum(c for c, _ in pairs_all), 2) if pairs_all else "",
            "Pm_bps_bagianA_rp_per_kg": bps.get("Pm_rp_per_kg", ""),
            "pangsa_impor_bps_A": bps.get("pangsa_impor", ""),
            "Pd_rp_per_kg": pdr.get("Pd_rp_per_kg", ""),
            "Pd_cakupan": pdr.get("cakupan_nilai_terbit", ""),
        }
        kbli_rows.append(row)
        out = dict(r)
        out.update({
            "Pm_usd_per_kg": row["Pm_usd_per_kg"],
            "Pm_rp_per_kg": row["Pm_rp_per_kg"],
            "lnPm": row["lnPm"],
            "Pm_intermed_rp_per_kg": row["Pm_intermed_rp_per_kg"],
            "lnPm_intermed": row["lnPm_intermed"],
            "Pm_match_level": level,
            "Pd_rp_per_kg": row["Pd_rp_per_kg"],
            "lnPd": (round(math.log(float(pdr["Pd_rp_per_kg"])), 6)
                     if pdr.get("Pd_rp_per_kg") not in (None, "") else ""),
            "lnULC": (round(math.log(float(r["ULC"])), 6)
                      if r.get("ULC") not in (None, "", "0") and float(r["ULC"]) > 0 else ""),
        })
        # skill ratio
        try:
            up, ul = float(r["upah_per_pekerja_produksi"]), float(r["upah_per_pekerja_lainnya"])
            out["rasio_keterampilan"] = round(ul / up, 4) if up > 0 else ""
        except (TypeError, ValueError, KeyError):
            out["rasio_keterampilan"] = ""
        merged.append(out)

    write_csv(DATA / "Pm_2012_KBLI5_beacukai.csv", kbli_rows)
    write_csv(DATA / "SI2012_KBLI5_with_prices.csv", merged)
    print(f"  tulis Pm_2012_KBLI5_beacukai.csv ({len(kbli_rows)})")
    print(f"  tulis SI2012_KBLI5_with_prices.csv ({len(merged)})")
    print("  tingkat pencocokan:", dict(n_lvl))

    have = [r for r in kbli_rows if r["Pm_rp_per_kg"] != ""]
    print(f"  KBLI dengan Pm Bea Cukai: {len(have)} / {len(kbli_rows)}")
    if have:
        pms = [r["Pm_rp_per_kg"] for r in have]
        print(f"  Pm Rp/kg  p10={pct(pms,10):,.0f}  median={st.median(pms):,.0f}  p90={pct(pms,90):,.0f}")

    # compare with BPS Bagian A where both exist
    both = []
    for r in have:
        b = r["Pm_bps_bagianA_rp_per_kg"]
        if b not in ("", None):
            try:
                both.append((r["kbli"], r["Pm_rp_per_kg"], float(b)))
            except ValueError:
                pass
    if both:
        # Spearman-ish: rank correlation via simple pearson on logs
        xs = [math.log(a) for _, a, b in both if a > 0 and b > 0]
        ys = [math.log(b) for _, a, b in both if a > 0 and b > 0]
        if len(xs) >= 5:
            mx, my = st.mean(xs), st.mean(ys)
            num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
            den = math.sqrt(sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys))
            corr = num / den if den else float("nan")
            print(f"  Korelasi ln Pm BeaCukai vs BPS Bagian A (n={len(xs)}): {corr:.3f}")

    print("6. Ringkasan per sektor...")
    print(f"{'sektor':24s} {'n_kbli':>7} {'n_Pm':>6} {'median Pm':>12} {'n_Pd':>6}")
    for sek in ["Resource Intensive", "Labor Intensive", "Capital Intensive", "DIKELUARKAN"]:
        rs = [r for r in kbli_rows if r["sektor"] == sek]
        pms = [r["Pm_rp_per_kg"] for r in rs if r["Pm_rp_per_kg"] != ""]
        pds = [r for r in rs if r["Pd_rp_per_kg"] not in ("", None)]
        med = f"{st.median(pms):,.0f}" if pms else "-"
        print(f"{sek:24s} {len(rs):7d} {len(pms):6d} {med:>12} {len(pds):6d}")

    print("Selesai.")


def write_csv(path, rows):
    if not rows:
        return
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)


if __name__ == "__main__":
    main()
