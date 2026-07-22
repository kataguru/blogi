---
title: Home
description: A selected journal in which events from my life are examined through the theses of the Human Operating System.
permalink: /en/
lang: en
translation_key: home
---

# The Human Operating System

A selected journal about life viewed as a system.

<figure class="hero-image">
  <img src="{{ '/assets/images/evijarvi-hero.png' | relative_url }}" alt="A lakeside evening in Evijärvi">
</figure>

This is where I look for recurring patterns in everyday events.

## Latest posts

<ul class="post-list">
{% assign language_posts = site.posts | where: "lang", "en" %}
{% for post in language_posts limit:5 %}
  <li>
    <p class="post-date">{{ post.date | date: "%d.%m.%Y" }}{% if post.categories contains 'ai' %} · Article{% elsif post.categories contains 'kirjoittaminen' %} · Book update{% else %} · Journal entry{% endif %}</p>
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    {% if post.description %}<p>{{ post.description }}</p>{% endif %}
  </li>
{% endfor %}
</ul>

## Explore

<div class="card">
<strong>All posts</strong><br>
Browse the archive by topic or date.

<p><a href="{{ '/en/archive/' | relative_url }}">Browse the archive</a></p>
</div>

<div class="card">
<strong>Theory and instructions</strong><br>
A short introduction to the Human Operating System and how to read these texts.

<p><a href="{{ '/en/instructions/' | relative_url }}">Read the theory and instructions</a></p>
</div>

<div class="card">
<strong>Books</strong><br>
The books bring individual observations together into larger wholes, with their status and availability clearly marked.

<p><a href="{{ '/en/books/' | relative_url }}">View the books</a></p>
</div>
