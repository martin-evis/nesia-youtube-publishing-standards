# Public repo režim

Aktuálny repozitár môže byť verejný. To mení spôsob práce s dátami.

## Povolené v public repo

- verejné URL YouTube videí,
- verejné názvy videí,
- verejné thumbnail URL,
- verejné alebo používateľom dodané popisy,
- ručne doplnené témy, hostia a moderátor,
- pracovné pravidlá a šablóny,
- public-safe analýza typu „čo fungovalo“ bez interných čísel,
- prepisy videí, ak sú povolené na interné použitie a neobsahujú citlivé údaje.

## Nepovolené v public repo

- nečistené exporty z YouTube Studio,
- CTR thumbnailu,
- retencia publika,
- watch time,
- zdroje návštevnosti,
- reklamné rozpočty,
- interné plány kampaní,
- neveľejné kontakty alebo dohody,
- MP4/MOV/video súbory.

## Odporúčaná prax

Ak treba pracovať s výkonom videí, použij jednu z možností:

1. v public repo ulož iba bezpečný súhrn bez citlivých detailov,
2. citlivé dáta nechaj v Google Sheete / YouTube Studio,
3. pre internú analytiku vytvor samostatný private repo alebo Drive priečinok.

## Praktický príklad

V public repo je OK:

```yaml
performance_public:
  views:
    value: 23806
    relation: "exact_from_user_snapshot"
  likes:
    value: 16
    relation: "exact_from_user_snapshot"
```

Do public repo nedávať:

```yaml
retention_curve: ...
ctr_thumbnail: ...
traffic_sources: ...
watch_time_hours: ...
```
