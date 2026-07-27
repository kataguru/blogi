---
title: "Näkymätön kulutus: näin LLM-agentti voi kasvattaa API-laskua ilman aktiivista käyttöä"
description: "LLM-agentin taustalla pyörivä silmukka voi kuluttaa miljoonia tokeneita vuorokaudessa. Näin tunnistat vuodon ja rajaat kustannusriskin."
date: 2026-07-27 06:00:00 +0300
categories: [tekoäly]
lang: fi
translation_key: 2026-07-27-nakymaton-kulutus
image: /assets/images/vuoto.png
image_alt: "Näkymätöntä kulutusta ja resurssivuotoa havainnollistava kuva"
---

LLM-agentti ei ainoastaan vastaa kysymyksiin. Se voi käyttää työkaluja, lukea tiedostoja, suorittaa komentoja ja jatkaa saman tehtävän käsittelyä useiden peräkkäisten mallikutsujen ajan. Claude Code, Codex ja vastaavat agentit tekevät työtä, jota käyttöliittymä näyttää vain osittain.

Juuri tämä tekee agentista tehokkaan — ja samalla vaikeammin valvottavan kuin tavallisen chatbotin. Yksi näkyvä vastaus voi kätkeä taakseen kymmeniä mallikutsuja.

Jos agentti jää silmukkaan, taustatehtävä käynnistyy liian usein tai automaatio tekee odottamattomia kutsuja, tokeneita kuluu silloinkin, kun käyttöliittymässä ei näytä tapahtuvan mitään. Paikallisella mallilla tämä maksaa lähinnä sähköä. Maksullisessa API:ssa jokainen laskutettava token kasvattaa laskua — pahimmillaan satoja tai tuhansia euroja kuukaudessa.

## Havainto: yli 3 000 tokenia minuutissa

Seuraava havainto on **paikallisesta LM Studio -ympäristöstä**. Se ei siis tuottanut yhtään laskutettavaa tokenia — mutta se paljastaa juuri sen kuvion, joka maksullisessa API:ssa alkaisi maksaa.

Käyttäjä huomasi lokista, että generoitujen tokenien laskuri kasvoi ilman näkyvää keskustelua:

```text
n_decoded: 36 204 → 38 056
Aikaa: 36 sekuntia
```

Erotus on 1 852 tokenia. Se vastaa noin 51 tokenia sekunnissa eli yli 3 000 tokenia minuutissa. Malli siis *generoi*, vaikka käyttäjä ei odottanut sitä.

Jos oletetaan — puhtaasti laskennallisena pahimpana tapauksena — että sama nopeus jatkuisi keskeytyksettä:

- tunnissa noin 185 000 tokenia
- vuorokaudessa noin 4,4 miljoonaa tokenia
- 30 päivässä noin 133 miljoonaa tokenia

Oletus keskeytymättömästä 24 tunnin generoinnista on tietoisen karkea; todellinen agenttiajo sisältää taukoja, virheitä ja odotusta. Lukujen tarkoitus ei ole ennuste vaan suuruusluokka: pieni jatkuva vuoto skaalautuu nopeasti isoksi.

Pelkkä lokihavainto ei kerro, *mikä* prosessi tokenit tuotti. Se kertoo silti olennaisen: mallipalvelimelle tuli generointia, jota käyttäjä ei pyytänyt.

## Mitä jatkuva generointi maksaisi API:ssa?

API-hinnat ilmoitetaan dollareina miljoonaa tokenia kohti, ja syöte-, tuloste-, välimuisti- ja päättelytokenit hinnoitellaan eri tavoin. Tarkka kustannus riippuu siksi kutsujen rakenteesta.

Jos yksinkertaistetaan ja oletetaan 4,4 miljoonaa laskutettavaa **tulostetokenia** vuorokaudessa, kustannus asettuu mallin tulostehinnan mukaan seuraavasti. Hintapisteet on ankkuroitu Anthropicin heinäkuun 2026 nykymalleihin:

| Tulostehinta / milj. tokenia | Esimerkkimalli | Päivässä | 30 päivässä |
|---:|---|---:|---:|
| 5 $ | Haiku 4.5 | noin 22 $ | noin 660 $ |
| 10 $ | Sonnet 5 (intro) | noin 44 $ | noin 1 320 $ |
| 15 $ | Sonnet 5 (standardi) | noin 66 $ | noin 1 980 $ |
| 25 $ | Opus 4.8 | noin 110 $ | noin 3 300 $ |
| 50 $ | Fable 5 / Mythos 5 | noin 220 $ | noin 6 600 $ |

Taulukko on suuntaa antava, ei ajantasainen hintavertailu. Todellinen lasku on usein **suurempi**, koska agentti lähettää joka kierroksella takaisin myös keskusteluhistoriaa, tiedostosisältöä ja työkalujen tuloksia — eli maksaa myös syötepuolella, ei vain tulosteesta.

Esimerkkihinnat heinäkuussa 2026: Opus 4.8 maksaa 5 $ / 25 $ (syöte/tuloste), Sonnet 5 introhinnalla 2 $ / 10 $ (standardi 3 $ / 15 $ 1.9.2026 alkaen), Haiku 4.5 1 $ / 5 $ ja Mythos-luokan Fable 5 10 $ / 50 $ miljoonalta tokenilta. Vertailun vuoksi: vielä Opus 4.1 -sukupolvessa tuloste maksoi 75 $ / milj., joten nykyinen kattohinta on selvästi matalampi kuin aiemmin. Välimuistilla ja eräajolla on omat hintansa. **Tarkista ajantasainen hinta aina palveluntarjoajalta.** [Anthropicin hinnasto](https://platform.claude.com/docs/en/about-claude/pricing)

Sama periaate koskee muitakin palveluita. Esimerkiksi Google kertoo agenttien laskutukseen voivan sisältyä syöte-, tuloste- ja päättelytokeneita sekä agenttisilmukoiden välivaiheita. [Gemini API:n hinnasto](https://ai.google.dev/gemini-api/docs/pricing)

## Mikä aiheuttaa taustakulutusta?

### 1. Agentti jää työkalusilmukkaan

Agentti voi yrittää samaa epäonnistuvaa vaihetta uudelleen:

1. malli päättää kutsua työkalua
2. työkalu palauttaa virheen tai epäselvän tuloksen
3. tulos lähetetään takaisin mallille
4. malli yrittää lähes samaa toimintoa uudestaan

Jokainen kierros voi sisältää uuden mallikutsun ja suuren osan aiemmasta kontekstista. Käyttöliittymässä tämä näyttää vain hitaalta tai jumiutuneelta tehtävältä.

### 2. Ajastettu tehtävä käynnistyy liian usein

Cron-jobi tai muu ajastus saattaa tehdä raportin, tarkistuksen tai synkronoinnin minuutin välein, vaikka tarkoitus oli suorittaa se kerran päivässä. Yksittäinen ajo voi olla halpa. Satoja tai tuhansia kertoja kuukaudessa toistuva ei välttämättä ole.

### 3. Päättynyt tehtävä käynnistyy uudelleen

Virheellinen automaatio voi tulkita keskeneräisen tilan uudeksi työksi. Agentti aloittaa saman tehtävän yhä uudestaan ilman ulkopuolista pyyntöä.

### 4. Pitkä konteksti lähetetään jokaisella kierroksella

Agentti voi liittää pyyntöön keskusteluhistorian lisäksi suuria tiedostoja, lokitulosteita tai työkalujen vastauksia. Tällöin lyhytkin vastaus edellyttää valtavan syötekontekstin käsittelyä.

Kulutus ei siis aina näy generointinopeudessa: agentti voi käyttää paljon rahaa myös lukemalla saman kontekstin toistuvasti.

### 5. MCP-integraatio käynnistää agenttityötä

MCP-palvelin ei tavallisesti kuluta LLM-tokeneita pelkästään siksi, että se on yhdistetty. Kustannuksia syntyy, jos agentti tai sitä ohjaava sovellus kutsuu mallia työkalujen löytämiseksi, valitsemiseksi tai niiden tulosten tulkitsemiseksi.

Mitä enemmän integraatioita agentille annetaan, sitä tärkeämpää on seurata: milloin niitä kutsutaan, mikä käynnistää kutsun, palautetaanko tulokset mallille ja onko kutsuille asetettu määrällisiä rajoja.

### 6. Mallien automaattinen etsintä toimii väärin

Joissakin sovelluksissa mallilista haetaan automaattisesti palveluntarjoajan `/models`-rajapinnasta. Tavallinen mallilistan hakeminen ei yleensä itsessään generoi laskutettavia LLM-tokeneita.

Jos kuitenkin havaitset `discover_models`-asetuksen yhteydessä jatkuvia pyyntöjä tai mallin uudelleenlatauksia, poista automaattinen etsintä käytöstä testin ajaksi. Vaikutusta ei kannata olettaa yleispäteväksi — se riippuu agentista, palveluntarjoajasta ja ohjelmistoversiosta.

### 7. Auki oleva käyttöliittymä ylläpitää aktiivista prosessia

Pelkkä WebSocket-yhteys tai avoin selainikkuna ei normaalisti kuluta tokeneita. Käyttöliittymä voi kuitenkin sisältää automaattista kyselyä, tilapäivityksiä tai tehtävän jatkamista, jotka käynnistävät mallikutsuja.

Olennaista ei siis ole se, onko yhteys avoinna, vaan lähetetäänkö sen kautta uusia generointipyyntöjä.

## Miksi kulutus jää helposti huomaamatta?

**Näkyvyyden puute.** Agentti voi näyttää yhden tehtävän tai istunnon, vaikka sen sisällä suoritetaan kymmeniä mallikutsuja.

**Laskutuksen viive.** Luottokorttilasku saapuu jälkikäteen, ja myös palveluntarjoajan käyttöraportit voivat päivittyä viiveellä.

**Kustannusten hajautuminen.** Agentin toiminta voi sisältää syöte-, tuloste- ja päättelytokeneita, välimuistin kirjoituksia ja lukuja, työkalu- tai hakumaksuja sekä useiden eri mallien kutsuja. Yksi näkyvä vastaus ei siksi vastaa yhtä API-kutsua.

## Tarkistuslista maksullisen API:n käyttäjälle

### Ennen agentin käynnistämistä

- Aseta hallintapaneelissa kulutus- ja budjettihälytykset.
- Käytä erillistä API-avainta jokaiselle agentille tai projektille.
- Aseta avaimelle mahdollisimman pieni käyttöraja.
- Tarkista kaikki ajastetut tehtävät.
- Poista käytöstä tarpeettomat integraatiot ja automaatiot.
- Rajoita agentin työkalukierrosten ja uudelleenyritysten määrää.
- Testaa asetukset ensin paikallisella tai halvemmalla mallilla.

### Käytön aikana

- Seuraa tokeneita pyyntökohtaisesti, ei vain istunnon tasolla.
- Tarkkaile API-pyyntöjen määrää ja aikaleimoja.
- Kiinnitä huomiota jatkuvaan GPU-, CPU- tai verkkokuormaan.
- Tarkista agentin oma kustannusnäkymä, jos sellainen on.
- Varmista, että keskeytyskomento lopettaa myös taustaprosessin.

### Jos kulutusta näkyy ilman aktiivista käyttöä

1. Keskeytä agentin tehtävä tai sulje istunto.
2. Pysäytä tarvittaessa agentin palvelinprosessi.
3. Peruuta tai vaihda API-avain, jos et pysty pysäyttämään liikennettä varmasti.
4. Tarkista palveluntarjoajan käyttöloki.
5. Etsi aikaleimoista, mallinimistä ja tunnisteista toistuva kuvio.
6. Käynnistä ominaisuudet uudelleen yksi kerrallaan, kunnes aiheuttaja löytyy.

Pelkkä käyttöliittymän sulkeminen ei riitä, jos agentti, ajastin tai palvelin jatkaa taustalla.

## Paikallinen malli on hyvä testiympäristö

LM Studio ja Ollama ovat hyödyllisiä juuri tällaisten ongelmien löytämisessä. Paikallisessa ympäristössä virheellinen silmukka ei aiheuta API-laskua, vaikka se varaa näytönohjaimen, kuormittaa prosessoria ja kuluttaa sähköä. Sama vika, jonka voi turvallisesti bongata paikallisesti, olisi pilvessä maksanut rahaa.

| Ominaisuus | Paikallinen malli | Maksullinen API |
|---|---|---|
| Suora tokenikustannus | Ei yleensä ole | Laskutetaan käytön mukaan |
| Keskeinen rajoite | GPU, muisti ja nopeus | Budjetti ja käyttörajat |
| Virheellisen silmukan seuraus | Laskentaresurssien tuhlaus | Mahdollisesti suuri lasku |
| Soveltuvuus testaukseen | Erittäin hyvä | Käytä tiukkoja rajoja |

Paikallinen testi ei silti paljasta kaikkia pilvipalvelun kustannuksia. API:ssa esimerkiksi pitkä syötekonteksti, päättelytokenit ja ulkoiset työkalut voivat muodostaa suuren osan laskusta.

## Tärkein turvamekanismi ei ole yksi asetus

Yksittäisen asetuksen — kuten mallien automaattisen etsinnän — poistaminen voi ratkaista tietyn ohjelmistoversion ongelman. Se ei kuitenkaan suojaa agenttisilmukoilta, liian tiheiltä ajastuksilta tai valtavilta konteksteilta.

Luotettava suoja muodostuu kerroksista:

- pieni käyttöraja
- automaattiset budjettihälytykset
- pyyntökohtainen lokitus
- rajoitettu määrä agenttikierroksia
- erilliset API-avaimet
- selkeä tapa pysäyttää kaikki taustaprosessit

## Lopuksi

LLM-agentin kustannusriski ei synny siitä, että agentti olisi lähtökohtaisesti vaarallinen. Se syntyy siitä, että agentti voi tehdä paljon enemmän kuin käyttöliittymä näyttää.

Noin 51 tokenin sekuntinopeudella jatkuva prosessi tuottaisi yli neljä miljoonaa tokenia vuorokaudessa. Halvalla mallilla (Haiku 4.5, 5 $ / milj.) se tarkoittaisi joitakin satoja dollareita kuukaudessa; ylimmän tason mallilla (Fable 5, 50 $ / milj.) noin 6 600 dollaria. Vanhan Opus 4.1 -sukupolven 75 dollarin tulostehinnalla luku olisi ollut lähes 10 000 — ero havainnollistaa, miksi pelkkä mallivalinta voi muuttaa riskin suuruusluokkaa.

Siksi maksullista API:a käyttävää agenttia ei kannata jättää valvomatta ennen kuin kolme asiaa ovat kunnossa: **kulutus näkyy, käyttö on rajattu ja prosessi voidaan pysäyttää varmasti.**

*Hinnat ja mallivalikoimat muuttuvat nopeasti. Tarkista aina ajantasaiset syöte-, tuloste-, päättely-, välimuisti- ja työkaluhinnat käyttämäsi palveluntarjoajan hinnastosta.*
