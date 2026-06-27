---
title: Etusivu
description: Henkilökohtainen blogi tekoälystä, systeemiajattelusta, resilienssistä ja kirjoittamisesta.
---

# Ihmisen käyttöjärjestelmä

Mitä oikeastaan on ihmisen käyttöjärjestelmä?

Se ei ole persoonallisuusteoria eikä tavallinen itseapumetafora. Se on tapa katsoa ihmistä toimivana järjestelmänä: kehollisena, kognitiivisena, sosiaalisena ja ympäristöön kytkeytyvänä kokonaisuutena, jolla on resurssit, sensorit, rajapinnat, suojausmekanismit, palautesilmukat ja käyttötilat.

Tietokoneessa käyttöjärjestelmä ei ole ohjelma, jolla tehdään yksi tehtävä. Se on kerros, joka jakaa resurssit, käsittelee keskeytykset, ajaa taustaprosessit, rajaa oikeudet ja palautuu virheistä. Ihmisessä vastaava kerros näkyy energian säätelynä, kehon signaaleina, mielihyvän kalibrointina, ajattelun lukkoina, sosiaalisina palomuureina ja kykynä palauttaa suunta.

Siksi ihmisen käyttöjärjestelmä ei kysy vain, miltä jokin tuntuu. Se kysyy: mikä osa järjestelmästä antaa tämän signaalin, mitä se suojaa, mitä se kuluttaa ja mikä muutos palauttaa toimintakyvyn?

Tämän blogin tehtävä on testata näitä malleja julkisesti: pieninä havaintoina, protokollina, korjausliikkeinä ja versioina. Järjestelmä ei valmistu yhdellä oivalluksella. Se kasvaa versioina, ei kaaoksena.

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

## Aihealueet

<div class="card">
<strong>AI ja lokaalit mallit</strong><br>
Avoimet mallit, paikallinen ajo, työkalut ja käytännön rajoitteet.
</div>

<div class="card">
<strong>Systeemiajattelu</strong><br>
Ihmisen, työn, terveyden ja teknologian rakenteet.
</div>

<div class="card">
<strong>Resilienssi ja elämäntapa</strong><br>
Energia, terveys, kitka, kurinalaisuus ja palautuminen.
</div>

<div class="card">
<strong>Kirjoittaminen</strong><br>
Kirjat, ideat, luonnokset ja ajattelun työkalut.
</div>
