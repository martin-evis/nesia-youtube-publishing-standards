# NESIA YouTube Publishing Standards

Interný repozitár pre štandardizáciu publikovania videí na YouTube kanáli NESIA.

Prvá verzia je zameraná na formát **TALKSHOW**. Repozitár je pripravený tak, aby sa neskôr dali doplniť ďalšie typy videí, napríklad produktové videá, showroom videá, reklamné videá, reels/shorts alebo zostrihy.

## Stav repozitára

- **Verzia:** `v0.1.0-talkshow`
- **Dátum založenia:** 2026-06-14
- **GitHub účet:** `martin-evis`
- **Projektová oblasť:** YouTube / obsah / štandardizácia
- **Aktuálny video typ:** TALKSHOW
- **Primárny jazyk výstupov:** slovenčina

## Cieľ

Pre každé nové NESIA TALKSHOW video pripraviť jednotný publikačný balík:

1. nadpis videa,
2. popis videa,
3. krátky úvodný hook,
4. kapitoly / časové značky,
5. hashtagy,
6. interné tagy / štítky,
7. odporúčaný playlist,
8. návrh thumbnailu,
9. návrh pripnutého komentára,
10. kontrolný checklist pred a po publikovaní.

## Zdrojové videá pre prvú TALKSHOW verziu

Playlist:

- https://www.youtube.com/playlist?list=PLUXZ_uBD6mO7SBnGWdxhZYnBHK6nHkrRL

Vstupné verejné videá:

- https://youtu.be/R4A0CzH93XI
- https://youtu.be/hKhO7xT_IxQ
- https://youtu.be/KdZ-HHPUpWs
- https://youtu.be/wnlNvGYrnhw
- https://youtu.be/7MfOiVWXNJg
- https://youtu.be/LU2foQMJVsg

Poznámka: V tejto verzii sú videá evidované ako verejné zdroje, ale konkrétne nadpisy, popisy, dĺžky, kapitoly a aktuálne tagy ešte treba doplniť manuálne alebo exportom z YouTube Studio. Štruktúra repozitára je pripravená tak, aby sa tieto dáta dali neskôr doplniť bez zmeny workflow.

## Štruktúra repozitára

```text
.
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── LICENSE.md
├── docs/
│   ├── 01-repository-workflow.md
│   ├── 02-youtube-official-rules.md
│   ├── 03-ai-use-rules.md
│   └── 04-future-video-types.md
├── video-types/
│   └── talkshow/
│       ├── README.md
│       ├── workflow.md
│       ├── title-description-rules.md
│       ├── tags-hashtags-metadata.md
│       ├── thumbnail-rules.md
│       ├── source-videos.md
│       ├── examples/
│       │   ├── published-videos-analysis.md
│       │   └── sample-output-package.md
│       ├── templates/
│       │   └── youtube-talkshow-template.md
│       └── prompts/
│           └── generate-talkshow-metadata.md
├── checklists/
│   ├── pre-publication-checklist.md
│   └── post-publication-checklist.md
├── metadata-packages/
│   └── talkshow/
│       └── 000-template.md
├── scripts/
│   └── validate_youtube_metadata.py
└── .github/
    └── ISSUE_TEMPLATE/
        └── talkshow-video-metadata.yml
```

## Rýchly workflow pre nové TALKSHOW video

1. Skopíruj `metadata-packages/talkshow/000-template.md`.
2. Premenuj súbor podľa epizódy, napríklad `metadata-packages/talkshow/007-meno-hosta-tema.md`.
3. Doplň vstupy: URL pracovného videa, hosť, hlavná téma, prepis alebo poznámky, CTA, odkazy.
4. Použi prompt z `video-types/talkshow/prompts/generate-talkshow-metadata.md`.
5. Výstup skontroluj podľa `checklists/pre-publication-checklist.md`.
6. Po zverejnení doplň URL finálneho videa a prejdi `checklists/post-publication-checklist.md`.

## Odporúčané GitHub nastavenie

Repo odporúčam vytvoriť ako **private**, keďže ide o interný štandard práce. Verejné sú iba zdrojové YouTube videá, nie nevyhnutne interné workflow, šablóny, poznámky a checklisty.

Odporúčaný názov repozitára:

```text
nesia-youtube-publishing-standards
```

Odporúčaný popis repozitára:

```text
Interné štandardy a šablóny pre publikovanie NESIA YouTube videí. Prvá verzia: TALKSHOW.
```

## Vytvorenie repozitára cez GitHub CLI

```bash
gh repo create martin-evis/nesia-youtube-publishing-standards \
  --private \
  --description "Interné štandardy a šablóny pre publikovanie NESIA YouTube videí. Prvá verzia: TALKSHOW." \
  --source=. \
  --remote=origin \
  --push
```

Ak má byť repo verejné, vymeň `--private` za `--public`.

## Manuálne vytvorenie cez web GitHubu

1. Otvor GitHub účet `martin-evis`.
2. Zvoľ **New repository**.
3. Repository name: `nesia-youtube-publishing-standards`.
4. Description: `Interné štandardy a šablóny pre publikovanie NESIA YouTube videí. Prvá verzia: TALKSHOW.`
5. Visibility: odporúčané `Private`.
6. Vytvor prázdny repozitár.
7. Nahraj obsah tohto priečinka alebo pushni cez Git.

## Minimálne pravidlá kvality

- Nevymýšľať mená hostí, pozície, firmy ani citácie.
- Ak chýba prepis videa, výstup označiť ako draft.
- Nadpis musí byť zrozumiteľný bez kontextu.
- Popis musí mať jasný úvod, obsah epizódy, odkazy, CTA a hashtagy.
- Hashtagy musia priamo súvisieť s videom.
- Tagy nepoužívať ako spam; sú len doplnkové.
- Finálny výstup musí prejsť ľudskou kontrolou pred publikovaním.
