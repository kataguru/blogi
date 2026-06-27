---
title: Kirjat
permalink: /kirjat/
---

# Kirjat

Tälle sivulle kootaan julkaistut, työn alla olevat ja päivitettävät kirjat.

Kirjat ovat osa samaa perusajatusta: ihminen ei ole pelkkä tunne-, tavoite- tai suoritusolento, vaan järjestelmä, jonka energia, kitka, ympäristö, päätökset, palautuminen, velka, huomio ja sosiaaliset rakenteet muodostavat kokonaisuuden.

Tarkoitus ei ole tehdä kirjoista irrallista luetteloa. Jokaisella kirjalla on oma teema, mutta ne kaikki käsittelevät samaa suurempaa kysymystä: miten ihminen säilyttää toimintakykynsä järjestelmissä, jotka kuluttavat hänen resurssejaan usein huomaamatta.

## Julkaistut, päivitettävät ja työn alla olevat kirjat

PDF-linkit ja muut lukutavat lisätään kirja kerrallaan. Tavoitteena on, että lukija saa kirjan myöhemmin joko suoraan sivustolta ladattavana PDF-versiona tai selkeän saatavuuslinkin kautta.

{% for book in site.data.books %}
<div class="card">
<strong>{{ book.title }}</strong><br>
<em>{{ book.status }}</em>

{% for paragraph in book.description %}
<p>{{ paragraph }}</p>
{% endfor %}

<p>
Osa <strong>Ihmisen käyttöjärjestelmä</strong> -kokonaisuutta.
</p>

<p><em>{{ book.availability }}</em></p>
</div>
{% endfor %}
