---
title: Etusivu
description: Valikoitu päiväkirjamainen blogi, jossa oman elämän tapahtumia analysoidaan Ihmisen käyttöjärjestelmän teesien kautta.
---

# Ihmisen käyttöjärjestelmä

Valikoitu päiväkirja elämästä, jota katsotaan järjestelmänä.

Mikään ei ole rikki. Ohjausjärjestelmän asetukset ovat vain säätämättä.

<figure class="hero-image">
  <img src="{{ '/assets/images/evijarvi-hero.png' | relative_url }}" alt="Evijärven rantamaisema iltavalossa">
</figure>

Täällä yksittäiset arjen tapahtumat muuttuvat malleiksi: sauna, koirat, työ, terveys, tekoäly, kirjoittaminen ja ne pienet häiriöt, joissa oma järjestelmä paljastuu.

## Viimeisimmät kirjoitukset

<ul class="post-list">
{% for post in site.posts limit:5 %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}{% if post.categories contains 'ai' %} · Artikkeli{% elsif post.categories contains 'kirjoittaminen' %} · Kirjapäivitys{% else %} · Päivämerkintä{% endif %}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>

## Selaa lisää

<div class="card">
<strong>Kaikki tekstit</strong><br>
Arkistossa kirjoitukset voi selata aiheittain tai aikajärjestyksessä.

<p><a href="{{ '/arkisto/' | relative_url }}">Selaa arkistoa</a></p>
</div>

<div class="card">
<strong>Teoria ja ohjeet</strong><br>
Lyhyt selitys siitä, mitä Ihmisen käyttöjärjestelmä tarkoittaa ja miten tekstejä kannattaa lukea.

<p><a href="{{ '/ohjeet/' | relative_url }}">Lue teoria ja ohjeet</a></p>
</div>

<div class="card">
<strong>Kirjat</strong><br>
Kirjat kokoavat yksittäiset havainnot laajemmiksi kokonaisuuksiksi. Jokaiselle teokselle merkitään tila, sisältökuvaus ja lukutapa.

<p><a href="{{ '/kirjat/' | relative_url }}">Katso kirjat</a></p>
</div>
