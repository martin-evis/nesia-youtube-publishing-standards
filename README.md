# NESIA YouTube Publishing Standards

Repo pre štandardizáciu YouTube publikovania pre NESIA. Aktuálny hlavný formát je **TALKSHOW**.

> Stav tejto verzie: `v0.6.1-sync-descriptions-metadata`  
> Dátum aktualizácie: 2026-06-15  
> GitHub účet: `martin-evis`  
> Oblasť: YouTube / obsah / štandardizácia

## Čo je cieľ repozitára

Repo má byť praktický pracovný štandard pre nové NESIA videá. Pri novom videu má pomôcť pripraviť:

1. 3–5 variantov nadpisu,
2. odporúčaný finálny nadpis,
3. krátky aj dlhý popis,
4. kapitoly / časové značky,
5. hashtagy,
6. tagy / štítky,
7. playlist,
8. thumbnail text a brief pre grafika,
9. pripnutý komentár,
10. interný kontrolný checklist pred publikovaním.

## Zásadné pravidlo

GitHub nie je archív videí. Do repozitára patria **texty, metadáta, pravidlá, šablóny, prompty, analýzy a výstupné balíky**.

Do repozitára nepatria veľké video súbory (`mp4`, `mov`, `mkv`) ani nečistené exporty z YouTube Studio. Pri verejnom repozitári sem nepatria ani interné dáta ako retencia, CTR, watch time, zdroje návštevnosti, rozpočty alebo neverejné kontakty.

## Aktuálny rozsah

Aktuálna verzia obsahuje 6 zdrojových TALKSHOW videí:

| # | Video | Typ | Stav |
|---:|---|---|---|
| 1 | `R4A0CzH93XI` | full episode | pôvodný popis, hashtagy a kapitoly doplnené |
| 2 | `hKhO7xT_IxQ` | full episode | pôvodný popis, hashtagy a kapitoly doplnené |
| 3 | `KdZ-HHPUpWs` | full episode + audience interaction | pôvodný popis, hashtagy a kapitoly doplnené |
| 4 | `wnlNvGYrnhw` | full episode + music segment | pôvodný popis, hashtagy a kapitoly doplnené; chýba presný deň publikovania |
| 5 | `7MfOiVWXNJg` | best-of compilation | pôvodný popis a hashtagy doplnené; kapitoly nie sú v popise |
| 6 | `LU2foQMJVsg` | full episode + music segment | pôvodný popis, hashtagy a kapitoly doplnené; výkon treba doplniť neskôr |

Detailné dáta sú v:

```text
content/talkshow/published/
```

## Nová odporúčaná štruktúra

```text
.
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── docs/
│   ├── 00-public-repo-mode.md
│   ├── 06-content-data-model.md
│   ├── 07-storage-policy.md
│   └── 08-iteration-workflow.md
├── content/
│   └── talkshow/
│       ├── README.md
│       ├── missing-data-tracker.md
│       ├── drafts/
│       └── published/
│           ├── index.md
│           └── YYYY-MM-DD-videoid-slug/
│               ├── source-metadata.yaml
│               ├── raw-input.md
│               ├── source-description.md
│               ├── source-transcript.md
│               ├── analysis.md
│               └── performance-notes.md
├── rules/
│   └── talkshow/
│       ├── voice-of-tone-draft-v0.4.md
│       ├── title-rules-draft-v0.4.md
│       ├── description-rules-draft-v0.4.md
│       ├── metadata-rules-draft-v0.4.md
│       └── thumbnail-rules-draft-v0.4.md
├── templates/
├── prompts/
├── outputs/
└── scripts/
```

## Ako repo používať

1. Pri novom TALKSHOW videu najprv vytvor brief podľa `templates/talkshow/new-video-brief-template.md`.
2. Doplň transcript alebo pracovné poznámky.
3. Použi prompt `prompts/talkshow/create-youtube-pack-from-transcript.md`.
4. Výstup ulož do `outputs/talkshow/`.
5. Po publikovaní doplň finálny záznam do `content/talkshow/published/`.
6. Pri väčšej zmene aktualizuj `CHANGELOG.md`.

## Aktuálne otvorené položky

- Doplnit transcripty / titulky pre 6 zdrojových videí.
- Doplnit tagy zo Studia, ak budú dostupné.
- Doplniť bezpečný public výkon pre video `LU2foQMJVsg`.
- Overiť presný dátum publikovania videa `wnlNvGYrnhw`.
- Skontrolovať hashtag `#matejsucha` pri videu `wnlNvGYrnhw`, keďže bol ponechaný podľa dodaného pôvodného popisu.
