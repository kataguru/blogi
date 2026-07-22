# blogi

Henkilökohtainen GitHub Pages -blogi.

Sivusto on kaksikielinen. Suomenkielinen sisältö julkaistaan juureen ja englanninkielinen sisältö `/en/`-polun alle. Jokaisella sivulla on Suomen ja Englannin lipuilla merkitty kielivalinta, joka vie saman sisällön toiseen kieliversioon.

## Rakenne

- `index.md` — etusivu
- `arkisto.md` — blogiarkisto
- `minusta.md` — esittelysivu
- `kirjat.md` — kirjasivu
- `_data/books.yml` — kirjatiedot
- `_data/books_en.yml` — englanninkieliset kirjatiedot
- `projektit.md` — projektisivu
- `teesit.md` — sivuston teesit
- `STYLE.md` — toimituksellinen tyyliohje
- `PAIVITYSOHJE.md` — ohje sivuston jatkamiseen uudessa keskustelussa
- `_posts/` — blogiartikkelit
- `_posts/en/` — englanninkieliset blogiartikkelit
- `en/` — englanninkieliset staattiset sivut
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
lang: fi
translation_key: YYYY-MM-DD-yhteinen-tunniste
---
```

Samassa muutoksessa luodaan englanninkielinen tiedosto `_posts/en/`-kansioon. Sen `lang` on `en`, `translation_key` on sama kuin suomenkielisessä tiedostossa ja `permalink` alkaa `/en/`. Julkaisua ei tehdä vain yhdellä kielellä.

## Kirjat

Kirjatietoja ei muokata ensisijaisesti `kirjat.md`-sivulle, vaan tiedostoon:

```text
_data/books.yml
```

`kirjat.md` lukee kirjatiedot tästä tiedostosta.

## Julkaisu

Sivusto julkaistaan GitHub Pagesilla:

`Settings → Pages → Build and deployment → Deploy from a branch → main / root`
