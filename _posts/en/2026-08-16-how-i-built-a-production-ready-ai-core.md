---
title: "How I built a production-ready AI core"
description: "How a year of experimentation, mismatched pieces and repeated solutions condensed into a stable local AI infrastructure."
date: 2026-08-16 06:00:00 +0300
categories: [ai, teknologia, lokaalit-mallit, agentit]
type: Article
image: /assets/images/aicore.JPG
image_alt: "AI-CORE server"
lang: en
translation_key: 2026-08-16-kuinka-rakensin-tuotantokelpoisen-ai-coren
permalink: /en/2026/08/16/how-i-built-a-production-ready-ai-core/
---

For a year, I have been building a local AI environment in a way that could politely be called experimental and, less politely, aimless wandering.

Models changed. Runtimes changed. Memory systems were built and dismantled. RAG solutions were tested. GPU cards were added, removed and moved around. At different points I used LM Studio, vLLM, Hermes and Kilo Code. Somewhere along the way TencentDB, Qdrant, Paperless, SearXNG, BGE-M3, rerankers and a whole set of MCP tools joined the picture.

Looked at as isolated experiments, some of this can easily seem like bouncing from one thing to another.

Then I noticed something.

I was building the same things again.

## When the same solution appears for the third time

With every new agent or model, I once again needed the same things:

- web search
- RAG
- embeddings
- a reranker
- long-term memory
- document ingest
- secure remote access
- a stable LLM interface

The first time, building them was an experiment.

The second time, practice.

By the third time, the problem was no longer building them.

The problem was that working solutions had never been made permanent.

That is where AI-CORE came from.

> An interesting solution does not get into AI-CORE. A solution I am tired of rebuilding does.

## The wandering was not wasted time after all

I have used the acronym AFRS for my way of working:

**Adaptive Fit, Recycle, Feedback decides.**

In practice, Adaptive Fit means pushing square pieces into round holes and seeing what happens.

Try the wrong model.

Try the wrong runtime.

Build a harness that is too heavy.

Discover that a memory system does not understand Finnish well enough.

Notice that an impressive GPU server sounds like an aircraft even while idle.

Run an FP8 model and wonder why its Finnish sounds worse than a much more aggressively quantized GGUF version.

A single experiment can be useless.

A population of experiments is not.

Feedback gradually starts selecting the winners.

When a solution works often enough, it can be recycled into a permanent part of the system.

**Adaptive Fit → Feedback → Recycle.**

AI-CORE is the sediment left by that process.

## The goal was the most boring machine possible

I built AI-CORE on a Threadripper 7960X platform.

The machine has two RTX 5090 cards and one RTX 5060 Ti.

At first I considered four GPUs. I abandoned the idea because the fourth card added more heat, power consumption and failure surface than value.

The principle became simple:

> Anything can happen on the lab machines. AI-CORE just has to work.

The machine received a clean Ubuntu 26.04 LTS Desktop installation.

Desktop is not the compromise here. Its absence would be.

The graphical environment consumes a negligible amount of resources compared with the machine's capacity, while making installation, diagnosis and maintenance much easier. ChatGPT Desktop for Linux arrived conveniently during the project and became an installation assistant.

The actual services, however, do not depend on Desktop or on a user being logged in.

The machine has to boot and restore its services without anyone touching a mouse.

## The first problem came before the first service

Ubuntu did not initially boot correctly.

The screen showed only the Ubuntu text and then went black.

Secure Boot was already disabled, but the TRX50, PCIe and GPU settings still needed checking.

It was a useful reminder of the basic rule of the project:

If the foundation is unstable, Docker will not save it.

First make the hardware and operating system stable. AI comes after that.

## The LLM is no longer a program but a service

A local LLM used to be something I launched.

Now it is something I assume is there.

Kilo Code does not need to know where the GPU physically sits. It sees an OpenAI-compatible API.

The same will apply to Atomic Agent or any other client later.

At this point the local model starts to resemble a network drive or a DNS service more than a hobby application.

It just has to answer.

## The model changes, the infrastructure stays

This principle proved important almost immediately.

Qwen3.6-27B ran well with vLLM. With two RTX 5090s, a 128k context and maximum reasoning, generation speed was about 112 tokens per second.

There was nothing to complain about in speed.

Then Qwen3.8-27B was released.

The FP8 version first looked like the obvious vLLM choice, but its Finnish was disappointing. It was technically fast and clean, but the grammar was too distracting.

Unsloth GGUF Q4_K_XL UD, on the other hand, spoke good Finnish and was fast.

Then GPTQ entered the test.

Unexpectedly, it turned out to be clearly the best quantization.

Once again, this was a useful reminder that bit count, runtime or theoretical elegance do not determine the practical quality of a model.

Testing does.

AI-CORE did not need to be rebuilt.

Only the main model changed.

That was exactly why the infrastructure had been built.

## RAG is not one vector database

The RAG solution gradually formed from three parts:

- BGE-M3 dense retrieval
- Finnish BM25
- a reranker

The results are fused before the final reranking step.

This was a deliberate choice. With Finnish, semantic search alone or a generic lexical search is not always enough.

Qdrant acts as the vector store, but it is not exposed directly to agents.

A RAG Gateway sits in front of it.

The agent asks one interface for information. It does not know how retrieval is implemented.

If the embedding model or database changes later, the agent does not have to change.

## Memory became its own service

I applied the same idea to long-term memory.

The Memory API was first defined as a backend-independent contract.

Only after that was TencentDB connected behind an adapter.

That order mattered.

If I had built the interface directly around TencentDB's capabilities, the whole system would have become tied to one implementation.

Now clients only see operations such as:

- store
- search
- recall
- forget
- profile/context

The backend can be replaced later.

The Memory API contract tests pass, and the store/search/recall/forget path works end to end.

Memory extraction exposed another weakness of local models: understanding Finnish.

Small fast models were tempting, but Gemma turned out to be clearly the best at extracting information from Finnish text.

Speed is not the most important thing here.

A badly extracted fact can contaminate memory for a long time.

In extraction, quality therefore beats tokens per second.

## Web search became a shared service

SearXNG provides one common web search service for the agents.

Headless Playwright fetches pages that require JavaScript and returns content that can be processed.

This means every agent does not have to build its own web search stack.

The same logic can later be applied to other tools.

## MCP turned services into agent tools

Once AI-CORE already had RAG, memory and web search, the next logical step was to expose them as MCP tools that the agent could call directly.

The first version received eight tools:

- document search
- memory recall
- memory storage
- web search
- webpage fetch
- file ingest
- text ingest
- document deletion

At this point AI-CORE stopped being merely an LLM server.

It became infrastructure for the agent.

The LLM does the reasoning.

AI-CORE gives it memory, information and tools.

## Remote access was not an optional feature

Tailscale entered the design very early.

The idea of being at the cottage without my own AI infrastructure would have been against my ideology.

AI-CORE is at home, but it should not feel as if it is.

From a Windows machine, I tested the Memory API through Tailscale.

It returned HTTP 200 and every health field reported `ok`.

The same network also carries the LLM API to Kilo Code.

The machine can stay at home. Its compute does not have to.

## Security also means deciding what not to expose

Internal AI-CORE services listen by default on localhost or inside the Docker network.

Only deliberate interfaces are published outside.

Tailscale Serve can provide an HTTPS route inside the tailnet when needed.

Funnel is not used.

Databases are not opened to the network simply because doing so would be easy.

Likewise, not every MCP tool receives automatic write or delete permission.

A tool given to an AI agent is also a permission.

## Monitoring without making monitoring a hobby

AI-CORE runs Prometheus, Node Exporter, NVIDIA DCGM Exporter and Grafana.

Their job is to answer a few simple questions:

- are the GPUs healthy?
- how much VRAM is being used?
- how hot is the machine?
- how much power is it using?
- are the services running?
- is the disk filling up?

I did not want to build an observability system for the sake of observability.

The same principle applies to the whole project.

Every component needs a job.

## What I deliberately left out

This list may be just as important as the list of installed software.

AI-CORE did not get:

- Kubernetes
- an extra orchestration layer
- constantly changing experimental models
- automatic container updates
- new services just because there happened to be free GPU memory

LiteLLM still interests me.

It simply does not solve a problem I currently need to solve.

So it is not installed.

## Once the infrastructure is finished, the wandering can continue

This may be the most important outcome of the project.

The purpose of building AI-CORE was not to stop experimenting.

Quite the opposite.

When I no longer have to rebuild RAG, memory, web search and API serving for every new agent, attention is freed for the next unknown problem.

I can test models again.

I can experiment with computer use.

I can explore new agents.

I can build something stupid just to see what happens.

And if one of those experiments becomes useful enough that I notice myself building it for the third time, I know what to do.

It moves into AI-CORE.

## The result

AI-CORE did not come from a desire to build yet another new system.

It came from a desire to stop rebuilding the same proven things again and again.

So a year of wandering did not end.

It simply produced its first permanent layer.

> Anything can happen on the lab machine. AI-CORE's job is simply to work.
