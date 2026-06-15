# Required fields – source-metadata.yaml

Každé publikované TALKSHOW video musí mať v `source-metadata.yaml` aspoň tieto polia:

```yaml
schema_version:
repo_version:
record_type:
record_status:
public_repo_safe:
video:
  id:
  url:
  playlist_url:
  thumbnail_url:
publication:
  published_date_text:
  published_date:
  published_date_precision:
  verification_status:
format:
  video_type:
  format_variant:
people:
  moderator:
  guests:
current_youtube_metadata:
  title:
  description_available:
  description_status:
content:
  topic_summary_raw:
  topic_summary_normalized:
  themes:
performance_public:
  views:
  likes:
missing_data:
```

Ak údaj chýba, nepoužívaj vymyslenú hodnotu. Použi `null`, `DOPLNIŤ`, `unknown` alebo status vysvetľujúci problém.
