#!/usr/bin/env python3
"""
FC 26 wonderkid Markdown üretici.

Kaynak: EAFC26-DataHub (Kaggle FC 26 dataset) `players.csv`.
Filtre: potential >= MIN_POT, age <= MAX_AGE.
Her oyuncu, player_positions içindeki her uygun kod için ilgili tablolara girer (çok mevkili oyuncular birden fazla bölümde yer alır).
"""

from __future__ import annotations

import re
import os
from pathlib import Path

import pandas as pd

_DEFAULT_CSV = Path(__file__).resolve().parents[1] / "data" / "fc26-players.csv"
CSV_PATH = Path(os.environ.get("FC26_PLAYERS_CSV", str(_DEFAULT_CSV)))
OUT_PATH = Path(__file__).resolve().parents[1] / "FC26-WONDERKID-LIST.md"

MIN_POT = 82
MAX_AGE = 23

# CSV pozisyon kodu -> (bucket_key, Türkçe mevki etiketi)
POS_MAP: list[tuple[str, str, str]] = [
    ("GK", "GK", "KL"),
    ("CB", "CB", "D(M)"),
    ("LCB", "CB", "D(M)"),
    ("RCB", "CB", "D(M)"),
    ("LB", "LB", "D(Sol)"),
    ("LWB", "LB", "D(Sol)"),
    ("RB", "RB", "D(Sağ)"),
    ("RWB", "RB", "D(Sağ)"),
    ("CDM", "CDM", "DOS"),
    ("LDM", "CDM", "DOS"),
    ("RDM", "CDM", "DOS"),
    ("CM", "CM", "OS(M)"),
    ("LCM", "CM", "OS(M)"),
    ("RCM", "CM", "OS(M)"),
    ("CAM", "CAM", "OOS"),
    ("LAM", "CAM", "OOS"),
    ("RAM", "CAM", "OOS"),
    ("RM", "RM_RW", "RM / RW"),
    ("RW", "RM_RW", "RM / RW"),
    ("RF", "RM_RW", "RM / RW"),
    ("LM", "LM_LW", "LM / LW"),
    ("LW", "LM_LW", "LM / LW"),
    ("LF", "LM_LW", "LM / LW"),
    ("ST", "ST_CF", "SNT / CF"),
    ("CF", "ST_CF", "SNT / CF"),
]

BUCKET_ORDER = [
    ("GK", "1. Kaleciler (GK / KL)"),
    ("CB", "2. Stoperler (CB / D(M))"),
    ("LB", "3. Sol Bekler (LB / D(Sol))"),
    ("RB", "4. Sağ Bekler (RB / D(Sağ))"),
    ("CDM", "5. Defansif Orta Saha (CDM / DOS)"),
    ("CM", "6. Merkez Orta Saha (CM / OS(M))"),
    ("CAM", "7. Ofansif Orta Saha (CAM / OOS)"),
    ("RM_RW", "8. Sağ Kanat & Sağ Orta Saha (RM / RW)"),
    ("LM_LW", "9. Sol Kanat & Sol Orta Saha (LM / LW)"),
    ("ST_CF", "10. Santraforlar (ST / CF / SNT)"),
]


def parse_positions(s: str) -> list[str]:
    if pd.isna(s) or not str(s).strip():
        return []
    return [p.strip() for p in str(s).split(",") if p.strip()]


def primary_position_code(pos: str | float | None) -> str | None:
    toks = parse_positions(str(pos) if pd.notna(pos) else "")
    return toks[0] if toks else None


def mask_primary_isin(u: pd.DataFrame, codes: set[str]) -> pd.Series:
    prim = u["player_positions"].map(lambda x: primary_position_code(x))
    return prim.isin(codes)


def fmt_money_gbp_from_eur(eur: float) -> str:
    if pd.isna(eur) or eur <= 0:
        return "—"
    gbp = float(eur) * 0.86 / 1_000_000
    if gbp >= 100:
        return f"£{gbp:.0f}M"
    if gbp >= 10:
        return f"£{gbp:.1f}M"
    if gbp >= 1:
        return f"£{gbp:.2f}M"
    k = float(eur) * 0.86 / 1000
    return f"£{k:.0f}k"


def fmt_wage_gbp_from_eur(eur: float) -> str:
    if pd.isna(eur) or eur <= 0:
        return "—"
    gbp = float(eur) * 0.86 / 1000
    if gbp >= 1000:
        return f"£{gbp/1000:.1f}M"
    return f"£{gbp:.0f}k"


def clean_tags(tags: str, max_len: int = 48) -> str:
    if pd.isna(tags) or not str(tags).strip():
        return "—"
    t = re.sub(r"#\s*", "", str(tags))
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) > max_len:
        t = t[: max_len - 1] + "…"
    return t


def nationality_tr(name: str) -> str:
    """Basit İngilizce -> Türkçe (yaygın ülkeler)."""
    m = {
        "Turkey": "Türkiye",
        "Brazil": "Brezilya",
        "Germany": "Almanya",
        "Spain": "İspanya",
        "France": "Fransa",
        "England": "İngiltere",
        "Portugal": "Portekiz",
        "Netherlands": "Hollanda",
        "Belgium": "Belçika",
        "Argentina": "Arjantin",
        "Italy": "İtalya",
        "Croatia": "Hırvatistan",
        "Serbia": "Sırbistan",
        "Norway": "Norveç",
        "Sweden": "İsveç",
        "Denmark": "Danimarka",
        "Greece": "Yunanistan",
        "Ukraine": "Ukrayna",
        "United States": "ABD",
        "Mexico": "Meksika",
        "Japan": "Japonya",
        "South Korea": "Güney Kore",
        "Senegal": "Senegal",
        "Cameroon": "Kamerun",
        "Colombia": "Kolombiya",
        "Ecuador": "Ekvador",
        "Uruguay": "Uruguay",
        "Paraguay": "Paraguay",
        "Chile": "Şili",
        "Austria": "Avusturya",
        "Switzerland": "İsviçre",
        "Poland": "Polonya",
        "Czech Republic": "Çekya",
        "Hungary": "Macaristan",
        "Romania": "Romanya",
        "Nigeria": "Nijerya",
        "Ghana": "Gana",
        "Ivory Coast": "Fildişi Sahili",
        "Morocco": "Fas",
        "Algeria": "Cezayir",
        "Egypt": "Mısır",
        "Australia": "Avustralya",
    }
    if pd.isna(name):
        return "—"
    return m.get(str(name).strip(), str(name).strip())


def build_notes(row: pd.Series, growth: int) -> str:
    notes: list[str] = []
    nat = row.get("nationality_name")
    if nat == "Türkiye" or (pd.notna(nat) and str(nat).strip() == "Türkiye"):
        notes.append("Türk Yeteneği")
    ovr = int(row["overall"]) if pd.notna(row["overall"]) else 0
    pot = int(row["potential"]) if pd.notna(row["potential"]) else 0
    val = float(row["value_eur"]) if pd.notna(row["value_eur"]) else 0
    if ovr <= 72 and pot >= 84:
        notes.append("Hidden Gem")
    if val > 0 and val <= 5_000_000 and pot >= 83:
        notes.append("Ucuz Cevher")
    if growth >= 12:
        notes.append("High Growth")
    if pd.isna(row.get("club_name")) or str(row.get("club_name")).strip() == "":
        notes.append("Serbest Oyuncu")
    if not notes:
        notes.append("—")
    return ", ".join(dict.fromkeys(notes))


def assign_buckets(pos_codes: list[str]) -> dict[str, str]:
    """bucket -> görünen mevki etiketi (ilk eşleşme öncelikli sıra korunur)."""
    out: dict[str, str] = {}
    for code in pos_codes:
        for csv_code, bucket, label in POS_MAP:
            if code == csv_code and bucket not in out:
                out[bucket] = label
    return out


def pick_hidden_gems(df_bucket: pd.DataFrame, k: int = 6) -> pd.DataFrame:
    """Türk oyuncuları öne al; sonra düşük OVR / düşük değer / yüksek büyüme."""
    if df_bucket.empty:
        return df_bucket
    t = df_bucket["nationality_name"].astype(str).eq("Türkiye")
    df = df_bucket.copy()
    df["_is_tr"] = t
    df["_score"] = (
        df["_is_tr"].astype(int) * 1000
        + (85 - df["overall"].clip(50, 85)) * 5
        + (df["potential"] - df["overall"]) * 3
        - (df["value_eur"].fillna(1e12) / 1_000_000) * 0.01
    )
    df = df.sort_values(["_score", "potential", "overall"], ascending=[False, False, False])
    # Aynı oyuncu tekrar etmesin
    df = df.drop_duplicates(subset=["player_id"])
    return df.head(k)


def main() -> None:
    if not CSV_PATH.is_file():
        raise SystemExit(f"CSV bulunamadı: {CSV_PATH} — EAFC26-DataHub klonlayın.")

    df = pd.read_csv(CSV_PATH, low_memory=False)
    meta_date = df["fifa_update_date"].dropna().max()
    meta_ver = df["fifa_version"].iloc[0] if len(df) else "?"

    base = df[(df["potential"] >= MIN_POT) & (df["age"] <= MAX_AGE)].copy()
    base["growth"] = base["potential"] - base["overall"]

    rows_by_bucket: dict[str, list[dict]] = {b: [] for b, _ in BUCKET_ORDER}

    for _, row in base.iterrows():
        codes = parse_positions(row["player_positions"])
        buckets = assign_buckets(codes)
        if not buckets:
            continue
        display_name = row["short_name"] if pd.notna(row["short_name"]) else row["long_name"]
        club = row["club_name"]
        if pd.isna(club) or str(club).strip() == "":
            club_disp = "Serbest Oyuncu"
        else:
            club_disp = str(club).strip()
        nat_tr = nationality_tr(row["nationality_name"])
        notes = build_notes(row, int(row["growth"]))
        wf = int(row["weak_foot"]) if pd.notna(row["weak_foot"]) else 0
        sm = int(row["skill_moves"]) if pd.notna(row["skill_moves"]) else 0
        h = int(row["height_cm"]) if pd.notna(row["height_cm"]) else 0
        w = int(row["weight_kg"]) if pd.notna(row["weight_kg"]) else 0
        body = f"{h} / {w}" if h and w else "—"

        for bucket_key, mevki_label in buckets.items():
            rows_by_bucket[bucket_key].append(
                {
                    "player_id": row["player_id"],
                    "Adı": str(display_name),
                    "Uyruk": nat_tr,
                    "Mevki(ler)": f"{mevki_label} ({row['player_positions']})",
                    "Takım": club_disp,
                    "Yaş": int(row["age"]),
                    "Değer (£)": fmt_money_gbp_from_eur(row["value_eur"]),
                    "OVR": int(row["overall"]),
                    "POT": int(row["potential"]),
                    "Maaş (£)": fmt_wage_gbp_from_eur(row["wage_eur"]),
                    "Büyüme": f"+{int(row['growth'])}",
                    "Taktiksel Rol / PlayStyle": clean_tags(row.get("player_tags")),
                    "Weak Foot": f"{wf}★" if wf else "—",
                    "Skill Moves": f"{sm}★" if sm else "—",
                    "Boy / Kilo": body,
                    "Notlar": notes,
                    "_pot": int(row["potential"]),
                    "_ovr": int(row["overall"]),
                }
            )

    lines: list[str] = []
    lines.append("# FC 26 Wonderkid List - Veri Seti ile Tam Tarama (POT ≥ 82)")
    lines.append("")
    lines.append("## Giriş ve metodoloji")
    lines.append("")
    lines.append(
        "Bu dosya **otomatik üretilmiştir** (`scripts/generate_fc26_wonderkid_list.py`). "
        "Ham veri: [EAFC26-DataHub](https://github.com/ismailoksuz/EAFC26-DataHub) içindeki Kaggle tabanlı **`players.csv`** "
        f"(yaklaşık {len(df):,} oyuncu, `fifa_version`={meta_ver}, son satır tarihi **{meta_date}**). "
        "**Not:** Bu dışa aktarım, yüzünüzdeki FC 26 sürümünden (ör. Mart 2026 title update) farklı olabilir; kesin değerler için kendi kariyer save’inizdeki gözlemciyi kullanın."
    )
    lines.append("")
    lines.append(f"- **Filtre:** `potential >= {MIN_POT}`, `age <= {MAX_AGE}`")
    lines.append(
        "- **Pozisyon:** `player_positions` alanındaki her kod (GK, CB, LB, …) ilgili tabloya bir satır üretir; "
        "aynı oyuncu çok mevkiliyse **birden fazla bölümde** görünür (scout mantığı: her hat için ayrı aday)."
    )
    lines.append(
        "- **Para birimi:** `value_eur` / `wage_eur` yaklaşık **£**’ye çevrilmiştir (EUR × 0,86; maaş haftalık)."
    )
    lines.append(
        "- **Türk oyuncular:** `nationality_name == Türkiye` olanlar **Notlar** sütununda `Türk Yeteneği` ile işaretlenir; "
        "her bölüm sonundaki öneri alt başlığında önceliklendirilir."
    )
    lines.append("")
    lines.append("### Veri kapsamı özeti (bu filtreye göre)")
    lines.append("")
    counts = {k: len(v) for k, v in rows_by_bucket.items()}
    total_unique = base["player_id"].nunique()
    lines.append(f"- **Benzersiz oyuncu sayısı (filtre içi):** {total_unique}")
    lines.append("- **Tablo satır sayıları (çok mevkili tekrarlar dahil):**")
    for key, title in BUCKET_ORDER:
        lines.append(f"  - {title.split('. ', 1)[-1]}: **{counts[key]}** satır")
    lines.append("")

    header = "| Adı | Uyruk | Mevki(ler) | Takım | Yaş | Değer (£) | OVR | POT | Maaş (£) | Büyüme | Taktiksel Rol / PlayStyle | Weak Foot | Skill Moves | Boy / Kilo | Notlar |"
    sep = "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"

    for bucket_key, title in BUCKET_ORDER:
        lines.append(f"## {title}")
        lines.append("")
        bucket_rows = rows_by_bucket[bucket_key]
        bucket_rows.sort(key=lambda r: (-r["_pot"], -r["_ovr"], str(r["Adı"]).lower()))
        lines.append(header)
        lines.append(sep)
        for r in bucket_rows:
            cells = [
                str(r[c])
                for c in [
                    "Adı",
                    "Uyruk",
                    "Mevki(ler)",
                    "Takım",
                    "Yaş",
                    "Değer (£)",
                    "OVR",
                    "POT",
                    "Maaş (£)",
                    "Büyüme",
                    "Taktiksel Rol / PlayStyle",
                    "Weak Foot",
                    "Skill Moves",
                    "Boy / Kilo",
                    "Notlar",
                ]
            ]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("")

        # Hidden gems subsection: re-use dataframe slice
        ids = [r["player_id"] for r in bucket_rows]
        sub = base[base["player_id"].isin(ids)].copy()
        gems = pick_hidden_gems(sub, k=6)
        lines.append(f"### Hidden Gems & Turkish Talents Recommendation ({title.split('. ', 1)[-1]})")
        lines.append("")
        if gems.empty:
            lines.append("*Bu bölümde öneri için yeterli kayıt yok.*")
        else:
            for _, g in gems.iterrows():
                why: list[str] = []
                if str(g.get("nationality_name")) == "Türkiye":
                    why.append("Türk kadrosu için doğal hedef")
                if pd.notna(g["value_eur"]) and g["value_eur"] <= 8_000_000:
                    why.append("düşük piyasa değeri")
                if int(g["potential"] - g["overall"]) >= 10:
                    why.append("güçlü büyüme payı")
                if int(g["overall"]) <= 74:
                    why.append("düşük başlangıç OVR ile gizli cevher profili")
                reason = "; ".join(why) if why else "yüksek POT / rol esnekliği"
                lines.append(
                    f"- **{g['short_name'] if pd.notna(g['short_name']) else g['long_name']}** "
                    f"({g['club_name'] if pd.notna(g['club_name']) else 'Serbest Oyuncu'}) — OVR {int(g['overall'])}, POT {int(g['potential'])}: {reason}."
                )
        lines.append("")

    # Bonus sections from full filtered set (unique players)
    u = base.drop_duplicates(subset=["player_id"]).copy()
    u["growth"] = u["potential"] - u["overall"]

    lines.append("## Bonus: Overall Top 11 Wonderkid XI (veri setine göre)")
    lines.append("")
    lines.append(
        "Formasyon: **4-3-3** (geniş). Her slotta **birincil mevki** (`player_positions` içinde virgülden önceki kod) kullanılır; "
        "böylece örn. `CM, CDM` oyuncuları CDM değil CM hattında değerlendirilir. Seçim: en yüksek POT (eşitlikte OVR); aynı oyuncu iki kez kullanılmaz."
    )
    lines.append("")

    def top_for(mask: pd.Series, n: int = 1, skip: set[int] | None = None) -> list[pd.Series]:
        skip = skip or set()
        sub = u[mask].sort_values(["potential", "overall"], ascending=False)
        out: list[pd.Series] = []
        for _, r in sub.iterrows():
            pid = int(r["player_id"])
            if pid in skip:
                continue
            out.append(r)
            if len(out) >= n:
                break
        return out

    def xi_name(r: pd.Series) -> str:
        return str(r["short_name"]) if pd.notna(r["short_name"]) else str(r["long_name"])

    used_xi: set[int] = set()
    xi_slots: list[tuple[str, list[pd.Series], bool]] = []

    gk = top_for(mask_primary_isin(u, {"GK"}), 1, used_xi)
    if gk:
        used_xi.add(int(gk[0]["player_id"]))
    xi_slots.append(("KL", gk, False))

    rb = top_for(mask_primary_isin(u, {"RB", "RWB"}), 1, used_xi)
    if rb:
        used_xi.add(int(rb[0]["player_id"]))
    xi_slots.append(("D(Sağ)", rb, False))

    cbs = top_for(mask_primary_isin(u, {"CB", "LCB", "RCB"}), 2, used_xi)
    for r in cbs:
        used_xi.add(int(r["player_id"]))
    xi_slots.append(("D(M)", cbs, True))

    lb = top_for(mask_primary_isin(u, {"LB", "LWB"}), 1, used_xi)
    if lb:
        used_xi.add(int(lb[0]["player_id"]))
    xi_slots.append(("D(Sol)", lb, False))

    cdm = top_for(mask_primary_isin(u, {"CDM", "LDM", "RDM"}), 1, used_xi)
    if cdm:
        used_xi.add(int(cdm[0]["player_id"]))
    xi_slots.append(("DOS", cdm, False))

    cms = top_for(mask_primary_isin(u, {"CM", "LCM", "RCM"}), 2, used_xi)
    for r in cms:
        used_xi.add(int(r["player_id"]))
    xi_slots.append(("OS(M)", cms, True))

    rm = top_for(mask_primary_isin(u, {"RM", "RW", "RF"}), 1, used_xi)
    if rm:
        used_xi.add(int(rm[0]["player_id"]))
    xi_slots.append(("RM/RW", rm, False))

    lm = top_for(mask_primary_isin(u, {"LM", "LW", "LF"}), 1, used_xi)
    if lm:
        used_xi.add(int(lm[0]["player_id"]))
    xi_slots.append(("LM/LW", lm, False))

    st = top_for(mask_primary_isin(u, {"ST", "CF"}), 1, used_xi)
    xi_slots.append(("SNT", st, False))

    lines.append("| Pozisyon | Oyuncu | Takım | OVR | POT |")
    lines.append("|---|---|---|---|---|")
    for label, players, multi in xi_slots:
        if not players:
            lines.append(f"| {label} | — | — | — | — |")
            continue
        if multi:
            for i, r in enumerate(players[:2], start=1):
                cl = r["club_name"] if pd.notna(r["club_name"]) else "Serbest Oyuncu"
                lines.append(f"| {label} #{i} | {xi_name(r)} | {cl} | {int(r['overall'])} | {int(r['potential'])} |")
            if len(players) < 2:
                lines.append(f"| {label} #2 | — | — | — | — |")
        else:
            r = players[0]
            cl = r["club_name"] if pd.notna(r["club_name"]) else "Serbest Oyuncu"
            lines.append(f"| {label} | {xi_name(r)} | {cl} | {int(r['overall'])} | {int(r['potential'])} |")
    lines.append("")

    lines.append("## Bonus: Budget Wonderkid Team (~£50M)")
    lines.append("")
    lines.append(
        "Aşağıdaki kadro, filtrelenmiş havuzdan **düşük `value_eur`** ve **yüksek `potential - overall`** skoruna göre otomatik seçilmiştir; "
        "transfer ücretleri oyun içi pazarlıkla değişir."
    )
    lines.append("")
    bud = u.copy()
    bud["_cheap"] = bud["value_eur"].fillna(999_999_999)
    bud["_grow"] = bud["potential"] - bud["overall"]
    bud = bud.sort_values(["_cheap", "_grow"], ascending=[True, False])

    need = [
        ("KL", lambda s: "GK" in s),
        ("RB", lambda s: bool(re.search(r"\bRB\b|RWB", s))),
        ("CB", lambda s: bool(re.search(r"\bCB\b|LCB|RCB", s))),
        ("CB", lambda s: bool(re.search(r"\bCB\b|LCB|RCB", s))),
        ("LB", lambda s: bool(re.search(r"\bLB\b|LWB", s))),
        ("CDM", lambda s: bool(re.search(r"\bCDM\b|LDM|RDM", s))),
        ("CM", lambda s: bool(re.search(r"\bCM\b|LCM|RCM", s))),
        ("CAM", lambda s: bool(re.search(r"\bCAM\b|LAM|RAM", s))),
        ("RM", lambda s: bool(re.search(r"\bRM\b|RW|RF", s))),
        ("LM", lambda s: bool(re.search(r"\bLM\b|LW|LF", s))),
        ("ST", lambda s: bool(re.search(r"\bST\b|\bCF\b", s))),
    ]
    picked: list[tuple[str, pd.Series]] = []
    used: set[int] = set()
    for label, pred in need:
        for _, r in bud.iterrows():
            pid = int(r["player_id"])
            if pid in used:
                continue
            pos = str(r["player_positions"])
            if pred(pos):
                picked.append((label, r))
                used.add(pid)
                break

    lines.append("| Rol | Oyuncu | Takım | Değer (£) | OVR | POT |")
    lines.append("|---|---|---|---|---|---|")
    total_gbp = 0.0
    for label, r in picked:
        v = float(r["value_eur"]) if pd.notna(r["value_eur"]) else 0
        total_gbp += v * 0.86
        nm = r["short_name"] if pd.notna(r["short_name"]) else r["long_name"]
        cl = r["club_name"] if pd.notna(r["club_name"]) else "Serbest Oyuncu"
        lines.append(
            f"| {label} | {nm} | {cl} | {fmt_money_gbp_from_eur(r['value_eur'])} | {int(r['overall'])} | {int(r['potential'])} |"
        )
    lines.append("")
    lines.append(f"- **Yaklaşık toplam değer (liste fiyatı, £):** £{total_gbp/1_000_000:.1f}M")
    lines.append("")

    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_PATH} ({OUT_PATH.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
