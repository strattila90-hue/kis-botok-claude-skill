#!/bin/bash
# SessionStart: skill-keret ellenőrzés. A kimenet bekerül a munkamenet kontextusába.
# Soha nem akasztja meg az indulást (mindig 0-val lép ki), nem telepít semmit.
set -uo pipefail

root="${CLAUDE_PROJECT_DIR:-.}"
script="$root/scripts/skill-check.py"
[ -f "$script" ] || exit 0
command -v python3 >/dev/null || exit 0

out="$(python3 "$script" "$root" 2>&1)"; rc=$?

# Csak akkor szólunk, ha van tennivaló (figyelmeztetés vagy hiba).
if [ $rc -ne 0 ] || printf '%s' "$out" | grep -qE '^(FIGYELEM|HIBA):'; then
  echo "SKILL-KERET FIGYELMEZTETÉS (kezdés előtt jelezd a felhasználónak):"
  printf '%s\n' "$out"
fi
exit 0
