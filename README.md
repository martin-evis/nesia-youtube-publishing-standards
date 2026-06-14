# NESIA YouTube Publishing Standards

Interný pracovný repozitár pre štandardizáciu publikovania videí na YouTube kanáli NESIA.

Repo je navrhnuté ako **operačný zdroj pravdy pre texty, metadáta, pravidlá, prompty a výstupy**, nie ako úložisko veľkých video súborov. Samotné videá ostávajú na YouTube alebo v samostatnom úložisku; v GitHube evidujeme odkazy, prepisy, popisy, analytické poznámky a pravidlá.

## Stav repozitára

- **Aktuálna pracovná verzia:** `v0.3.0-talkshow-source-videos`
- **Pôvodná verzia:** `v0.1.0-talkshow`
- **Dátum aktualizácie:** 2026-06-14
- **GitHub účet:** `martin-evis`
- **Projektová oblasť:** YouTube / obsah / štandardizácia
- **Aktuálny video typ:** TALKSHOW
- **Primárny jazyk výstupov:** slovenčina

## Čo tento repozitár rieši

Pre každé nové NESIA TALKSHOW video má repo pomôcť vytvoriť jednotný publikačný balík:

1. názov videa,
2. krátky hook,
3. YouTube popis,
4. kapitoly / časové značky,
5. hashtagy,
6. YouTube tagy,
7. odporúčaný playlist,
8. thumbnail text a brief,
9. pripnutý komentár,
10. kontrolný checklist pred a po publikovaní.

## Základný princíp

V repozitári dôsledne oddeľujeme tri vrstvy:

```text
source data  = fakty a pôvodné vstupy k videám
analysis     = pozorovania, čo fungovalo / nefungovalo
rules        = až nami schválené pravidlá pre budúce videá
```

To je dôležité preto, aby AI pri tvorbe nových textov nepovažovala odhady alebo pracovné poznámky za overené fakty.

## Odporúčaná štruktúra

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
├── content/
│   └── talkshow/
│       ├── README.md
│       ├── missing-data-tracker.md
│       └── published/
│           ├── index.md
│           └── YYYY-MM-DD-videoid-topic/
│               ├── raw-input.md
│               ├── source-metadata.yaml
│               ├── source-description.md
│               ├── source-transcript.md
│               ├── analysis.md
│               └── performance-notes.md
├── rules/
│   └── talkshow/
│       ├── voice-of-tone-draft-v0.3.md
│       ├── title-rules-draft-v0.3.md
│       └── description-rules-draft-v0.3.md
├── templates/
│   └── talkshow/
│       └── source-video-record-template.md
├── video-types/
│   └── talkshow/
│       ├── README.md
│       ├── workflow.md
│       ├── title-description-rules.md
│       ├── tags-hashtags-metadata.md
│       ├── thumbnail-rules.md
│       └── source-videos.md
├── checklists/
├── metadata-packages/
└── scripts/
```

## Zdrojové TALKSHOW videá v prvej fáze

Playlist:

- https://www.youtube.com/playlist?list=PLUXZ_uBD6mO7SBnGWdxhZYnBHK6nHkrRL

Publikované vstupné videá:

1. https://youtu.be/R4A0CzH93XI
2. https://youtu.be/hKhO7xT_IxQ
3. https://youtu.be/KdZ-HHPUpWs
4. https://youtu.be/wnlNvGYrnhw
5. https://youtu.be/7MfOiVWXNJg
6. https://youtu.be/LU2foQMJVsg

Detailné záznamy sú v `content/talkshow/published/`.

## Workflow pre nové TALKSHOW video

1. Načítaj pravidlá z `rules/talkshow/`.
2. Načítaj publikované príklady z `content/talkshow/published/`.
3. Pre nové video vytvor nový záznam podľa `templates/talkshow/source-video-record-template.md`.
4. Doplň brief, transcript, tému, hostí, CTA a dostupné odkazy.
5. Vygeneruj publikačný balík cez prompt v `video-types/talkshow/prompts/`.
6. Výstup skontroluj cez `checklists/pre-publication-checklist.md`.
7. Po publikovaní doplň finálnu URL, dátum, reálny názov, popis a poznámky k výkonu.

## Verejné vs. interné údaje

Repo je aktuálne verejné. Preto doň nepatria:

- heslá,
- API tokeny,
- súkromné kontakty,
- interné rozpočty,
- neverejné YouTube Studio exporty,
- interné strategické poznámky, ktoré nemajú byť verejné.

Ak budeme ukladať retenciu, CTR, zdroje návštevnosti alebo interné poznámky zo Studia, odporúčané riešenie je zmeniť repo na private alebo oddeliť verejné šablóny od interného private repozitára.

## Minimálne pravidlá kvality

- Nevymýšľať mená hostí, pozície, firmy ani citácie.
- Ak údaj chýba, označiť ho ako `DOPLNIŤ`, `NEOVERENÉ` alebo `NEDOSTUPNÉ`.
- Nadpis musí byť zrozumiteľný bez ďalšieho kontextu.
- Popis musí jasne povedať, čo sa divák dozvie.
- Hashtagy musia byť relevantné.
- Tagy nepoužívať ako spam.
- Finálny výstup musí prejsť ľudskou kontrolou pred publikovaním.

## Najbližší cieľ

Doplniť chýbajúce pôvodné popisy, hashtagy, tagy, kapitoly a transkripty k existujúcim TALKSHOW videám. Po doplnení dát pripraviť prvú záväznú verziu pravidiel `v1.0-talkshow`.
