# kis-botok

Hatékony, subagent-alapú munkavégzés Claude Code-ban. A fő modell tervez és szintetizál, a rutinmunkát olcsóbb subagentek végzik, így a heti keret tovább tart.

## Telepítés
- **Claude Code:** a gyökér `SKILL.md`-t másold a `~/.claude/skills/kis-botok/` alá, a `skills/*` mappákat a `~/.claude/skills/` alá, a `kutato.md`, `ellenorzo.md`, `osszefoglalo.md`, `auditor.md` fájlokat a `~/.claude/agents/` alá.
- **Claude.ai:** a skill-mappákat (benne a `SKILL.md`-vel) egyenként zip-ben töltsd fel a beállításokban.

## Tartalom

> 🧩 **SKILL** jelölés: minden skill leírása `🧩 SKILL · ` előtaggal kezdődik, a címe `# 🧩` jellel, így a skill-listában és a fájlban is azonnal látszik, hogy skillről van szó. A `name` mező szándékosan sima (kisbetű, kötőjel), mert a Claude csak ilyet fogad el. A `skill-check.py` szól, ha egy skillről hiányzik a jelölés.

| | Skill | Mit csinál |
|---|---|---|
| 🧩 | **`kis-botok`** | mikor és hogyan használj subagenteket |
| 🧩 | **`kod-audit`** | szigorú kódaudit + design + szakmai programozó szemlélet; addig nem engedi lezárni a munkát, amíg a hibák ki nincsenek javítva |
| 🧩 | **`auto-git`** | a kész, auditált munkát kérdés nélkül, önállóan commitolja, pusholja és mainbe mergeli az állandó `munka` ágról (kapuval és tiltott műveletekkel védve) |
| 🧩 | **`skill-keret`** | + `scripts/skill-check.py`: számolja a skilleket, figyelmeztet, ha túl sok, túl hosszú vagy jelöletlen |

Egyéb:
- 🤖 `kutato`, `ellenorzo`, `osszefoglalo`, `auditor`: előre beállított subagentek
- 🪝 `.claude/hooks/session-start.sh`: SessionStart hook, minden munkamenet elején lefuttatja a skill-check-et, és csak akkor szól, ha gond van (a repóra érvényes; más repóba a `scripts/` és `.claude/` mappát is másold át)
