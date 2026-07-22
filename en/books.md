---
title: Books
permalink: /en/books/
lang: en
translation_key: books
---

# Books

This page brings together published books, books being updated and works in progress.

The books share the same premise: a person is not merely a creature of emotions, goals or performance, but a system in which energy, friction, environment, decisions, recovery, debt, attention and social structures form a whole.

Each book has its own theme, but all of them ask the same larger question: how can a person preserve their ability to function inside systems that often consume their resources unnoticed?

## Published books, updates and works in progress

PDF links and other reading options will be added one book at a time.

{% for book in site.data.books_en %}
<div class="card">
<strong>{{ book.title }}</strong><br>
<em>{{ book.status }}</em>

{% for paragraph in book.description %}
<p>{{ paragraph }}</p>
{% endfor %}

<p>Part of the <strong>Human Operating System</strong> series.</p>
<p><em>{{ book.availability }}</em></p>
</div>
{% endfor %}
