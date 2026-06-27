# blogi

Henkilökohtainen GitHub Pages -blogi.

## Rakenne

- `index.md` — etusivu
- `arkisto.md` — blogiarkisto
- `minusta.md` — esittelysivu
- `kirjat.md` — kirjasivu
- `projektit.md` — projektisivu
- `_posts/` — blogiartikkelit
- `_layouts/` — Jekyll-sivupohjat
- `assets/css/style.css` — ulkoasu

## Uusi artikkeli

Luo tiedosto kansioon `_posts/` muodossa:

```text
YYYY-MM-DD-otsikko.md
```

Artikkelin alkuun:

```yaml
---
title: "Otsikko"
description: "Lyhyt kuvaus."
categories: [aihe]
---
```

## Julkaisu

Sivusto julkaistaan GitHub Pagesilla. Jos Pages ei ole vielä päällä, ota se käyttöön repositoryn asetuksista:

`Settings → Pages → Build and deployment → Deploy from a branch → main / root`
