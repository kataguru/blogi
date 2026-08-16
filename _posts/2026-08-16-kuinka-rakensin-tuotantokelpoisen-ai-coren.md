---
title: "Kuinka rakensin tuotantokelpoisen AI-coren"
description: "Miten vuoden kokeilu, väärät palat ja toistuvat ratkaisut tiivistyivät vakaaksi paikalliseksi AI-infrastruktuuriksi."
date: 2026-08-16 06:00:00 +0300
categories: [ai, teknologia, lokaalit-mallit, agentit]
type: Artikkeli
image: /assets/images/aicore.JPG
image_alt: "AI-CORE-palvelin"
lang: fi
translation_key: 2026-08-16-kuinka-rakensin-tuotantokelpoisen-ai-coren
---

Vuoden ajan olen rakentanut paikallista tekoäly-ympäristöä tavalla, jota voisi ystävällisesti kutsua kokeilevaksi ja vähän vähemmän ystävällisesti päämäärättömäksi haahuiluksi.

Malleja on vaihdettu. Runtimeja on vaihdettu. Muistijärjestelmiä rakennettu ja purettu. RAG-ratkaisuja kokeiltu. GPU-kortteja lisätty, poistettu ja siirretty. Välillä käytössä on ollut LM Studio, välillä vLLM, välillä Hermes, välillä Kilo Code. Jossain välissä mukana olivat TencentDB, Qdrant, Paperless, SearXNG, BGE-M3, rerankerit ja kokonainen joukko MCP-työkaluja.

Yksittäisinä kokeiluina osa tästä näyttää helposti poukkoilulta.

Sitten huomasin jotain.

Rakensin samoja asioita uudelleen.

## Kun sama ratkaisu syntyy kolmannen kerran

Jokaisen uuden agentin tai mallin yhteydessä tarvitsin taas samat asiat:

- verkkohaku
- RAG
- embeddingit
- reranker
- pitkäkestoinen muisti
- dokumenttien ingest
- turvallinen etäkäyttö
- vakaa LLM-rajapinta

Ensimmäisellä kerralla niiden rakentaminen oli kokeilu.

Toisella kerralla harjoitus.

Kolmannella kerralla ongelma ei enää ollut rakentaminen.

Ongelma oli se, ettei toimivista ratkaisuista ollut tehty pysyviä.

Siitä syntyi AI-CORE.

> AI-coreen ei pääse kiinnostava ratkaisu. Sinne pääsee ratkaisu, jonka rakentamiseen uudelleen olen kyllästynyt.

## Haahuilu ei ollutkaan hukkaan heitettyä aikaa

Olen käyttänyt omasta työskentelytavastani lyhennettä AFRS:

**Adaptive Fit, Recycle, Feedback decides.**

Adaptive Fit on käytännössä sitä, että tungetaan neliön paloja pyöreisiin reikiin ja katsotaan mitä tapahtuu.

Kokeillaan väärää mallia.

Kokeillaan väärää runtimea.

Rakennetaan liian raskas harness.

Todetaan, ettei jokin muistijärjestelmä ymmärrä suomea.

Huomataan, että hieno GPU-palvelin huutaa tyhjäkäynnillä kuin lentokone.

Ajetaan FP8-mallia ja ihmetellään, miksi sen suomen kieli kuulostaa huonommalta kuin paljon aggressiivisemmin kvantisoidun GGUF-version.

Yksittäinen kokeilu voi olla turha.

Kokeilujen populaatio ei ole.

Palaute alkaa vähitellen valita voittajia.

Kun ratkaisu toimii tarpeeksi monta kertaa, se voidaan kierrättää pysyväksi osaksi järjestelmää.

**Adaptive Fit → Feedback → Recycle.**

AI-CORE on tämän prosessin sedimentti.

## Tavoitteena mahdollisimman tylsä kone

Rakensin AI-COREn Threadripper 7960X -alustalle.

Koneessa on kaksi RTX 5090 -korttia ja yksi RTX 5060 Ti.

Aluksi mietin neljää GPU:ta. Luovuin ajatuksesta, koska neljäs kortti lisäsi enemmän lämpöä, sähkönkulutusta ja vikapintaa kuin hyötyä.

Periaatteeksi tuli yksinkertainen:

> Laboratoriokoneilla saa tapahtua mitä tahansa. AI-COREn pitää vain toimia.

Koneeseen asennettiin puhdas Ubuntu 26.04 LTS Desktop.

Desktop ei ole tässä kompromissi. Sen puute olisi.

Graafinen ympäristö kuluttaa mitättömän määrän resursseja verrattuna koneen kapasiteettiin, mutta helpottaa asennusta, diagnostiikkaa ja ylläpitoa huomattavasti. Linuxille julkaistu ChatGPT Desktop tuli vielä sopivasti juuri projektin aikana ja toimi asennusapuna.

Varsinaiset palvelut eivät kuitenkaan riipu Desktopista tai käyttäjän kirjautumisesta.

Koneen pitää bootata ja palauttaa palvelut ilman että kukaan koskee hiireen.

## Ensimmäinen ongelma tuli ennen ensimmäistä palvelua

Ubuntu ei aluksi käynnistynyt kunnolla.

Näytölle jäi vain Ubuntu-teksti ja musta ruutu.

Secure Boot oli jo pois päältä, mutta TRX50-, PCIe- ja GPU-asetuksia piti vielä tarkistaa.

Se oli hyvä muistutus projektin perusperiaatteesta:

Jos pohja ei ole vakaa, Docker ei pelasta sitä.

Ensin rauta ja käyttöjärjestelmä vakaaksi. Vasta sen jälkeen AI.

## LLM ei ole enää ohjelma vaan palvelu

Aiemmin paikallinen LLM oli jotain, minkä käynnistin.

Nyt se on jotain, minkä oletan olevan olemassa.

Kilo Code ei tarvitse tietää, missä GPU sijaitsee. Se näkee OpenAI-yhteensopivan API:n.

Sama pätee myöhemmin Atomic Agentiin tai mihin tahansa muuhun clientiin.

Tässä vaiheessa paikallinen malli alkaa muistuttaa enemmän verkkolevyä tai DNS-palvelua kuin harrastusohjelmaa.

Sen pitää vain vastata.

## Malli vaihtuu, infra jää

Tämä periaate osoittautui tärkeäksi lähes heti.

Qwen3.6-27B toimi vLLM:llä hyvin. Kahdella RTX 5090:llä, 128k kontekstilla ja maksimaalisella reasoningilla generaationopeus oli noin 112 tokenia sekunnissa.

Nopeudessa ei ollut mitään valittamista.

Sitten Qwen3.8-27B julkaistiin.

FP8-versio näytti ensin loogiselta vLLM-valinnalta, mutta suomen kieli oli pettymys. Se oli teknisesti nopea ja siisti, mutta kielioppi häiritsi liikaa.

GGUF Unsloth Q4_K_XL UD taas puhui hyvää suomea ja oli nopea.

Sen jälkeen testiin tuli GPTQ.

Yllättäen se osoittautui selvästi parhaaksi kvantiksi.

Tämä oli jälleen hyvä muistutus siitä, ettei bittimäärä, runtime tai teoreettinen eleganssi ratkaise mallin käytännön laatua.

Testi ratkaisee.

AI-COREa ei kuitenkaan tarvinnut rakentaa uudelleen.

Vain päämalli vaihtui.

Juuri sitä varten infrastruktuuri oli tehty.

## RAG ei ole yksi vektoritietokanta

RAG-ratkaisu rakentui vähitellen kolmesta osasta:

- BGE-M3 dense retrieval
- suomenkielinen BM25
- reranker

Tulokset yhdistetään ennen lopullista rerankkausta.

Tämä oli tietoinen ratkaisu. Suomen kielessä pelkkä semanttinen haku tai geneerinen lexical-haku ei aina riitä.

Qdrant toimii vektorivarastona, mutta sitä ei julkaista suoraan agenteille.

Sen edessä on RAG Gateway.

Agentti kysyy tietoa yhdestä rajapinnasta. Se ei tiedä, miten retrieval on toteutettu.

Jos embedding-malli tai tietokanta vaihtuu myöhemmin, agenttia ei tarvitse muuttaa.

## Muistista tuli oma palvelunsa

Sama ajatus vietiin pitkäkestoiseen muistiin.

Memory API määriteltiin ensin backend-riippumattomaksi sopimukseksi.

Sen jälkeen TencentDB liitettiin adapterin taakse.

Tämä järjestys oli tärkeä.

Jos olisin rakentanut rajapinnan suoraan TencentDB:n ominaisuuksien ympärille, koko järjestelmä olisi lukittunut yhteen toteutukseen.

Nyt asiakkaat näkevät vain toiminnot:

- store
- search
- recall
- forget
- profile/context

Backend voidaan joskus vaihtaa.

Memory API:n contract-testit menevät läpi ja store/search/recall/forget-polku toimii end-to-end.

Muistilouhinnassa törmäsin vielä yhteen paikallisten mallien ongelmaan: suomen ymmärtäminen.

Pienet nopeat mallit olivat houkuttelevia, mutta Gemma osoittautui selvästi parhaaksi suomalaisen tekstin extractionissa.

Tässä nopeus ei ole tärkein asia.

Huonosti louhittu fakta voi saastuttaa muistia pitkään.

Siksi extractionissa laatu voittaa tokenit sekunnissa.

## Verkkohaku omaksi palvelukseen

SearXNG tarjoaa agenteille yhteisen verkkohakupalvelun.

Headless Playwright puolestaan hakee JavaScriptiä tarvitsevat sivut ja palauttaa niistä käsiteltävän sisällön.

Tämän ansiosta jokaisen agentin ei tarvitse rakentaa omaa web-hakuaan.

Sama pätee myöhemmin muihinkin työkaluihin.

## MCP teki palveluista agentin työkaluja

Kun AI-COREssa oli jo RAG, muisti ja verkkohaku, seuraava looginen askel oli tehdä niistä agentille suoraan kutsuttavia MCP-työkaluja.

Ensimmäiseen versioon tuli kahdeksan työkalua:

- dokumenttihaku
- muistin recall
- muistin tallennus
- verkkohaku
- verkkosivun fetch
- tiedoston ingest
- tekstin ingest
- dokumentin poisto

Tässä kohtaa AI-CORE lakkasi olemasta vain LLM-palvelin.

Siitä tuli agentin infrastruktuuri.

LLM tekee päättelyn.

AI-CORE antaa sille muistin, tiedon ja työkalut.

## Etäkäyttö ei ollut lisäominaisuus

Tailscale tuli mukaan hyvin aikaisin.

Ajatus siitä, että mökillä olisin ilman omaa AI-infraani, olisi ollut ideologiani vastainen.

AI-CORE on kotona, mutta sen ei pidä tuntua siltä.

Windows-koneelta testattiin Tailscalen kautta Memory API.

Vastaus tuli HTTP 200:na ja kaikki palvelun health-kentät olivat `ok`.

Sama verkko kuljettaa myös LLM-API:n Kilo Codelle.

Kone voi siis jäädä kotiin. Sen laskentateho ei jää.

## Turvallisuus tarkoittaa myös sitä, mitä jätetään julkaisematta

AI-COREssa sisäiset palvelut kuuntelevat lähtökohtaisesti localhostia tai Docker-verkon sisällä.

Ulkopuolelle julkaistaan vain tarkoitukselliset rajapinnat.

Tailscale Serve antaa tarvittaessa HTTPS-reitin tailnetin sisällä.

Funnelia ei käytetä.

Tietokantoja ei avata verkkoon vain siksi, että se olisi helppoa.

Samoin MCP-työkalujen kohdalla kaikki eivät saa automaattista kirjoitus- tai poisto-oikeutta.

AI-agentille annettu työkalu on samalla oikeus.

## Monitoring ilman monitoring-harrastusta

AI-COREssa pyörivät Prometheus, Node Exporter, NVIDIA DCGM Exporter ja Grafana.

Niiden tehtävä on vastata muutamaan yksinkertaiseen kysymykseen:

- ovatko GPU:t terveitä?
- paljonko VRAMia käytetään?
- kuinka kuuma kone on?
- paljonko tehoa se kuluttaa?
- ovatko palvelut käynnissä?
- loppuuko levytila?

En halunnut rakentaa observability-järjestelmää observabilityn vuoksi.

Sama periaate pätee koko projektiin.

Jokaisella komponentilla pitää olla työ.

## Mitä jätin tietoisesti pois

Tämä lista on ehkä yhtä tärkeä kuin asennettujen ohjelmien lista.

AI-COREen ei tullut:

- Kubernetesia
- ylimääräistä orkestrointikerrosta
- jatkuvasti vaihtuvia kokeilumalleja
- automaattisia container-päivityksiä
- uusia palveluita vain siksi, että GPU:ssa on vapaata muistia

LiteLLM kiinnostaa edelleen.

Se ei vain ratkaise tällä hetkellä ongelmaa, joka minun pitäisi ratkaista.

Siksi sitä ei asenneta.

## Kun infra valmistuu, haahuilu voi jatkua

Tämä on ehkä projektin tärkein lopputulos.

AI-COREn rakentamisen tarkoitus ei ollut lopettaa kokeilemista.

Päinvastoin.

Kun RAG:ia, muistia, verkkohakua ja API-palvelua ei tarvitse rakentaa jokaisen uuden agentin yhteydessä uudelleen, huomio vapautuu seuraavaan tuntemattomaan ongelmaan.

Voin taas testata malleja.

Voin kokeilla computer usea.

Voin tutkia uusia agentteja.

Voin rakentaa jotain typerää vain nähdäkseni mitä tapahtuu.

Ja jos jokin niistä osoittautuu niin hyödylliseksi, että huomaan rakentavani sen kolmannen kerran, tiedän mitä tehdä.

Se siirretään AI-COREen.

## Lopputulos

AI-CORE ei syntynyt tarpeesta rakentaa taas yksi uusi järjestelmä.

Se syntyi tarpeesta lopettaa samojen toimiviksi todettujen asioiden rakentaminen uudelleen.

Vuoden haahuilu ei siis päättynyt.

Se vain tuotti ensimmäisen pysyvän kerroksensa.

> Laboratoriokoneella saa tapahtua mitä tahansa. AI-COREn tehtävä on vain toimia.
