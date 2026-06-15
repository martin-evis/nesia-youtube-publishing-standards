# Changelog

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
