# Restructure plan v0.4.0

Cieľ: prerobiť prvú skeleton verziu repozitára na praktickú dátovo-pravidlovú štruktúru pre NESIA TALKSHOW.

## Čo sa mení

1. `content/talkshow/published/` sa stáva hlavným miestom pre už zverejnené videá.
2. Každé video má vlastný priečinok a oddelené súbory pre fakty, raw vstup, popis, transcript, analýzu a výkonové poznámky.
3. `rules/talkshow/` obsahuje zatiaľ iba draft pravidlá.
4. `templates/talkshow/` a `prompts/talkshow/` pripravujú workflow pre nové videá.
5. Public repo režim je explicitne popísaný v `docs/00-public-repo-mode.md`.

## Čo ponechať

- `video-types/talkshow/` môže zatiaľ zostať ako staršia dokumentačná vrstva.
- Po stabilizácii v1.0 môžeme rozhodnúť, či sa staré `video-types/` zjednoduší alebo presunie do `docs/legacy/`.

## Ako commitnúť

```bash
git checkout -b restructure/v0.4-public-content-architecture
rsync -av /cesta/k/rozbalenemu/nesia-youtube-publishing-standards/ ./
python scripts/validate_talkshow_source_records.py
git add .
git commit -F COMMIT_MESSAGE_v0.4.0.md
git push -u origin restructure/v0.4-public-content-architecture
```

Potom vytvor PR do `main` alebo merge priamo, ak zatiaľ nechceš robiť pull request workflow.
