---
name: skill-keret
description: Skill-mennyiség őrzése. Futtasd, amikor új skillt adsz hozzá, skillt módosítasz, vagy a skillek száma, hossza vagy pontatlan kiválasztása miatt aggódsz. Figyelmeztet, ha túl sok vagy túl hosszú a skill.
---

# Skill-keret

Új vagy módosított skill után futtasd: `python3 scripts/skill-check.py`

- **Hiba** (kemény korlát: név > 64, leírás > 1024 karakter, hiányzó mező): javítsd, mielőtt továbblépsz.
- **Figyelem** (> 12 skill, > 25 skill, leírások > 6000 karakter, törzs > 300 sor): jelezd a felhasználónak, és javasolj konkrétan egyesítést, rövidítést vagy törlést.

Hatékony skill: egy egyedi, konkrét "mikor használd" leírás, rövid törzs, a hosszú részletek külön fájlban. Ne adj hozzá skillt, ha egy meglévő bővítése is elég.
