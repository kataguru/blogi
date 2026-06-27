---
title: Etusivu
description: Henkilökohtainen blogi tekoälystä, systeemiajattelusta, resilienssistä ja kirjoittamisesta.
---

# Ihmisen käyttöjärjestelmä

Tämä on henkilökohtainen blogi tekoälystä, lokaaleista malleista, systeemiajattelusta, resilienssistä, kirjoittamisesta ja arjen käyttöjärjestelmistä.

Tarkoitus ei ole tuottaa kohinaa, vaan julkaista havaintoja, malleja ja käytännöllisiä periaatteita.

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
