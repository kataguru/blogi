---
title: Archive
permalink: /en/archive/
lang: en
translation_key: archive
---

# Archive

Browse published posts by topic or in chronological order.

<div class="archive-toggle">
  <input type="radio" id="archive-topic" name="archive-view" checked>
  <input type="radio" id="archive-time" name="archive-view">

  <div class="archive-toggle-buttons" role="group" aria-label="Archive view">
    <label for="archive-topic">By topic</label>
    <label for="archive-time">By date</label>
  </div>

  <section class="archive-view archive-view-topic">
    <h2>By topic</h2>
    {% assign language_posts = site.posts | where: "lang", "en" %}

    <h3>AI and technology</h3>
    <ul class="post-list">
    {% for post in language_posts %}
      {% if post.categories contains 'ai' or post.categories contains 'lokaalit-mallit' or post.categories contains 'yritykset' %}
      <li><p class="post-date">{{ post.date | date: "%d.%m.%Y" }} · Article</p><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>{% if post.description %}<p>{{ post.description }}</p>{% endif %}</li>
      {% endif %}
    {% endfor %}
    </ul>

    <h3>Structures of everyday life</h3>
    <ul class="post-list">
    {% for post in language_posts %}
      {% if post.categories contains 'arki' or post.categories contains 'rakentaminen' or post.categories contains 'koirat' %}
      <li><p class="post-date">{{ post.date | date: "%d.%m.%Y" }} · Journal entry</p><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>{% if post.description %}<p>{{ post.description }}</p>{% endif %}</li>
      {% endif %}
    {% endfor %}
    </ul>

    <h3>Writing and books</h3>
    <ul class="post-list">
    {% for post in language_posts %}
      {% if post.categories contains 'kirjoittaminen' or post.categories contains 'blogi' or post.categories contains 'kirjat' %}
      <li><p class="post-date">{{ post.date | date: "%d.%m.%Y" }} · Book update</p><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>{% if post.description %}<p>{{ post.description }}</p>{% endif %}</li>
      {% endif %}
    {% endfor %}
    </ul>
  </section>

  <section class="archive-view archive-view-time">
    <h2>By date</h2>
    <ul class="post-list">
    {% for post in language_posts %}
      <li><p class="post-date">{{ post.date | date: "%d.%m.%Y" }}{% if post.categories contains 'ai' %} · Article{% elsif post.categories contains 'kirjoittaminen' or post.categories contains 'blogi' %} · Book update{% else %} · Journal entry{% endif %}</p><h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>{% if post.description %}<p>{{ post.description }}</p>{% endif %}</li>
    {% endfor %}
    </ul>
  </section>
</div>
