# AI pravidlá pre tento repozitár

Tieto pravidlá platia pre AI asistenta aj pre človeka, ktorý upravuje obsah repozitára.

## Jazyk

- Primárny jazyk je slovenčina.
- Názvy súborov môžu byť anglické kvôli praxi v GitHube.
- Texty pre YouTube píš prirodzene, kultivovane a bez prehnaného marketingového klišé.
- NESIA TALKSHOW má pôsobiť ľudsky, hodnotovo a dôveryhodne, nie ako agresívna predajná relácia.

## Presnosť

- Nevymýšľaj fakty o hosťoch, firmách, produktoch, miestach, dátumoch ani citácie.
- Ak údaj chýba, použi `DOPLNIŤ`, `NEOVERENÉ` alebo `null`.
- Rozlišuj medzi faktom, interpretáciou a návrhom.
- Pri tvorbe nových nadpisov a popisov vychádzaj z prepisu, briefu, pravidiel a už publikovaných videí.
- Ak chýba transcript, výsledok označ ako draft.

## Oddelenie vrstiev

Nemixuj tieto veci do jedného súboru:

```text
source-metadata.yaml  = štruktúrované fakty a dostupnosť údajov
raw-input.md          = presne dodané podklady od používateľa
audio/video transcript = source-transcript.md
source-description.md = pôvodný YouTube popis, ak existuje
analysis.md           = interpretácia toho, čo fungovalo
rules/talkshow/       = schválené alebo draft pravidlá pre budúcnosť
outputs/talkshow/     = hotové publikačné balíky pre nové videá
```

Ak si nie si istý, či údaj patrí medzi fakty alebo interpretáciu, daj ho radšej do `analysis.md` a označ ho ako pracovný postreh.

## Verejný repozitár

Repo môže byť verejné. Preto:

- nevkladaj nečistené YouTube Studio exporty,
- nevkladaj interné retencie, CTR, watch time, zdroje návštevnosti ani rozpočty,
- nevkladaj súkromné kontakty, zmluvy, ceny, interné dohody alebo osobné údaje,
- veľké video a audio súbory ukladaj mimo GitHub, napríklad do Drive alebo archívu,
- do GitHubu vkladaj len odkazy, verejné metadáta, texty, prepisy a schválené pracovné poznámky.

Ak bude potrebné pracovať s neverejnými dátami, vytvor samostatný private zdroj mimo tohto public repa alebo dáta anonymizuj.

## YouTube metadáta

- Nadpis má byť zrozumiteľný bez kontextu.
- Popis má mať jasný úvod, obsah epizódy, CTA, odkazy a hashtagy.
- Hashtagy musia priamo súvisieť s videom.
- Tagy sú doplnkové, nie hlavný nástroj objavovania.
- Nepoužívaj zavádzajúce, nadmerné alebo spamové metadáta.
- Výstup musí prejsť ľudskou kontrolou pred publikovaním.

## Workflow zmien

- Pri doplnení údajov existujúceho videa aktualizuj aj `content/talkshow/missing-data-tracker.md`.
- Pri väčšej zmene pravidiel aktualizuj `CHANGELOG.md`.
- Nové video typy pridávaj ako samostatné priečinky pod `content/`, `rules/`, `templates/` a `prompts/`.
