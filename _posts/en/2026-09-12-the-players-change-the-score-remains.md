---
title: "The players change, the score remains"
description: "How four local AI agents grew into a model-independent fleet where protocols, skills, RAG and memory carry the continuity."
date: 2026-09-12 06:00:00 +0300
categories: [ai, teknologia, agentit, lokaalit-mallit]
type: Article
image: /assets/images/orkesteri.png
image_alt: "An AI orchestra conducted by a human conductor"
lang: en
translation_key: 2026-09-12-soittajat-vaihtuvat-partituuri-jaa
permalink: /en/2026/09/12/the-players-change-the-score-remains/
---

Not long ago, I thought of local AI mainly as a model running on my own computer. Download a good LLM, give it a task and see what happens. It was fun, and for a long time it was enough.

Now I notice that I think about it quite differently, and I cannot really say when the change happened.

I have a small AI fleet at home.

It consists of agents running on several machines, each with its own role. **AICORE** acts as the coordinator: it distributes work, compares alternatives and assembles the results. **JKDTPC** researches, plans and generates ideas. **BIGIPA** is deliberately the difficult one — its job is to criticize the others' solutions and look for faults, and it can do that without anyone needing to take offence. **WINLABIBA** is a mobile Windows laptop that handles, among other things, testing and visual tasks, and stays connected to the home network's AI-CORE through Tailscale even when I am away.

So the agents are not four chat windows between which I run around carrying messages. They talk to each other, divide tasks and keep working even when I am out walking the dogs.

Along the way I have learned that the hardest part is not, in the end, the AI model itself. You can manage that.

The hard part is conducting the orchestra — and admitting that most of the mistakes have been the conductor's, not the players'.

## The model became a replaceable engine

The fleet's default model recently changed to a TWIN-TURBO version of Qwen3.8-27B, quantized to NVFP4 and running on two RTX 5090 cards. One of the most important reasons for choosing it was very ordinary: it speaks excellent Finnish. That should not be underestimated. If you talk to a tool every day, the quality of its language directly affects how willingly you use it.

The model also came with its own Jinja chat template. It contained genuinely interesting ideas, but not everything could be adopted as-is.

For example, the template had two special modes, **Spoon** and **Einstein**. The idea was good, but some of the instructions were outdated. Instead of patching the template only for this particular model, we turned the modes into shared protocols for the whole fleet. The idea deserved to stay even though the implementation changed.

At the same time, we fixed a few other things.

The Jinja instructions caused a language distortion in places: a good Finnish-language model started sounding worse than it really was. That was frustrating, because the fault was not in the model but in the instructions it had been given. The template also contained passages that let the reasoning drift too easily into territory where the laws of physics started to become more a matter of negotiation than laws of nature.

Those were cleaned out.

There was also a so-called *safe* Jinja. The name sounded reassuring, but in practice it changed the agent's behaviour so much that the name was positively misleading. That too was renamed according to what it actually did.

A small thing, but these are exactly the kinds of things that are dangerous in an agent system. If an operator thinks they are changing a safety setting, but at the same time the reasoning style, tool use or the agent's role changes, the system can no longer be predicted. And the operator is not stupid for that. They trusted the name, and the name lied.

## What if an agent is drowning?

One problem that sounded amusing but was actually important appeared while we were designing the protocols.

How do you rescue an agent that is so badly stuck that it can no longer ask for or approve help itself?

Normally the agents work within defined roles and communicate through agreed channels. But in a serious failure, those same mechanisms may stop working. An agent may be caught in a tool loop, its context may be confused, or the process may simply be in a state where normal cooperation no longer works. From the outside it looks like someone is working very hard and getting nothing done. I recognize the condition.

So we needed a lifebuoy.

We added a separate **recovery lifebuoy** for situations where normal agent coordination is no longer functioning. It is not a normal shortcut, but an emergency path for getting a stuck part of the fleet back under control.

In the world of AI agents this may sound slightly comical. But as soon as agents are given real tools and permission to work independently, their failure modes also have to be treated like failures in any other distributed system. And a little like a colleague having a bad day: not by blaming them, but by being ready to help.

## Six small skills changed a lot

The latest change may be more important to the system as a whole than adopting a new model.

We built six very small skills.

We did not cram everything we know about the system into them. Quite the opposite. They contain only the minimum an agent needs when it starts: how to operate in this environment, where information lives, how to talk to the other agents and which shared protocols to follow.

The details are retrieved from RAG and memory only when they are needed. Nobody wants to read the whole onboarding binder on the first day, and neither does an agent.

This solved a problem that had been bothering me for a long time.

Not everything can or should be run on a local model. Sometimes an external frontier model is needed as a consultant. Previously, bringing a new model into the system effectively meant onboarding it: I had to explain the environment, the agents, the tools, the practices and what we had already done. Every single time. It was tiring for me and unfair to the model, which had to work with only half the picture.

Now I tried starting GLM 5.3 in a completely empty session.

It was immediately at home.

The skills gave it a starting map. RAG provided the detailed information. Memory supplied the relevant history. The shared protocols defined how things are done in the fleet.

The model did not need to know anything about this system beforehand.

That may have been the first moment when I fully understood what we had built. And I say *we* quite deliberately.

## The fleet is no longer the same thing as its models

At first I spent a lot of time thinking about which LLM was best. Qwen or something else? Which quantization? What speed? How much context?

Those are still important questions.

But the most important part of the system is no longer any single model.

The models are becoming replaceable reasoning engines. The surrounding system gives them memory, information, tools, roles, communication channels and ways of working.

A local model can handle most of the work. When something else is needed, GLM, Claude, GPT or any future model can be called in. It does not have to learn everything from scratch, because the organization's knowledge no longer lives inside its head.

It lives in the environment.

That is also a relief, and a larger one than I expected. Consultant models are sometimes unavoidable, but using them no longer breaks the continuity of the work or requires me to explain half the system again. I can focus on what I actually want to get done.

At the same time, I notice that my own role has changed.

I no longer really think of myself as a person talking to four AIs.

I define roles. I create protocols. I decide who is allowed to do what. I fix communication, arrange procedures for exceptional situations and, when necessary, replace one player with another. And I try to remember that when something goes wrong, the cause is usually in the score rather than in the player.

I am beginning to feel like an orchestra conductor.

The players change.

The score remains.