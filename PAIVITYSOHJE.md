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
- `projektit.md` — projektisivu
- `teesit.md` — sivuston teesit
- `_posts/` — blogiartikkelit
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

Kun käyttäjä sanoo `julkaise`, se on nimenomainen hyväksyntä julkaista valmis aineisto loppuun asti.

Tällöin:

1. tarkista tekninen rakenne
2. tee vain välttämättömät tekniset korjaukset
3. julkaise suoraan `main`-haaraan
4. älä pyydä uutta vahvistusta
5. tarkista repositoryyn tallennettu lopputulos
6. ilmoita tiedostopolku, commit ja mahdollinen poikkeama

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

### 5.2 Tiedostonimi

Kirjoitus tallennetaan kansioon `_posts/` muodossa:

```text
YYYY-MM-DD-otsikon-slug.md
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

## 6. Julkaisuaika

**Kaikkien blogijulkaisujen kellonaika on aina 06:00 Suomen aikaa.**

Tämä sääntö koskee myös tilannetta, jossa julkaisu tehdään myöhemmin saman päivän aikana.

- Päivämäärä määräytyy käyttäjän antaman tai sovitun julkaisupäivän mukaan.
- Kellonaika asetetaan aina muotoon `06:00:00`.
- Kesäajalla käytetään `+0300` ja talviajalla `+0200`.
- Vanhaa kirjoitusta korjattaessa alkuperäistä päivämäärää ja aikaa ei muuteta.
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

Yksi looginen muutos tehdään yhdellä selkeällä commitilla.

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

- tiedosto löytyy oikeasta `_posts/`-polusta
- front matter on ehjä
- otsikko, kuvaus, päivämäärä ja kategoriat ovat oikein
- kellonaika on `06:00:00`
- UTC-poikkeama vastaa Suomen kesä- tai talviaikaa
- kuvatiedosto löytyy täsmälleen ilmoitetusta polusta
- koko kirjoituksen sisältö tallentui
- commit onnistui

Kun julkinen sivu on muodostunut, julkaisun osoite noudattaa rakennetta:

```text
https://kataguru.github.io/blogi/YYYY/MM/DD/otsikon-slug/
```

GitHub Pagesin päivittyminen voi tapahtua viiveellä. Repositoryyn tallennettu tiedosto tarkistetaan aina heti commitin jälkeen.

## 12. Korjausten työnkulku

Kun jo julkaistua kirjoitusta korjataan:

1. hae nykyinen tiedosto ja sen SHA
2. tee koko tiedoston hallittu korvaus
3. säilytä päivämäärä ja kellonaika
4. muuta vain pyydetty asia
5. tee erillinen, kuvaava commit
6. tarkista muutettu kohta repositoryssa

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
2. tarkista otsikko, kuvaus, päivämäärä ja kategoria
3. aseta kellonajaksi aina `06:00:00`
4. muodosta oikea `_posts/YYYY-MM-DD-slug.md`-polku
5. tarkista kuva repositoryssa
6. julkaise suoraan `main`-haaraan
7. hae tiedosto uudelleen ja varmista sisältö
8. ilmoita tiedostopolku, commit ja mahdolliset poikkeamat
