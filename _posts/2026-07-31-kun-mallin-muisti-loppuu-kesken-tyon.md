---
title: "Kun mallin muisti loppuu kesken työn"
description: "Pitkässä agenttitehtävässä keskustelukonteksti ei ole luotettava projektimuisti. Lokaali malli tarvitsee ympärilleen prosessin, joka säilyttää tavoitteet, tarkistaa työn ja auttaa viemään tehtävän loppuun."
date: 2026-07-31 06:00:00 +0300
categories: [tekoäly]
lang: fi
translation_key: 2026-07-31-kun-mallin-muisti-loppuu-kesken-tyon
---

Olen viime aikoina ajanut paikallisia kielimalleja Hermes-agentin ohjelmointivaljaissa. Tavoitteena ei ole ollut tieteellinen mallivertailu vaan käytännön kokeilu: löytää yhdistelmiä, jotka osaavat käyttää työkaluja, noudattaa ohjeita ja rakentaa kokonaisen toimivan sovelluksen alusta loppuun.

Yksi havainto on toistunut riittävän monta kertaa, että uskallan kirjoittaa sen ylös.

Pitkässä tehtävässä keskustelu ei ole luotettava projektimuisti. Ja koska se ei ole, mallin ympärille on rakennettava jotain, joka on.

## Konteksti ei ole sama asia kuin muisti

Kielimallilla on käytettävissään rajallinen konteksti. Kun keskustelu, työkalutulokset, lähdekoodi ja virheilmoitukset täyttävät sen, vanhaa sisältöä joudutaan poistamaan tai tiivistämään.

Tiivistäminen kuulostaa harmittomalta huoltotoimelta, mutta se on häviöllinen prosessi — ja se, mitä siinä häviää, on usein juuri se osa, jota tehtävän loppuunsaattaminen vaatii.

Tiivistyksessä säilyvät yleensä suuret linjat: mitä ollaan rakentamassa, millä tekniikalla, mitkä moduulit ovat olemassa ja missä vaiheessa työ suunnilleen etenee.

Sen sijaan pienet mutta sitovat yksityiskohdat heikkenevät ensimmäisinä:

- käyttäjän täsmälliset vaatimukset
- tehdyt rajaukset
- aiemmin korjatut väärinkäsitykset
- teknisten päätösten perustelut
- avoimet virheet
- tieto siitä, mitä todella testattiin
- hyväksymiskriteerit, joiden perusteella työ voidaan sanoa valmiiksi

Ongelman salakavaluus on siinä, että malli jatkaa työskentelyä aivan vakuuttavasti, vaikka sen käsitys alkuperäisestä tehtävästä olisi jo hiljaa muuttunut.

Se ei koe unohtaneensa mitään. Sillä ei ole mekanismia huomata muistin rappeutumista, koska sille rappeutunut versio on nyt koko totuus tehtävästä.

## Keskustelun ulkopuolinen muisti

Ratkaisu on periaatteessa yksinkertainen: tärkeää tehtävää ei säilytetä pelkässä keskustelussa.

Olen päätynyt neljään projektitiedostoon, joilla on tietoisesti eri rooli ja eri elinkaari.

**`TASK.md`** on tehtävän muuttumaton totuuslähde. Se sisältää tavoitteen, pakolliset vaatimukset, rajaukset, hyväksymiskriteerit, käyttäjän nimenomaiset ohjeet ja työn alussa tehdyt oletukset.

**`PLAN.md`** on toteutussuunnitelma: moduulit ja niiden vastuut, toteutusjärjestys, riippuvuudet, tekniset päätökset, testausmenetelmät ja moduulien tilanne.

**`FINDINGS.md`** sisältää tutkimuksen: dokumentaatiosta ja nettihauista löytyneet asiat, kokeelliset havainnot, lähteet, hylätyt vaihtoehdot ja teknisten päätösten perustelut.

**`STATUS.md`** on työn todellinen nykytila: valmistuneet osat, ajetut testit ja niiden tulokset, avoimet virheet, tunnetut puutteet ja seuraava konkreettinen työvaihe.

Kun konteksti tiivistyy, mallin ei tarvitse päätellä tilannetta hataran keskusteluyhteenvedon perusteella. Se lukee tiedostot uudelleen ja jatkaa niistä.

Tärkein yksityiskohta ei kuitenkaan ole tiedostojen olemassaolo vaan se, että `TASK.md` on suojattu.

Mallin ei saa antaa kirjoittaa sitä jatkuvasti uudelleen. Syy on sama, joka aiheutti koko ongelman: jos malli päivittää totuuslähdettä nykyisen — jo osittain rapautuneen — käsityksensä pohjalta, se ei korjaa muistia vaan siirtää vääristymän tiedostoon.

Ulkoinen muisti auttaa vain, jos se on suojassa samalta häviölliseltä prosessilta, joka söi kontekstin.

Käytännössä tämä tarkoittaa selkeää jakoa:

- `TASK.md` kertoo, mitä ja miksi tehdään
- `PLAN.md` kertoo, miten työ on tarkoitus toteuttaa
- `FINDINGS.md` kertoo, mihin tietoihin ja havaintoihin päätökset perustuvat
- `STATUS.md` kertoo, missä todella mennään

Muuttuva työtila ei saa ylikirjoittaa alkuperäistä tehtävää.

Rakentamassani Hermes-skillissä `TASK.md` voidaan lisäksi lukita SHA-256-tarkisteella. Jos tiedosto muuttuu myöhemmin huomaamatta, agentti pystyy havaitsemaan ristiriidan ennen työn jatkamista.

## Moduuli kerrallaan valmiiksi

Toinen toistuva havainto liittyy työn laajuuteen.

Kielimalli yrittää helposti rakentaa koko järjestelmän yhdellä kertaa. Se luo kansiot, tiedostot, käyttöliittymän, tietomallit ja suuren joukon toimintoja. Lopputulos näyttää vaikuttavalta, mutta suuri osa jää puolivalmiiksi.

Parempi periaate on karsivampi:

> Toteuta yksi moduuli kerrallaan huolellisesti valmiiksi asti. Jätä mieluummin osa moduuleista kokonaan tekemättä kuin tee kaikki keskeneräisesti.

Jokaisen moduulin jälkeen agentin pitäisi:

1. lukea alkuperäinen tehtävänanto
2. tarkistaa moduuli vaatimuksia vasten
3. ajaa moduulin omat testit
4. ajaa tarvittavat regressiotestit
5. varmistaa, ettei aiempi toiminnallisuus rikkoutunut
6. tarkistaa näkyvä lopputulos tarvittaessa vision avulla
7. korjata havaitut puutteet
8. päivittää suunnitelma ja työn tila
9. siirtyä vasta sitten seuraavaan moduuliin

Näkyvä eteneminen hidastuu hieman, mutta myöhempi korjaustyö vähenee selvästi. Kokonaisuutena tämä on lähes aina nopeampi tie valmiiseen.

## Mallin täytyy myös osata jatkaa

Hyvät valjaat eivät yksin riitä.

Agenttikäyttö vaatii mallilta ominaisuuksia, joita tavallinen keskustelutesti ei paljasta:

- se ei saa lopettaa ensimmäiseen virheeseen
- sen pitää noudattaa annettuja ohjeita
- sen pitää käyttää työkaluja oikeassa järjestyksessä
- sen pitää lukea virheilmoitus ennen korjaamista
- sen pitää tarkistaa lopputulos
- sen pitää tietää, milloin tehtävä on oikeasti valmis

Olen käyttänyt esimerkiksi KAT-Coderia, joka on toiminut Hermesissä hyvin. Se noudattaa ohjeita ja etenee järjestelmällisesti.

Sen merkittävä puute on vision puuttuminen.

Ilman näkökykyä malli voi todeta, että käyttöliittymän elementti löytyy DOM-rakenteesta ja testi läpäisee. Se ei kuitenkaan näe, että elementit ovat päällekkäin, teksti ei erotu taustasta tai peli näyttää keskeneräiseltä.

Tässä toistuu tuttu ansa: malli verifioi työnsä välikappaletta vasten — DOM-rakennetta tai testitulosta — sen sijaan, että se tarkistaisi käyttäjän todellisuudessa näkemän lopputuloksen.

Kun mittarista tulee tavoite, se lakkaa mittaamasta oikeaa asiaa.

Multimodaalinen malli sulkee tämän silmukan ainakin periaatteessa, koska se voi tarkistaa oman jälkensä samasta kuvasta, jonka käyttäjäkin näkee.

**Arvio:** nykyiset lokaalit vision-mallit ovat vielä epävarmoja hienojakoisen asettelun arvioinnissa, joten kyse on suunnasta eikä ratkaistusta ongelmasta.

Silti juuri tämä vaatimus — että sama malli hoitaa yhdellä 32 Gt:n näytönohjaimella suunnittelun, ohjelmoinnin, työkalut, testaamisen, virheenkorjauksen ja kuvakaappausten tarkastamisen — rajaa mallivalikoimaa paljon enemmän kuin yksikään yksittäinen ohjelmointibenchmark.

## Nettihaku parantaa suunnittelua

Yksi selvästi tuloksia parantanut muutos oli hakukyvyn lisääminen valjaisiin — ja ennen kaikkea mallin ohjaaminen käyttämään hakua jo suunnitteluvaiheessa, ei vasta virheen jälkeen.

Silloin mallin ei tarvitse keksiä kaikkea muististaan. Se voi tarkistaa:

- ajantasaisen dokumentaation
- kirjastojen nykyiset rajapinnat
- tunnetut ongelmat
- vakiintuneet toteutusmallit
- oikeat asetukset
- olemassa olevat ratkaisut

Suunnitteluvaiheen virhe on kallis. Myöhemmin löytyvä syntaksivirhe on yleensä halpa.

Haku siirtää painopistettä oikeaan suuntaan.

Se ei silti ole ilmainen. Haulla on oma vinoumansa: ensimmäinen hakutulos ei ole sama asia kuin oikea arkkitehtuuri, ja heikko malli voi ankkuroitua suosittuun mutta huonoon ratkaisuun yhtä varmasti kuin se aiemmin ankkuroitui omaan arvaukseensa.

Haku vähentää vanhentuneen tiedon varaan rakentamista, mutta ei poista tarvetta arvioida löydettyä tietoa.

Myös löydökset on kirjattava pysyvään muistiin. Muuten dokumentaation lukemiseen käytetty aika valuu hukkaan seuraavassa kontekstin tiivistyksessä.

Rakentamassani prosessissa agenttia muistutetaan kirjaamaan tärkeät havainnot `FINDINGS.md`-tiedostoon jo tutkimuksen aikana, ei vasta työn lopussa.

## Paikallinen ei tarkoita automaattisesti halvempaa

Kokeilin vertailun vuoksi OpenAI:n edullista Luna-mallia Hermesissä.

Annoin sille tehtäväksi rakentaa shakkipelin. Se teki täysin toimivan pelin, jonka vastustaja pelasi suunnilleen lukiolaisen tasolla. Hienosäätöä tarvittiin lähinnä väreihin.

Ajo käytti noin kolme prosenttia 20 euron viikkokiintiöstä. Yhden toimivan shakkipelin hinnaksi tuli siis noin 0,60 euroa.

Tämä on tärkeä vertailupiste.

Paikallista mallia ei voi perustella pelkästään sillä, että kaupallinen malli maksaa. Jos kaupallinen malli tuottaa valmiin sovelluksen alle eurolla, tokenkustannus ei ole varsinainen ongelma.

Rehellinen kokonaislasku näyttää lisäksi, ettei lokaalikaan ole ilmainen. Sen todellinen hinta ei ole tokeneissa vaan laitteiston poistoissa, sähkössä ja ennen kaikkea siinä ajassa, jonka itse käytän valjaiden rakentamiseen ja virheiden jäljittämiseen.

Harrastajalle tuo aika on koko pointti eikä kustannus. Tuotannossa se olisi hallitseva erä.

Paikallisen mallin todelliset edut ovat siksi muualla:

- riippumattomuus palveluntarjoajasta
- tietosuoja
- rajaton kokeilu
- mahdollisuus muokata koko valjasta
- omat muistit ja työkalut
- ennakoitava käyttö
- mahdollisuus tutkia mallien käyttäytymistä ilman tokenmittaria

Kaupallinen malli toimii samalla hyödyllisenä vertailutasona. Ilman sitä on vaikea tietää, kuinka paljon paremmasta mallista oikeasti maksetaan.

## Valjaat auttavat kaikkia malleja

Hyvä agenttivaljas kaventaa paikallisen ja kaupallisen mallin väliä.

Se tarjoaa mallille:

- pysyvän projektimuistin
- hakutyökalut
- selaimen
- terminaalin
- automaattiset testit
- kuvakaappaukset
- työn vaiheistamisen
- pakolliset tarkistuspisteet
- selkeän valmistumiskriteerin

Heikompi malli hyötyy näistä suhteellisesti enemmän, koska valjaat keventävät sen muistikuormaa ja pakottavat järjestelmälliseen työskentelyyn.

Samat työkalut auttavat kuitenkin myös vahvaa kaupallista mallia. Se vain käyttää niitä yleensä tehokkaammin ja tarvitsee vähemmän korjauskierroksia.

Valjaat eivät siis poista mallien välisiä eroja. Ne nostavat koko järjestelmän tasoa.

## Ajatus ei ollut uusi

Kun olin hahmotellut oman tiedostopohjaisen prosessini, aloin etsiä, oliko joku muu jo päätynyt samaan ratkaisuun.

Oli.

Löysin `planning-with-files`-skillin, joka käyttää pitkässä agenttityössä erillisiä suunnittelu-, löydös- ja etenemistiedostoja. Siinä oli myös Hermes-adapteri, joka pystyy palauttamaan projektin tilaa mallin kontekstiin.

Tämä oli samaan aikaan hieman nolostuttavaa ja rohkaisevaa.

Nolostuttavaa siksi, että olin käyttänyt aikaa jo ratkaistun ongelman löytämiseen.

Rohkaisevaa siksi, että käytännön kokeilu oli johtanut itsenäisesti lähes samaan arkkitehtuuriin.

Valmis ratkaisu ei kuitenkaan ollut aivan sama kuin se, mitä itse tarvitsin. Yhdistin siksi sen periaatteet omaan prosessiini ja rakensin Hermesille uuden skillin.

Siinä on:

- muuttumaton ja tarkisteella suojattu `TASK.md`
- erillinen `PLAN.md`
- tutkimuksen säilyttävä `FINDINGS.md`
- todellista tilaa ylläpitävä `STATUS.md`
- kontekstin automaattinen palauttaminen
- moduulikohtaiset testausportit
- vision-tarkistus näkyville lopputuloksille
- virheistä palautumisen kolmen yrityksen prosessi
- valmistumisportti, joka tarkistaa vaatimukset ennen kuin tehtävä voidaan ilmoittaa valmiiksi

Tämäkin prosessi voi epäonnistua, jos malli ei noudata sitä. Valjaat eivät voi pakottaa heikkoa mallia ajattelemaan oikein.

Ne voivat kuitenkin tehdä oikeasta toimintatavasta helpomman ja väärästä vaikeamman.

Se on usein riittävä parannus.

## Mallikortti ei kerro käyttömukavuudesta

Osa lupaavista malleista on osoittautunut käytännössä hyviksi, osa pettymyksiksi mittaustuloksista huolimatta.

Laguna S 2.1 on tähän mennessä ollut heikko kokemus:

- ohjeiden noudattaminen on ollut epävarmaa
- agenttityöskentely on harhaillut
- tulokset ovat vaihdelleet
- suomen kieli on ollut heikkoa

Yhteisössä uskotaan, että mallin pahimmat tekniset ongelmat voidaan korjata nopeasti, ja se voi hyvin pitää paikkansa.

Suomen kielen heikkous on kuitenkin eri asia.

Jos tehtävänannot, muistit ja raportointi ovat suomeksi, kielitaito vaikuttaa suoraan siihen:

- ymmärtääkö malli vivahteet
- säilyttääkö se rajaukset
- tulkitseeko se ohjeet oikein
- onko sen kanssa miellyttävä työskennellä

**Arvio:** tämä ei ole sattumaa. Suomi on kielimalleille niukkaresurssinen kieli, ja ohjeiden noudattaminen voi heikentyä niukkaresurssisilla kielillä silloinkin, kun malli on vahva englanniksi.

Koodausmalli on myös käyttöliittymä.

Jos sen kanssa joutuu jatkuvasti vaihtamaan kieltä tai korjaamaan väärinymmärryksiä, käyttömukavuus laskee nopeasti — eikä tätä yksikään mallikortti mittaa.

## Nopeus ei ole ainoa mittari

Yhdellä 32 Gt:n kortilla saan tällä hetkellä noin 170 000 tokenin kontekstin ja noin 55 tokenia sekunnissa.

Nopeus ei ole ihanteellinen, mutta se ei ole varsinainen ongelma. Paljon tärkeämpää on se, mitä malli tekee ajan kanssa.

Nopeakin malli voi olla käytännössä hidas, jos se:

- harhautuu
- unohtaa vaatimuksia
- keskeyttää työn
- korjaa väärää asiaa
- joutuu tekemään saman työn uudelleen

Luotettava agentti 55 tokenilla sekunnissa voi valmistua ennen tällaista mallia.

Tarkkuuden vuoksi: kyse ei ole siitä, etteikö nopeus merkitsisi. Kun luotettavuus pidetään vakiona, suurempi läpäisy on aina parempi.

Olennaista on, että kun nopeus ja luotettavuus joutuvat vastakkain, luotettavuus ratkaisee kokonaisajan valmiiseen.

Paikallisissa malleissa valinta ei useinkaan ole huippunopean ja yhtä luotettavan mallin välillä. Useammin tarjolla on hidas mutta järjestelmällinen tai nopea mutta harhaileva.

Silloin valinta on helppo.

## Malli ei ole koko järjestelmä

Paikallisia kielimalleja verrataan usein kuin ne olisivat itsenäisiä tuotteita.

Agenttikäytössä tulos syntyy kuitenkin kokonaisuudesta:

- mallista
- kvantisoinnista
- kontekstista
- muistista
- työkaluista
- hakukyvystä
- työskentelyprosessista
- testauksesta
- vision käytöstä
- valjaiden kyvystä palautua virheistä

Tästä seuraa kiusallinen tosiasia benchmarkeille: ne mittaavat mallia yksin, mutta agenttitulos on mallin ja valjaiden yhteinen ominaisuus, jolle ei ole vakiintunutta mittaria.

Hyvä malli huonoissa valjaissa voi epäonnistua.

Hieman heikompi malli hyvissä valjaissa voi yllättää.

Siksi kiinnostavin löytö ei välttämättä ole paras yksittäinen malli. Se voi olla toimintatapa, jonka avulla useat eri mallit tekevät parempaa työtä.

Ja pitkissä tehtävissä tärkein näistä toimintatavoista saattaa olla kaikkein yksinkertaisin:

Älä luota siihen, että malli muistaa.

Kirjoita tärkeät asiat tiedostoon.

Ja varmista, ettei se kirjoita alkuperäistä tehtävää uudelleen.
