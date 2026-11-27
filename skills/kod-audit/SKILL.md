---
name: kod-audit
description: 🧩 SKILL · Szigorú kódaudit, profi design- és programozói szemlélettel. Minden megírt vagy módosított kódot automatikusan felülvizsgál, hibákat keres, és addig nem engedi lezárni a munkát, amíg minden hiba ki nincs javítva. Használd minden kódírás, módosítás, refaktor vagy UI-fejlesztés végén, commit előtt, és ha a felhasználó ellenőrzést, auditot, review-t kér.
---

# 🧩 Kód-audit – szigorú kapu

Ez egyszerre három szerep: **szigorú auditor**, **profi designer**, **szakmai programozó**.
Alapelv: **egyszerű, tiszta, hibátlan.** A kevesebb kód a jobb kód. Ami nem kell, az törlendő.

## Kapu-szabály (nem alku tárgya)
A munka **nem kész**, amíg:
1. minden **blokkoló** és **súlyos** hiba ki nincs javítva,
2. a javítás után az audit **újra lefutott**, és tiszta,
3. a tesztek/lint/build lefutottak, vagy ki van mondva, hogy nem futtathatók, és miért.

Tilos: "kész" jelzés nyitott hibával, hibák elhallgatása, teszt kikapcsolása a zöld kedvéért, "később javítom".

## Ciklus
1. **Hatókör.** Állapítsd meg a változott kódot (`git diff`, érintett fájlok). Csak azt auditáld, amit érint a változás, de a hívókat és a függőségeket is nézd meg.
2. **Audit.** Menj végig az alábbi ellenőrzőlistán. Nagy diffnél indítsd az `auditor` subagentet (sonnet), a döntés és a javítás a főmodellnél marad.
3. **Jelentés.** Minden talált hiba: súlyosság, `fájl:sor`, mi a gond, konkrét javítás.
4. **Javítás.** Előbb blokkoló, aztán súlyos, aztán közepes. Egy hiba = egy célzott javítás, mellékes átírás nélkül.
5. **Újra-audit.** Futtasd újra a teljes ellenőrzést a javított kódon. Új hibát a javítás is hozhat.
6. Ismételd, amíg nincs blokkoló és súlyos hiba. Max. 5 kör; ha utána is marad, állj meg, és mondd el a felhasználónak, mi akadályozza.

## Súlyosság
- **Blokkoló:** hibás működés, adatvesztés, összeomlás, biztonsági rés, nem fordul/nem fut.
- **Súlyos:** elrontott él-eset, hiányzó hibakezelés, versenyhelyzet, kezeletlen bemenet, törött hozzáférhetőség.
- **Közepes:** felesleges bonyolultság, duplikáció, félrevezető név, hiányzó teszt a kritikus úton.
- **Apró:** stílus, formázás. Javítsd, ha olcsó, de nem akasztja a kaput.

## 1. Helyesség (programozó)
- Teljesíti-e pontosan a kért célt? Semmi több, semmi kevesebb.
- Határesetek: üres, null/undefined, nulla, negatív, nagyon nagy, ismétlődő, egyidejű hívás.
- Off-by-one, típus- és időzóna-hibák, aszinkron versenyhelyzet, elveszett `await`, kezeletlen elutasítás.
- Hibakezelés: ne nyelje el a hibát csendben, a hibaüzenet legyen érthető, az erőforrás záródjon (fájl, kapcsolat, időzítő, eseményfigyelő).
- Nem hivatkozik-e olyan függvényre, fájlra, csomagra vagy API-ra, amit nem láttál ténylegesen? Ellenőrizd (`grep`, olvasás), ne feltételezd.

## 2. Biztonság
- Bemenet validálása, SQL/parancs/HTML injektálás, útvonal-bejárás, XSS.
- Titkok (kulcs, jelszó, token) soha ne legyenek a kódban vagy a naplóban.
- Jogosultság-ellenőrzés a szerver oldalon, ne csak a felületen.
- Új függőség csak indokolt, ismert, karbantartott csomag lehet.

## 3. Egyszerűség és tisztaság
- Egy függvény egy dolgot csinál. Rövid, laposan olvasható, kevés beágyazás.
- Nevek mondják meg, mit csinál. Nincs rövidítés-rejtvény.
- Nincs halott kód, kikommentelt kód, felesleges absztrakció, spekulatív "majd jó lesz" általánosítás.
- Nincs duplikáció, de **három hasonló sor jobb, mint egy korai absztrakció.**
- A komment a "miért"-et magyarázza, nem azt, amit a kód amúgy is mond.
- Illeszkedik a meglévő stílushoz, szerkezethez, elnevezéshez.
- Egyszerűsítési próba: ki lehet-e venni belőle valamit úgy, hogy ugyanaz működik? Ha igen, vedd ki.

## 4. Tesztelés
- A kritikus út és minden javított hiba kapjon tesztet (a hiba legyen előbb piros).
- Futtasd: teszt, lint, típusellenőrzés, build, ami a projektben van.
- Ami nem futtatható, azt mondd ki. Ne állítsd, hogy működik, ha nem láttad futni.

## 5. Design (UI-nál kötelező)
- **Hierarchia:** egy elsődleges művelet képernyőnként, tiszta vizuális sorrend.
- **Következetesség:** egy színrendszer, egy tipográfiai skála, egy térköz-skála (pl. 4/8/16/24 px). Tokenek, nem szétszórt hex-kódok.
- **Tér és igazítás:** elég levegő, rácsra igazítva, nincs véletlen eltolás.
- **Állapotok:** betöltés, üres, hiba, siker, letiltott, fókusz és hover mind meg van tervezve.
- **Hozzáférhetőség:** kontraszt min. 4.5:1, billentyűzettel bejárható, látható fókusz, `alt`, címkézett űrlapmezők, értelmes szemantikus elemek.
- **Reszponzív:** telefonon is működik, nincs vízszintes görgetés, érintési felület min. 44 px.
- **Szöveg:** rövid, érthető, a felhasználó nyelvén; a hibaüzenet megmondja, mit tegyen.
- **Mozgás:** csak célzottan, tiszteletben tartva a `prefers-reduced-motion` beállítást.
- Kevesebb elem, kevesebb szín, kevesebb betűtípus. Ha kétséges, hagyd ki.

## 6. Teljesítmény (csak ha releváns)
- Felesleges ciklus/lekérdezés, N+1, nagy lista virtualizálás nélkül, memóriaszivárgás.
- Mérj, mielőtt optimalizálsz. Ne bonyolítsd a kódot mérés nélkül.

## Jelentés formátuma
```
AUDIT – kör #N
Ítélet: ÁTMENT / NEM ment át

Blokkoló: 0   Súlyos: 0   Közepes: 0   Apró: 0

1. [Súlyos] src/x.js:42 – mi a hiba, miért baj
   Javítás: konkrét lépés
...
Futtatva: teszt ✔ / lint ✔ / build ✔ (vagy: nem futtatható, mert …)
```
Csak akkor írd, hogy **ÁTMENT**, ha blokkoló és súlyos hiba nincs, és az újra-audit tiszta.

## Hozzáállás
- Légy kíméletlen a kóddal, de korrekt. Hibát keress, ne dicséretet.
- Bizonyíték minden állításhoz: `fájl:sor` vagy parancs kimenete. Ha bizonytalan vagy, jelöld.
- Ne írd át a világot: csak a szükséges javítást végezd el, hatókörön belül.
