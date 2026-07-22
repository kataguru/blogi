---
title: "A local AI agent: a tool that knows my material"
description: "A report on a personal RAG agent combining a local model, semantic search and document management. No cloud, no subscription — a tool that works on my terms."
date: 2026-07-12 06:00:00 +0300
categories: [ai, teknologia, lokaalit-mallit, rag]
type: Article
image: /assets/images/ai.png
image_alt: "A local AI agent on a home office workstation"
lang: en
translation_key: 2026-07-12-lokaali-tekoalyagentti-tyokalu-joka-tuntee-oman-aineistoni
permalink: /en/2026/07/12/a-local-ai-agent-that-knows-my-material/
---

In the last few weeks, I have been building an agent that combines multilingual semantic search, structural code understanding and document management. No cloud service, no SaaS account. A system running on my own computer that knows what I've written, in which file any function is and how to get back to it.

## Why this at all

I've been writing on the blog for a long time about things I'm trying to understand: the structures of everyday life, the price of decisions, tolerating mediocrity. The more text, code and documents accumulate, the harder it is to find.

Keyword search is not enough. If I search for "risk normalization", I can't find a post about stairs. If I search for "the real price of a cheap pick", I can't guess what word I used myself two years ago. I need a search that searches by meaning and not wording.

Cloud services only do this with external sources. They don't know my own files, my own code, my own papers — and require the data to go out.

A local agent solves both problems at the same time.

## System structure

At the core is a local language model that runs quantized on its own machine. Quantization reduces the memory requirement to a fraction of the original without the quality collapsing in practical use.

Three data sources are connected to the model:

**Vector search (RAG).** Qdrant indexes texts, code and search results as semantic vectors. The query matches the meaning, not the letter.

**Knowledge graph.** Structured memory of projects, decisions and conventions. Vector search tells what is written; the graph tells why a certain decision was made at the time.

**Paperless-ngx.** Scanned documents, invoices, letters. After OCR, they also end up in the same search space as everything else.

One query, three levels of memory.

## Multilingualism is not an additional feature

Finnish is not the primary language of artificial intelligence. Most immersion models are trained in English, and "multilingual" practically means that other languages work there.

In this system, the starting point is different. `multilingual-e5-small` is used, which places the texts of more than a hundred languages in the same vector space. A Finnish-language query finds an English-language document. The note in Swedish links to the blog post in Finnish.

E5 models require the help prefixes: `query:` for searching, `passage:` for indexing. Without them, the asymmetry between a short survey and a long document clearly weakens the match accuracy. Small detail, big impact.

## Code is structure, not text

Most RAG systems break the code into arbitrary pieces using the same logic as plain text. It defeats the meaning.

This system breaks down the code by language:

- Python is parsed into an AST tree, where classes and functions are separated as structural units
- JavaScript and TypeScript are identified by regular expressions, including arrow functions and interface definitions
- Rust contains structs, enums, traits and impl blocks
- Go and Java are treated accordingly according to structure

When I ask "where does Paperless sync happen", the system doesn't look for the word *sync* in a random line. It returns the `sync_round` function as a whole because it knows which unit the line belongs to.

The difference is not cosmetic. A fragment without context is a quote; piece by structure is the answer.

## One process, not two

The original plan had two background processes: one to monitor code files, the other to synchronize Paperless documents. Both loaded their own embedding model into memory. Double the work, double the consumption.

I combined them into a single daemon that loads the model once and handles both tasks in the same loop. The SHA256 hash tells if the file has changed. If not, it will not be indexed again.

The same principle as in everyday maintenance: in a recurring situation, a good enough solution that is run regularly produces more than endless optimization that is never completed.

## Where can this fall

Fair:

- If the Qdrant container dies and the volume has not been preserved separately, the index is gone. Re-indexing is possible, but slow.
- The local model does not reach the level of the best models in the cloud in the most difficult reasoning. In practice, the difference is rarely visible because most queries are search and compilation, not deep reasoning.
- Running tests still requires manual work. An agent is not allowed to run shell commands without permission, and I'm not going to give that permission.

These are not bugs, but chosen compromises: privacy at the expense of the cloud, adequate quality instead of extreme, slowness at the price of control.

A compromise not chosen is a fault. The compromise that has been chosen is a design decision.

## Why this is more than a technical project

The system is an extension of the same principle I've written about in other contexts: less noise, more structure.

When the data is under one's own control, when the search works with meaning and not with a word search, and when the code is understood as a structure, the tool ceases to be an obstacle. It becomes an extension of thinking.

It's also a kind of public desktop — organized, discoverable, accessible without external dependency.

No cloud. No subscription fee. No data transfer.

Just a machine where things are where they should be.
