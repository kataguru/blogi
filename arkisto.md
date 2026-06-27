---
title: Arkisto
permalink: /arkisto/
---

# Arkisto

Arkisto näyttää julkaistut tekstit joko aiheittain tai aikajärjestyksessä. Valitse näkymä.

<div class="archive-toggle">
  <input type="radio" id="archive-topic" name="archive-view" checked>
  <input type="radio" id="archive-time" name="archive-view">

  <div class="archive-toggle-buttons" role="group" aria-label="Arkiston näkymä">
    <label for="archive-topic">Aiheittain</label>
    <label for="archive-time">Aikajärjestyksessä</label>
  </div>

  <section class="archive-view archive-view-topic">
    <h2>Aiheittain</h2>

    <h3>AI ja teknologia</h3>

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

    <h3>Arjen rakenteet</h3>

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

    <h3>Kirjoittaminen ja kirjat</h3>

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
  </section>

  <section class="archive-view archive-view-time">
    <h2>Aikajärjestyksessä</h2>

    <ul class="post-list">
    {% for post in site.posts %}
      <li>
        <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}{% if post.categories contains 'ai' %} · Artikkeli{% elsif post.categories contains 'kirjoittaminen' or post.categories contains 'blogi' %} · Kirjapäivitys{% else %} · Päivämerkintä{% endif %}</p>
        <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
        {% if post.description %}<p>{{ post.description }}</p>{% endif %}
      </li>
    {% endfor %}
    </ul>
  </section>
</div>
