# Content data model

Repo používa jednoduchý model: zdrojové dáta, analýza a pravidlá sú oddelené.

## Hlavné vrstvy

```text
content/     = zdrojové prípady, drafty a údaje o videách
rules/       = pravidlá pre budúce výstupy
templates/   = ručne vypĺňané šablóny
prompts/     = AI prompty
outputs/     = hotové výstupy pre nové videá
docs/        = metodika a rozhodnutia
```

## Štruktúra publikovaného TALKSHOW videa

```text
content/talkshow/published/YYYY-MM-DD-videoid-slug/
  source-metadata.yaml
  raw-input.md
  source-description.md
  source-transcript.md
  analysis.md
  performance-notes.md
```

## Význam súborov

### `source-metadata.yaml`

Štruktúrované fakty a stav dostupnosti údajov. Má byť strojovo čitateľný a čo najstručnejší.

### `raw-input.md`

Presné podklady dodané používateľom. Slúži ako auditná stopa.

### `source-description.md`

Pôvodný YouTube popis. Ak nie je dostupný, musí byť jasne označený ako `DOPLNIŤ`.

### `source-transcript.md`

Prepis videa. Kým chýba, pravidlá voice of tone sú iba draft.

### `analysis.md`

Interpretácia: čo fungovalo, čo je riziko, aký vzor si všímame. Tento súbor nie je faktografický zdroj.

### `performance-notes.md`

Iba public-safe výkonové poznámky. Interné YouTube Studio dáta patria mimo public repo.

## Pravidlo proti chaosu

Ak sa údaj týka minulého videa, patrí do `content/`.
Ak ide o poučenie pre budúcnosť, patrí do `rules/`.
Ak ide o finálny text pre nové video, patrí do `outputs/`.
