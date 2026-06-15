# Changelog

## v0.6.1-sync-descriptions-metadata – 2026-06-15

### Zmenené

- Zosúladené `source-metadata.yaml` so stavom doplnených pôvodných YouTube popisov.
- Zosúladený `content/talkshow/published/index.md`: všetkých 6 TALKSHOW videí má popis označený ako `OK`.
- Zosúladený `content/talkshow/missing-data-tracker.md`: popisy a dostupné kapitoly/hashtagy sú označené ako doplnené.
- Aktualizovaný nadpis a metadáta pre epizódu so Zuzanou Šebovou podľa dodaného pôvodného popisu.
- Doplnené kapitoly a hashtagy do metadát tam, kde boli súčasťou dodaného popisu.

### Poznámky na kontrolu

- Pri videu `wnlNvGYrnhw` je v pôvodnom popise hashtag `#matejsucha`; ponechaný ako pôvodný údaj, ale označený na manuálnu kontrolu.
- Pri videu `7MfOiVWXNJg` pôvodný popis neobsahuje kapitoly; pre `best_of_compilation` sú kapitoly voliteľné.

## v0.6.0-complete-original-descriptions – 2026-06-15

### Pridané

- Doplnené pôvodné YouTube popisy pre videá 3, 4, 5 a 6:
  - Matej Šucha / zákaznícka psychológia,
  - Gabriela Končitíková / Tomáš Baťa,
  - BEST OF NESIA TALKSHOW 2025,
  - Zuzana Šebová.
- Nahradený pôvodný kratší záznam pri Baťa epizóde plným dodaným popisom s kapitolami.

## v0.5.0-original-descriptions-1-2 – 2026-06-15

### Pridané

- Doplnené pôvodné YouTube popisy pre videá 1 a 2:
  - Lucia Hablovičová & Karin Majtánová,
  - Martin Spano.
- Pri videu 1 boli doplnené aj kapitoly a hashtagy do `source-metadata.yaml`.

## v0.4.0-public-content-architecture – 2026-06-14

### Pridané

- Zavedená jasná dátová vrstva `content/talkshow/published/` pre publikované TALKSHOW videá.
- Každé zo 6 vstupných videí má samostatný priečinok so súbormi:
  - `source-metadata.yaml`,
  - `raw-input.md`,
  - `source-description.md`,
  - `source-transcript.md`,
  - `analysis.md`,
  - `performance-notes.md`.
- Pridaný verejno-súkromný dátový režim pre public repo.
- Pridané draft pravidlá v `rules/talkshow/`.
- Pridané šablóny pre nové video a existujúci video záznam.
- Pridaný prompt pre tvorbu YouTube publikačného balíka z transcriptu.
- Pridaný validátor `scripts/validate_talkshow_source_records.py`.

### Zmenené

- README prerobené z pôvodnej skeleton dokumentácie na praktický pracovný štandard.
- AGENTS.md rozšírený o pravidlá pre verejný repozitár a oddelenie faktov od analýzy.
- `content/talkshow/missing-data-tracker.md` je hlavný zoznam chýbajúcich údajov.

### Poznámka

Repo je použiteľné aj vo verejnom režime. Interné YouTube Studio dáta však patria mimo public repozitára alebo musia byť anonymizované.

## v0.3.0-talkshow-source-videos-1-6 – 2026-06-14

- Doplnených 6 TALKSHOW videí ako zdrojové prípady.
- Pridané prvé drafty voice of tone, title rules a description rules.

## v0.1.0-talkshow – 2026-06-14

- Založená prvá kostra repozitára pre NESIA YouTube TALKSHOW workflow.
