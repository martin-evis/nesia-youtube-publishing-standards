# Iteračný workflow

Repo sa bude dopĺňať postupne. Cieľ nie je mať všetko dokonalé v prvom commite, ale mať jasný systém.

## Iterácia A – zdrojové videá

- doplniť základné metadáta všetkých publikovaných TALKSHOW videí,
- označiť chýbajúce údaje,
- oddeliť bežné epizódy od variantov ako best-of alebo hudobný vstup.

## Iterácia B – chýbajúce texty

- doplniť pôvodné YouTube popisy,
- doplniť hashtagy,
- doplniť tagy,
- doplniť kapitoly,
- doplniť transcript.

## Iterácia C – pravidlá

Až po doplnení transcriptov uzavrieť:

```text
rules/talkshow/voice-of-tone.md
rules/talkshow/title-rules.md
rules/talkshow/description-rules.md
rules/talkshow/thumbnail-rules.md
rules/talkshow/metadata-rules.md
```

## Iterácia D – nové video

Pri novom videu použiť existujúce pravidlá a vygenerovať výstup do:

```text
outputs/talkshow/YYYY-MM-DD-slug/youtube-pack.md
```

## Commit pravidlo

Každý commit má mať jeden jasný účel:

- `data:` doplnenie údajov k videám,
- `rules:` zmena pravidiel,
- `template:` zmena šablón,
- `prompt:` zmena promptov,
- `docs:` metodické dokumenty,
- `fix:` opravy chýb.
