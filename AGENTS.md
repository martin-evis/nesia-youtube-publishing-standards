# AI pravidlá pre tento repozitár

Tieto pravidlá platia pre AI asistenta alebo kohokoľvek, kto upravuje súbory v repozitári.

## Jazyk

- Primárny jazyk je slovenčina.
- Názvy súborov môžu byť anglické kvôli GitHub praxi.
- Texty určené na YouTube NESIA píš v prirodzenej slovenčine bez prehnaného marketingového klišé.
- Používaj diakritiku a jasné formulácie.

## Presnosť

- Nevymýšľaj fakty o hosťoch, firmách, produktoch, miestach ani udalostiach.
- Ak údaj chýba, použi značku `DOPLNIŤ`, `NEOVERENÉ` alebo `NEDOSTUPNÉ`.
- Pri tvorbe nadpisov a popisov vychádzaj z prepisu videa, poznámok od tímu a už zverejnených videí.
- Výkonové alebo analytické tvrdenia označ ako verejné, interné alebo neoverené podľa zdroja.

## Dôležitá štruktúra dát

Nemiešaj tieto vrstvy:

```text
source-metadata.yaml     = fakty, metadáta a stav dostupnosti údajov
raw-input.md             = pôvodné údaje dodané tímom / používateľom
source-description.md    = pôvodný YouTube popis, ak je dostupný
source-transcript.md     = transcript / prepis, ak je dostupný
analysis.md              = interpretácia a pozorovania
performance-notes.md     = výkonové poznámky a zdroj dát
rules/talkshow/*.md      = schválené alebo draft pravidlá
```

Ak je poznámka iba interpretácia, neukladaj ju ako fakt do YAML bez označenia.

## YouTube pravidlá

- Dodržiavaj oficiálne limity YouTube: názov max. 100 znakov, popis max. 5 000 znakov.
- Hashtagy musia byť relevantné a bez medzier.
- Nepoužívaj nepravdivé, zavádzajúce alebo nadmerné metadáta.
- Tagy sú doplnkové, nie hlavný nástroj objavovania.
- Pri chýbajúcom transcripte označ výstup ako draft.

## Pravidlá pre verejný repozitár

Repo je aktuálne verejné. Preto doň nevkladaj:

- heslá,
- prístupové tokeny,
- súkromné kontakty,
- interné rozpočty,
- neverejné YouTube Studio exporty,
- interné strategické poznámky,
- osobné údaje, ktoré nie sú už verejne súčasťou videa.

Ak sa majú ukladať interné výkonové dáta zo Studia, odporúčané riešenie je private repo alebo samostatná private dátová vrstva.

## Štruktúra zmien

- Pre TALKSHOW zdrojové dáta upravuj primárne v `content/talkshow/`.
- Pravidlá a šablóny pre TALKSHOW upravuj v `rules/talkshow/`, `templates/talkshow/` a `video-types/talkshow/`.
- Nové video typy pridávaj ako samostatné priečinky do `content/`, `rules/`, `templates/` a `video-types/`.
- Každá väčšia zmena má mať zápis v `CHANGELOG.md`.

## Stavové označenia

Používaj jednotné hodnoty:

```text
available        = údaj je dostupný
missing          = údaj chýba a treba ho doplniť
not_available    = údaj sa nedá získať z aktuálneho zdroja
unknown          = nevieme, či údaj existuje
needs_review     = údaj treba skontrolovať človekom
needs_followup   = treba sa k nemu vrátiť neskôr
```

## Tvorba nových YouTube výstupov

Pri tvorbe nového publikačného balíka vždy:

1. prečítaj príslušné pravidlá,
2. skontroluj relevantné publikované príklady,
3. rozlišuj medzi faktami a návrhmi,
4. uveď viac variantov nadpisu,
5. označ odporúčanú voľbu,
6. pridaj krátke odôvodnenie,
7. nechaj finálnu kontrolu na človeku.
