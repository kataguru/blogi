---
title: "When the model runs out of memory halfway through the task"
description: "In a long agent task, the conversation context is not a reliable project memory. A local model needs a process around it that preserves goals, verifies the work, and helps carry the task to completion."
date: 2026-07-31 06:00:00 +0300
categories: [artificial-intelligence]
lang: en
translation_key: 2026-07-31-kun-mallin-muisti-loppuu-kesken-tyon
permalink: /en/2026/07/31/when-the-model-runs-out-of-memory/
---

Lately I have been running local language models inside the Hermes agent's coding harness. The goal has not been a scientific model comparison, but a practical experiment: to find combinations that can use tools, follow instructions, and build a complete working application from start to finish.

One observation has repeated often enough that I am willing to write it down.

In a long task, the conversation is not a reliable project memory. Because it is not, the model needs something around it that is.

## Context is not the same as memory

A language model has a limited context window. When the conversation, tool outputs, source code, and error messages fill it, older content has to be removed or compressed.

Compression sounds like harmless maintenance, but it is a lossy process—and what disappears is often exactly what completing the task requires.

The broad outline usually survives: what is being built, which technology is being used, which modules exist, and roughly where the work has reached.

The small but binding details tend to weaken first:

- the user's exact requirements
- agreed boundaries
- misunderstandings that were corrected earlier
- the reasons behind technical decisions
- open errors
- knowledge of what was actually tested
- the acceptance criteria that determine whether the work can be called complete

The insidious part is that the model can continue working quite convincingly even after its understanding of the original task has quietly changed.

It does not feel that it has forgotten anything. It has no mechanism for noticing that its memory has degraded, because the degraded version is now its entire truth about the task.

## Memory outside the conversation

The solution is simple in principle: an important task should not live only in the conversation.

I have settled on four project files with deliberately different roles and lifecycles.

**`TASK.md`** is the immutable source of truth for the task. It contains the goal, mandatory requirements, boundaries, acceptance criteria, explicit user instructions, and assumptions made at the beginning.

**`PLAN.md`** is the implementation plan: modules and their responsibilities, implementation order, dependencies, technical decisions, testing methods, and module status.

**`FINDINGS.md`** contains the research: information found in documentation and web searches, experimental observations, sources, rejected alternatives, and the evidence behind technical decisions.

**`STATUS.md`** describes the actual current state: completed parts, tests that were run and their results, open errors, known limitations, and the next concrete action.

When the context is compressed, the model does not have to reconstruct the situation from a fragile conversation summary. It reads the files again and continues from them.

The most important detail is not that the files exist, but that `TASK.md` is protected.

The model must not be allowed to rewrite it continuously. The reason is the same one that caused the problem in the first place: if the model updates the source of truth using its current—already partly degraded—understanding, it does not repair memory. It transfers the distortion into the file.

External memory helps only if it is protected from the same lossy process that consumed the context.

In practice, the division is clear:

- `TASK.md` says what is being done and why
- `PLAN.md` says how the work is intended to be done
- `FINDINGS.md` says which information and observations support the decisions
- `STATUS.md` says where the work actually stands

The changing work state must not overwrite the original task.

In the Hermes skill I built, `TASK.md` can also be locked with a SHA-256 checksum. If the file changes unnoticed later, the agent can detect the mismatch before continuing.

## Finish one module at a time

A second recurring observation concerns scope.

A language model easily tries to build the entire system at once. It creates folders, files, a user interface, data models, and a large set of features. The result looks impressive, but much of it remains half finished.

A better principle is more selective:

> Complete one module carefully before moving on. It is better to leave some modules entirely unimplemented than to leave everything unfinished.

After each module, the agent should:

1. reread the original task
2. check the module against the requirements
3. run the module's own tests
4. run the necessary regression tests
5. verify that earlier functionality still works
6. inspect the visible result with vision when needed
7. fix the problems it finds
8. update the plan and project status
9. only then move to the next module

Visible progress becomes slightly slower, but later repair work falls sharply. In total, this is almost always the faster route to a finished result.

## The model must also know how to continue

A good harness is not enough by itself.

Agent work requires properties that an ordinary chat test does not reveal:

- the model must not stop at the first error
- it must follow the instructions
- it must use tools in the right order
- it must read the error message before attempting a fix
- it must verify the result
- it must know when the task is genuinely complete

I have used KAT-Coder, for example, and it has worked well in Hermes. It follows instructions and progresses systematically.

Its major limitation is the lack of vision.

Without vision, the model may verify that a user-interface element exists in the DOM and that the test passes. It cannot see that elements overlap, text disappears into the background, or the game still looks unfinished.

This is a familiar trap: the model verifies its work against an intermediary—the DOM or a test result—instead of checking what the user actually experiences.

When a metric becomes the target, it stops measuring the right thing.

A multimodal model can close this loop, at least in principle, because it can inspect its own work in the same image the user sees.

**Estimate:** current local vision models are still unreliable at judging fine-grained layout, so this is a direction rather than a solved problem.

Even so, this requirement—that one model on a single 32 GB graphics card handles planning, coding, tool use, testing, debugging, and screenshot review—narrows the model selection far more than any single coding benchmark.

## Web search improves planning

One change that clearly improved the results was adding search capability to the harness—and, above all, instructing the model to use it during planning rather than only after an error.

The model no longer has to invent everything from memory. It can check:

- current documentation
- the present interfaces of libraries
- known problems
- established implementation patterns
- correct settings
- existing solutions

A design error is expensive. A syntax error discovered later is usually cheap.

Search moves the emphasis in the right direction.

It is not free of bias, however. The first search result is not the same thing as the correct architecture, and a weak model can anchor itself to a popular but poor solution just as confidently as it previously anchored itself to its own guess.

Search reduces the risk of building on outdated information, but it does not remove the need to evaluate what was found.

The findings must also be written to persistent memory. Otherwise, the time spent reading documentation disappears during the next context compression.

In the process I built, the agent is reminded to record important observations in `FINDINGS.md` during the research, not only at the end.

## Local does not automatically mean cheaper

For comparison, I tested OpenAI's inexpensive Luna model inside Hermes.

I asked it to build a chess game. It produced a completely working game whose opponent played at roughly high-school level. The only significant refinement concerned the colors.

The run used about three percent of a €20 weekly allowance. The price of one working chess game was therefore about €0.60.

That is an important reference point.

A local model cannot be justified only by saying that a commercial model costs money. If the commercial model produces a finished application for less than one euro, token cost is not the real problem.

An honest total-cost calculation also shows that local inference is not free. Its real price is not expressed in tokens, but in hardware depreciation, electricity, and above all the time I spend building the harness and tracing failures.

For a hobbyist, that time is the whole point rather than a cost. In production, it would dominate the calculation.

The real advantages of a local model lie elsewhere:

- independence from a service provider
- privacy
- unrestricted experimentation
- the ability to modify the entire harness
- private memories and tools
- predictable availability
- the ability to study model behavior without watching a token meter

A commercial model also provides a useful reference level. Without one, it is difficult to know what better performance is actually worth.

## Harnesses help every model

A good agent harness narrows the gap between a local and a commercial model.

It provides the model with:

- persistent project memory
- search tools
- a browser
- a terminal
- automated tests
- screenshots
- staged work
- mandatory checkpoints
- a clear completion criterion

A weaker model benefits proportionally more because the harness reduces its memory load and forces systematic work.

The same tools also help a strong commercial model. It generally uses them more effectively and requires fewer correction rounds.

The harness therefore does not remove the differences between models. It raises the level of the entire system.

## The idea was not new

After outlining my own file-based process, I started looking for someone who had already reached the same conclusion.

Someone had.

I found the `planning-with-files` skill, which uses separate planning, findings, and progress files during long agent tasks. It also included a Hermes adapter capable of restoring project state into the model's context.

The discovery was both slightly embarrassing and encouraging.

Embarrassing because I had spent time rediscovering an already solved problem.

Encouraging because practical experimentation had independently led to almost the same architecture.

The existing solution was not quite what I needed, however. I combined its principles with my own process and built a new skill for Hermes.

It includes:

- an immutable, checksum-protected `TASK.md`
- a separate `PLAN.md`
- a `FINDINGS.md` that preserves research
- a `STATUS.md` that tracks the real state
- automatic context restoration
- module-specific testing gates
- vision review for visible outputs
- a three-attempt recovery process for errors
- a completion gate that verifies the requirements before the task can be declared complete

This process can still fail if the model does not follow it. A harness cannot force a weak model to reason correctly.

It can, however, make the correct behavior easier and the wrong behavior harder.

That is often enough to make a meaningful difference.

## A model card does not describe usability

Some promising models have proved good in practice, while others have been disappointing despite impressive measurements.

Laguna S 2.1 has so far been a poor experience:

- instruction following has been unreliable
- agent work has wandered
- results have varied
- Finnish has been weak

The community believes the model's worst technical problems can be fixed quickly, and that may well be true.

Weak Finnish is a different issue.

When the task descriptions, memory files, and reports are in Finnish, language ability directly affects whether the model:

- understands nuance
- preserves boundaries
- interprets instructions correctly
- is pleasant to work with

**Estimate:** this is not accidental. Finnish is a low-resource language for language models, and instruction following can weaken in low-resource languages even when the model is strong in English.

A coding model is also a user interface.

If I constantly have to switch languages or correct misunderstandings, usability falls quickly—and no model card measures that.

## Speed is not the only metric

On one 32 GB card, I currently get a context of about 170,000 tokens at roughly 55 tokens per second.

The speed is not ideal, but it is not the main problem. What matters more is what the model does with the time.

Even a fast model can be slow in practice if it:

- wanders
- forgets requirements
- stops working
- fixes the wrong thing
- has to repeat the same work

A reliable agent at 55 tokens per second may finish before such a model.

To be precise, this does not mean speed is irrelevant. With reliability held constant, higher throughput is always better.

The important point is that when speed and reliability conflict, reliability determines the total time to a finished result.

With local models, the choice is rarely between a very fast model and an equally reliable one. More often, the options are slow but systematic or fast but wandering.

Then the choice is easy.

## The model is not the whole system

Local language models are often compared as if they were independent products.

In agent work, the result comes from the whole system:

- the model
- quantization
- context
- memory
- tools
- search capability
- the working process
- testing
- vision
- the harness's ability to recover from errors

This creates an awkward fact for benchmarks: they measure the model alone, while the agent result is a joint property of the model and the harness, for which no established metric exists.

A good model can fail in a poor harness.

A slightly weaker model can surprise in a good one.

The most interesting discovery may therefore not be the best individual model. It may be a working method that helps several different models do better work.

And in long tasks, the most important of those methods may be the simplest one:

Do not trust the model to remember.

Write the important things to files.

And make sure it does not rewrite the original task.
