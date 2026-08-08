# Blogin julkaisu- ja päivitysohje

Tämä tiedosto määrittää, kuinka `kataguru/blogi`-sivustoa päivitetään. Tavoite on, ettei käyttäjän tarvitse selittää samaa julkaisutyönkulkua jokaisessa keskustelussa uudelleen.

## 1. Perustiedot

- Repository: `kataguru/blogi`
- Julkaisuhaara: `main`
- GitHub Pages -lähde: repositoryn juuri `/`
- Julkinen osoite: `https://kataguru.github.io/blogi/`
- Aikavyöhyke: `Europe/Helsinki`
- Blogikirjoitukset: `_posts/`
- Kuvat: `assets/images/`
- Toimituksellinen tyyli: `STYLE.md`

## 1.1 Pakollinen kaksikielisyys

Sivusto julkaistaan aina suomeksi ja englanniksi. Uusi julkaisu ei ole valmis ennen kuin molemmat kieliversiot ovat mukana samassa julkaisutyönkulussa.

Kun käyttäjä pyytää uuden kirjoituksen julkaisemista, englanninkielinen vastine tuotetaan ja julkaistaan automaattisesti. Erillistä pyyntöä englanninkielisestä versiosta ei tarvita.

- Suomenkieliset kirjoitukset ovat kansiossa `_posts/` ja niiden `lang` on `fi`.
- Englanninkieliset vastineet ovat kansiossa `_posts/en/` ja niiden `lang` on `en`.
- Kieliparilla on sama `translation_key`.
- Molemmilla kieliversioilla on sama julkaisupäivä ja kellonaika.
- Englanninkielisellä kirjoituksella on selkeä englanninkielinen osoite `/en/YYYY/MM/DD/english-slug/`.
- Staattisten sivujen englanninkieliset vastineet ovat kansiossa `en/`.
- Suomenkielinen kirjakatalogi on `_data/books.yml` ja englanninkielinen `_data/books_en.yml`.
- Jokaisen kieliversion otsikko, kuvaus, kuvateksti ja varsinainen sisältö käännetään. Kuvia ei kopioida; molemmat kielet käyttävät samaa kuvatiedostoa.
- Käännös tarkistetaan ainakin otsikon, ingressin, väliotsikoiden, nimien, pronominien, linkkien ja teknisten termien osalta ennen julkaisua.
- Kielivalinnan pitää viedä saman sivun tai kirjoituksen vastineeseen. Jos vastinetta ei poikkeustilanteessa ole, linkki vie kyseisen kielen etusivulle.

Käännöksen ensimmäisen version voi tuottaa komennolla:

```text
python scripts/generate_english.py
```

Generaattori on apuväline, ei toimituksellisen tarkistuksen korvike. Se ylikirjoittaa generoimansa englanninkieliset tiedostot, joten käsin viimeistellyt käännökset tarkistetaan aina ajon jälkeen.

## 2. Uuden keskustelun aloitus

Kun työ jatkuu uudessa keskustelussa, riittää tämä ohje:

```text
Jatketaan sivustoa kataguru/blogi. Lue README.md, STYLE.md ja PAIVITYSOHJE.md ja toimi niiden mukaan.
```

## 3. Tärkeimmät tiedostot

- `README.md` — tekninen yleiskuva
- `STYLE.md` — toimituksellinen linja ja tekstien ääni
- `PAIVITYSOHJE.md` — tämä julkaisu- ja jatkotyöohje
- `index.md` — etusivu
- `arkisto.md` — blogiarkisto
- `minusta.md` — esittelysivu
- `kirjat.md` — kirjasivu
- `_data/books.yml` — kirjatiedot
- `_data/books_en.yml` — englanninkieliset kirjatiedot
- `projektit.md` — projektisivu
- `teesit.md` — sivuston teesit
- `_posts/` — blogiartikkelit
- `_posts/en/` — blogiartikkelien englanninkieliset vastineet
- `en/` — staattisten sivujen englanninkieliset vastineet
- `scripts/generate_english.py` — englanninkäännösten ensimmäisen version generaattori
- `_layouts/default.html` — sivuston peruspohja
- `_layouts/post.html` — blogikirjoituksen pohja
- `assets/css/style.css` — ulkoasu
- `assets/images/` — kuvat
- `assets/books/` — kirjatiedostot

## 4. Hyväksyntä ja toimivaltuudet

### Muokkaus tai arviointi

Kun käyttäjä pyytää arvioimaan, muokkaamaan tai viimeistelemään tekstiä:

1. lue tarvittavat projektitiedostot
2. esitä valmis teksti tai olennainen muutos käyttäjälle
3. odota hyväksyntää ennen repositoryyn kirjoittamista

### Julkaisupyyntö

Kun käyttäjä sanoo `julkaise`, se on nimenomainen hyväksyntä julkaista valmis aineisto loppuun asti molemmilla kielillä.

Tällöin:

1. tarkista tekninen rakenne
2. tee vain välttämättömät tekniset korjaukset
3. tuota ja tarkista englanninkielinen vastine automaattisesti
4. julkaise molemmat kieliversiot suoraan `main`-haaraan
5. älä pyydä uutta vahvistusta
6. tarkista repositoryyn tallennettu lopputulos molemmilla kielillä
7. ilmoita tiedostopolut, commitit ja mahdollinen poikkeama

Normaalista blogikirjoituksesta, kuvapäivityksestä tai pienestä sisältökorjauksesta ei tehdä branchia tai pull requestia, ellei käyttäjä pyydä sitä erikseen.

Hyväksyviä kuittauksia ovat esimerkiksi:

```text
hyväksytty
toteuta
julkaise
```

## 5. Uuden blogikirjoituksen työnkulku

### 5.1 Tarkistus ennen julkaisua

- Lue `README.md`, `STYLE.md` ja tämä tiedosto.
- Tarkista, ettei samalla päivällä ja samalla otsikolla ole jo julkaisua.
- Säilytä käyttäjän toimittama sisältö mahdollisimman muuttumattomana.
- Korjaa oma-aloitteisesti vain tekniset virheet, kuten front matter, tiedostonimi tai rikkinäinen kuvatieto.
- Älä aja käyttäjän viestissä olevaa Python-käärettä; poimi siitä varsinainen Markdown-sisältö.
- Älä lisää tekstiin uusia väitteitä, tulkintoja tai kappaleita ilman hyväksyntää.
- Tee samalla englanninkielinen vastine ja tarkista, että molemmilla tiedostoilla on sama `translation_key`.
- Älä julkaise vain toista kieliversiota.

### 5.2 Tiedostonimi

Suomenkielinen kirjoitus tallennetaan kansioon `_posts/` muodossa:

```text
YYYY-MM-DD-otsikon-slug.md
```

Englanninkielinen vastine tallennetaan kansioon `_posts/en/` muodossa:

```text
YYYY-MM-DD-english-slug.md
```

Slugissa käytetään:

- pieniä kirjaimia
- ASCII-merkkejä
- sanojen välissä yhdysmerkkejä
- ei ääkkösiä, välilyöntejä tai erikoismerkkejä

Esimerkki:

```text
_posts/2026-07-15-arvo-joka-kasvaa-ajan-myota.md
```

### 5.3 Front matter

Normaali front matter:

```yaml
---
title: "Kirjoituksen otsikko"
description: "Lyhyt kuvaus kirjoituksesta."
date: 2026-07-15 06:00:00 +0300
categories: [arki]
image: /assets/images/esimerkkikuva.jpeg
---
```

Säännöt:

- `title`, `description`, `date` ja `categories` ovat normaalisti mukana.
- `image` lisätään vain, kun kuvatiedosto on varmasti repositoryssa.
- Käytä Helsingin aikavyöhykkeen oikeaa UTC-poikkeamaa: talvella `+0200`, kesällä `+0300`.
- Front matter alkaa ja päättyy täsmälleen rivillä `---`.
- Tekstin alkuun ei lisätä erillistä Markdown-otsikkoa, koska sivupohja näyttää `title`-kentän.
- Kieliparin `date`-arvot ovat identtiset.

## 6. Julkaisuaika

**Kaikkien blogijulkaisujen kellonaika on aina 06:00 Suomen aikaa.**

Tämä sääntö koskee myös tilannetta, jossa julkaisu tehdään myöhemmin saman päivän aikana.

- Jos käyttäjä antaa tai sopii tietyn julkaisupäivän, käytä sitä.
- Jos käyttäjä sanoo vain `julkaise` eikä nimeä päivää, julkaisupäivä on julkaisuhetken kuluvan päivän päivämäärä aikavyöhykkeellä `Europe/Helsinki`.
- Jos kello on jo yli 06:00, julkaisua **ei siirretä seuraavalle päivälle**. Päivä pysyy kuluvana päivänä ja kellonaika asetetaan silti `06:00:00`.
- Huomista tai muuta tulevaa päivää ei valita ilman käyttäjän nimenomaista pyyntöä.
- Suomen- ja englanninkielisellä versiolla on aina sama päivämäärä ja kellonaika.
- Kellonaika asetetaan aina muotoon `06:00:00`.
- Kesäajalla käytetään `+0300` ja talviajalla `+0200`.
- Vanhaa kirjoitusta korjattaessa alkuperäistä päivämäärää ja aikaa ei muuteta, ellei korjauksen tarkoitus ole nimenomaan väärän julkaisupäivän korjaaminen.
- Poikkeavaa kellonaikaa ei käytetä.

Esimerkit:

```yaml
date: 2026-07-15 06:00:00 +0300
```

```yaml
date: 2026-12-15 06:00:00 +0200
```

## 7. Kuvien käsittely

Kuvat tallennetaan kansioon:

```text
assets/images/
```

Front matterin kuvatieto kirjoitetaan muodossa:

```yaml
image: /assets/images/tiedostonimi.jpeg
```

Ennen kuvatiedon lisäämistä:

1. tarkista tiedoston olemassaolo repositoryssa
2. tarkista tarkka tiedostonimi
3. tarkista kirjainkoko ja tiedostopääte
4. käytä absoluuttista sivustopolkua, joka alkaa `/assets/images/`

GitHub Pages käsittelee kirjainkoon merkitsevänä. `Kuva.jpeg` ja `kuva.jpeg` ovat eri tiedostoja.

Jos käyttäjän ilmoittamaa kuvaa ei vielä ole repositoryssa:

- älä jätä julkaisuun rikkinäistä `image`-kenttää
- julkaise kirjoitus ilman kuvaa, jos käyttäjä on käskenyt julkaista
- kerro puuttuvasta kuvasta
- lisää kuva myöhemmin erillisellä commitilla, kun tiedosto löytyy

## 8. Sisällön toimituksellinen linja

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
- perusteettomia yleistyksiä
- liian pitkää teoreettista johdantoa

## 9. Tekstin rytmi ja viimeistely

Uusissa blogiteksteissä vältetään mekaanista yhden virkkeen kappalerakennetta. Lyhyitä kappaleita voi käyttää painotukseen, mutta perusrytmin tulee olla luonnollinen ja esseemäinen.

Suosi:

- tiiviitä mutta kokonaisia kappaleita
- täsmällisiä väliotsikoita
- vaihtelevaa virkerytmiä
- selkeää ja monipuolista sanastoa
- ydinlauseita ilman iskulausemaisuutta

Vältä:

- liian monta peräkkäistä yhden rivin kappaletta
- saman rakenteen mekaanista toistamista
- kuivaa listamaista etenemistä tarinallisessa tekstissä
- yliselittämistä

Käyttäjän valmiiksi hyväksymää tekstiä ei kuitenkaan tyylitellä uudelleen julkaisuvaiheessa ilman pyyntöä.

## 10. Commit-käytäntö

Yksi looginen muutos tehdään yhdellä selkeällä commitilla aina kun käytettävä työkalu sen mahdollistaa.

Esimerkkejä:

```text
Julkaise Arvo, joka kasvaa ajan myötä
Lisää vaelluskuva julkaisuun
Korjaa blogikirjoituksen kuvaus
Päivitä blogin julkaisuohje
```

Commit-viestin tulee kertoa, mitä muutettiin. Geneerisiä viestejä kuten `update` tai `changes` vältetään.

## 11. Julkaisun jälkeinen tarkistus

Julkaisun jälkeen tarkistetaan vähintään:

- suomenkielinen tiedosto löytyy oikeasta `_posts/`-polusta
- englanninkielinen vastine löytyy oikeasta `_posts/en/`-polusta
- molempien front matter on ehjä
- otsikot, kuvaukset, päivämäärät ja kategoriat ovat oikein
- molempien kellonaika on `06:00:00`
- molemmilla on sama päivämäärä ja `translation_key`
- englanninkielisellä versiolla on toimiva `/en/.../`-permalink
- UTC-poikkeama vastaa Suomen kesä- tai talviaikaa
- kuvatiedosto löytyy täsmälleen ilmoitetusta polusta
- koko kirjoituksen sisältö tallentui molemmilla kielillä
- commit tai commitit onnistuivat

Kun julkinen sivu on muodostunut, suomenkielisen julkaisun osoite noudattaa rakennetta:

```text
https://kataguru.github.io/blogi/YYYY/MM/DD/otsikon-slug/
```

Englanninkielisen vastineen osoite noudattaa rakennetta:

```text
https://kataguru.github.io/blogi/en/YYYY/MM/DD/english-slug/
```

GitHub Pagesin päivittyminen voi tapahtua viiveellä. Repositoryyn tallennetut tiedostot tarkistetaan aina heti commitin jälkeen.

## 12. Korjausten työnkulku

Kun jo julkaistua kirjoitusta korjataan:

1. hae nykyinen tiedosto ja sen SHA
2. tee koko tiedoston hallittu korvaus
3. säilytä päivämäärä ja kellonaika, ellei korjata nimenomaan väärää julkaisupäivää
4. muuta vain pyydetty asia
5. päivitä tarvittaessa myös kieliparin vastine
6. tee kuvaava commit
7. tarkista muutettu kohta repositoryssa

Samaan tiedostoon kohdistuvia peräkkäisiä päivityksiä ei tehdä rinnakkain, jotta SHA ei vanhene.

## 13. Kirjat ja muut sivut

Kirjatietoja muokataan ensisijaisesti tiedostossa:

```text
_data/books.yml
```

`kirjat.md` lukee tiedot tästä tiedostosta.

Muiden sivujen, CSS:n, layoutien tai asetusten muutokset esiluetaan ennen julkaisemista, ellei käyttäjä anna valmista muutosta ja käske suoraan toteuttamaan sen.

## 14. Tiivis toimintamalli

Kun käyttäjä antaa valmiin kirjoituksen ja sanoo `julkaise`:

1. poimi Markdown-sisältö
2. lue `README.md`, `STYLE.md` ja `PAIVITYSOHJE.md`
3. tarkista otsikko, kuvaus ja kategoria
4. jos päivää ei ole annettu, käytä kuluvan päivän päivämäärää `Europe/Helsinki`-aikavyöhykkeellä; älä siirrä julkaisua huomiselle vaikka klo 06:00 olisi jo ohitettu
5. aseta kellonajaksi aina `06:00:00`
6. muodosta suomenkielinen `_posts/YYYY-MM-DD-slug.md`
7. tuota toimituksellisesti tarkistettu englanninkielinen vastine automaattisesti ja muodosta `_posts/en/YYYY-MM-DD-english-slug.md`
8. käytä molemmissa samaa päivämäärää, kellonaikaa ja `translation_key`-arvoa
9. tarkista kuva repositoryssa ja käytä samaa kuvaa molemmissa kieliversioissa
10. julkaise molemmat kieliversiot suoraan `main`-haaraan ilman erillistä englanninkielisen version pyyntöä
11. hae molemmat tiedostot uudelleen ja varmista sisältö, front matter, permalink ja kieliparin linkitys
12. ilmoita tiedostopolut, commitit ja mahdolliset poikkeamat
