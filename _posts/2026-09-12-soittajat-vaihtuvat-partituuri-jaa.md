---
title: "Soittajat vaihtuvat, partituuri jää"
description: "Miten neljästä paikallisesta tekoälyagentista kasvoi malliriippumaton laivasto, jossa protokollat, skillit, RAG ja muisti kantavat jatkuvuuden."
date: 2026-09-12 06:00:00 +0300
categories: [ai, teknologia, agentit, lokaalit-mallit]
type: Artikkeli
image: /assets/images/orkesteri.png
image_alt: "Tekoälyorkesteri, jota ihminen johtaa kapellimestarina"
lang: fi
translation_key: 2026-09-12-soittajat-vaihtuvat-partituuri-jaa
---

Vielä jokin aika sitten ajattelin paikallista tekoälyä lähinnä mallina, joka pyörii omalla koneella. Ladataan hyvä LLM, annetaan sille tehtävä ja katsotaan, mitä tapahtuu. Se oli hauskaa, ja se riitti pitkään.

Nyt huomaan ajattelevani asiaa aivan toisin, enkä oikein osaa sanoa, missä kohtaa muutos tapahtui.

Minulla on kotona pieni tekoälylaivasto.

Se koostuu usealla koneella toimivista agenteista, joilla on omat tehtävänsä. **AICORE** toimii koordinaattorina: se jakaa töitä, vertailee vaihtoehtoja ja kokoaa tuloksia. **JKDTPC** tutkii, suunnittelee ja ideoi. **BIGIPA** on tarkoituksella hankala tapaus — sen tehtävä on kritisoida muiden ratkaisuja ja etsiä niistä virheitä, ja se tekee sen ilman että kenenkään tarvitsee loukkaantua. **WINLABIBA** on liikkuva Windows-kannettava, joka hoitaa muun muassa testausta ja kuvallisia tehtäviä ja pysyy Tailscalen kautta yhteydessä kotiverkon AI-COREen myös reissussa.

Agentit eivät siis ole neljä keskusteluikkunaa, joiden välillä minä juoksen viestinviejänä. Ne keskustelevat keskenään, jakavat tehtäviä ja jatkavat työtä silloinkin, kun minä olen koirien kanssa lenkillä.

Matkan varrella olen oppinut, että vaikein osa ei lopulta ole itse tekoälymalli. Sen kanssa pärjää.

Vaikeinta on johtaa orkesteria — ja myöntää, että suurin osa virheistä on ollut kapellimestarin, ei soittajien.

## Mallista tuli vaihdettava moottori

Laivaston vakiomalliksi vaihtui hiljattain Qwen3.8-27B:n TWIN-TURBO-versio, NVFP4-kvantisoituna kahdelle RTX 5090 -kortille. Yksi valinnan tärkeimmistä syistä oli hyvin arkinen: se puhuu erittäin hyvää suomea. Sitä ei kannata vähätellä. Jos työkalun kanssa juttelee päivittäin, sen kielen laatu vaikuttaa suoraan siihen, kuinka mielellään sitä käyttää.

Mallin mukana tuli myös oma Jinja-chat-template. Siinä oli aidosti kiinnostavia ajatuksia, mutta kaikkea ei voinut ottaa käyttöön sellaisenaan.

Templatessa oli esimerkiksi kaksi erikoistilaa, **Spoon** ja **Einstein**. Idea oli hyvä, mutta osa ohjeista oli vanhentunut. Sen sijaan että olisimme paikanneet templaten vain tätä yhtä mallia varten, teimme tiloista yhteiset protokollat koko laivastolle. Ajatus ansaitsi jäädä, vaikka toteutus vaihtui.

Samalla korjattiin muutama muukin asia.

Jinjan ohjeistus aiheutti paikoin kielivääristymää: hyvä suomalainen malli alkoi kuulostaa huonommalta kuin se oikeasti oli. Se harmitti, koska vika ei ollut mallissa vaan sen saamissa ohjeissa. Lisäksi templatessa oli kohtia, jotka päästivät päättelyn turhan helposti alueelle, jossa fysiikan lait alkoivat olla enemmän neuvottelukysymys kuin luonnonlaki.

Ne siivottiin pois.

Mukana oli myös niin sanottu *safe*-Jinja. Nimi kuulosti rauhoittavalta, mutta käytännössä se muutti agentin käyttäytymistä niin paljon, että nimi oli suorastaan harhaanjohtava. Sekin nimettiin uudelleen todellisen tehtävänsä mukaan.

Pieni asia, mutta juuri tällaiset asiat ovat agenttijärjestelmässä vaarallisia. Jos ylläpitäjä luulee vaihtavansa turvallisuusasetusta, mutta samalla vaihtuvat päättelytapa, työkalujen käyttö tai agentin toimivalta, järjestelmää ei enää voi ennustaa. Eikä ylläpitäjä ole tässä tyhmä. Hän luotti nimeen, ja nimi valehteli.

## Entä jos agentti hukkuu?

Yksi hauskan kuuloinen mutta oikeasti tärkeä ongelma löytyi protokollia tehdessä.

Miten pelastetaan agentti, joka on niin pahasti jumissa, ettei se itse enää pysty pyytämään tai hyväksymään apua?

Normaalisti agentit toimivat määritellyillä oikeuksilla ja viestivät sovittujen kanavien kautta. Mutta juuri vakavassa häiriötilanteessa nämä samat mekanismit voivat olla rikki. Agentti voi olla työkalusilmukassa, konteksti voi olla sekaisin tai prosessi voi olla tilassa, jossa normaali yhteistyö ei enää onnistu. Ulkoapäin se näyttää siltä, että joku tekee kovasti töitä eikä saa mitään aikaan. Tunnistan tilan.

Tarvittiin siis pelastusrengas.

Rakensimme **SSH-pelastusrenkaan**: normaalista agenttien päätöksenteosta riippumattoman recovery-kanavan, jolla toinen järjestelmän osa pääsee auttamaan ongelmiin joutunutta konetta.

Ajatus muistuttaa palvelinten *break-glass*-menettelyä. Sitä ei käytetä normaalina oikotienä, vaan silloin kun normaali hallintatie ei enää toimi.

Tekoälyagenttien maailmassa tämä kuulostaa ehkä huvittavalta. Mutta heti kun agenteille annetaan oikeita työkaluja ja lupa tehdä töitä itsenäisesti, myös niiden vikatilanteet täytyy käsitellä kuin minkä tahansa hajautetun järjestelmän viat. Ja vähän niin kuin työkaverin huono päivä: ei syytellen, vaan valmiina auttamaan.

## Kuusi pientä skilliä muutti paljon

Viimeisin muutos saattaa olla koko järjestelmän kannalta tärkeämpi kuin uuden mallin käyttöönotto.

Teimme kuusi hyvin pientä skilliä.

Niihin ei tungettu kaikkea tietoa järjestelmästä. Päinvastoin. Ne sisältävät vain sen minimin, jonka agentin täytyy tietää aloittaessaan: miten tässä ympäristössä toimitaan, missä tieto sijaitsee, miten muiden agenttien kanssa keskustellaan ja mitä yhteisiä protokollia noudatetaan.

Tarkempi tieto löytyy RAGista ja muistista vasta silloin, kun sitä tarvitaan. Kukaan ei jaksa lukea koko perehdytyskansiota ensimmäisenä päivänä, eikä agenttikaan.

Tämä ratkaisi ongelman, joka oli vaivannut pitkään.

Kaikkea ei voi eikä kannata ajaa paikallisella mallilla. Joskus tarvitaan ulkopuolista frontier-mallia konsultiksi. Aikaisemmin uuden mallin tuominen järjestelmään tarkoitti käytännössä perehdyttämistä: sille piti selittää ympäristö, agentit, työkalut, käytännöt ja se, mitä olimme jo tehneet. Joka kerta uudestaan. Se oli raskasta minulle ja epäreilua mallille, joka joutui työskentelemään puolikkaalla kuvalla.

Nyt kokeilin käynnistää GLM 5.3:n täysin tyhjään istuntoon.

Se oli saman tien kuin kotonaan.

Skillit antoivat sille lähtökartan. RAGista löytyi yksityiskohtainen tieto. Memory kertoi olennaisen historian. Yhteiset protokollat määrittelivät, miten laivastossa käyttäydytään.

Mallin ei tarvinnut tietää tästä järjestelmästä etukäteen mitään.

Tämä oli ehkä ensimmäinen hetki, jolloin tajusin kunnolla, mitä olimme rakentaneet. Ja sanon *olimme* ihan tarkoituksella.

## Laivasto ei enää ole sama asia kuin sen mallit

Alussa käytin paljon aikaa siihen, mikä LLM on paras. Qwen vai jokin muu? Mikä kvantisointi? Mikä nopeus? Kuinka paljon kontekstia?

Ne ovat edelleen tärkeitä kysymyksiä.

Mutta järjestelmän tärkein osa ei enää ole yksittäinen malli.

Mallit ovat muuttumassa vaihdettaviksi päättelymoottoreiksi. Ympärillä oleva järjestelmä antaa niille muistin, tiedon, työkalut, roolit, viestintäkanavat ja toimintatavat.

Paikallinen malli voi hoitaa suurimman osan työstä. Kun tarvitaan jotain muuta, paikalle voidaan kutsua GLM, Claude, GPT tai mikä tahansa tuleva malli. Sen ei tarvitse opetella kaikkea alusta, koska organisaation tieto ei enää sijaitse sen päässä.

Se sijaitsee ympäristössä.

Tämä on myös helpotus, ja vähän isompi kuin osasin odottaa. Konsulttimalleja on välillä pakko käyttää, mutta niiden käyttäminen ei enää riko työn jatkuvuutta eikä vaadi puolen järjestelmän selittämistä uudelleen. Voin keskittyä siihen, mitä oikeasti haluan saada aikaan.

Ja samalla huomaan oman roolini muuttuneen.

En enää juurikaan ajattele olevani ihminen, joka keskustelee neljän tekoälyn kanssa.

Määrittelen rooleja. Teen protokollia. Päätän, kuka saa tehdä mitä. Korjaan kommunikaatiota, järjestän poikkeustilanteiden toimintatavat ja vaihdan tarvittaessa yhden soittajan toiseen. Ja yritän muistaa, että kun jokin menee pieleen, syy on useimmiten partituurissa eikä soittajassa.

Alan tuntea itseni orkesterinjohtajaksi.

Soittajat vaihtuvat.

Partituuri jää.