---
title: Etusivu
description: Henkilökohtainen blogi ihmisen käyttöjärjestelmästä, tekoälystä, systeemiajattelusta, resilienssistä ja kirjoittamisesta.
---

# Ihmisen käyttöjärjestelmä

Kaikki ei ollut rikki. Järjestelmä vain käytti väärää tilaa.

Tämä sivusto on yritys kuvata, mitä tapahtuu, kun omaa elämää alkaa katsoa järjestelmänä: ei luonteen testinä, ei motivaation puutteena, ei sankaritarinana, vaan rakenteena, jossa keho, ympäristö, työ, huomio, palaute, kitka ja resurssit vaikuttavat toisiinsa.

<figure class="hero-image">
  <img src="{{ '/assets/images/evijarvi-hero.png' | relative_url }}" alt="Evijärven rantamaisema iltavalossa">
</figure>

Ihmisen käyttöjärjestelmä ei ole persoonallisuusteoria eikä valmis oppi hyvästä elämästä. Se on omaan elämään perustuva analyysimalli. Havainnot syntyvät siitä, mitä olen kokenut, tehnyt, korjannut, rikkonut, mitannut, epäillyt ja tulkinnut.

Siksi väitteet ovat rajattuja. En väitä, että sama malli toimii kaikille. Väitän, että näin järjestelmä näkyi omassa elämässäni. Jos tunnistat saman rakenteen omassasi, malli voi olla hyödyllinen.

## Mitä käyttöjärjestelmä tarkoittaa?

Tietokoneessa käyttöjärjestelmä ei ole yksittäinen ohjelma. Se on kerros, joka jakaa resurssit, käsittelee häiriöt, pitää taustaprosessit käynnissä, rajaa oikeudet ja palautuu virheistä.

Ihmisessä vastaava kerros näkyy toisella tavalla.

Se näkyy siinä, miten energia riittää tai loppuu. Miten keho antaa signaaleja. Miten mielihyvä kalibroituu. Miten ajattelu lukittuu. Miten ympäristö ohjaa valintoja. Miten sosiaaliset rajat suojaavat tai vuotavat. Miten ihminen palauttaa suunnan, kun järjestelmä on ajautunut liian kauas omasta tarkoituksestaan.

Tässä mielessä ihmisen käyttöjärjestelmä kysyy toisenlaisia kysymyksiä:

- mikä osa järjestelmästä antaa tämän signaalin?
- mitä se yrittää suojata?
- mitä se kuluttaa?
- mikä palaute puuttuu?
- mikä kitka on hyödyllistä ja mikä vain kuormittaa?
- mikä pieni korjausliike palauttaisi toimintakykyä?

## Miksi tämä blogi on olemassa?

Tämä blogi on julkinen testialusta.

Täällä omaa elämää ei esitetä valmiina ratkaisuna, vaan havaintoaineistona. Yksittäisestä kokemuksesta etsitään rakennetta. Rakenteesta muodostetaan malli. Mallia verrataan todellisuuteen. Jos se ei toimi, sitä säädetään.

Tavoite ei ole tehdä elämästä helppoa. Tavoite on tehdä siitä luettavampaa.

Kun ongelma muuttuu epämääräisestä tunteesta näkyväksi rakenteeksi, sitä voi alkaa korjata ilman tarpeetonta syyllisyyttä.

## Mistä täällä kirjoitetaan?

<div class="card">
<strong>Ihmisen käyttöjärjestelmä</strong><br>
Oman elämän analyysiä järjestelmänä: resurssit, kitka, palaute, rajat, kuorma, kapasiteetti ja palautuminen.
</div>

<div class="card">
<strong>AI ja lokaalit mallit</strong><br>
Tekoäly käytännön työkaluna. Avoimet mallit, paikallinen ajo, automaatio ja se, missä kohtaa järjestelmä oikeasti helpottuu.
</div>

<div class="card">
<strong>Systeemiajattelu</strong><br>
Ihmisen, työn, terveyden, teknologian ja yhteiskunnan rakenteet. Ei irrallisia vinkkejä, vaan syy-seuraussuhteita.
</div>

<div class="card">
<strong>Resilienssi</strong><br>
Resilienssi tarkoittaa kykyä kestää häiriöitä ja palautua niistä. Täällä se tarkoittaa käytännössä varaa, rytmiä, rajoja ja järjestelmiä, jotka kestävät myös heikot päivät.
</div>

<div class="card">
<strong>Kirjoittaminen</strong><br>
Kirjat, luonnokset, teesit ja ajattelun työkalut. Kirjoittaminen ei ole vain ilmaisua, vaan tapa rakentaa järjestystä havaintojen ympärille.
</div>

## Hyvä aloituskohta

Jos haluat ymmärtää sivuston rungon, aloita teeseistä:

[Katso ihmisen käyttöjärjestelmän teesit]({{ '/teesit/' | relative_url }})

Ne tiivistävät tämän blogin perusajatuksen: ihminen ei ole irrallinen päätöskone. Hän on järjestelmä, jossa keho, ympäristö, huomio, palaute, kitka, resurssit, muistot, suhteet ja rakenteet ohjaavat toisiaan.

## Viimeisimmät kirjoitukset

<ul class="post-list">
{% for post in site.posts limit:5 %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
