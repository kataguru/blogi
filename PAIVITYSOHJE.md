# Päivitysohje uutta keskustelua varten

Tämä tiedosto kertoo, miten sivustoa täydennetään, kun työ jatkuu uudessa keskusteluikkunassa.

## Perustiedot

- Repo: `kataguru/blogi`
- Sivusto: GitHub Pages
- Julkaisuhaara: `main`
- Julkaisupolku: repositoryn juuri eli `/`
- Julkinen osoite: `https://kataguru.github.io/blogi/`

Uudessa keskustelussa aloita näin:

```text
Jatketaan GitHub Pages -sivustoa kataguru/blogi. Lue ensin README.md, STYLE.md ja PAIVITYSOHJE.md. Noudata sivuston nykyistä rakennetta. Älä julkaise ennen kuin sanon "Julkaise", ellei pyydetty muutos ole selvästi tekninen ylläpitomuutos.
```

## Tärkeimmät tiedostot

- `README.md` — tekninen yleiskuva sivustosta
- `STYLE.md` — toimituksellinen linja ja tekstien ääni
- `PAIVITYSOHJE.md` — tämä jatkotyöohje
- `index.md` — etusivu
- `arkisto.md` — blogiarkisto
- `kirjat.md` — kirjasivu
- `_data/books.yml` — kirjatiedot
- `_posts/` — blogiartikkelit
- `_layouts/default.html` — sivuston peruspohja
- `_layouts/post.html` — blogitekstin pohja
- `assets/css/style.css` — ulkoasu
- `assets/images/` — kuvat
- `assets/books/` — myöhemmin julkaistavat PDF-tiedostot

## Toimituksellinen linja

Noudata `STYLE.md`-tiedostoa.

Sivuston ääni on **empaattinen insinööri**:

- tekninen selkeys ilman kylmyyttä
- henkilökohtainen kokemus ilman tunnemyyntiä
- käytännöllinen mallintaminen ilman gurupuhetta
- rehellinen rajaus ilman itsensä pienentämistä

Merkittävän tekstin perusrakenne:

1. oma havainto
2. järjestelmämalli
3. lukijan peili

Vältä:

- moralismia
- mystiikkaa
- sankaritarinaa
- motivaatioteatteria
- yleistämistä ilman rajausta
- liian pitkää teoreettista johdantoa

## Julkaisu ja hyväksyntä

Sisältöä ei julkaista suoraan ilman hyväksyntää.

Normaali työnkulku:

1. Luonnos kirjoitetaan ensin keskusteluun.
2. Tekstiä hienosäädetään tarvittaessa.
3. Julkaisu tehdään vasta hyväksynnällä.

Hyväksyntäkomento:

```text
Julkaise
```

Tekniset ylläpitomuutokset, kuten kirjoitusvirheen korjaus, linkin lisääminen, kirjatiedon siirto rakenteisempaan muotoon tai selvästi pyydetty pieni muutos, voidaan tehdä suoraan, jos käyttäjä käskee tekemään muutoksen.

## Uuden blogitekstin lisääminen

Uudet blogitekstit tehdään kansioon `_posts/`.

Tiedostonimi:

```text
YYYY-MM-DD-otsikko.md
```

Esimerkki:

```text
_posts/2026-06-27-saunan-lattia-ja-yhden-nelion-virhe.md
```

Front matter:

```yaml
---
title: "Otsikko"
description: "Lyhyt kuvaus tekstistä."
date: 2026-06-27 12:00:00 +0300
categories: [arki, rakentaminen]
---
```

Jos `date` puuttuu, Jekyll käyttää tiedostonimen päivämäärää. Ajankohtaisissa päivämerkinnöissä päivämäärä ja paikka voidaan lisätä myös tekstin alkuun:

```html
<p class="meta">27.6.2026 · Evijärvi</p>
```

## Blogitekstien tyypit

Blogitekstin tyyppi päätellään pääosin kategorioista.

- `ai` → Artikkeli
- `kirjoittaminen`, `blogi` tai `kirjat` → Kirjapäivitys
- muut → Päivämerkintä

Sopivia kategorioita:

- `arki`
- `rakentaminen`
- `koirat`
- `ai`
- `yritykset`
- `lokaalit-mallit`
- `kirjoittaminen`
- `blogi`
- `kirjat`

## Arkisto

Arkistosivu on `arkisto.md`.

Arkistossa on valintakytkin:

- Aiheittain
- Aikajärjestyksessä

Molempia näkymiä ei näytetä yhtä aikaa.

Aiheittainen jako perustuu kategorioihin:

- AI ja teknologia: `ai`, `lokaalit-mallit`, `yritykset`
- Arjen rakenteet: `arki`, `rakentaminen`, `koirat`
- Kirjoittaminen ja kirjat: `kirjoittaminen`, `blogi`, `kirjat`

Kun lisäät uuden blogitekstin, valitse kategoriat niin, että arkisto osaa sijoittaa sen oikeaan ryhmään.

## Kirjasivun päivittäminen

Kirjasivu `kirjat.md` ei sisällä kaikkia kirjakortteja käsin.

Kirjatiedot ovat tiedostossa:

```text
_data/books.yml
```

`kirjat.md` lukee kirjat Liquid-loopilla:

```liquid
{% for book in site.data.books %}
```

Uusi kirja lisätään ensisijaisesti tiedostoon `_data/books.yml`.

Kirjan rakenne:

```yaml
- title: "Kirjan nimi"
  status: "PDF-versio 2025"
  availability: "PDF-versio tulossa ladattavaksi."
  description:
    - >
      Ensimmäinen kuvauskappale.
    - >
      Toinen kuvauskappale.
    - >
      Kolmas kuvauskappale.
```

Pidä kuvaukset tiiviinä. Kirjasivu ei ole koko kirjan esipuhe, vaan lukijalle annettu orientaatio.

Jos PDF julkaistaan myöhemmin repositoryyn, suositeltu polku on:

```text
assets/books/kirjan-tiedostonimi.pdf
```

Tämän jälkeen kirjatietoon voidaan lisätä esimerkiksi `pdf:`-kenttä ja muuttaa `kirjat.md` näyttämään latauslinkki.

Älä yritä lisätä PDF- tai kuvatiedostoja GitHubin tekstipohjaisella `create_file`-toiminnolla, ellei käytössä ole varmasti binääritiedostolle sopiva työkalu. Tekstitiedostojen luonti sopii Markdown-, YAML-, HTML- ja CSS-tiedostoille.

## Etusivu

Etusivu on `index.md`.

Etusivun tehtävä:

- kertoa sivuston perusajatus
- antaa sisääntuloreitti teeseihin, arkistoon ja kirjoihin
- näyttää viimeisimmät kirjoitukset

Etusivun nykyinen avauslause:

```text
Mikään ei ole rikki, ohjausjärjestelmän asetukset ovat vain säätämättä.
```

Älä muuta etusivun peruslinjaa kevyesti. Etusivu on sivuston käyttöliittymä, ei blogiteksti.

## Ulkoasu

Ulkoasu on tiedostossa:

```text
assets/css/style.css
```

Nykyinen korostusväri on sinertävä petrooli:

```css
--accent: #2f6f95;
```

Sivusto on tarkoituksella kevyt, luettava ja rauhallinen. Älä lisää raskaita efektejä, animaatioita tai monimutkaista käyttöliittymää ilman erillistä pyyntöä.

## Kuvien käyttö

Kuvat sijaitsevat kansiossa:

```text
assets/images/
```

Etusivun nykyinen hero-kuva:

```text
assets/images/evijarvi-hero.png
```

Kuvien kanssa pitää varmistaa, että tiedosto on oikeasti repositoryssä eikä vain keskustelun tai työkalun paikallinen tiedosto.

## Päivityksen tarkistuslista

Ennen commitia tarkista:

1. Muuttuiko oikea tiedosto?
2. Säilyikö nykyinen rakenne?
3. Onko teksti linjassa `STYLE.md`-ohjeen kanssa?
4. Onko uusi blogiteksti oikeassa kansiossa ja oikealla tiedostonimellä?
5. Onko kirjalisäys tehty `_data/books.yml`-tiedostoon eikä käsin `kirjat.md`-sivulle?
6. Onko YAML sisennyksiltään oikein?
7. Onko linkkipolku suhteellinen ja Jekyll-yhteensopiva?
8. Onko commit-viesti kuvaava?

## Käytännön aloitus uudessa keskustelussa

Kopioi tämä uuteen keskusteluun:

```text
Jatketaan sivustoa kataguru/blogi. Lue README.md, STYLE.md ja PAIVITYSOHJE.md. Päivitä sivustoa niiden mukaan. Kirjat ovat tiedostossa _data/books.yml. Uudet blogitekstit tulevat _posts-kansioon. Noudata ääntä: oma havainto → järjestelmämalli → lukijan peili. Älä julkaise uutta sisältöä ennen hyväksyntääni komennolla “Julkaise”.
```
