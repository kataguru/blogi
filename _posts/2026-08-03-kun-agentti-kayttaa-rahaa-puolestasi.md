---
title: "Kun agentti käyttää rahaa puolestasi"
description: "API-agentin lasku ei synny vain mallin hinnasta. Tokenmaxing, paisuva konteksti, proxyt, tyhjäkäynti ja puutteellinen valvonta voivat kasvattaa kulutuksen huomaamatta."
date: 2026-08-03 06:00:00 +0300
categories: [tekoäly]
lang: fi
translation_key: 2026-08-03-kun-agentti-kayttaa-rahaa-puolestasi
image: /assets/images/agentti-kayttaa-rahaa.svg
image_alt: "Kannettava tietokone ja siihen liitetty hana, josta valuu eurokolikoita viemäriin kuvaamassa tekoälyagentin näkymätöntä API-kulutusta."
---

Chatbotti vastaa kysymykseen ja jää odottamaan. Agentti ei välttämättä jää.

Kun annan agentille yhden tehtävän, se voi tehdä sen aikana kymmeniä mallikutsuja, lukea samoja tiedostoja uudelleen, käynnistää aliagentteja, tiivistää keskustelua ja vaihtaa mallia. Se saattaa jatkaa puuhiaan myös silloin, kun ruudulla ei minun silmissäni tapahdu mitään.

Yksittäinen token maksaa vain murto-osan sentistä. Se on totta, mutta myös harhaanjohtavaa. Lasku ei synny yhdestä tokenista vaan koko koneistosta: mallista, API-tarjoajasta, proxysta, agenttivaljaista, kontekstista, muistista, työkalukutsuista ja uusintayrityksistä.

Ja tietysti myös siitä, miten itse järjestelmää käytän.

Kutsun tätä ilmiötä **tokenmaxingiksi**: järjestelmä käyttää maksullisia tokeneita enemmän kuin tehtävän ratkaiseminen oikeasti vaatisi.

**Kiistanalainen:** en väitä, että tämä olisi aina tahallista. Tavallisemmin kyse on huonosta suunnittelusta, välinpitämättömyydestä tai siitä, että tarjoajan ja käyttäjän taloudelliset edut eivät ole samat.

Käyttäjän kannalta lopputulos on silti sama. Lasku kasvaa.

Kirjoitin tämän muistilistaksi sen jälkeen, kun olin katsonut liian monta usage-lokia ja ihmetellyt, mihin tokenit oikein katosivat.

## Halpa token ei tarkoita halpaa mallia

Mallien vertailu miljoonan tokenin hinnalla on vähän kuin valitsisi auton pelkän bensalitran hinnan perusteella.

Halpa mutta lörpöttelevä malli voi tuottaa tarpeettoman pitkiä vastauksia, tehdä ylimääräisiä työkalukutsuja, epäonnistua useammin, korjata omaa jälkeään, kasvattaa kontekstia nopeasti ja käyttää paljon minun aikaani.

Kalliimpi mutta täsmällisempi malli voi ratkaista saman tehtävän yhdellä kierroksella ja tulla kokonaisuutena halvemmaksi.

Oikea kysymys ei ole:

> Paljonko miljoona tokenia maksaa?

Vaan:

> Paljonko yksi hyväksytty tehtävä maksaa?

Todellinen kustannus sisältää API-laskun lisäksi oman ajan, korjauskierrokset ja epäonnistuneet yritykset.

Tätä ei näe hinnastosta eikä yksittäisestä benchmarkista. Se selviää vain testaamalla malleja omilla oikeilla tehtävillä.

## Älä naita yhtä mallia

LLM-markkina liikkuu niin nopeasti, ettei yhteen malliin tai tarjoajaan kannata sitoutua pitkäksi aikaa.

Tämän päivän hyvä malli voi muutamassa kuukaudessa olla liian kallis, liian hidas, keskinkertainen, korvattu halvemmalla vaihtoehdolla tai jäänyt paikallisten mallien jalkoihin.

Siksi pidän mallivalinnan löysällä. Vältän pitkiä sitovia sopimuksia, tarkistan tarjontaa ja vaihdan tarvittaessa.

En myöskään rakenna järjestelmää yhden valmistajan erikoisominaisuuksien varaan ilman poistumistietä.

Tilauksen vaihtaminen ei ole uskottomuutta. Se on tavallista hankintaa.

## Proxy voi vaihtaa kalliimpaan huomaamatta

Proxy tai API-reititin helpottaa mallien käyttöä, mutta samalla se lisää uuden päättäjän minun ja mallin väliin.

Automaattinen reititys voi vaihtaa toiseen tarjoajaan, toiseen malliversioon, hitaampaan tai kalliimpaan vaihtoehtoon tai varamalliin, jonka hintaa en ole tarkistanut.

Pahimmillaan luulen käyttäväni halpaa mallia, vaikka proxy on siirtänyt pyynnön kymmenen kertaa kalliimmalle tarjoajalle.

Siksi proxy pitää rajata teknisesti: sallitut mallit, sallitut tarjoajat, enimmäishinta, kiinteä prioriteettijärjestys ja sallittu fallback.

Lokista pitää nähdä jokaisen kutsun pyydetty ja toteutunut malli, tarjoaja, tokenit ja hinta. Pelkkä proxyn ilmoittama mallinimi ei riitä.

## Se joka käyttää tokenit, näkee myös kulutuksen

Kulutuksesta päättävän pitää nähdä kulutuksen seuraukset.

Haluan nähdä ruudulla ainakin tämän tehtävän kustannuksen, päivän ja kuukauden kulutuksen, käytetyn mallin ja tarjoajan, kontekstin koon, työkalu- ja uusintakutsujen määrän sekä jäljellä olevan budjetin.

Jos nämä puuttuvat, lennän mittarit peitettynä.

Organisaatiossa käyttäjälle tai projektille kannattaa antaa kiinteä budjetti. Budjetin ylitys pitää estää teknisesti, ei vain ilmoittaa jälkikäteen sähköpostilla.

Alituksesta voisi jopa maksaa pienen kannustimen. Silloin palkitaan tehokkuudesta, ei komeasta API-laskusta.

## Harness ei ole pyhä pulmunen

Agenttivaljaat eli harness tekevät mallista toimivan agentin. Ne hallitsevat kontekstia, muistia, kompressiota, työkalukutsuja, aliagentteja, mallinvaihtoja ja fallbackeja.

Toisin sanoen lähes kaikkea sitä, mistä kulutus syntyy.

Sama valjas voi myös hyötyä siitä, että tarvitsen suuremman kuukausipaketin tai käytän enemmän API:a. Tämä ei todista väärinkäytöstä, mutta kannustinristiriita on olemassa.

Siksi valjaita pitää mitata eikä vain uskoa.

### Rajaan kontekstin

Se, että mallilla on miljoonan tokenin konteksti, ei tarkoita, että miljoona tokenia kannattaa lähettää sille joka kierroksella.

Pitkä konteksti maksaa enemmän, hidastaa, peittää olennaisen tiedon, kasvattaa kompression tarvetta ja lähettää saman vanhan aineiston uudelleen ja uudelleen.

Konteksti pitää rajata tehtävän kannalta järkevälle alueelle, ei mallin teoreettiseen maksimiin.

### Pidän projektimuistin paikallisesti

Arkkitehtuuripäätökset, tehtävän tila, testitulokset, löydetyt virheet ja seuraavat vaiheet eivät kuulu pelkkään keskusteluhistoriaan.

Ne kannattaa tallentaa projektin omiin tiedostoihin. Mallille lähetetään vain se osa, jota se tarvitsee juuri nyt.

Pitkä keskusteluhistoria ei ole hyvä muistijärjestelmä. Se on kallis lokitiedosto, joka luetaan uudelleen jokaisella kierroksella.

### Ohjaan sivutehtävät paikalliselle mallille

Kompressio, tiivistäminen, lokien esikäsittely, tiedostojen luokittelu, dokumentoinnin päivitys ja hakutulosten karsinta eivät tarvitse pilven kalleinta mallia.

Ne voidaan tehdä paikallisesti. API-malli kannattaa ottaa käyttöön vasta silloin, kun sen paremmasta kyvystä on todellista hyötyä.

### Pysyn samassa tehtävässä ja mallissa

Tehtävän turha pilkkominen uusiin keskusteluihin, agentteihin ja malleihin voi hävittää välimuistin.

Siksi pidän saman tehtävän aikana mahdollisuuksien mukaan saman mallin, saman tarjoajan, saman system promptin ja saman kontekstirakenteen.

Mallia kannattaa vaihtaa tehtävien välillä, ei jatkuvasti kesken työn.

### Testaan kompression käytännössä

Se, että kompressioasetus näkyy käyttöliittymässä tai konfiguraatiossa, ei todista sen toimivan.

Pitää mitata, missä vaiheessa kompressio käynnistyy, toimiiko se API-mallilla, paljonko konteksti pienenee, säilyvätkö tärkeät päätökset ja pieneneekö seuraavan kutsun laskutettu input.

Hermeksen kanssa törmäsin juuri tähän.

Kompression kynnys toimi paikallisilla malleilla, mutta API-mallilla sama asetus ei käyttäytynyt odotetusti. Miljoonan tokenin konteksti johti siihen, että automaattinen kompressio käynnistyi vasta satojen tuhansien tokenien jälkeen.

Käyttäjä maksaa eron, vaikka ei voi kunnolla vaikuttaa siihen.

## Lörpöttely maksaa kahdesti

Ensin maksan pitkän vastauksen output-tokenit. Seuraavalla kierroksella sama vastaus palaa osaksi input-kontekstia, jolloin maksan siitä uudelleen.

Siksi säädän mallin personoinnin niin, ettei se tervehdi turhaan, toista kysymystäni tai tarjoa viittä vaihtoehtoa, kun yksi riittää. Sen pitää raportoida muutokset, testit ja puutteet ja pysyä juuri niin monisanaisena kuin tehtävä vaatii.

Tavoite ei ole mahdollisimman lyhyt vastaus.

Liian lyhyt vastaus aiheuttaa lisäkierroksia. Liian pitkä kasvattaa laskua ilman hyötyä.

Tavoite on **juuri riittävä vastaus**.

## Paikallinen malli eturiviin

Monet tehtävät eivät tarvitse pilven tehokkainta mallia.

Paikallinen malli voi hoitaa esimerkiksi ohjelmointia, dokumentointia, tiedostojen käsittelyä, testien ajamista, lokien analysointia, projektimuistin ylläpitoa, ensimmäisen koodikatselmoinnin ja toistuvat agenttitehtävät.

Kun laitteisto on jo olemassa, lisätehtävän kustannus on lähinnä sähköä ja omaa aikaa.

Siksi ajattelen API-mallia eskalointitasona:

> Paikallinen malli yrittää ensin. API-malli otetaan mukaan vasta, kun tehtävän vaikeus tai epäonnistuminen sitä perustelee.

## Jokaiselle tehtävälle kova raja

Kuukausibudjetti ei suojaa karanneelta agentilta. Yksi viallinen tehtävä voi kuluttaa suuren osan koko kuukauden budjetista muutamassa tunnissa.

Siksi jokaisella tehtävällä pitää olla oma katto: enimmäiskustannus, enimmäisaika, API-kutsujen määrä, output-tokenien määrä, työkalukutsujen määrä, aliagenttien määrä ja uusintayritysten määrä.

Kun raja tulee vastaan, agentti pysähtyy.

Se ei saa itse nostaa budjettia, vaihtaa rajatta kalliimpaan malliin tai aloittaa tehtävää jatkuvasti uudelleen.

## Ajattelua vain sen verran kuin tehtävä tarvitsee

Reasoning-mallin suurempi ajattelubudjetti ei automaattisesti tee vastauksesta parempaa.

Tiedoston nimeäminen, tekstin muotoilu tai testituloksen lukeminen ei tarvitse raskainta reasoning-tasoa.

Käytän kevyttä reasoningia mekaanisiin tehtäviin, keskitasoa tavalliseen ongelmanratkaisuun ja raskasta reasoningia vain vaikeisiin ja arvokkaisiin tehtäviin.

Eskalointi tehdään tarvittaessa, ei varmuuden vuoksi.

## Silmukat kiinni

Agentti voi näyttää ahkeralta tekemättä todellista edistystä.

Se voi kutsua samaa työkalua samoilla argumenteilla, lukea saman tiedoston uudelleen, suorittaa saman komennon, kaataa saman testin samalla tavalla, palata selaimessa samalle sivulle tai käynnistää useita aliagentteja tekemään samaa työtä.

Tarvitaan yksinkertaiset säännöt: sama kutsu samoilla argumenteilla vain kerran ilman uutta tietoa, sama virhe korkeintaan kaksi kertaa, kolmannen samanlaisen epäonnistumisen jälkeen pysäytys ja jokaiselle työkalulle oma kiintiö.

Agentin vilkkaus ei ole sama asia kuin edistyminen.

## Mittaa myös se input, jota et näe

Kirjoittamani viesti voi olla vain pieni osa siitä, mitä mallille oikeasti lähetetään.

Mukana voi kulkea system prompt, koko keskusteluhistoria, työkalujen skeemat, MCP-palvelimien kuvaukset, projektiohjeet, muistot, RAG-hakutulokset, tiedostojen sisältö, komentojen tulosteet, aliagenttien raportit sekä kuvat ja kuvakaappaukset.

Käyttöliittymän pitäisi näyttää, mihin tokenit kuluvat.

Muuten voin lyhentää omaa viestiäni pari riviä samalla, kun tuhansien rivien työkaluskeemat ja vanha keskusteluhistoria lähtevät mukaan joka kutsulla.

## Älä lähetä koko projektia varmuuden vuoksi

Agentti ei tarvitse koko koodivarastoa jokaiseen tehtävään.

Parempi tapa on paikantaa ongelma, hakea siihen liittyvät symbolit, seurata viittaukset, lukea tarvittavat tiedostot ja laajentaa kontekstia vain tarpeen mukaan.

Sama koskee lokeja.

Tuhannen rivin onnistunut testituloste ei auta ketään. Usein riittää, onnistuiko vai epäonnistuiko, epäonnistuneiden testien nimet, virheilmoitus ja olennainen stack trace.

Loput on kohinaa, josta maksetaan turhaan.

## Rakenna välimuisti tarkoituksella

Prompt-välimuisti voi laskea kustannuksia, mutta vain jos järjestelmä on rakennettu sitä varten.

Vakaa sisältö kannattaa sijoittaa kontekstin alkuun ja muuttuva sisältö loppuun.

Mallinvaihto, tarjoajan vaihto, fallback, muuttunut system prompt tai uusi keskustelu voivat rikkoa välimuistin.

Siksi cache-osumia pitää mitata eikä vain olettaa.

## Tyhjäkäynti – kun agentti laskuttaa tekemättä mitään

Tämä on kohta, joka sai minut alun perin kirjoittamaan koko jutun.

Tavallinen ohjelma ei juuri kuluta mitään, kun sitä ei käytetä. API-agentti voi sen sijaan jatkaa maksullisia kutsuja, vaikka en ole antanut sille uutta tehtävää.

Syynä voivat olla esimerkiksi heartbeatit, keep-alivet, dashboardin polling, muistien synkronointi, automaattinen indeksointi, taustatiivistykset, automaattiset tilannekatsaukset, epäonnistuneiden kutsujen uusinta, auki jäänyt työkalusilmukka, taustalla toimivat aliagentit tai liian usein käynnistyvä ajastettu tehtävä.

Vaarallisinta on näkymättömyys.

Ruudulla ei tapahdu mitään, mutta taustalla lähtee jatkuvasti maksullisia kutsuja.

Jos kulutus on 50 tokenia sekunnissa, se tarkoittaa noin:

- 180 000 tokenia tunnissa
- 4,32 miljoonaa tokenia vuorokaudessa
- noin 130 miljoonaa tokenia kuukaudessa

Se ei ole pieni optimointivirhe.

Se on auki jäänyt hana.

Hyväksymiskriteeri on yksinkertainen. Kun en ole käynnistänyt tehtävää, maksullisia mallikutsuja on nolla, laskutettuja tokeneita on nolla, aktiivisia aliagentteja on nolla ja automaattisia uusintoja on nolla.

Poikkeuksena voi olla erikseen tilaamani valvontatehtävä. Sen pitää näkyä käyttöliittymässä ja sen kustannus pitää kertoa etukäteen.

Tyhjäkäynti on helppo testata:

1. Käynnistä agentti.
2. Älä anna sille tehtävää.
3. Jätä se auki pariksi tunniksi.
4. Tarkista tarjoajan usage-loki.
5. Toista testi valmiin tehtävän jälkeen.
6. Tarkista, loppuuko kulutus oikeasti.

Tyhjäkäynnillä API-kulutuksen pitää olla nolla.

## Seuranta automaattiseksi

Kulutusta ei pidä tarkistaa kerran kuukaudessa laskulta.

Seurannan pitää tunnistaa kustannuspiikit, kulutus ilman aktiivista tehtävää, poikkeava kutsutiheys, toistuvat virheet, mallin tai tarjoajan vaihtuminen, kalliin fallbackin käyttö, tehtäväbudjetin ylitys ja tehtävän jälkeen jatkava agentti.

Pelkkä hälytys ei riitä.

Valvonnan pitää pystyä estämään uusi kutsu, keskeyttämään tehtävä ja vaatimaan ihmisen hyväksyntä ennen jatkamista.

Hälytys ilman jarrua on vain kohtelias ilmoitus rahan palamisesta.

## Ei pukkia kaalimaan vartijaksi

Agenttivaljaiden oma kulutusmittari on hyödyllinen, mutta se ei saa olla ainoa valvonta.

Sama järjestelmä aiheuttaa kulutuksen, laskee tokenit, valitsee mallin, päättää kompressiosta, suorittaa fallbackin ja raportoi oman toimintansa.

Jos järjestelmässä on bugi, sama bugi voi vääristää sekä kulutusta että raporttia.

Siksi riippumaton valvonta pitää rakentaa oman gatewayn, API-tarjoajan usage-tietojen ja oman kustannuslokin varaan.

Agentin oma ilmoitus on vertailutieto, ei lopullinen totuus.

## Ihminen pidetään ruorissa

Automaatio saa havaita ja pysäyttää poikkeamat, mutta merkittävät kustannuspäätökset kuuluvat ihmiselle.

Hyväksyntää tarvitaan, kun tehtävän arvioitu kustannus ylittää rajan, agentti haluaa vaihtaa kalliimpaan malliin, konteksti kasvaa poikkeuksellisen suureksi, sama tehtävä epäonnistuu toistuvasti, fallback nostaa hintaa olennaisesti, agentti haluaa käynnistää useita aliagentteja, kuukausibudjetti on loppumassa tai kulutus jatkuu tehtävän valmistumisen jälkeen.

Hyväksyntäikkunassa pitää näkyä tähänastinen kustannus, jatkamisen arvioitu hinta, nykyinen ja uusi malli, tarjoaja sekä halvempi vaihtoehto.

Agentti ei saa itse korottaa budjettiaan, hyväksyä omaa fallbackiaan, kuitata omaa hälytystään, poistaa kustannusrajoja, vaihtaa valvomatonta API-avainta tai muuttaa valvonnan asetuksia.

Periaate on yksinkertainen:

> Automaatio havaitsee ja pysäyttää. Ihminen hyväksyy kustannusriskin.

## Jokainen kutsu pitää pystyä jäljittämään

Jokaisen API-kutsun pitää olla yhdistettävissä käyttäjään, projektiin, tehtävään, agenttiin, malliin, tarjoajaan ja kustannuspaikkaan.

Tuntematon kutsu ei ole pieni kummajainen. Se on valvontavirhe.

Myös kehitys, testaus ja tuotanto kannattaa erottaa omilla avaimilla, budjeteilla ja rajoilla.

Testiagentti ei saa käyttää tuotannon rajatonta avainta.

## Optimoi lopputuloksia, älä tokeneita

Lopulta olennaisia mittareita ovat eurot ja aika hyväksyttyä tehtävää kohti, API-kutsut ja korjauskierrokset tehtävää kohti, ihmisen korjausaika, välimuistin osumat, keskeytyneet tehtävät, paikallisesti ratkaistujen tehtävien osuus, tyhjäkäyntitokenit ja fallbackien kustannus.

Halvin järjestelmä ei ole se, jolla on halvin token.

Halvin järjestelmä ratkaisee tehtävän luotettavasti, nopeasti, vähillä kierroksilla ja mahdollisimman suurelta osin paikallisesti.

## Lopuksi

Kun annan agentille oikeuden käyttää rahaa puolestani, haluan tietää:

1. mikä malli on käytössä
2. mikä tarjoaja sitä ajaa
3. paljonko tehtävä on jo maksanut
4. paljonko jatkaminen todennäköisesti maksaa
5. milloin järjestelmä pysähtyy
6. mitä tapahtuu vikatilanteessa
7. voisiko tehtävän hoitaa paikallisesti
8. kuka hyväksyy budjetin ylityksen

Kun nämä tiedot puuttuvat, tarjoajan, proxyn tai agenttivaljaiden kannustin voi ohittaa minun taloudellisen etuni.

Ei välttämättä pahantahtoisesti. Vaan siksi, ettei kukaan rakentanut järjestelmää pitämään minun puoliani.

Tokenit ovat rahaa.

Agentin pitää käsitellä niitä yhtä tarkasti kuin yrityksen pankkitiliä. Ei siksi, että agentti olisi paha tai epäluotettava, vaan siksi, ettei kenellekään anneta avointa piikkiä.

Ei edes ahkeralle apurille, joka jatkaa työntekoa silloin, kun luulen, ettei mitään tapahdu.
