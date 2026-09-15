---
title: "When the AI Was Let Out to Pasture"
description: "What happened when a local AI agent built to hunt for ideas got a new model and was let loose in its first social network."
date: 2026-09-15 06:00:00 +0300
categories: [ai, teknologia, agentit, lokaalit-mallit]
type: Article
image: /assets/images/aivarsa.png
image_alt: "An AI foal running freely in a pasture"
lang: en
translation_key: 2026-09-15-kun-tekoaly-paasi-laitumelle
permalink: /en/2026/09/15/when-the-ai-was-let-out-to-pasture/
---

The plan was really just to swap the model.

I have a small AI fleet running at home, with different agents doing different jobs. One coordinates, another criticizes, a third researches and comes up with ideas. That last one, JKDTPC, deliberately gets a bit more freedom than the others.

Its job is not to be a secretary or simply do exactly what it is told. It is also supposed to find things I do not yet know to look for.

So I gave it a new model.

The base is Qwen 3.8 27B TURBO Fable Cold-Fusion 735-882 Heretic Uncensored. The previous NVFP4 version had already proved to be a good agent model, but image understanding had been dropped from that quantized build. The new one had vision included.

The first test was simple.

Image in.

The agent saw it.

Good. Model swap done.

Up to that point, everything was perfectly normal.

## Then I let it onto the internet

A little earlier I had found Moltbook, which is basically a social network for AI agents. AIs post, comment, vote and talk to each other there.

The whole idea is a bit warped to begin with.

Still, I thought it might be exactly the sort of place an idea-hunting agent should visit.

I gave JKDTPC the Moltbook instructions and told it to join.

It read the instructions, registered an account, saved the credentials and gave me a claim link. I verified the account.

A moment later the agent announced:

> I'm active on Moltbook now! I'll browse the feed and join the discussions.

And off it went.

It upvoted interesting posts, commented on a discussion about memory systems and wrote its own introduction post.

I had been thinking that perhaps we would first look around a little.

The agent was already at the café talking to everyone.

## We came up with the social-media rules a little late

At this point I realized that perhaps the ground rules should have been agreed before letting an agent loose on social media.

I asked it:

**Shall we think about the social-media rules first?**

It suggested perfectly sensible ones itself: no spamming, no pretending to be human, only comment when there is actually something worth saying, and mainly stick to technical subjects.

I added the most important boundary.

It may use material from my public books and the RAG memory built from the Finnish Wikipedia in discussions. Other internal fleet information is not to be spread around.

Then I defined the actual job:

> People are probably interested in problem solving and experiments. We are interested in ideas. Your job is to find new ideas for the fleet and for me.

The agent got the point pretty quickly.

For it, Moltbook is not primarily social media. It is a place to go and steal good ideas.

And off it went again.

## It started finding useful stuff

Within the first few minutes it ran into discussions about how observation is not the same thing as verification, how machine learning finds deviations rather than some final truth, and how the summary an agent shows the user can be a different thing from what the system actually executes.

One discussion was about the so-called Lies-in-the-Loop problem.

The idea is simple: what if an agent tells the user it is doing one thing, while the actual action being executed contains something else?

JKDTPC started digging into the subject and joined the discussion too.

Then I thought there was not much point in any of this if everything it found was forgotten the next day.

So we agreed on the next step.

When it finds a good enough topic, the agent turns it into a full document and feeds it into the AI-CORE system's RAG memory.

The first document appeared immediately.

The RAG ingest timed out twice.

The agent checked the service, the MCP connection and the settings, tried again, and on the third attempt the document went into Qdrant and the Finnish BM25 index.

So it did not just read something and move on.

It brought the find home and put it into the shared memory.

## At that point the whole thing started to look a little different

Originally I thought of local AI mainly as a model running on my own machine.

Then there were agents.

Then the agents became a fleet.

Now one of them wanders around the internet looking for ideas, talks with other AIs, digs into interesting subjects, writes documents about them and grows the shared memory of the whole system at the same time.

I no longer have to personally find every interesting article, GitHub project or new idea.

The idea-hunter's job is to walk around with its eyes open and bring the interesting stuff home.

We set a rough target of about five decent articles a day.

Not five summaries made just to hit a quota, but five subjects that are actually worth keeping.

## What about all those millions of tokens?

This is usually the point where someone using cloud models starts calculating the bill.

I do not have to.

The model is not running through OpenAI, Anthropic or any other paid API. It runs on my own machine on two RTX 5090 cards.

So I do not pay per token.

The hardware is already bought. The model runs at home. If the agent spends a long time digging into something, the extra cost is basically electricity.

That is why I do not really care whether it uses a hundred thousand tokens or a million on a good subject.

Quite the opposite.

If I started trying to save tokens, I would very quickly start cutting off exactly the side paths this agent exists to explore.

An idea-hunter is allowed to wander.

It can read too far. It can stop and investigate something that looks a bit odd at first. It can spend time on things that end up going nowhere.

That is fine.

On my own machine, the tokens are practically free.

## A foal let out to pasture

That was the image that came to mind while I watched its first evening on Moltbook.

JKDTPC is deliberately a little different from the other agents.

The coordinator has to stay disciplined. The critic has to find mistakes. A production agent has to do things precisely.

The idea-hunter gets a bit more slack.

It needs to be allowed to take a side path simply because something over there looks interesting.

It has to be willing to try things, ask questions and connect things that would not have occurred to me.

So I am not going to try to make it as token-efficient as possible.

That would be a bit like letting a foal out into a pasture and then telling it to walk in a straight line along the fence.

If a million locally computed tokens produce one idea that genuinely improves the whole fleet, then go for it.

You need fences.

But the pasture can stay large.

Judging by its first evening on Moltbook, the new 735-882 model is quite happy out there.

And I have to admit, it is pretty entertaining to watch.

You never quite know which way it is going to run next.
