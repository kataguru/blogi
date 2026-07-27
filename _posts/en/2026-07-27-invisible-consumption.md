---
title: "Invisible consumption: how an LLM agent can increase your API bill without active use"
description: "A background loop in an LLM agent can consume millions of tokens per day. Here is how to identify the leak and contain the cost risk."
date: 2026-07-27 06:00:00 +0300
categories: [artificial-intelligence]
lang: en
translation_key: 2026-07-27-nakymaton-kulutus
permalink: /en/2026/07/27/invisible-consumption/
image: /assets/images/vuoto.png
image_alt: "An illustration of invisible consumption and leaking resources"
---

An LLM agent does more than answer questions. It can use tools, read files, run commands, and continue working on the same task through several consecutive model calls. Claude Code, Codex, and similar agents do work that the user interface reveals only in part.

That is precisely what makes an agent powerful—and harder to monitor than a conventional chatbot. A single visible answer can conceal dozens of model calls.

If an agent gets stuck in a loop, a background task runs too often, or an automation makes unexpected calls, tokens can be consumed even when nothing appears to be happening in the interface. With a local model, the main cost is electricity. With a paid API, every billable token increases the invoice—potentially by hundreds or thousands of euros per month.

## An observation: more than 3,000 tokens per minute

The following observation comes from a **local LM Studio environment**. It did not produce any billable tokens, but it reveals exactly the pattern that would start costing money with a paid API.

The user noticed that the generated-token counter in the log kept increasing without a visible conversation:

```text
n_decoded: 36,204 → 38,056
Time: 36 seconds
```

The difference is 1,852 tokens. That is roughly 51 tokens per second, or more than 3,000 tokens per minute. The model was *generating* even though the user did not expect it to.

If we assume—as a purely mathematical worst case—that the same rate continued without interruption:

- about 185,000 tokens per hour
- about 4.4 million tokens per day
- about 133 million tokens over 30 days

The assumption of uninterrupted generation for 24 hours is deliberately crude. A real agent run includes pauses, errors, and waiting. These figures are not a forecast; they show the order of magnitude. A small continuous leak scales into a large one quickly.

The log observation alone does not reveal *which* process produced the tokens. It still tells us something essential: the model server received generation work that the user had not requested.

## What would continuous generation cost through an API?

API prices are usually quoted in dollars per million tokens. Input, output, cache, and reasoning tokens can have different prices, so the exact cost depends on the structure of the calls.

For a simplified example, assume 4.4 million billable **output tokens** per day. Based on output prices anchored to Anthropic's current models in July 2026, the cost would look like this:

| Output price / million tokens | Example model | Per day | 30 days |
|---:|---|---:|---:|
| $5 | Haiku 4.5 | about $22 | about $660 |
| $10 | Sonnet 5 introductory price | about $44 | about $1,320 |
| $15 | Sonnet 5 standard price | about $66 | about $1,980 |
| $25 | Opus 4.8 | about $110 | about $3,300 |
| $50 | Fable 5 / Mythos 5 | about $220 | about $6,600 |

This table is illustrative, not a live price comparison. The actual bill is often **higher**, because on every round the agent may send back conversation history, file contents, and tool results. You pay for the input side as well, not just the output.

Example prices in July 2026: Opus 4.8 costs $5 / $25 for input/output, Sonnet 5 has an introductory price of $2 / $10 (standard pricing of $3 / $15 from September 1, 2026), Haiku 4.5 costs $1 / $5, and the Mythos-class Fable 5 costs $10 / $50 per million tokens. For comparison, output from the older Opus 4.1 generation cost $75 per million tokens, so the present ceiling is clearly lower. Caching and batch processing have their own prices. **Always check current prices with the provider.** [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing)

The same principle applies to other providers. Google, for example, explains that agent billing may include input, output, and reasoning tokens as well as intermediate stages in agent loops. [Gemini API pricing](https://ai.google.dev/gemini-api/docs/pricing)

## What causes background consumption?

### 1. The agent gets stuck in a tool loop

An agent may keep retrying the same unsuccessful step:

1. the model decides to call a tool
2. the tool returns an error or an ambiguous result
3. the result is sent back to the model
4. the model tries almost the same action again

Every round may contain a new model call and much of the previous context. In the interface, this may simply look like a slow or frozen task.

### 2. A scheduled task runs too often

A cron job or another scheduler may create a report, run a check, or synchronize data every minute when it was meant to run once a day. One run can be cheap. A task repeated hundreds or thousands of times per month may not be.

### 3. A finished task starts again

A faulty automation may interpret an incomplete state as new work. The agent then starts the same task again and again without an external request.

### 4. A long context is sent on every round

Alongside conversation history, an agent may include large files, log output, or tool responses in its request. Even a short answer can then require processing an enormous input context.

Consumption does not always show up as generation speed. An agent can also spend a great deal by repeatedly reading the same context.

### 5. An MCP integration initiates agent work

An MCP server does not usually consume LLM tokens merely because it is connected. Costs arise if the agent or its host application calls the model to discover or select tools, or to interpret their results.

The more integrations an agent has, the more important it is to monitor when they are called, what triggers the call, whether results are returned to the model, and whether numerical limits have been configured.

### 6. Automatic model discovery misbehaves

Some applications automatically retrieve the available model list from a provider's `/models` endpoint. A normal model-list request does not generally generate billable LLM tokens by itself.

If you observe continuous requests or model reloads in connection with a `discover_models` setting, disable automatic discovery during testing. Do not assume its effect is universal: it depends on the agent, provider, and software version.

### 7. An open interface keeps a process active

A WebSocket connection or an open browser tab does not normally consume tokens on its own. The interface may, however, perform automatic polling, status updates, or task continuation that triggers model calls.

The important question is not whether the connection is open, but whether it sends new generation requests.

## Why is this easy to miss?

**Lack of visibility.** An agent can display one task or session while running dozens of model calls inside it.

**Billing delay.** The credit-card bill arrives later, and provider usage reports may also update with a delay.

**Distributed costs.** Agent work may include input, output, and reasoning tokens; cache writes and reads; tool or search fees; and calls to several different models. One visible answer therefore does not necessarily correspond to one API call.

## Checklist for users of paid APIs

### Before starting an agent

- Configure spending and budget alerts in the provider dashboard.
- Use a separate API key for every agent or project.
- Set the smallest practical usage limit for the key.
- Review all scheduled tasks.
- Disable unnecessary integrations and automations.
- Limit the number of tool rounds and retries.
- Test the configuration with a local or less expensive model first.

### During use

- Monitor tokens per request, not only per session.
- Watch API request counts and timestamps.
- Pay attention to continuous GPU, CPU, or network load.
- Check the agent's own cost view if it has one.
- Make sure the stop command also terminates the background process.

### If consumption continues without active use

1. Interrupt the agent task or close the session.
2. Stop the agent server process if necessary.
3. Revoke or rotate the API key if you cannot reliably stop the traffic.
4. Inspect the provider's usage log.
5. Look for recurring patterns in timestamps, model names, and identifiers.
6. Re-enable features one at a time until you find the cause.

Closing the interface is not enough if the agent, scheduler, or server continues running in the background.

## A local model is a good test environment

LM Studio and Ollama are particularly useful for detecting problems like these. In a local environment, a faulty loop does not produce an API bill, although it still occupies the GPU, loads the CPU, and consumes electricity. The same fault that can be found safely on a local machine would have cost money in the cloud.

| Feature | Local model | Paid API |
|---|---|---|
| Direct token cost | Usually none | Billed according to use |
| Main constraint | GPU, memory, and speed | Budget and usage limits |
| Result of a faulty loop | Wasted computing resources | A potentially large bill |
| Suitability for testing | Very good | Use strict limits |

A local test still does not reveal every cloud cost. With an API, a long input context, reasoning tokens, and external tools may account for a large share of the bill.

## The most important safeguard is not one setting

Disabling one setting—such as automatic model discovery—may solve a problem in a particular software version. It does not protect against agent loops, overly frequent schedules, or huge contexts.

Reliable protection is layered:

- a low spending limit
- automatic budget alerts
- per-request logging
- a limited number of agent rounds
- separate API keys
- a clear way to stop every background process

## Finally

The cost risk of an LLM agent does not arise because the agent is inherently dangerous. It arises because the agent can do much more than its interface shows.

At roughly 51 tokens per second, a continuous process would produce more than four million tokens per day. With a low-cost model such as Haiku 4.5 at $5 per million output tokens, that already means hundreds of dollars per month. With a top-tier model such as Fable 5 at $50 per million, the figure is about $6,600. At the older Opus 4.1 output price of $75, it would have been close to $10,000. The difference shows why model choice alone can change the order of magnitude of the risk.

Do not leave an agent using a paid API unattended until three things are in place: **consumption is visible, usage is limited, and the process can be stopped reliably.**

*Prices and model lineups change quickly. Always check the current input, output, reasoning, cache, and tool prices in your provider's own pricing documentation.*
