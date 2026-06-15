# NESIA YouTube Publishing Standards

Repo pre štandardizáciu YouTube publikovania pre NESIA. Aktuálny hlavný formát je **TALKSHOW**.

> Stav tejto verzie: `v0.4.0-public-content-architecture`  
> Dátum aktualizácie: 2026-06-14  
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
| 1 | `R4A0CzH93XI` | full episode | základné metadáta doplnené |
| 2 | `hKhO7xT_IxQ` | full episode | základné metadáta doplnené |
| 3 | `KdZ-HHPUpWs` | full episode + audience interaction | základné metadáta doplnené |
| 4 | `wnlNvGYrnhw` | full episode | má pôvodný popis, chýba presný deň publikovania |
| 5 | `7MfOiVWXNJg` | best-of compilation | samostatný variant, nepoužívať ako bežnú epizódu |
| 6 | `LU2foQMJVsg` | full episode + music segment | čerstvé video, výkon treba doplniť neskôr |

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
│       └── metadata-rules-draft-v0.4.md
├── templates/
│   └── talkshow/
├── prompts/
│   └── talkshow/
├── outputs/
│   └── talkshow/
└── scripts/
    └── validate_talkshow_source_records.py
```

Starší priečinok `video-types/talkshow/` môže zostať ako dokumentačná vrstva k formátu. Zdrojové dáta o publikovaných videách však majú byť primárne v `content/talkshow/published/`.

## Pracovný postup pre dopĺňanie existujúcich videí

1. Otvor konkrétny priečinok videa v `content/talkshow/published/`.
2. Pôvodný YouTube popis doplň do `source-description.md`.
3. Prepis videa doplň do `source-transcript.md`.
4. Ak doplníš hashtagy, tagy alebo kapitoly, aktualizuj `source-metadata.yaml`.
5. Aktualizuj `content/talkshow/missing-data-tracker.md`.
6. Pri významnej zmene dopíš krátky záznam do `CHANGELOG.md`.

## Pracovný postup pre nové TALKSHOW video

1. Vytvor nový priečinok v `content/talkshow/drafts/`.
2. Použi `templates/talkshow/new-video-brief-template.md`.
3. Doplň transcript alebo čo najlepší pracovný brief.
4. Použi prompt `prompts/talkshow/create-youtube-pack-from-transcript.md`.
5. Výstup ulož do `outputs/talkshow/`.
6. Pred publikovaním prebehni checklist v `checklists/pre-publication-checklist.md`.
7. Po publikovaní presuň záznam medzi `published` a doplň finálnu URL.

## Najbližšie kroky

- doplniť pôvodné popisy videí 1, 2, 3, 5 a 6,
- doplniť prepisy všetkých 6 videí,
- doplniť kapitoly, ak existujú,
- doplniť hashtagy a tagy zo Studia,
- po doplnení prepisov uzavrieť `rules/talkshow/voice-of-tone.md` ako v1.0.

## Validácia

```bash
python scripts/validate_talkshow_source_records.py
```

Validátor kontroluje, či má každé publikované video povinné súbory a základné metadáta.
