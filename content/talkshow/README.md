# Content / TALKSHOW

Tento priečinok obsahuje pracovnú dátovú vrstvu pre formát **NESIA TALKSHOW**.

Cieľom nie je iba archivovať linky na videá, ale postupne vytvoriť spoľahlivý zdroj pre nové publikačné balíky: názvy, popisy, kapitoly, hashtagy, tagy, thumbnail briefy a pripnuté komentáre.

## Štruktúra

```text
content/talkshow/
├── README.md
├── missing-data-tracker.md
└── published/
    ├── index.md
    └── YYYY-MM-DD-videoid-topic/
        ├── raw-input.md
        ├── source-metadata.yaml
        ├── source-description.md
        ├── source-transcript.md
        ├── analysis.md
        └── performance-notes.md
```

## Význam súborov

| Súbor | Účel |
|---|---|
| `raw-input.md` | Neupravené alebo minimálne upravené informácie dodané tímom. |
| `source-metadata.yaml` | Štruktúrované fakty a stav dostupnosti údajov. |
| `source-description.md` | Pôvodný YouTube popis, ak je dostupný. |
| `source-transcript.md` | Transcript / prepis videa, ak je dostupný. |
| `analysis.md` | Pozorovania, čo fungovalo a čo sa dá použiť pre pravidlá. |
| `performance-notes.md` | Výkonové poznámky, views, likes a stav overenia. |

## Pravidlo práce

Ak chýba údaj, nevymýšľame ho. Označíme ho ako `DOPLNIŤ`, `NEDOSTUPNÉ`, `NEOVERENÉ` alebo `NEZNÁME`.

## Najbližší cieľ

1. Doplniť chýbajúce pôvodné popisy.
2. Doplniť transcripty.
3. Doplniť hashtagy, tagy a kapitoly.
4. Z existujúcich epizód odvodiť voice of tone.
5. Po schválení uložiť finálne pravidlá do `rules/talkshow/`.
