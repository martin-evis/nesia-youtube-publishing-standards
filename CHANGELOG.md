# Changelog

## v0.3.0-talkshow-source-videos – 2026-06-14

Prerobená štruktúra repozitára z jednoduchej kostry na pracovný dátový systém pre NESIA TALKSHOW.

Pridané:

- nová dátová vrstva `content/talkshow/`,
- index publikovaných TALKSHOW videí,
- samostatné záznamy pre 6 existujúcich verejných videí,
- tracker chýbajúcich údajov,
- oddelenie faktov, raw vstupov, analýzy a pravidiel,
- draft pravidiel pre voice of tone,
- draft pravidiel pre nadpisy,
- draft pravidiel pre popisy,
- šablóna pre nové source video record-y.

Zmenené:

- `README.md` teraz popisuje repo ako operačný zdroj pravdy pre YouTube texty, metadáta a pravidlá,
- `AGENTS.md` dopĺňa pravidlá pre verejný repozitár a stavové označenia,
- `video-types/talkshow/source-videos.md` obsahuje reálne dostupné metadáta k 6 videám.

Dôležité rozhodnutia:

- GitHub neslúži ako úložisko veľkých MP4 súborov,
- verejný repozitár nesmie obsahovať interné YouTube Studio exporty ani citlivé údaje,
- výkonové poznámky sú zatiaľ evidované iba z dodaných / verejne použiteľných údajov,
- finálne pravidlá pre voice of tone vzniknú až po doplnení chýbajúcich textov a transcriptov.

Známe obmedzenia:

- chýbajú pôvodné popisy k viacerým videám,
- chýbajú hashtagy a tagy,
- chýbajú kapitoly,
- chýbajú kompletné transcripty,
- dátum publikovania Baťa epizódy je zatiaľ len `Január 2026`,
- metadáta čerstvého videa so Zuzanou Šebovou treba neskôr overiť.

## v0.1.0-talkshow – 2026-06-14

Založená prvá verzia repozitára pre NESIA YouTube publishing standards.

Pridané:

- základná štruktúra repozitára,
- workflow pre TALKSHOW videá,
- pravidlá pre nadpisy a popisy,
- pravidlá pre tagy, hashtagy a metadáta,
- pravidlá pre thumbnail,
- šablóna publikačného balíka,
- AI prompt na tvorbu metadát,
- checklist pred a po publikovaní,
- evidované zdrojové verejné YouTube videá,
- jednoduchý validačný skript pre dĺžku nadpisu, popisu a počet hashtagov.

Známe obmedzenia:

- Konkrétne aktuálne nadpisy, popisy, tagy a kapitoly existujúcich videí ešte nie sú doplnené.
- Repozitár zatiaľ pokrýva iba typ videa TALKSHOW.
