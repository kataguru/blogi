---
title: Arkisto
permalink: /arkisto/
---

# Arkisto

Arkisto kokoaa julkaistut tekstit sekä aiheittain että aikajärjestyksessä. Tavoite ei ole pelkkä päiväkirjavirta, vaan löydettävä rakenne.

## Aiheittain

### AI ja teknologia

<ul class="post-list">
{% for post in site.posts %}
  {% if post.categories contains 'ai' or post.categories contains 'lokaalit-mallit' or post.categories contains 'yritykset' %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }} · Artikkeli</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

### Arjen rakenteet

<ul class="post-list">
{% for post in site.posts %}
  {% if post.categories contains 'arki' or post.categories contains 'rakentaminen' or post.categories contains 'koirat' %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }} · Päivämerkintä</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

### Kirjoittaminen ja kirjat

<ul class="post-list">
{% for post in site.posts %}
  {% if post.categories contains 'kirjoittaminen' or post.categories contains 'blogi' or post.categories contains 'kirjat' %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }} · Kirjapäivitys</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
  {% endif %}
{% endfor %}
</ul>

## Aikajärjestyksessä

<ul class="post-list">
{% for post in site.posts %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}{% if post.categories contains 'ai' %} · Artikkeli{% elsif post.categories contains 'kirjoittaminen' or post.categories contains 'blogi' %} · Kirjapäivitys{% else %} · Päivämerkintä{% endif %}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>
