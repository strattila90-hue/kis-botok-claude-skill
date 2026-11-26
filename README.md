# kis-botok

Hatékony, subagent-alapú munkavégzés Claude Code-ban. A fő modell tervez és szintetizál, a rutinmunkát olcsóbb subagentek végzik, így a heti keret tovább tart.

## Telepítés
- **Claude Code:** másold a `skills/kis-botok/` mappát a `~/.claude/skills/` alá, az `agents/` fájljait pedig a `~/.claude/agents/` alá.
- **Claude.ai:** a `skills/kis-botok/` mappát zip-ben töltsd fel a beállításokban.

## Tartalom
- `kis-botok` skill: mikor és hogyan használj subagenteket
- `kod-audit` skill: szigorú kódaudit + design + szakmai programozó szemlélet; addig nem engedi lezárni a munkát, amíg a hibák ki nincsenek javítva
- `kutato`, `ellenorzo`, `osszefoglalo`, `auditor`: előre beállított subagentek
