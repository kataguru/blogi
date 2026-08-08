---
title: "Are we already on the singularity curve?"
description: "Local AI, memory systems and efficient agent harnesses can change the economics of AI work. Perhaps the singularity's rising curve begins here."
date: 2026-08-08 06:00:00 +0300
categories: [artificial-intelligence]
lang: en
translation_key: 2026-08-08-olemmeko-jo-singulariteetin-nousukayralla
permalink: /en/2026/08/08/are-we-already-on-the-singularity-curve/
image: /assets/images/singulariteetin-nousukayralla.jpg
image_alt: "A diagram in which local AI, memory, tools, web search and personal archives converge into a steeply rising singularity curve."
---

Not long ago, discussion about the future of AI revolved around one question: when will models reach human-level capability? I have started to suspect that this was the wrong question. A more interesting one is:

> What happens when a sufficiently capable digital worker can run on your own computer almost without limit?

So far, it has been easy to think about AI progress in terms of models. A new GPT, Claude, Gemini, Qwen. More parameters, a better benchmark score, a larger context window. But over the past few months I have come to think that the real change is happening somewhere else. Not in the model, but around it.

## The model is not the whole system

An LLM on its own is a bit like an exceptionally talented employee with no memory, desk, phone or access to company information. It can think, but it cannot really work. That is why we build a harness around it — a system that gives the model memory, tools, internet access, projects, documents, databases, files, a browser and the ability to actually do things on a computer.

A harness, however, has one dangerous property: it can also make a good model perform badly.

I saw this in practice with Hermes Agent. With the default setup, the system was heavy — lots of tools, MCP schemas, memory, context, compression and all kinds of meta-work. A local 27-billion-parameter model managed for a while and then started to choke. The obvious first reaction was to reach for a commercial API model. That was exactly the point where it made sense to stop and reconsider.

## What if the problem was not the model?

I started dismantling the harness. Unnecessary tools out. Unused MCP services out. Compression moved to its own auxiliary model. Web-page processing moved to another model. Memory moved to TencentDP, with embeddings handled locally. The main model was left with only the work that actually required reasoning.

Then something interesting happened. The local Qwen3.6-27B started working well again. The same cleaned-up harness also runs the commercial Ling-3.0-Flash, and the two models are roughly in the same capability class. The difference was not that the local model was too stupid.

**The harness was consuming its intelligence.**

That observation changed the way I think about the entire agent landscape. I had blamed the model for a problem I had built around it myself.

## Not every token should cost the same

Take one long agent session in which the system processes, say, 10 million tokens. Perhaps only three million of them genuinely require an expensive and capable main model. The rest is memory retrieval, compression, summarisation, document extraction, search-result processing, classification, embeddings and simple sub-agent work — tasks that do not need frontier-level reasoning.

Consider the numbers. If the main model costs €10 per million tokens and all ten million tokens go through it, the bill is €100. If only three million go to the main model and the remaining seven million go to an auxiliary model costing €0.10 per million, the total is €30.70. If those auxiliary models run on your own hardware, the API bill is effectively about €30. Same task, same main model, roughly 70 percent lower cost.

To me, this is a much more important optimisation than whether one model costs €8 or €10 per million tokens. Pricing tables obsess over the latter, while the real saving comes from deciding who should perform each part of the work in the first place.

## A vendor's harness has an interesting incentive

Model vendors understandably like to provide their own agent harnesses. They are easy to adopt. But at the same time, I hand over one important decision to the service provider: **routing the work.**

I do not know how every closed system handles its internal side tasks. They may use models of different sizes, deterministic services and specialised components. I would actually be surprised if every part of the work were always done by the same most expensive model. Yet to the customer, the whole system can still be presented as one model under one pricing structure. That raises a question a cost-conscious customer should ask:

> Which model is actually used at each stage of my work, and on what basis am I billed for it?

In my own harness, this problem does not exist because I decide. The main model reasons, a small local model summarises, an embedding model retrieves, a reranker orders results, ordinary code calculates and web search fetches current information. A model is used only when a model is needed — not simply because it happens to be running.

## Memory and the harness are two sides of the same change

Another major area of development right now is LLM memory. I have connected TencentDP memory to Hermes, and the effect is substantial. The agent knows who I am, remembers my projects, earlier decisions and conversations. The experience starts to resemble ChatGPT, except that the system runs in my own environment.

Memory alone is not enough. If every memory is dumped into the main model's context, we are back in the same swamp: a good model chokes on its harness. Memory has to be retrieved semantically and according to the situation, and the same applies to personal archives. A good digital agent needs fast, multilingual and multimodal semantic search over documents, PDFs, images, email and projects — perhaps later also audio and video. In addition, it needs real-time access to the outside world.

The system then has three different information sources: the model's own knowledge, the user's personal history and the current state of the world. Combining these correctly may matter more than squeezing a few more percentage points out of a benchmark. A benchmark measures the model. This measures the system.

## And then comes next week

As I write this, I am waiting for one model release with more curiosity than usual: Qwen3.8-27B. If expectations hold, it may be clearly stronger than today's Qwen3.6-27B while staying in the same size class.

Twenty-seven billion parameters is an important number. It is not a data-centre model. It is a consumer-hardware model, and when quantised it can run on a powerful home computer. If its agent capability, reliability and hallucination control improve enough, something fundamental shifts. Until now, frontier-level AI has effectively meant a chain like this: cloud → API → token bill. The next stage may look like this:

> open model → your own GPU → your own harness → your own memory → your own data

With electricity as the main marginal cost.

## Stop asking only which model you use

When tokens cost money, we have become used to comparing models: which costs €2 per million tokens, which costs €10, which is fastest and which is smartest.

But in the age of agents, that question is too narrow.

> **Do not ask only which model you use. Ask which harness you use.**

The harness determines how much of the work reaches the expensive main model at all. It decides whether compression, memory retrieval, embeddings, reranking, web extraction, classification and sub-agent work are handled by a cheap auxiliary model, locally, or by the same expensive model that performs the actual reasoning.

That means two users can run exactly the same frontier model and pay completely different amounts for the same work.

The model's price list tells you the price of a token.

**The harness tells you how many expensive tokens you need to buy.**

That is why the harness may ultimately determine the economics of AI work more than the model choice itself.

## This is where the labour-market question changes

Cost is still one of the biggest constraints on AI labour. If an agent burns through millions of tokens on a long task, having it do the work may not actually be cheap. But what happens if several things occur at the same time: models reach a sufficient level of capability, open models close the gap with closed frontier models, inference moves onto consumer hardware, and harnesses learn to reserve top-tier models for only the small fraction of work that is genuinely difficult?

Then the cost of AI labour can collapse. Not by 20 percent, but by orders of magnitude. At that point, the labour-market question is no longer "can AI do this job?" It becomes:

> How many people are still needed to do this work?

A five-person team may not become a zero-person team. It may become one or two people working with twenty agents. The economic effect can be almost as large, even if the end result looks more human.

## Are we already on the singularity curve?

**Estimate:** I do not know whether we are heading toward a true technological singularity. Nobody does. But there is something singularity-like about this development.

Individually, the changes do not look dramatic. A model becomes a little better. Memory works a little better. A harness consumes fewer tokens. Embeddings improve. GPUs get faster. Open models move closer to closed ones. One auxiliary model now costs only ten cents per million tokens. Looked at separately, none of these is a major story.

Then the curves multiply. That is the part that is easy to miss. If intelligence improves by 30 percent, reliability by 30 percent, autonomy doubles and cost falls to one tenth, the outcome is not "a slightly better chatbot". It is an entirely different production technology.

Perhaps the beginning of the singularity will not look like a superintelligence waking up one morning in a data centre. Perhaps it will look much more ordinary. Someone notices in their home office that a 27-billion-parameter open model now runs all day on their own GPU, remembers their projects, searches their archives, uses the internet, performs its work autonomously and costs practically nothing beyond electricity. Then the same observation is made in a million other home offices.

At that point, the curve may already be rising. We may simply be standing too close to it to see how steep it is.
