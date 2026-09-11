#!/usr/bin/env python3
"""
Inspeksi awal seluruh file .dta / .csv / .xlsx di folder tesis.

Tujuan: sebelum satu regresi pun dijalankan, pastikan kita tahu persis
dataset mana yang punya berapa observasi, berapa industri, variabel apa saja,
dan mana yang layak dijadikan DATASET MASTER.

Jalankan:  python3 scripts/00_inspeksi_data.py
Hasil:     dicetak ke layar + disimpan ke output/00_inspeksi_data.md
"""
import os, sys, glob
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "output")
os.makedirs(OUT, exist_ok=True)

CANDIDATE_ID = ["isic3", "isic", "isic4", "kode", "kbli", "industri", "id"]
CANDIDATE_T = ["tahun", "year", "thn", "t"]

def guess(cols, cands):
    low = {c.lower(): c for c in cols}
    for c in cands:
        if c in low:
            return low[c]
    return None

def baca(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".dta":
        # pandas membaca .dta secara native; pyreadstat tidak diperlukan
        return pd.read_stata(path, convert_categoricals=False)
    if ext == ".csv":
        return pd.read_csv(path)
    if ext in (".xlsx", ".xls"):
        return pd.read_excel(path)
    raise ValueError(ext)

def laporkan(path, lines):
    rel = os.path.relpath(path, ROOT)
    lines.append(f"\n## `{rel}`\n")
    try:
        df = baca(path)
    except Exception as e:
        lines.append(f"GAGAL DIBACA: {e}\n")
        return
    lines.append(f"- Observasi: **{len(df):,}**")
    lines.append(f"- Kolom: **{df.shape[1]}**")

    idc = guess(df.columns, CANDIDATE_ID)
    tc = guess(df.columns, CANDIDATE_T)
    if idc:
        lines.append(f"- Pengenal industri: `{idc}` — **{df[idc].nunique():,} grup**")
    if tc:
        yrs = sorted(pd.Series(df[tc].dropna().unique()).tolist())
        lines.append(f"- Tahun: `{tc}` — {yrs}")
    if idc and tc:
        n_i, n_t = df[idc].nunique(), df[tc].nunique()
        seimbang = "SEIMBANG" if len(df) == n_i * n_t else f"TIDAK SEIMBANG (penuh = {n_i*n_t:,})"
        lines.append(f"- Bentuk panel: **{seimbang}**")
        dup = df.duplicated(subset=[idc, tc]).sum()
        if dup:
            lines.append(f"- PERINGATAN: {dup} baris duplikat pada ({idc}, {tc})")

    lines.append("\n| Variabel | Tipe | Non-null | Rata-rata | Min | Maks |")
    lines.append("|---|---|---|---|---|---|")
    for c in df.columns:
        s = df[c]
        if pd.api.types.is_numeric_dtype(s):
            lines.append(f"| `{c}` | {s.dtype} | {s.notna().sum():,} | "
                         f"{s.mean():,.4g} | {s.min():,.4g} | {s.max():,.4g} |")
        else:
            lines.append(f"| `{c}` | {s.dtype} | {s.notna().sum():,} | — | — | — |")

def main():
    pola = []
    for ext in ("dta", "csv", "xlsx", "xls"):
        pola += glob.glob(os.path.join(ROOT, f"**/*.{ext}"), recursive=True)
    pola = sorted(set(p for p in pola if "/output/" not in p))

    lines = ["# INSPEKSI DATA — hasil otomatis",
             "",
             f"Ditemukan **{len(pola)} berkas data** di folder tesis.",
             "",
             "Tujuan: menetapkan satu DATASET MASTER dan mengunci angka N."]
    if not pola:
        lines.append("\n**Belum ada file data.** Letakkan `.dta` / `.do` ke folder ini.")
    for p in pola:
        laporkan(p, lines)

    teks = "\n".join(lines)
    dest = os.path.join(OUT, "00_inspeksi_data.md")
    with open(dest, "w") as f:
        f.write(teks + "\n")
    print(teks)
    print(f"\n---\nDisimpan ke: {os.path.relpath(dest, ROOT)}")

if __name__ == "__main__":
    main()
