# Source video record template – NESIA TALKSHOW

Tento template použi pri dopĺňaní ďalšieho existujúceho alebo nového TALKSHOW videa.

Odporúčané umiestnenie:

```text
content/talkshow/published/YYYY-MM-DD-videoid-topic/
```

alebo pri pripravovanom videu:

```text
content/talkshow/drafts/YYYY-MM-DD-working-title/
```

## Súbory v zázname

```text
raw-input.md
source-metadata.yaml
source-description.md
source-transcript.md
analysis.md
performance-notes.md
```

---

## source-metadata.yaml

```yaml
schema_version: "0.3"
record_type: "published_video_source"
video_type: "talkshow"
episode_variant: "full_episode"

video_id: "DOPLNIŤ"
video_url: "DOPLNIŤ"
thumbnail_url: "DOPLNIŤ"
playlist_url: "DOPLNIŤ"
playlist_status: "DOPLNIŤ"

published_date: "DOPLNIŤ"
published_date_precision: "day | month | unknown"
published_date_verification_status: "DOPLNIŤ"

current_title: "DOPLNIŤ"
current_description: null
current_description_status: "DOPLNIŤ"

hashtags: []
hashtags_status: "DOPLNIŤ"
tags: []
tags_status: "DOPLNIŤ"
chapters_available: null
chapters_status: "DOPLNIŤ"

moderator: "Andrea Vadkerti"
guests:
  - "DOPLNIŤ"

topic_summary: >-
  DOPLNIŤ stručné zhrnutie témy.

performance_public:
  views: null
  likes: null
  metrics_status: "DOPLNIŤ"

source_status:
  raw_input: "DOPLNIŤ"
  description: "DOPLNIŤ"
  transcript: "DOPLNIŤ"
  chapters: "DOPLNIŤ"
  studio_tags: "DOPLNIŤ"
  studio_analytics: "DOPLNIŤ"
```

---

## raw-input.md

```markdown
# Raw input – VIDEO_ID

> Tento súbor obsahuje dodané vstupy. Nejde o finálnu analýzu ani pravidlá.

## Video

- **Video URL:** DOPLNIŤ
- **Aktuálny nadpis:** DOPLNIŤ
- **Aktuálny popis:** DOPLNIŤ / NEDOSTUPNÉ
- **Hashtagy:** DOPLNIŤ / NEDOSTUPNÉ
- **Tagy / štítky:** DOPLNIŤ / NEDOSTUPNÉ
- **Playlist:** DOPLNIŤ / NEDOSTUPNÉ
- **Dátum publikovania:** DOPLNIŤ
- **Hosť:** DOPLNIŤ
- **Moderuje:** Andrea Vadkerti
- **Má kapitoly:** áno / nie / neznáme
- **Thumbnail:** DOPLNIŤ

## Téma videa

DOPLNIŤ

## Dodaná poznámka k výkonu / obsahu

DOPLNIŤ
```

---

## analysis.md

```markdown
# Analysis – VIDEO_ID

## Čo fungovalo

- DOPLNIŤ

## Hypotézy pre budúce videá

- DOPLNIŤ

## Riziká / čo zlepšiť

- DOPLNIŤ

## Použitie pri tvorbe pravidiel

DOPLNIŤ
```

---

## performance-notes.md

```markdown
# Performance notes – VIDEO_ID

## Dostupné metriky

- Zhliadnutia: DOPLNIŤ
- Lajky: DOPLNIŤ
- Dátum stavu metrík: DOPLNIŤ

## Interpretácia

DOPLNIŤ

## Doplniť neskôr, ak bude dostupné

- retencia,
- CTR thumbnailu,
- zdroje návštevnosti,
- komentáre,
- výkon po 7 / 30 / 90 dňoch.
```
