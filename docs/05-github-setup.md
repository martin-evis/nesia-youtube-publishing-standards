# GitHub setup

Tento dokument popisuje presný postup, ako vytvoriť repozitár pod účtom `martin-evis`.

## Odporúčané nastavenie

| Pole | Hodnota |
|---|---|
| Owner | `martin-evis` |
| Repository name | `nesia-youtube-publishing-standards` |
| Description | `Interné štandardy a šablóny pre publikovanie NESIA YouTube videí. Prvá verzia: TALKSHOW.` |
| Visibility | `Private` odporúčané |
| Default branch | `main` |

## Postup cez GitHub web

1. Prihlás sa do GitHub účtu `martin-evis`.
2. Klikni na **New repository**.
3. Vyplň názov `nesia-youtube-publishing-standards`.
4. Vyplň popis repozitára.
5. Zvoľ `Private`, ak má ísť o interný pracovný manuál.
6. Nevytváraj README cez web, ak budeš nahrávať celý tento balík.
7. Vytvor repozitár.
8. Nahraj súbory z tohto priečinka alebo použi Git príkazy nižšie.

## Postup cez terminál bez GitHub CLI

```bash
cd nesia-youtube-publishing-standards

git init
git branch -M main
git add .
git commit -m "Initial NESIA YouTube TALKSHOW publishing standards"

git remote add origin git@github.com:martin-evis/nesia-youtube-publishing-standards.git
git push -u origin main
```

Ak používaš HTTPS namiesto SSH:

```bash
git remote add origin https://github.com/martin-evis/nesia-youtube-publishing-standards.git
git push -u origin main
```

## Postup cez GitHub CLI

```bash
gh repo create martin-evis/nesia-youtube-publishing-standards \
  --private \
  --description "Interné štandardy a šablóny pre publikovanie NESIA YouTube videí. Prvá verzia: TALKSHOW." \
  --source=. \
  --remote=origin \
  --push
```

Ak má byť repo verejné:

```bash
gh repo create martin-evis/nesia-youtube-publishing-standards \
  --public \
  --description "Štandardy a šablóny pre publikovanie NESIA YouTube videí. Prvá verzia: TALKSHOW." \
  --source=. \
  --remote=origin \
  --push
```

## Prvé issues po založení repozitára

Odporúčané prvé GitHub issues:

1. `Doplniť aktuálne nadpisy a popisy existujúcich TALKSHOW videí`.
2. `Doplniť jednotný CTA blok do TALKSHOW šablóny`.
3. `Vybrať finálny thumbnail štýl pre NESIA TALKSHOW`.
4. `Pripraviť ďalší video type: showroom`.
5. `Pripraviť ďalší video type: product-video`.

## Prvá release verzia

Po nahratí na GitHub vytvor release:

```text
v0.1.0-talkshow
```

Release poznámka:

```text
Prvá verzia interných YouTube publishing standards pre NESIA TALKSHOW. Obsahuje workflow, šablóny, checklisty, prompt a zdrojové verejné videá.
```
