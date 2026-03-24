#!/usr/bin/env python3
"""
Emit ONLY ASCII tables (tabulate grid) to FC26-WONDERKID-LIST.txt.

Data: workspace/data/fc26-players.csv (FC 26 player dump used across community DBs).

Cross-reference context (editorial, not printed): SoFIFA 260017/260025, GOAL Mar 2026,
VG247 wonderkid guides, FUTWIZ Career DB page, FIFACM player pages. CMTracker blocked
from automation in this environment.
"""

from __future__ import annotations

import os
from pathlib import Path

import pandas as pd
from tabulate import tabulate

CSV = Path(os.environ.get("FC26_PLAYERS_CSV", str(Path(__file__).resolve().parents[1] / "data" / "fc26-players.csv")))
OUT = Path(__file__).resolve().parents[1] / "FC26-WONDERKID-LIST.txt"

MIN_POT = 82
MAX_AGE = 23

POS_MAP = [
    ("GK", "GK", "KL"),
    ("CB", "CB", "D(M)"),
    ("LCB", "CB", "D(M)"),
    ("RCB", "CB", "D(M)"),
    ("LB", "LB", "D(Sol)"),
    ("LWB", "LB", "D(Sol)"),
    ("RB", "RB", "D(Sag)"),
    ("RWB", "RB", "D(Sag)"),
    ("CDM", "CDM", "DOS"),
    ("LDM", "CDM", "DOS"),
    ("RDM", "CDM", "DOS"),
    ("CM", "CM", "OS(M)"),
    ("LCM", "CM", "OS(M)"),
    ("RCM", "CM", "OS(M)"),
    ("CAM", "CAM", "OOS"),
    ("LAM", "CAM", "OOS"),
    ("RAM", "CAM", "OOS"),
    ("RM", "RM_RW", "RM/RW"),
    ("RW", "RM_RW", "RM/RW"),
    ("RF", "RM_RW", "RM/RW"),
    ("LM", "LM_LW", "LM/LW"),
    ("LW", "LM_LW", "LM/LW"),
    ("LF", "LM_LW", "LM/LW"),
    ("ST", "ST_CF", "SNT/CF"),
    ("CF", "ST_CF", "SNT/CF"),
]

ORDER = [
    ("GK", "1 | KALECILER | GK"),
    ("CB", "2 | STOPERLER | CB"),
    ("LB", "3 | SOL BEKLER | LB"),
    ("RB", "4 | SAG BEKLER | RB"),
    ("CDM", "5 | DEFANSIF ORTA SAHA | CDM"),
    ("CM", "6 | MERKEZ ORTA SAHA | CM"),
    ("CAM", "7 | OFANSIF ORTA SAHA | CAM"),
    ("RM_RW", "8 | SAG KANAT | RM/RW"),
    ("LM_LW", "9 | SOL KANAT | LM/LW"),
    ("ST_CF", "10 | SANTRAFOR | ST/CF"),
]


def tokens(s):
    if pd.isna(s) or not str(s).strip():
        return []
    return [x.strip() for x in str(s).split(",") if x.strip()]


def assign_buckets(codes: list[str]) -> dict[str, str]:
    out: dict[str, str] = {}
    for c in codes:
        for csv_c, bucket, label in POS_MAP:
            if c == csv_c and bucket not in out:
                out[bucket] = label
    return out


def fmt_gbp_mil(eur) -> str:
    if pd.isna(eur) or float(eur) <= 0:
        return "-"
    gbp = float(eur) * 0.86 / 1e6
    if gbp >= 100:
        return f"{gbp:.0f}M"
    if gbp >= 1:
        return f"{gbp:.2f}M"
    return f"{float(eur)*0.86/1000:.0f}k"


def fmt_wage_gbp(eur) -> str:
    if pd.isna(eur) or float(eur) <= 0:
        return "-"
    w = float(eur) * 0.86 / 1000
    return f"{w:.0f}k"


def main() -> None:
    df = pd.read_csv(CSV, low_memory=False)
    base = df[(df["potential"] >= MIN_POT) & (df["age"] <= MAX_AGE)].copy()
    base["growth"] = base["potential"] - base["overall"]

    rows_by: dict[str, list[list]] = {b: [] for b, _ in ORDER}

    for _, row in base.iterrows():
        codes = tokens(row["player_positions"])
        buckets = assign_buckets(codes)
        if not buckets:
            continue
        name = row["short_name"] if pd.notna(row["short_name"]) else row["long_name"]
        club = row["club_name"] if pd.notna(row["club_name"]) else "Free Agent"
        nat = row["nationality_name"] if pd.notna(row["nationality_name"]) else "-"
        wf = int(row["weak_foot"]) if pd.notna(row["weak_foot"]) else 0
        sm = int(row["skill_moves"]) if pd.notna(row["skill_moves"]) else 0
        h = int(row["height_cm"]) if pd.notna(row["height_cm"]) else 0
        wkg = int(row["weight_kg"]) if pd.notna(row["weight_kg"]) else 0

        for bucket_key, label in buckets.items():
            mevk = f"{label} | {row['player_positions']}"
            rows_by[bucket_key].append(
                [
                    str(name),
                    str(nat),
                    mevk,
                    str(club),
                    int(row["age"]),
                    fmt_gbp_mil(row["value_eur"]),
                    int(row["overall"]),
                    int(row["potential"]),
                    fmt_wage_gbp(row["wage_eur"]),
                    f"+{int(row['growth'])}",
                    f"{wf}*" if wf else "-",
                    f"{sm}*" if sm else "-",
                    str(h) if h else "-",
                    str(wkg) if wkg else "-",
                ]
            )

    chunks: list[str] = []
    headers = [
        "Ad",
        "Uyruk",
        "Mevki",
        "Kulup",
        "Yas",
        "Deger_GBP",
        "OVR",
        "POT",
        "Maas_GBP_hafta",
        "Buyume",
        "WF",
        "SM",
        "Boy_cm",
        "Kilo_kg",
    ]

    for key, title in ORDER:
        section_tbl = tabulate([[title]], tablefmt="grid")
        chunks.append(section_tbl)
        bucket_rows = rows_by[key]
        bucket_rows.sort(key=lambda r: (-int(r[7]), -int(r[6]), r[0].lower()))
        if not bucket_rows:
            empty = tabulate([["(bu kriterde satir yok)"]], tablefmt="grid")
            chunks.append(empty)
            continue
        chunks.append(tabulate(bucket_rows, headers=headers, tablefmt="grid"))

    OUT.write_text("\n".join(chunks).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
