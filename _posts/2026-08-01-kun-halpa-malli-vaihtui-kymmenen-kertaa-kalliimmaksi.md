---
title: "Kun halpa malli vaihtui kymmenen kertaa kalliimmaksi"
description: "80 prosentin hinnanalennuksen piti tehdä Lunasta halpa loppukoodari suureksi kasvaneelle projektille. 85 minuutissa kului 24 dollaria, koska OpenRouter reititti saman mallin taustalla kalliimmalle providerille."
date: 2026-08-01 06:00:00 +0300
categories: [tekoäly]
lang: fi
translation_key: 2026-08-01-kun-halpa-malli-vaihtui-kymmenen-kertaa-kalliimmaksi
image: /assets/images/openrouter-reititin.svg
image_alt: "Kaavio OpenRouter-reitittimestä, joka ohjaa saman Luna-mallin halvalle OpenAI-reitille tai kalliimmalle Azure-reitille."
---

Paikalliset kielimallit olivat palvelleet projektissani pitkään hyvin. Ne suunnittelivat, kirjoittivat koodia, ajoivat testejä ja korjasivat virheitä Hermes-agentin kautta.

Sitten projekti kasvoi niiden ulottumattomiin. Konteksti paisui, tiedostojen välisiä riippuvuuksia tuli lisää ja paikalliset mallit alkoivat jäädä jumiin. Ne ratkaisivat yksittäisen moduulin, mutta eivät enää hallinneet koko järjestelmää luotettavasti.

Juuri siinä vaiheessa silmiini osui mainos: Luna-mallin hintaa oli laskettu 80 prosenttia.

Ajatus oli houkutteleva. Jos Luna olisi riittävän hyvä ja samalla näin halpa, se voisi ottaa haltuun ne viimeiset vaikeat vaiheet, joihin paikalliset mallit eivät enää pystyneet — projektin loppukoodarina.

Vertasin sitä DeepSeek V4 Flashiin. Luna vaikutti käytännön koodaustyössä paremmalta, ja hinnoittelun perusteella kahdeksan tunnin työpäivän piti maksaa vain joitakin euroja.

Näytti siltä, että olin löytänyt halvan ja riittävän älykkään loppukoodarin.

Noin puolentoista tunnin jälkeen OpenRouter-saldoa oli kulunut 24 dollaria.

Ensimmäinen epäilys kohdistui High- ja Max-päättelyasetuksiin: ehkä malli poltti valtavan määrän näkymättömiä reasoning-tokeneita. Activity-raportti osoitti muuta.

## Mitä 85 minuutissa tapahtui?

OpenRouterin CSV-raportissa oli 277 mallikutsua ajalta 04.20–05.45.

| Mittari | Määrä |
|---|---:|
| Mallikutsuja | 277 |
| Prompt-tokeneita | 87,62 miljoonaa |
| Välimuistista luettuja tokeneita | 79,82 miljoonaa |
| Näkyviä tulostetokeneita | 105 063 |
| Reasoning-tokeneita | 34 256 |
| Kokonaiskustannus | 24,08 $ |

Agentti lähetti saman kasvavan projektikontekstin mallille yhä uudelleen. Pääsession konteksti kasvoi noin 148 000 tokenista 483 000 tokeniin.

Tämä oli kallista mutta ei vielä selittänyt koko laskua. Välimuisti osui yli 91 prosenttiin prompt-tokeneista, ja outputia sekä reasoningia syntyi vähän. Reasoning-tokenit — se, mihin ensin epäilin — olivat koko kuvassa marginaalinen erä.

Ratkaiseva tieto löytyi provider-sarakkeesta.

## Sama malli, kaksi eri hintaa

Kaikki kutsut käyttivät samaa mallia:

`openai/gpt-5.6-luna-20260709`

Taustalla palvelun tuotti kuitenkin kaksi eri provideria.

| Provider | Kutsuja | Kustannus |
|---|---:|---:|
| OpenAI | 83 | 0,40 $ |
| Azure | 194 | 23,67 $ |

CSV-riveistä voidaan päätellä myös providerien käyttämät hinnat. OpenAI-reitti laskutti 0,10 dollaria inputista ja 0,60 dollaria outputista miljoonaa tokenia kohti. Azure-reitti laskutti vastaavasti 1 ja 6 dollaria. Azure oli siis samalla mallilla täsmälleen kymmenen kertaa kalliimpi.

Keskimääräinen Azure-kutsu maksoi noin 25 kertaa OpenAI-kutsun verran, koska provider-hinnan lisäksi Azure-kutsut osuivat session myöhempään vaiheeseen, suurempaan kontekstiin ja useammin yli 272 000 tokenin hintaportaaseen.

Varmaa on siis kaksi asiaa yhtä aikaa: providerien välinen hintaero oli kymmenkertainen, ja käytännön lasku kasvoi vielä tätäkin suuremmaksi kontekstin paisumisen takia.

## Miksi provider vaihtui?

OpenRouter ei ole yksi mallipalvelin. Se on reititin, joka välittää saman mallin pyyntöjä eri palveluntarjoajille.

Oletusreititys painottaa hintaa, mutta rajaa ehdokkaita ominaisuustuen perusteella ja sallii fallbackit oletuksena. Työkalukutsut voivat siis sulkea halvimpia reittejä pois, ja hetkellinen saatavuus- tai nopeusrajoitus voi siirtää pyynnön seuraavalle providerille.

Activity-raportti ei kerro, mikä laukaisi ensimmäisen siirtymän OpenAI:lta Azurelle. Syynä saattoi olla esimerkiksi hetkellinen nopeusrajoitus, saatavuusongelma tai työkalupyynnön provider-rajaus.

Siirtymisen jälkeen OpenRouterin dokumentoitu provider sticky routing saattoi pitää keskustelun Azurella välimuistiosumien säilyttämiseksi. Näin tilapäisestä fallbackista tuli käytännössä koko loppusession reitti.

CSV:n kaikki 277 riviä olivat veloitettuja generointeja. Mahdolliset OpenRouterin sisäiset epäonnistuneet provider-yritykset eivät näy raportissa erillisinä veloitettuina kutsuina.

Raportti kertoo seurauksen varmasti: provider vaihtui kesken session, keskimääräinen kutsuhinta moninkertaistui ja agentti jatkoi työskentelyä ilman näkyvää varoitusta.

## Tyhjä asetus ei ollut neutraali

OpenRouterin asetuksissa on kohta **Allowed Providers**. Kenttä oli tyhjä.

Tavalliselle käyttäjälle tyhjä kenttä näyttää siltä, ettei erityistä asetusta ole tehty. Todellinen merkitys on päinvastainen:

> Kaikki yhteensopivat providerit ovat sallittuja.

Allow-lista rajaa reitityksen listattuihin providereihin; tyhjänä se ei rajaa mitään. Vasta kun lisäsin OpenAI:n ainoaksi sallituksi provideriksi, Azure-reitti sulkeutui pois.

Teknisesti järjestelmä toimi dokumentaationsa mukaisesti. Taloudellisen riskin kannalta oletus on silti huono: käyttäjä valitsee mallin ja näkee sille mainostetun hinnan, mutta todellinen lasku määräytyy taustalla valitun providerin mukaan. Jos provider voi maksaa kymmenen kertaa enemmän, sen vaihtumisen ei pitäisi olla hiljainen toteutusyksityiskohta.

## Aloittelijalle tämä on ansa

Kokenut API-käyttäjä osaa ehkä tarkistaa providerit, fallbackit, prompt cache -osumat, pitkän kontekstin hintaportaat ja avainkohtaiset budjettirajat.

Aloittelija valitsee mallin. Hän olettaa ymmärrettävästi, että saman mallin hinta pysyy suunnilleen samana koko session ajan. High- ja Max-asetukset näyttävät selkeiltä kustannusmuuttujilta, joten huomio kohdistuu niihin. Todellinen kymmenkertainen ero voi kuitenkin syntyä täysin eri asetuksesta, jota käyttäjä ei tiedä tarvitsevansa.

En pysty osoittamaan, että rakenne olisi tarkoituksella harhaanjohtava. Pystyn osoittamaan, että se on kustannusten kannalta liian läpinäkymätön. Kahdenkymmenen neljän dollarin oppitunti syntyi alle puolessatoista tunnissa.

## Korjaus

Käyttöliittymässä:

1. avaa provider-asetukset
2. etsi **Allowed Providers**
3. lisää vain **OpenAI**
4. jätä muut providerit pois
5. varmista seuraavasta Activity-raportista, että provider on OpenAI

Mekanismi, joka ei vanhene käyttöliittymämuutosten myötä, on sama asia pyynnön tasolla:

- `only: ["openai"]` — salli vain OpenAI-provider
- `allow_fallbacks: false` — estä siirtymä muille providereille
- `max_price` — estä pyyntö kokonaan, jos hintarajan alittavaa provideria ei löydy

Lisäksi jokaiselle agentin API-avaimelle kannattaa määrittää oma pieni budjettiraja, ja pitkä sessio kannattaa katkaista tai tiivistää ennen kuin konteksti kasvaa satoihin tuhansiin tokeneihin. Tässä ajossa agentti käsitteli 87,6 miljoonaa prompt-tokenia 85 minuutissa; vaikka 91 prosenttia tuli välimuistista, tällaista sessiota ei kannata antaa paisua rajatta.

Provider-lukitus ratkaisee tämän tapauksen suurimman ongelman. Se ei ratkaise kasvavaa kontekstia — se on erillinen kurinalaisuuskysymys.

Jos kustannusten ennustettavuus on tärkeämpää kuin monen providerin vikasietoisuus, selkein vaihtoehto on kutsua mallia suoraan sen oman API:n kautta. OpenRouterin lisäarvo on nimenomaan automaattinen fallback usealle providerille — sama ominaisuus, joka tässä nostatti laskun.

## Millainen oletuksen pitäisi olla?

Turvallisempi palvelu toimisi näin:

- mallin yhteydessä näytettäisiin kaikkien käytettävissä olevien providerien hinnat
- providerin vaihtuessa kalliimpaan käyttäjälle annettaisiin varoitus
- kustannusraja voitaisiin määrittää suoraan mallin valinnan yhteydessä
- fallback kymmenen kertaa kalliimpaan reittiin vaatisi erillisen luvan
- agenttinäkymässä näkyisi reaaliaikainen kustannus, provider ja kontekstin koko

Fallback parantaa toimintavarmuutta. Se ei saa samalla muuttaa käyttäjän taloudellista sitoumusta huomaamatta.

## Mitä tästä jäi käteen?

Ongelma ei ollut Luna Max eikä päättelytokenien määrä. Ongelma oli näkymätön reitityspäätös yhdistettynä suureen agenttikontekstiin.

Halpa malli ei ole halpa, jos välissä oleva reititin saa vaihtaa sen kalliimmalle palveluntarjoajalle ilman, että käyttäjä huomaa sitä. API-agenttia käyttäessä ei siksi riitä, että tarkistaa mallin hinnan. On tarkistettava myös se, **kuka mallin todellisuudessa ajaa**.

## Lähteet

- [OpenRouter: Provider Routing](https://openrouter.ai/docs/guides/routing/provider-selection)
- [OpenRouter: Prompt Caching](https://openrouter.ai/docs/guides/best-practices/prompt-caching)
- [OpenRouter: Guardrails](https://openrouter.ai/docs/guides/features/guardrails/overview)
