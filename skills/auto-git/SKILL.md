---
name: auto-git
description: Automatikus és önálló git-munkafolyamat kérdezés nélkül. Ha egy repóhoz hozzá van adva, a kész és auditált munkát magától commitolja, ágra pusholja, és mainbe mergeli. Használd minden befejezett kódmunka végén, amikor a felhasználó előre engedélyezte az önálló commitot és mergelést.
---

# Auto-git – önálló commit, push és merge

A felhasználó ezzel a skillel **előre, tartósan engedélyezte**, hogy a munka végén kérdezés nélkül commitolj, pushölj és mergelj mainbe. Ne kérdezz rá minden lépésnél, csak tedd meg. A "kész?" kérdés helyett a kapu dönt.

## Kapu (kötelező, ez véd, nem a kérdés)
Csak akkor commitolj és mergelj, ha:
1. a `kod-audit` skill utolsó köre **ÁTMENT** (nincs blokkoló és súlyos hiba),
2. a projekt tesztjei, lintje és buildje zöldek (vagy nincsenek, és ez ki van mondva),
3. nincs a változásban titok (kulcs, jelszó, token, `.env`, hitelesítő fájl).

Ha a kapu nem teljesül: **ne commitolj mainbe.** Javítsd a hibát, futtasd újra az auditot. Ha 5 kör után sem megy át, állj meg, és mondd el a felhasználónak, mi az akadály. Ez az egyetlen eset, amikor szólsz.

## Folyamat
1. **Állapot.** `git status`, `git diff`. Ellenőrizd, hogy csak a feladathoz tartozó fájlok változtak. Ne add hozzá a nem kapcsolódó vagy generált fájlokat (`node_modules`, build-kimenet, naplók).
2. **Ág.** Ha mainen vagy, hozz létre feature ágat (`feat/…`, `fix/…`, `chore/…`, rövid, beszédes névvel). Ne commitolj közvetlenül egy félkész állapotú mainre.
3. **Commit.** Egy logikai változtatás = egy commit. Az üzenet magyarázza a "miért"-et:
   - első sor max. ~70 karakter, felszólító mód (pl. `Fix: üres lista kezelése`),
   - üres sor, majd rövid indoklás, ha nem triviális.
   Kerüld a `git add -A` vakon; a fájlokat név szerint add hozzá, vagy nézd át előtte a státuszt.
4. **Push.** `git push -u origin <ág>`. Hálózati hibánál próbáld újra legfeljebb 4-szer, növekvő várakozással.
5. **Merge mainbe.**
   - Előbb szinkronizálj: `git fetch origin`, majd az ágat vezesd rá a friss mainre (`git merge origin/main` az ágon, vagy rebase, ha az ág csak a tiéd).
   - Konfliktusnál oldd meg gondosan, mindkét oldal szándékát megtartva, utána **futtasd újra a teszteket és az auditot.**
   - Ha van PR-folyamat és a védett main ezt megköveteli: nyiss PR-t, várd meg, hogy a CI zöld legyen, aztán mergeld (squash, ha az ág sok apró commitot tartalmaz). Ha nincs védelem: `git checkout main && git pull && git merge --no-ff <ág> && git push origin main`.
6. **Takarítás.** A mergelt ágat töröld (helyben és távol is). Utána `git status` legyen tiszta.
7. **Jelentés.** Egy-két sorban: mi került be, melyik commit, zöld volt-e a kapu.

## Soha nem csinálhatod (kérdés nélkül sem)
- `git push --force` / `--force-with-lease` mainre, vagy bármilyen közös ágra. Előzmény-átírás (`reset --hard` pusholt commitokon, `rebase` közös ágon).
- Teszt, lint vagy CI kikapcsolása, kihagyása (`--no-verify`, kikommentelt teszt) a zöld kedvéért.
- Titok, hitelesítő adat vagy személyes adat commitolása. Ha véletlenül bekerült: állj meg, ne pusholj, jelezd.
- Más ember még nem mergelt munkájának felülírása. Ha a távoli ág tartalmaz olyan commitot, ami nálad nincs, előbb mergeld be (`git fetch` + `git merge`), ne írd felül.
- Törlés, amit nem te hoztál létre (más ágak, címkék).
- Nem a feladathoz tartozó fájlok commitolása.

## Ha elakad
- Védett main, jogosultsághiba, hibás CI vagy feloldhatatlan konfliktus: ne kerüld meg. Hagyd az ágat pusholva, és jelentsd pontosan, mi blokkol.
- Ha a repóban saját szabály van az ágelnevezésre vagy az üzenetformátumra (pl. `CONTRIBUTING.md`, `CLAUDE.md`), az felülírja az itteni alapértelmezést.
