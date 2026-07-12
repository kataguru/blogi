---
title: "Lokaali tekoälyagentti: työkalu, joka tuntee oman aineistoni"
description: "Raportti henkilökohtaisesta RAG-agentista, joka yhdistää lokaalin mallin, semanttisen haun ja dokumenttienhallinnan. Ei pilveä, ei tilausta — työkalu, joka toimii omilla ehdoilla."
date: 2026-07-12 06:00:00 +0300
categories: [ai, teknologia, lokaalit-mallit, rag]
type: Artikkeli
image: /assets/images/ai.png
image_alt: "Lokaali tekoälyagentti kotitoimiston työasemassa"
---

Olen viime viikkoina rakentanut agentin, joka yhdistää monikielisen semanttisen haun, koodin rakenteellisen ymmärtämisen ja dokumenttienhallinnan. Ei pilvipalvelua, ei SaaS-tiliä. Omalla koneella pyörivä järjestelmä, joka tietää mitä olen kirjoittanut, missä tiedostossa mikäkin funktio on ja miten asiaan pääsee takaisin.

## Miksi tämä ylipäätään

Olen kirjoittanut blogiin pitkään asioista, joita yritän ymmärtää: arjen rakenteita, päätösten hintaa, keskinkertaisuuden sietämistä. Mitä enemmän tekstiä, koodia ja dokumentteja kertyy, sitä vaikeampaa löytäminen on.

Avainsanahaku ei riitä. Jos haen "riskin normalisointia", en löydä postausta rappusista. Jos haen "halvan valinnan todellista hintaa", en osaa arvata mitä sanaa itse käytin kaksi vuotta sitten. Tarvitsen haun, joka etsii merkityksen perusteella eikä sananmuodon.

Pilvipalvelut tekevät tämän vain ulkoisilla lähteillä. Ne eivät tunne omia tiedostojani, omaa koodiani, omia paperejani — ja edellyttävät, että data siirtyy ulos.

Lokaali agentti ratkaisee molemmat ongelmat samalla kertaa.

## Järjestelmän rakenne

Ytimessä on lokaali kielimalli, joka pyörii omalla koneella kvantisoituna. Kvantisointi pienentää muistintarpeen murto-osaan alkuperäisestä ilman, että laatu käytännön käytössä romahtaa.

Malliin on kytketty kolme tietolähdettä:

**Vektorihaku (RAG).** Qdrant indeksoi tekstit, koodin ja hakutulokset semanttisina vektoreina. Kysely osuu merkitykseen, ei kirjaimeen.

**Tietämysgraafi.** Rakenteellinen muisti projekteista, päätöksistä ja konventioista. Vektorihaku kertoo mitä on kirjoitettu; graafi kertoo miksi jokin päätös aikanaan tehtiin.

**Paperless-ngx.** Skannatut dokumentit, laskut, kirjeet. OCR:n jälkeen nekin päätyvät samaan hakuavaruuteen kuin kaikki muu.

Yksi kysely, kolme muistin tasoa.

## Monikielisyys ei ole lisäominaisuus

Suomi ei ole tekoälyn ensisijainen kieli. Useimmat upotusmallit koulutetaan englanniksi, ja "monikielisyys" tarkoittaa käytännössä sitä, että muut kielet toimivat sinnepäin.

Tässä järjestelmässä lähtökohta on toinen. Käytössä on `multilingual-e5-small`, joka sijoittaa yli sadan kielen tekstit samaan vektoriavaruuteen. Suomenkielinen kysely löytää englanninkielisen dokumentin. Ruotsinkielinen muistiinpano kytkeytyy suomenkieliseen blogipostaukseen.

E5-mallit vaativat ohjeprefiksit: `query:` haussa, `passage:` indeksoinnissa. Ilman niitä lyhyen kyselyn ja pitkän dokumentin välinen epäsymmetria heikentää osumatarkkuutta selvästi. Pieni yksityiskohta, iso vaikutus.

## Koodi on rakennetta, ei tekstiä

Useimmat RAG-järjestelmät pilkkovat koodin mielivaltaisiin palasiin samalla logiikalla kuin tavallisen tekstin. Se rikkoo merkityksen.

Tämä järjestelmä pilkkoo koodin kielikohtaisesti:

- Python jäsennetään AST-puuksi, jolloin luokat ja funktiot erottuvat rakenteellisina yksikköinä
- JavaScript ja TypeScript tunnistetaan säännöllisillä lausekkeilla, myös nuolifunktiot ja rajapintamäärittelyt
- Rustista löytyvät structit, enumit, traitit ja impl-lohkot
- Go ja Java käsitellään vastaavasti rakenteen mukaan

Kun kysyn "missä Paperless-synkronointi tapahtuu", järjestelmä ei etsi sanaa *synkronointi* satunnaiselta riviltä. Se palauttaa `sync_round`-funktion kokonaisena, koska se tietää mihin yksikköön rivi kuuluu.

Ero ei ole kosmeettinen. Palanen ilman kontekstia on lainaus; palanen rakenteen mukaan on vastaus.

## Yksi prosessi, ei kahta

Alkuperäisessä suunnitelmassa oli kaksi taustaprosessia: toinen valvoi kooditiedostoja, toinen synkronoi Paperless-dokumentteja. Molemmat latasivat oman upotusmallinsa muistiin. Kaksinkertainen työ, kaksinkertainen kulutus.

Yhdistin ne yhdeksi daemoniksi, joka lataa mallin kerran ja hoitaa molemmat tehtävät samassa silmukassa. SHA256-tiiviste kertoo onko tiedosto muuttunut. Jos ei ole, sitä ei indeksoida uudelleen.

Sama periaate kuin arjen ylläpidossa: toistuvassa tilanteessa riittävän hyvä ratkaisu, joka ajetaan säännöllisesti, tuottaa enemmän kuin loputon optimointi, jota ei koskaan saada valmiiksi.

## Mistä tämä voi kaatua

Rehellisesti:

- Jos Qdrant-kontti kuolee eikä volumea ole erikseen säilötty, indeksi on mennyttä. Uudelleenindeksointi on mahdollinen, mutta hidas.
- Lokaali malli ei yllä pilven parhaiden mallien tasolle vaikeimmassa päättelyssä. Käytännössä ero näkyy harvoin, koska useimmat kyselyt ovat hakua ja koostamista, eivät syvää päättelyä.
- Testien ajo vaatii yhä käsityötä. Agentti ei saa ajaa shell-komentoja ilman lupaa, enkä aio antaa sitä lupaa.

Nämä eivät ole vikoja vaan valittuja kompromisseja: yksityisyys pilven kustannuksella, riittävä laatu äärimmäisen sijaan, hitaus hallinnan hintana.

Kompromissi, jota ei ole valittu, on vika. Kompromissi, joka on valittu, on suunnittelupäätös.

## Miksi tämä on enemmän kuin tekninen projekti

Järjestelmä on jatke samalle periaatteelle, josta olen kirjoittanut muissakin yhteyksissä: vähemmän kohinaa, enemmän rakennetta.

Kun data on omassa hallinnassa, kun haku toimii merkityksellä eikä sanahaulla ja kun koodi ymmärretään rakenteena, työkalu lakkaa olemasta este. Siitä tulee ajattelun jatke.

Se on myös eräänlainen julkinen työpöytä — järjestetty, löydettävä, käytettävä ilman ulkoista riippuvuutta.

Ei pilveä. Ei tilausmaksua. Ei datan luovutusta.

Vain kone, jossa asiat ovat siellä missä niiden kuuluukin olla.
