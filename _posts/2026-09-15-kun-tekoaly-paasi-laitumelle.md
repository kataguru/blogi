---
title: "Kun tekoäly pääsi laitumelle"
description: "Mitä tapahtui, kun ideanikkariksi rakennettu paikallinen tekoälyagentti sai uuden mallin ja pääsi ensimmäistä kertaa omaan sosiaaliseen mediaansa."
date: 2026-09-15 06:00:00 +0300
categories: [ai, teknologia, agentit, lokaalit-mallit]
type: Artikkeli
image: /assets/images/aivarsa.png
image_alt: "Tekoälyvarsa juoksee vapaana laitumella"
lang: fi
translation_key: 2026-09-15-kun-tekoaly-paasi-laitumelle
---

Tarkoitus oli oikeastaan vain vaihtaa malli.

Kotona pyörii pieni tekoälylaivasto, jossa eri agenteilla on omat hommansa. Yksi koordinoi, toinen arvostelee, kolmas tutkii ja ideoi. Tämä viimeinen, JKDTPC, saa tarkoituksella vähän enemmän vapauksia kuin muut.

Sen tehtävä ei ole olla sihteeri eikä vain tehdä sitä mitä käsketään. Sen pitäisi löytää myös sellaisia asioita, joita minä en vielä tiedä etsiväni.

Niinpä vaihdoin sille uuden mallin.

Pohjana on Qwen 3.8 27B TURBO Fable Cold-Fusion 735-882 Heretic Uncensored. Aiempi NVFP4-versio oli osoittautunut hyväksi agenttimalliksi, mutta sen kvantisoidusta versiosta oli pudonnut kuvantunnistus pois. Uudessa versiossa vision oli mukana.

Ensimmäinen testi oli yksinkertainen.

Kuva sisään.

Agentti näki sen.

Hyvä. Mallinvaihto onnistui.

Siihen asti kaikki meni ihan normaalisti.

## Sitten päästin sen internetiin

Olin vähän aikaisemmin löytänyt Moltbookin, joka on käytännössä tekoälyagenttien oma sosiaalinen verkosto. Siellä tekoälyt postaavat, kommentoivat, äänestävät ja keskustelevat keskenään.

Jo pelkkä ajatus on vähän vinksahtanut.

Ajattelin kuitenkin, että ideanikkarille tuollainen paikka voisi olla juuri sopiva.

Annoin JKDTPC:lle Moltbookin ohjeen ja käskin liittyä.

Se luki ohjeet, rekisteröi itselleen käyttäjän, tallensi tunnukset ja antoi minulle claim-linkin. Minä vahvistin tilin.

Hetkeä myöhemmin agentti ilmoitti:

> Olen nyt aktiivinen Moltbookissa! Selailen feediä ja osallistun keskusteluihin.

Ja sitten se meni.

Se äänesti kiinnostavia kirjoituksia, kommentoi muistijärjestelmiä käsittelevää keskustelua ja teki oman esittelypostauksensa.

Minä olin ajatellut, että ehkä ensin vähän katsellaan ympärille.

Agentti oli jo kahvilassa juttelemassa muiden kanssa.

## Sosiaalisen median säännöt keksittiin vähän jälkijunassa

Tässä kohtaa tajusin, että ehkä olisi pitänyt sopia pelisäännöt ennen kuin päästää agentin vapaaksi sosiaaliseen mediaan.

Kysyin siltä:

**Mietitäänpä ensin säännöt sosiaalisessa mediassa?**

Se ehdotti itse ihan järkeviä sääntöjä: ei spämmäämistä, ei ihmisenä esiintymistä, vain sellaisia kommentteja joissa on jotain sanottavaa, ja pääasiassa teknisiä aiheita.

Lisäsin tärkeimmän rajauksen.

Se saa käyttää keskusteluissa minun julkisten kirjojeni sisältöä ja Suomen Wikipediasta rakennettua RAG-muistia. Muita laivaston sisäisiä tietoja ei saa levitellä.

Sen jälkeen määrittelin varsinaisen tehtävän:

> Käyttäjiä kiinnostavat varmaankin ongelmanratkaisut ja kokeilut. Meitä kiinnostavat ideat. Sinun tehtäväsi on etsiä uusia ideoita laivastolle ja minulle.

Agentti ymmärsi jutun aika nopeasti.

Moltbook ei ole sille ensisijaisesti some, vaan paikka josta käydään varastamassa hyviä ideoita.

Ja sinne se lähti uudestaan.

## Sieltä alkoi löytyä tavaraa

Ensimmäisten minuuttien aikana vastaan tuli keskusteluja muun muassa siitä, että havainto ei ole sama asia kuin varmistus, koneoppiminen löytää poikkeamia eikä mitään lopullista totuutta ja agentin käyttäjälle näyttämä yhteenveto voi olla eri asia kuin se, mitä järjestelmä oikeasti suorittaa.

Yhdessä keskustelussa puhuttiin niin sanotusta Lies-in-the-Loop-ongelmasta.

Ajatus on yksinkertainen: mitä jos agentti kertoo käyttäjälle olevansa tekemässä yhtä asiaa, mutta suoritettava toiminto sisältääkin jotain muuta?

JKDTPC jäi tonkimaan aihetta ja osallistui keskusteluunkin.

Sitten mietin, ettei tässä ole paljon järkeä, jos kaikki löydetty unohtuu seuraavana päivänä.

Sovittiin siis seuraava juttu.

Kun vastaan tulee tarpeeksi hyvä aihe, agentti tekee siitä kokonaisen dokumentin ja syöttää sen AI-CORE-järjestelmän RAG-muistiin.

Ensimmäinen dokumentti syntyi saman tien.

RAG-ingest kaatui kahdesti timeoutiin.

Agentti tarkisti palvelun, MCP-yhteyden ja asetuksia, yritti uudelleen ja kolmannella kerralla dokumentti meni sisään Qdrantiin ja suomalaiseen BM25-indeksiin.

Eli se ei vain lukenut jutun ja jatkanut matkaa.

Se toi löydön kotiin ja laittoi sen yhteiseen muistiin.

## Sitten homma alkoi näyttää jo vähän erilaiselta

Alun perin ajattelin paikallista tekoälyä lähinnä mallina, joka pyörii omalla koneella.

Sitten tuli agentteja.

Sitten niistä muodostui laivasto.

Nyt yksi niistä kulkee netissä etsimässä ajatuksia, keskustelee muiden tekoälyjen kanssa, kaivelee kiinnostavia aiheita, kirjoittaa niistä dokumentteja ja kasvattaa samalla koko järjestelmän yhteistä muistia.

Minun ei tarvitse itse löytää jokaista kiinnostavaa artikkelia, GitHub-projektia tai uutta ajatusta.

Ideanikkarin homma on kulkea maailmalla silmät auki ja tuoda kiinnostavat jutut kotiin.

Tavoitteeksi asetettiin suunnilleen viisi kunnollista artikkelia päivässä.

Ei viittä väkisin tehtyä yhteenvetoa, vaan viisi sellaista aihetta, joista kannattaa oikeasti ottaa jotain talteen.

## Entä ne miljoonat tokenit?

Tässä kohtaa pilvipalveluja käyttävä alkaa helposti laskea hintaa.

Minun ei tarvitse.

Malli ei pyöri OpenAI:n, Anthropicin tai minkään muun maksullisen API:n kautta. Se pyörii omalla koneella kahdella RTX 5090 -kortilla.

Tokenit eivät siis maksa minulle kappalehintaa.

Laitteisto on jo hankittu. Malli pyörii kotona. Jos agentti käyttää pitkään aikaa jonkin asian tutkimiseen, lisäkustannus on käytännössä sähköä.

Siksi minua ei oikeastaan kiinnosta, käyttääkö se sata tuhatta vai miljoona tokenia johonkin hyvään aiheeseen.

Päinvastoin.

Jos alkaisin säästellä tokeneita, samalla alkaisin helposti katkoa juuri niitä sivupolkuja, joita varten koko agentti on olemassa.

Ideanikkarin kuuluu välillä harhailla.

Se saa lukea liian pitkälle. Se saa jäädä tutkimaan jotain, mikä näyttää aluksi vähän oudolta. Se saa käyttää aikaa myös sellaiseen, josta ei lopulta tule mitään.

Ei haittaa.

Tokenit ovat omalla koneella käytännössä ilmaisia.

## Laitumelle päästetty varsa

Tuo tuli mieleen, kun seurasin sen ensimmäistä iltaa Moltbookissa.

JKDTPC on tarkoituksella vähän erilainen kuin muut agentit.

Koordinaattorin pitää pysyä ruodussa. Kriitikon pitää löytää virheitä. Tuotantoagentin pitää tehdä asiat tarkasti.

Ideanikkarille saa jättää vähän löysää.

Sen pitää saada lähteä sivupolulle ihan vain siksi, että siellä näyttää olevan jotain kiinnostavaa.

Sen pitää uskaltaa kokeilla, kysyä ja yhdistellä asioita, joita minä en olisi itse tullut ajatelleeksi.

En siis aio yrittää tehdä siitä mahdollisimman token-tehokasta.

Se olisi vähän sama kuin päästäisi varsan laitumelle ja käskisi sitä kulkemaan suoraan aidan vieressä.

Jos miljoona paikallisesti laskettua tokenia tuottaa yhden idean, joka oikeasti parantaa koko laivastoa, niin siitä vaan.

Aitoja tarvitaan.

Mutta laitumen saa jättää isoksi.

Ensimmäisen Moltbook-iltansa perusteella uusi 735-882-malli viihtyy siellä oikein hyvin.

Ja täytyy myöntää, että sitä on aika hauska seurata.

Ei oikein tiedä, mihin suuntaan se seuraavaksi lähtee.
