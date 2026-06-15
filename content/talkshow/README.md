# Content / TALKSHOW

Tento priečinok je zdrojová databáza pre NESIA TALKSHOW.

## Priečinky

```text
published/  = už zverejnené videá, ktoré slúžia ako zdroj štýlu a pravidiel
drafts/     = pripravované nové videá
```

## Princíp

Každé video je samostatný prípad. Nepíšeme všetko do jedného súboru, lebo neskôr budeme dopĺňať popisy, transcripty, kapitoly a výkonové poznámky po častiach.

## Ako doplniť chýbajúci text

Ak používateľ dodá napríklad pôvodný popis videa:

1. otvor priečinok konkrétneho videa,
2. vlož text do `source-description.md`,
3. v `source-metadata.yaml` zmeň `description_status`,
4. v `missing-data-tracker.md` označ popis ako doplnený,
5. zapíš zmenu do changelogu, ak ide o významnejšie doplnenie.

## Ako doplniť transcript

Transcript vlož do `source-transcript.md`. Neparafrázuj ho ako fakt. Ak robíš čistený transcript, označ to v hlavičke súboru.
