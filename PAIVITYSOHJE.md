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
Jatketaan GitHub Pages -sivustoa kataguru/blogi. Lue ensin README.md, STYLE.md ja PAIVITYSOHJE.md. Noudata sivuston nykyistä rakennetta. Esilue aina muutoksen sisältö tai tiivis diff keskustelussa ja odota kuittausta ennen commitia, PR:ää, mergeä tai muuta sivustopäivitystä.
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

Kaikki sivuston muutokset esiluetaan ennen päivitystä.

Tämä koskee sisältömuutoksia, teknisiä ylläpitomuutoksia, linkkejä, CSS:ää, asetuksia, kuvia, PR:iä, mergejä ja suoria committeja.

Normaali työnkulku:

1. Lue tarvittavat nykyiset tiedostot.
2. Näytä käyttäjälle muutoksen sisältö tai tiivis diff keskustelussa.
3. Odota käyttäjän kuittausta.
4. Tee vasta sen jälkeen tiedostomuutos, commit, PR tai merge.

Hyväksyviä kuittauksia ovat esimerkiksi:

```text
hyväksytty
toteuta
julkaise
```

Ilman kuittausta älä tee commitia, PR:ää, mergeä, tiedostopäivitystä tai muuta sivustoa.

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

{% raw %}
```liquid
{% for book in site.data.books %}
```
{% endraw %}

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

## Kuvitusperiaate

Jokaiseen blogitekstiin pyritään lisäämään yksi aito kuva.

Kuvan tehtävä ei ole koristella tekstiä, vaan antaa lukijalle tarttumapinta: paikka, esine, yksityiskohta, työvaihe, jälki, virhe, eläin, maisema tai hetki, johon tarina kiinnittyy.

Ensisijainen kuva on oma valokuva. Se tekee tekstistä todemman ja sitoo järjestelmäajattelun arkeen.

Perussääntö:

**Yksi teksti, yksi aito kuva, yksi tarttumapinta.**

Kuva sijoitetaan yleensä johdannon jälkeen ennen varsinaista analyysiä.

Kuva lisätään näin:

{% raw %}
```html
<figure class="post-image">
  <img src="{{ '/assets/images/kuvan-tiedostonimi.png' | relative_url }}" alt="Lyhyt kuvaus kuvasta">
</figure>
```
{% endraw %}

Nykyisiä käytettäviä kuvia:

- `assets/images/olivia_ja_kaapo.png`
- `assets/images/saunan_lattia.jpg`

AI-kuvia ei käytetä ensisijaisena kuvituksena. Niitä voidaan käyttää vain poikkeustapauksessa, jos aitoa kuvaa ei ole ja kuva on selvästi symbolinen eikä esitä tapahtumaa dokumentaarisena.

## Kävijälaskuri

Sivustolla on GoatCounter-pohjainen kävijälaskurituki.

Tärkeät tiedostot:

- `_config.yml` — asetus `goatcounter_code`
- `_layouts/default.html` — GoatCounter-seuranta ja footerissa näkyvä kokonaislaskuri
- `assets/css/style.css` — laskurin ulkoasu

Nykyinen oletuskoodi:

```yaml
goatcounter_code: "kataguru"
```

Jos GoatCounter-sivuston koodi vaihtuu, muuta vain `_config.yml`-tiedoston `goatcounter_code`-arvo.

Jos arvoksi asetetaan tyhjä merkkijono, laskuri ja seurantascripti eivät näy sivustolla:

```yaml
goatcounter_code: ""
```

GoatCounterin hallinnasta pitää sallia laskurin näyttäminen sivustolla. Asetuksen nimi on:

```text
Allow adding visitor counts on your website
```

Laskuri näyttää footerissa koko sivuston katselukerrat, ei yksittäisen sivun lukemaa.

## Päivityksen tarkistuslista

Ennen commitia tarkista:

1. Onko muutos esiluettu käyttäjälle?
2. Onko käyttäjä kuitannut muutoksen?
3. Muuttuiko oikea tiedosto?
4. Säilyikö nykyinen rakenne?
5. Onko teksti linjassa `STYLE.md`-ohjeen kanssa?
6. Onko uusi blogiteksti oikeassa kansiossa ja oikealla tiedostonimellä?
7. Onko kirjalisäys tehty `_data/books.yml`-tiedostoon eikä käsin `kirjat.md`-sivulle?
8. Onko YAML sisennyksiltään oikein?
9. Onko linkkipolku suhteellinen ja Jekyll-yhteensopiva?
10. Onko commit-viesti kuvaava?

## Käytännön aloitus uudessa keskustelussa

Kopioi tämä uuteen keskusteluun:

```text
Jatketaan sivustoa kataguru/blogi. Lue README.md, STYLE.md ja PAIVITYSOHJE.md. Päivitä sivustoa niiden mukaan. Kirjat ovat tiedostossa _data/books.yml. Uudet blogitekstit tulevat _posts-kansioon. Noudata ääntä: oma havainto → järjestelmämalli → lukijan peili. Esilue aina muutoksen sisältö tai tiivis diff keskustelussa ja odota kuittausta ennen commitia, PR:ää, mergeä tai muuta sivustopäivitystä.
```
