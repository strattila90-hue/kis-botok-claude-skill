---
name: kis-botok
description: Hatékony többlépcsős munka subagentekkel, kódoláshoz és app-fejlesztéshez is. Nagyobb, több részből álló feladatnál a fő modell tervez és szintetizál, a rutinmunkát olcsóbb subagentek végzik, és a fő kontextus tiszta marad. Használd kutatásnál, több fájl átnézésénél, összehasonlításnál, hibakeresésnél, refaktornál vagy ha a feladat független részekre bontható.
---

# Kis botok – hatékony subagent-munka

## Döntés: kell-e subagent?
- **Igen**, ha 3+ független részfeladat van, sok fájlt vagy nagy kimenetet kell átnézni, kutatás vagy összehasonlítás a cél, vagy app-fejlesztésnél külön réteg (UI, adatmodell, logika, tesztek) is van.
- **Nem**, ha a feladat egyetlen fájlos változtatás, rövid kérdés, vagy a részek egymástól függnek. Ilyenkor a subagent csak tokent pazarol, a főmodell maga csinálja.

## Modellválasztás
- **Főmodell** (tervezés, döntés, kódírás, szintézis): Opus 5.5 kódolásnál és app-fejlesztésnél.
- **Rutinbotok** (keresés, olvasás, kivonatolás): `haiku`.
- **Ellenőrzés** (ítélet, kódellenőrzés): `sonnet`.
- A végső döntés és a szerkesztés mindig a főmodellnél marad.

## Subagentek

Ezek a subagentek a `agents/` mappában vannak. Használd őket az alábbi célokra:

- Kutatás, fájlolvasás, kivonatolás, dokumentáció-keresés → `kutato`
- Egy változtatás vagy eredmény ellenőrzése a célhoz képest → `ellenorzo`
- Több részeredmény egy tiszta összefoglalóba rendezése → `osszefoglalo`
- Megírt vagy módosított kód szigorú auditja, hibakeresés és javíttatás → `kod-audit` skill (`auditor` subagent)

Ha a kódolás részfeladatai (pl. UI, adatmodell, tesztek) függetlenek, saját megbízással is indíthatók subagentek. Ilyenkor a főmodell marad az, aki a fájlokat összeilleszti.

- Kész, auditált munka önálló commitja és mergelése → `auto-git` skill

## Munkamenet

1. **Cél és kimenet.** Egy mondatban rögzítsd, mi kell, és milyen formában (kód, döntés, lista, dokumentum).
2. **Kontextus felmérés.** Mielőtt botot indítasz, nézd meg a releváns fájlokat a repóban. A botok ne találgassanak a projekt szerkezetéről.
3. **Felbontás.** 2–5 független részfeladat. Többet ne, mert minden bot külön költség.
4. **Megbízás.** Minden subagent kapjon szűk, önálló leírást:
   - a saját részfeladata
   - a bemenet (fájlútvonal, URL, adat)
   - a kimenet formátuma és maximális hossza
   - mit NE csináljon (pl. „ne írj kódot, csak olvass")
5. **Párhuzamos futtatás.** A független botok egyszerre fussanak.
6. **Ellenőrzés.** Kódnál mindig futtasd a `kod-audit` skillt, és addig ne zárd le, amíg tiszta. Döntésnél teszt, lint vagy `ellenorzo`. Rutin kivonatolásnál nem kell.
7. **Szintézis.** A főmodell tömör összefoglalót ír, és elvégzi a végleges változtatásokat. A subagentek nyers kimenetét nem másolja be.

## Kódolási szabályok
- Mielőtt módosítasz, olvasd el a meglévő kódot és a stílust. Ne vezess be új függőséget engedély nélkül.
- Egy logikai változtatás = egy összefüggő módosítás. Ne keverd a refaktort és a funkciót.
- Ha tesztek vannak, futtasd őket. Ha nincsenek, jelezd a felhasználónak, és javasolj minimális tesztet.
- Ne írj olyan kódot, amelyet nem tudsz futtatni vagy ellenőrizni, és ezt jelezd.

## Kimeneti elvek
- Először a lényeg, utána a részletek.
- Rövid bekezdések, értelmes címek. Táblázat csak valódi összehasonlításnál.
- Forrás (fájl:sor vagy URL) minden fontos állításhoz.
- Bizonytalanság külön jelölve.
- A nyelv a felhasználó nyelve.

## Költséghatárok
- Max. 5 subagent egy feladatra.
- Ha egy subagent kimenete 500 szó fölé nőne, kérd rövidebbre.
- Ugyanazt a fájlt ne olvassa több bot.
