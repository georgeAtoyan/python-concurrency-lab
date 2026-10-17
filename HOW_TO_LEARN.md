# How to use this lab (so you actually learn)

There are **no solutions in this repo, on purpose.** Copying working code feels like progress, but
the understanding stays with whoever wrote it. This lab is built so the understanding ends up with you.

## The loop for every exercise

```
 1. READ      the exercise README: the problem first, then the idea
 2. PREDICT   write your prediction in LEARNING_LOG.md, then commit it
 3. BUILD     write the code yourself, from the docs, by typing it
 4. CHECK     run the tests: red -> green
 5. RUN       run the experiment and compare numbers with your prediction
 6. BREAK     do the "break it on purpose" steps: predict, run, undo
 7. EXPLAIN   answer the questions in LEARNING_LOG.md in your own words
 8. COMMIT    one commit per exercise, with a real message
```

### Why each step matters

- **Predict before you run.** A wrong prediction is the most valuable moment in the lab: it shows you
  exactly where your mental model is broken. If you never predict, you can't be surprised, and you
  can't learn from surprise. Committing the prediction first keeps you honest.
- **Docs, not answers.** Read the official Python docs linked in each README. Searching for
  "python thread return value" will hand you a solution, and you'll copy it. Reading `threading.Thread`
  docs makes you *derive* it.
- **Type, never paste.** Even when you look at an example in the docs, type it. Your fingers slow your
  brain down enough to notice what each line does.
- **Tests are your teacher.** They tell you *what's wrong* without telling you *how to fix it*.
  Read the failing test's name and its assert message. They're written as clues.
- **Break it on purpose.** Knowing why correct code works is half the knowledge. Knowing exactly how it
  fails is the other half, and it's the half you use when debugging at 2 a.m.
- **Explain it back.** If you can't explain it in plain words, you don't understand it yet. (This is
  also exactly what interviewers check.)

## When you're stuck

1. **Re-read the failing test.** What does it check? What did your code return instead?
2. **Shrink the problem.** Make a 5-line file that tests just the one thing you're unsure about
   (e.g. "what does a thread do with the return value?"). Experiments in a scratch file are the
   fastest way to learn.
3. **Add prints.** Print `threading.current_thread().name` and timestamps. Watch what actually happens.
4. **Stuck for 20+ minutes? Open `HINTS.md`**, one level at a time. Level 1 is just a nudge.
   Only go to the next level after trying again.

## Using Claude (or any AI) as a tutor, not a solver

AI will happily write the whole solution, which is exactly what you don't want. Tell it the rules
up front. Copy-paste prompts that work:

**When stuck on a bug:**
> I'm doing exercise 01 of my Python concurrency lab. I want to learn, so don't give me code or the fix.
> Here's my code and the failing test output. Ask me questions that lead me to find the bug myself.

**For a code review after tests pass:**
> Review my solution like a senior engineer would. Don't rewrite it. Point to specific lines,
> say what's wrong or risky and why, and let me fix it.

**When a concept doesn't click:**
> Explain [the GIL / why join() is needed / what await does] with an analogy, without referring
> to my exercise's solution. Then give me a tiny experiment I can run to see it for myself.

**To check your understanding:**
> Here's my explanation of [concept] from my learning log. Quiz me with 3 questions that would
> expose it if my understanding is wrong.

If the AI starts writing your solution, say "stop, no code" and ask for a question instead.

## Commit messages that tell a learning story

Your git history is part of the portfolio. Write messages a reviewer would enjoy:

```
ex01: predictions for thread speedup
ex01: thread-per-item runner, keeping results in order
ex01: notes, join() inside the loop made it sequential again
ex03: process pool, plus why 20k tiny tasks got slower
```
