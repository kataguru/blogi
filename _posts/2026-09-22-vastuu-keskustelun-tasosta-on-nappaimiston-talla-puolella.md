---
title: "Vastuu keskustelun tasosta on näppäimistön tällä puolella"
description: "Kielimalli jatkaa sille annettua maailmaa. Käyttäjän tehtävä on asettaa älyllinen rima, purkaa vakuuttavuusteatteri ja tarkistaa seuraukset."
date: 2026-09-22 06:00:00 +0300
categories: [tekoäly]
lang: fi
translation_key: 2026-09-22-vastuu-keskustelun-tasosta
---

Kielimalleja soimataan vuoroin kahdesta vastakkaisesta synnistä. Välillä ne tuottavat unettavan latteaa, ympäripyöreää konsulttijargonia, jossa sanotaan paljon sanomatta yhtään mitään. Toisinaan taas törmätään päinvastaiseen ääripäähän: malli vastaa vaikeaan pulmaan häikäisevän itsevarmasti, jäsennellysti ja kaunopuheisesti – mutta puhuu sisällöllisesti aivan puuta heinää.

Kumpikin havainto pitää paikkansa. Kumpikaan niistä ei silti todista, että kielimalli olisi perimmiltään tyhmä tai käyttökelvoton.

Ne kertovat ennen kaikkea siitä, miten kielimalli matemaattisesti toimii – ja siitä, millaiseen kehikkoon ihminen sen kulloinkin asettaa.

Vastuu ei tietenkään ole aina ja yksinomaan käyttäjällä. Mallin kouluttaja kantaa vastuun perusmassasta ja sovellusalueesta, kehittäjä vastaa järjestelmäkehotteista ja käyttöliittymästä, ja palveluntarjoaja siitä, miten järjestelmää markkinoidaan. Mutta sillä sekunnilla, kun kursori vilkkuu tyhjässä syötekentässä ja keskustelu alkaa, käyttäjällä on käsissään enemmän vipuvartta kuin yleensä ymmärretään.

Älyllinen rima asetetaan aina näppäimistöltä.

### Kielimalli jatkaa annettua maailmaa

Kielimalli ei ole tietokanta, hakukone eikä tietoinen ajattelija, vaikka se voi ajoittain matkia niitä kaikkia. Sen perimmäinen moottori tiivistyy seuraavan sananosan tai merkin ehdolliseen todennäköisyyteen:

$$P(w_t \mid w_{<t})$$

Käytännössä malli punnitsee jatkuvasti yhtä ainoaa kysymystä: *mikä jatko sopii matemaattisesti parhaiten kaikkeen siihen, mitä tähän mennessä on sanottu?*

Modernit mallit tukeutuvat toki järjestelmäohjeisiin, hienosäädettyihin ajatusmalleihin ja ulkoisiin työkaluihin, joten yksinkertainen todennäköisyyskaava ei kerro koko tarinaa. Se paljastaa silti koneen ytimen: **jokainen vastaus syntyy suhteessa kontekstiin.**

Jos syöte on laiska ja väljä – *"kirjoita hyvä juttu tekoälystä"* – mahdollisuuksien avaruus on valtava. Turvallisin ja todennäköisin reitti on tällöin harjoitusdatan harmaa keskiarvo: muutama yleinen hyöty, pari tuttua riskiä ja lopuksi tasapainotteleva yhteenveto. Teksti on kieliopillisesti moitteetonta, mutta täysin merkityksetöntä.

Kun käyttäjä sen sijaan määrittelee väitteen, rajaa kohderyhmän, asettaa reunaehdot ja osoittaa, mitä oletuksia pitää epäillä, mahdollisten vastausten avaruus leikkautuu jyrkästi. Malli ei muutu maagisesti älykkäämmäksi, mutta tehtävä muuttuu täsmälliseksi. Silloin sillä on edellytykset aktivoida oppimaansa tarkoituksenmukaisesti.

Tutkimuskirjallisuudessa ilmiötä kutsutaan promptiherkkyydeksi (*prompt sensitivity*). Pienetkin nyanssit tehtävänannossa keikauttavat mallin suoritusta. Täsmällinen rajaus ja hyvät esimerkit vähentävät satunnaisuutta, mutta vastuu ohjauksesta ei poistu koskaan.

### Inhimillinen peili koneen sisällä

Ilmiö on tuttu arkielämästä.

Puuduttavassa virastopalaverissa terävinkin asiantuntija alkaa helposti puhua passiivimuodoilla ja turvallisilla fraaseilla. Hän sopeutuu tilan kieleen, odotuksiin ja riskitasoon. Mutta viepä sama ihminen kahvipöytään, jossa ajatuksia saa vapaasti haastaa, keskeneräisiä ideoita pyöritellä ja huonoille oletuksille nauraa, keskustelusta tulee aivan toisenlaista.

Kielimalli ei tietenkään koe ilmapiiriä, turhaudu tai innostu. Vertaus toimii silti puhtaasti kielen tasolla. Koska malli on opetettu ihmisten tuottamalla tekstimassalla, se tunnistaa erilaiset kielelliset rekisterit ja jatkaa niitä.

Geneerinen kysymys kutsuu väistämättä geneerisen vastauksen. Täsmällinen, kriittinen ja vivahteikas vuoropuhelu puolestaan pakottaa esiin tarkemmat käsitteet ja kestävämmän argumentaation.

Tätä ei kuitenkaan pidä mystifioida. Mallin huomiomekanismi (*self-attention*) ei "virity toiselle taajuudelle", eikä neuroverkon kätköistä avata salaista asiantuntijakammiota. Kyse on puhtaasti siitä, miten huomiomatriisi painottaa kontekstin eri osien keskinäisiä suhteita. Kun syöte sisältää täsmällisiä käsitteitä ja tiukkoja rajauksia, ne ohjaavat seuraavien sanojen todennäköisyyksiä vääjäämättömästi.

Hyvä keskustelu ei herätä koneessa piilevää persoonaa. Se antaa laskennalle paremman matemaattisen lähtötilanteen.

### Testaajan silmä paljastaa feikkiteatterin

Kielimallilla on silti yksi kiusallinen, inhimillistä käyttäytymistä muistuttava heikkous: se pyrkii täyttämään käyttäjän odotukset silloinkin, kun sillä ei ole aavistustakaan totuudesta.

Törmäsin tähän hiljattain omassa mallikokeilussani. Annoin mallille syvällisen, fysiologista säätelyä koskevan kysymyksen. Ensi silmäyksellä tulos oli mykistävän vaikuttava: malli marssitti esiin "eri alojen asiantuntijapaneelin", vertaili tieteellisiä hypoteeseja ja lätkäisi vastauksensa perään itsevarmasti arvosanan 5/5 todeten: *"Luottamustaso: Korkea"*.

Tavallinen lukija olisi saattanut pitää vastausta nerokkaana ja perusteellisena analyysina. Ohjelmistotestaajan silmään osui kuitenkin kaksi hälytyskelloa:

1. **Ilmiselvä asiavirhe**: Malli väitti Walter Cannonin kehittäneen allostaasin käsitteen vuonna 1932. Cannon teki tunnetuksi homeostaasin; allostaasin loivat Peter Sterling ja Joseph Eyer vasta vuonna 1988.
2. **Keinotekoinen kulissi**: Asiantuntijapaneeli, pisteet ja korkea luottamusaste eivät olleet riippumattomia todisteita laadusta. Ne olivat taustapromptista vuotanutta esitystapaa – feikkiteatteria, jolla vakuuttava ulkokuori naamioi epävarman ja virheellisen sisällön.

Mallin itselleen antama luottamusluku ei ole objektiivinen laadunvarmennus. Se on vain lisää mallin tuottamaa tekstiä. Sama järjestelmä, joka pystyy keksimään väärän vuosiluvun, pystyy keksimään myös vakuuttavan selityksen omasta erehtymättömyydestään.

Helppo johtopäätös olisi ollut levitellä käsiä ja todeta, että tekoäly on rikki. Testaajan kysymys on aina toinen: *mikä järjestelmän osakomponentti tuottaa tämän virheellisen käytöksen?*

Kun mallin ohjeistuksesta karsittiin tarpeeton roolileikki, itse annetut kouluarvosanat ja teennäinen luottamustasoteatteri, vastaus muuttui kerralla: siitä tuli lyhyempi, suorempi ja vaivattomasti todennettava. Korjaus ei tehnyt mallista kaikkitietävää, mutta se poisti silmänkääntötempun, joka sai virheen näyttämään kovalta tieteeltä.

Tämä ero on laadun kannalta ratkaiseva.

### Hyvä prompti ei korvaa laadunvalvontaa

Keskustelun tason nostaminen ei vaadi kikkailua tai monimutkaista "prompti-insinööritaitoa". Olennaista on tehdä koneelle selväksi, millaista ajattelun laatua tehtävä vaatii.

Käytännössä hyvä keskustelunavaus määrittelee:

* Mikä ongelma oikeastaan pyritään ratkaisemaan?
* Mitkä oletukset pitää kyseenalaistaa?
* Mikä tiedetään varmaksi ja mikä on epävarmaa?
* Millä kriteereillä onnistumista arvioidaan?
* Haetaanko neutraalia tiivistelmää, kriittistä vasta-argumenttia vai perusteltua päätösehdotusta?
* Milloin mallin on syytä sanoa suoraan, ettei tietoa ole?

Vielä tärkeämpää on keskustelun jatkaminen. Haasta mallia: *Mikä tässä päättelyssä on heikoin oletus? Mikä empiirinen havainto kumoaisi tämän johtopäätöksen? Mikä osa perustuu lähteisiin ja mikä on mallin omaa päättelyketjua?* Ja jos väite on kriittinen, tarkista aina alkuperäinen lähde.

Tämä ei ole mitään tekoälytaikuutta. Se on normaalia asiantuntijatyötä: tehtävän rajaamista, oletusten testaamista ja tulosten validointia.

Hyvä käyttäjä ei siis vain pyydä konetta jauhamaan lisää tekstiä. Hän rakentaa olosuhteet, joissa heikko ajattelu jää heti kiinni.

### Vastuu jakautuu, mutta sitä ei voi ulkoistaa

Kielimallilla ei ole makua, kunnianhimoa eikä totuudentajua inhimillisessä merkityksessä. Eikä se kanna pienintäkään vastuuta siitä, jos sen sujuvasti generoima puolitotuus päätyy raporttiin, päätöksentekoon tai tuotantokoodiin.

Käyttäjälle jää aina kolme luovuttamatonta tehtävää:

1. **Aseta rima.** Määrittele ongelma niin kirkkaasti, että laadukkaan ja huonon vastauksen voi erottaa toisistaan.
2. **Pura teatteri.** Älä sekoita runsasta pituutta, varmaa äänenpainoa tai monimutkaista rakennetta laadun takeeksi.
3. **Mittaa seuraukset.** Mitä kriittisempi asia on kyseessä, sitä vähemmän mallin omalla vakuuttavuudella on merkitystä.

Tämä ei poista palveluntarjoajan tai mallikehittäjän vastuuta. Huonosti koulutettua tai vaarallisesti viritettyä järjestelmää ei voi paikata pelkällä käyttäjän näppäryydellä. Mutta toisaalta: paraskaan kielimalli ei pelasta keskustelua, jossa tavoitetta ei rajata, väitteitä ei haasteta eikä tuloksia tarkisteta.

Tekoäly tarjoaa tilastollisia polkuja eteenpäin. Ihminen päättää, mihin kysymyksellä tähdätään, mikä hyväksytään todeksi ja mitä tehdään seuraavaksi.

Siksi vastuu keskustelun tasosta on lopulta aina näppäimistön tällä puolella.

### Lähteet

* **Sterling, P. & Eyer, J. (1988)**: *Allostasis: A New Paradigm to Explain Arousal Pathology.* Teoksessa Fisher, S. & Reason, J. (toim.): *Handbook of Life Stress, Cognition and Health.* John Wiley & Sons.
* **Vaswani, A. ym. (2017)**: [Attention Is All You Need](https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf). *Advances in Neural Information Processing Systems (NeurIPS 2017).*
* **Zhuo, J. ym. (2024)**: [Assessing and Understanding the Prompt Sensitivity of LLMs](https://aclanthology.org/2024.findings-emnlp.108/). *Findings of the Association for Computational Linguistics: EMNLP 2024.*
* **Chatterjee, A. ym. (2024)**: [POSIX: A Prompt Sensitivity Index for Large Language Models](https://arxiv.org/abs/2410.02185). *arXiv preprint arXiv:2410.02185.*
