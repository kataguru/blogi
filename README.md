# blogi

Henkilökohtainen GitHub Pages -blogi.

## Rakenne

- `index.md` — etusivu
- `arkisto.md` — blogiarkisto
- `minusta.md` — esittelysivu
- `kirjat.md` — kirjasivu
- `_data/books.yml` — kirjatiedot
- `projektit.md` — projektisivu
- `teesit.md` — sivuston teesit
- `STYLE.md` — toimituksellinen tyyliohje
- `PAIVITYSOHJE.md` — ohje sivuston jatkamiseen uudessa keskustelussa
- `_posts/` — blogiartikkelit
- `_layouts/` — Jekyll-sivupohjat
- `assets/css/style.css` — ulkoasu
- `assets/images/` — kuvat
- `assets/books/` — kirjatiedostot

## Uusi keskusteluikkuna

Kun sivuston päivittäminen jatkuu uudessa keskustelussa, anna ensin tämä ohje:

```text
Jatketaan sivustoa kataguru/blogi. Lue README.md, STYLE.md ja PAIVITYSOHJE.md. Päivitä sivustoa niiden mukaan.
```

Tarkemmat jatko-ohjeet ovat tiedostossa `PAIVITYSOHJE.md`.

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

## Kirjat

Kirjatietoja ei muokata ensisijaisesti `kirjat.md`-sivulle, vaan tiedostoon:

```text
_data/books.yml
```

`kirjat.md` lukee kirjatiedot tästä tiedostosta.

## Julkaisu

Sivusto julkaistaan GitHub Pagesilla:

`Settings → Pages → Build and deployment → Deploy from a branch → main / root`
