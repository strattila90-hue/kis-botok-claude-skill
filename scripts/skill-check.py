#!/usr/bin/env python3
"""Skill-keret ellenőrző: számolja a skilleket, és figyelmeztet, ha túl sok vagy túl hosszú.
Használat: python3 scripts/skill-check.py [repo-útvonal]   (hibakód 1, ha kemény hiba van)"""
import re, sys
from pathlib import Path

MAX_NAME, MAX_DESC = 64, 1024      # kemény korlát
WARN_COUNT, MAX_COUNT = 12, 25     # figyelmeztetés / erős figyelmeztetés
WARN_TOTAL = 6000                  # összes leírás karakterszáma
WARN_BODY_LINES = 300              # SKILL.md törzs hossza
BADGE = "🧩 SKILL"                  # látható skill-jelölés a leírás elején

root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
files = sorted(p for p in root.rglob("SKILL.md") if ".git" not in p.parts)
errors, warns, total, rows = [], [], 0, []

for f in files:
    text = f.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        errors.append(f"{f}: hiányzik a frontmatter"); continue
    meta = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
    name, desc = meta.get("name", ""), meta.get("description", "")
    lines = m.group(2).count("\n")
    total += len(desc)
    rows.append((name or "?", len(desc), lines))
    if not name or not desc: errors.append(f"{f}: name/description hiányzik")
    if len(name) > MAX_NAME: errors.append(f"{name}: név > {MAX_NAME} karakter")
    if len(desc) > MAX_DESC: errors.append(f"{name}: leírás {len(desc)} > {MAX_DESC} karakter")
    if not desc.startswith(BADGE): warns.append(f"{name}: a leírás nem '{BADGE} · ' jelöléssel kezdődik")
    if lines > WARN_BODY_LINES: warns.append(f"{name}: {lines} soros törzs, vidd külön fájlba a részleteket")

n = len(files)
if n > MAX_COUNT: warns.append(f"TÚL SOK skill ({n} > {MAX_COUNT}): a kiválasztás pontatlan lesz, vonj össze vagy törölj")
elif n > WARN_COUNT: warns.append(f"Sok skill ({n} > {WARN_COUNT}): vonj össze átfedőket, élesítsd a leírásokat")
if total > WARN_TOTAL: warns.append(f"Leírások együtt {total} karakter (> {WARN_TOTAL}): rövidítsd őket")

print(f"{n} skill, leírások összesen {total} karakter")
for name, d, l in rows: print(f"  {name:20} leírás {d:4}  törzs {l:4} sor")
for w in warns: print("FIGYELEM:", w)
for e in errors: print("HIBA:", e)
if not warns and not errors: print("Rendben.")
sys.exit(1 if errors else 0)
