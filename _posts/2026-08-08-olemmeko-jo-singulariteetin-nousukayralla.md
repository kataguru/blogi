---
title: "Olemmeko jo singulariteetin nousukäyrällä?"
description: "Paikallinen tekoäly, muistijärjestelmät ja tehokkaat agenttivaljaat voivat muuttaa tekoälytyön kustannusrakenteen. Ehkä singulariteetin nousukäyrä alkaa tästä."
date: 2026-08-08 06:00:00 +0300
categories: [tekoäly]
lang: fi
translation_key: 2026-08-08-olemmeko-jo-singulariteetin-nousukayralla
image: /assets/images/singulariteetin-nousukayralla.jpg
image_alt: "Kaavio, jossa paikallinen tekoäly, muisti, työkalut, verkkohaku ja omat arkistot yhdistyvät jyrkästi nousevaan singulariteettikäyrään."
---

Vielä jokin aika sitten tekoälyn tulevaisuudesta puhuttiin yhden kysymyksen kautta: milloin mallit saavuttavat ihmisen tason. Olen alkanut epäillä, että se oli väärä kysymys. Kiinnostavampi kuuluu näin:

> Mitä tapahtuu, kun riittävän älykäs digitaalinen työntekijä voidaan ajaa omalla koneella lähes rajattomasti?

Tähän asti tekoälyn etenemistä on ollut helppo ajatella mallien kautta. Uusi GPT, Claude, Gemini, Qwen. Lisää parametreja, parempi benchmark, isompi konteksti. Mutta viime kuukausina olen tullut siihen tulokseen, että varsinainen muutos tapahtuu jossain muualla. Ei mallissa, vaan sen ympärillä.

## Malli ei ole koko järjestelmä

LLM yksinään on vähän kuin poikkeuksellisen lahjakas työntekijä, jolla ei ole muistia, työpöytää, puhelinta eikä pääsyä yrityksen tietoihin. Se osaa ajatella, mutta ei oikein tehdä työtä. Siksi ympärille rakennetaan valjaat — harness — joka antaa mallille muistin, työkalut, internetin, projektit, dokumentit, tietokannat, tiedostot, selaimen ja mahdollisuuden oikeasti tehdä jotain koneella.

Harnessissa on kuitenkin yksi vaarallinen ominaisuus: se voi myös tehdä hyvästä mallista huonon.

Huomasin tämän käytännössä Hermes Agentin kanssa. Oletusasetuksilla järjestelmä oli raskas — paljon työkaluja, MCP-skeemoja, muistia, kontekstia, kompressiota ja kaikenlaista metatyötä. Paikallinen 27 miljardin parametrin malli pärjäsi hetken ja alkoi sitten tukehtua. Ensimmäinen luonteva ratkaisu oli tarttua kaupalliseen API-malliin. Ja juuri tässä kohtaa kannatti pysähtyä.

## Entä jos vika ei ollutkaan mallissa?

Aloin purkaa harnessia. Turhat työkalut pois. Käyttämättömät MCP-palvelut pois. Kompressio omalle apumallilleen. Web-sivujen käsittely toiselle mallille. Muisti TencentDP:hen, embedding paikallisesti. Päämallille jäi vain se työ, jossa oikeasti tarvitaan päättelyä.

Ja tapahtui jotain kiinnostavaa. Paikallinen Qwen3.6-27B alkoi taas toimia hyvin. Samassa siivotussa harnessissa pyörii myös kaupallinen Ling-3.0-Flash, ja mallit ovat suunnilleen samaa kyvykkyysluokkaa. Ero ei siis ollutkaan siinä, että paikallinen malli olisi liian tyhmä.

**Harness söi sen älykkyyden.**

Tämä havainto muutti käsitykseni koko agenttimaailmasta. Olin syyttänyt mallia ongelmasta, jonka olin itse rakentanut sen ympärille.

## Kaikkien tokenien ei pitäisi maksaa samaa

Otetaan yksi pitkä agenttisessio, jossa järjestelmä käsittelee vaikkapa 10 miljoonaa tokenia. Niistä ehkä vain kolme miljoonaa tarvitsee oikeasti kallista ja älykästä päämallia. Loput on muistihakua, kompressiota, tiivistämistä, dokumenttien louhintaa, hakutulosten käsittelyä, luokittelua, embeddingiä ja yksinkertaisia subagenttitehtäviä — työtä, joka ei kaipaa frontier-tason ajattelua.

Lasketaanpa. Jos päämalli maksaa 10 euroa miljoonalta tokenilta ja kaikki kymmenen miljoonaa ajetaan sillä, lasku on 100 euroa. Jos vain kolme miljoonaa annetaan päämallille ja loput seitsemän 0,10 €/M maksavalle apumallille, hinta on 30,70 euroa. Ja jos apumallit pyörivät omalla koneella, API-lasku jää käytännössä kolmeenkymppiin. Sama tehtävä, sama päämalli, noin 70 prosenttia pienempi lasku.

Tämä on mielestäni paljon tärkeämpi optimointi kuin se, maksaako yksi malli 8 vai 10 euroa miljoonalta tokenilta. Sitä jälkimmäistä hierotaan hinnastoissa, kun oikea säästö on siinä, kuka ylipäätään tekee minkäkin osan työstä.

## Valmistajan harnessissa on kiinnostava kannustin

Mallivalmistajat tarjoavat mielellään omat agenttivaljaansa, ja se on ymmärrettävää — ne ovat helppoja ottaa käyttöön. Mutta samalla luovutan yhden tärkeän asian palveluntarjoajalle: **työn reitityksen.**

En tiedä, miten kukin suljettu järjestelmä sisäisesti hoitaa sivutehtävänsä. Ne voivat käyttää eri kokoisia malleja, deterministisiä palveluita ja erikoistuneita komponentteja. Olisin itse asiassa hyvin yllättynyt, jos kaikki työ tehtäisiin aina samalla kaikkein kalleimmalla mallilla. Mutta asiakkaalle koko homma voidaan silti esittää yhden mallin ja yhden hinnoittelun kautta. Siitä syntyy kysymys, joka kustannustietoisen asiakkaan kannattaisi esittää:

> Mitä mallia työni eri vaiheissa todellisuudessa käytetään, ja millä perusteella minua niistä laskutetaan?

Omassa harnessissa tätä ongelmaa ei ole, koska minä päätän. Päämalli ajattelee, pieni paikallinen malli tiivistää, embedding-malli etsii, reranker järjestää, ohjelmakoodi laskee ja web-haku hakee ajantasaisen tiedon. Mallia käytetään vain silloin, kun tarvitaan mallia — ei siksi, että se sattuu olemaan päällä.

## Muisti ja harness ovat saman muutoksen kaksi puolta

Toinen tämän hetken iso kehitysalue on LLM-muisti. Olen liittänyt Hermekseen TencentDP-muistin, ja vaikutus on huomattava. Agentti tietää kuka olen, muistaa projektini, aiemmat päätökset ja keskustelut. Kokemus alkaa muistuttaa ChatGPT:tä, paitsi että järjestelmä pyörii omassa ympäristössäni.

Pelkkä muisti ei silti riitä. Jos kaikki muistot dumpataan päämallin kontekstiin, ollaan taas samassa suossa: hyvä malli tukehtuu valjaisiin. Muisti pitää hakea semanttisesti ja tilanteen mukaan, ja sama koskee omia arkistojani. Hyvä digitaalinen agentti tarvitsee nopean, monikielisen ja multimodaalisen semanttisen haun omiin dokumentteihin, PDF:iin, kuviin, sähköposteihin ja projekteihin — ehkä myöhemmin myös ääneen ja videoon. Sen lisäksi se tarvitsee reaaliaikaisen pääsyn ulkomaailmaan.

Silloin järjestelmällä on kolme erilaista tietolähdettä: mallin oma tietämys, käyttäjän oma historia ja maailman tämänhetkinen tila. Näiden oikea yhdistäminen on ehkä tärkeämpää kuin vielä muutama prosentti lisää benchmark-pisteitä. Benchmark mittaa mallia. Tämä mittaa järjestelmää.

## Ja sitten tulee ensi viikko

Tätä kirjoittaessani odotan yhtä mallijulkaisua tavallista uteliaampana: Qwen3.8-27B. Jos odotukset pitävät, kyseessä voi olla selvästi nykyistä Qwen3.6-27B:tä vahvempi avoin malli samassa kokoluokassa.

27 miljardia parametria on tärkeä numero. Se ei ole datakeskusmalli. Se on kuluttajaraudan malli, ja kvantisoituna sellainen pyörii tehokkaalla kotikoneella. Jos sen agenttikyvykkyys, luotettavuus ja hallusinaatioiden hallinta paranevat riittävästi, jotain olennaista siirtyy paikaltaan. Tähän asti frontier-tason tekoäly on käytännössä tarkoittanut ketjua pilvi → API → tokenilasku. Seuraava vaihe voi näyttää tältä:

> avoin malli → oma GPU → oma harness → oma muisti → oma data

Marginaalikustannuksena lähinnä sähkö.

## Älä enää kysy vain, mitä mallia käytät

Kun tokenit maksavat, olemme tottuneet vertailemaan malleja: mikä maksaa 2 euroa miljoonalta tokenilta, mikä 10 euroa, mikä on nopein ja mikä älykkäin.

Mutta agenttien aikakaudella kysymys on liian kapea.

> **Älä kysy enää vain, mitä mallia käytät. Kysy, mitä harnessia käytät.**

Harness ratkaisee, kuinka suuri osa työstä ylipäätään päätyy kalliille päämallille. Se päättää, käsitelläänkö kompressio, muistihaku, embedding, reranking, web-extract, luokittelu ja subagenttityö halvalla apumallilla, paikallisesti vai samalla kalliilla mallilla kuin varsinainen päättely.

Siksi kaksi käyttäjää voi käyttää täsmälleen samaa frontier-mallia ja maksaa samasta työstä täysin eri summan.

Mallin hinnasto kertoo tokenin hinnan.

**Harness kertoo, kuinka monta kallista tokenia sinun tarvitsee ostaa.**

Ja juuri siksi harness voi lopulta ratkaista tekoälytyön talouden enemmän kuin itse mallivalinta.

## Tässä kohtaa työmarkkinakysymys muuttuu

Yksi suurimmista tekoälytyön esteistä on yhä kustannus. Jos agentti polttaa miljoonia tokeneita pitkään tehtävään, työn teettäminen sillä ei välttämättä ole halpaa. Mutta mitä tapahtuu, jos samaan aikaan toteutuvat nämä: mallit saavuttavat riittävän älykkyystason, avoimet mallit kurovat suljetut frontier-mallit kiinni, inference siirtyy kuluttajaraudalle ja harnessit oppivat käyttämään huippumallia vain siihen muutamaan vaikeaan prosenttiin työstä?

Silloin tekoälytyön hinta voi romahtaa. Ei 20 prosenttia — kertaluokkia. Ja juuri siinä kohtaa työmarkkinoiden kysymys ei enää ole "voiko tekoäly tehdä tämän työn", vaan:

> Kuinka monta ihmistä tämän työn tekemiseen enää tarvitaan?

Viiden hengen tiimi ei välttämättä muutu nollan hengen tiimiksi. Se saattaa muuttua yhden tai kahden ihmisen ja kahdenkymmenen agentin tiimiksi. Taloudellinen vaikutus voi olla lähes yhtä suuri, vaikka lopputulos näyttää inhimillisemmältä.

## Olemmeko singulariteetin nousukäyrällä?

**Arvio:** en tiedä, olemmeko matkalla varsinaiseen teknologiseen singulariteettiin. Kukaan ei tiedä. Mutta jotain singulariteetin kaltaista tässä kehityksessä on.

Yksittäiset muutokset eivät näytä valtavilta. Mallista tulee vähän parempi. Muisti toimii vähän paremmin. Harness kuluttaa vähän vähemmän tokeneita. Embedding paranee. GPU:t nopeutuvat. Avoimet mallit lähestyvät suljettuja. Yksi apumalli maksaa enää kymmenen senttiä miljoonalta tokenilta. Erikseen katsottuna mikään näistä ei ole uutinen.

Sitten nämä käyrät kerrotaan keskenään. Se on se kohta, joka helposti jää huomaamatta. Jos älykkyys kasvaa 30 prosenttia, luotettavuus 30 prosenttia, autonomisuus kaksinkertaistuu ja kustannus putoaa kymmenesosaan, lopputulos ei ole "hieman parempi chatbot". Se on kokonaan erilainen tuotantoteknologia.

Ehkä singulariteetin alku ei näytäkään siltä, että jonain aamuna superäly herää datakeskuksessa. Ehkä se näyttää paljon tylsemmältä. Joku huomaa työhuoneessaan, että 27 miljardin parametrin avoin malli toimii nyt koko päivän hänen omalla näytönohjaimellaan, muistaa hänen projektinsa, hakee hänen arkistonsa, käyttää internetiä, tekee työnsä itse ja maksaa käytännössä vain sähköä. Ja sitten sama havainto tehdään miljoonassa muussa työhuoneessa.

Siinä kohtaa käyrä saattaa jo olla nousussa. Me vain seisomme vielä niin lähellä sitä, ettemme näe sen jyrkkyyttä.
