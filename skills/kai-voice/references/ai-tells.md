# AI-tell checklist

Scan pass. Run this against a draft before the final rewrite. Condensed from
Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup), trimmed to the tells
that actually show up in Kai's kind of writing: emails, product copy, docs, posts,
research summaries.

Grep-able trigger words are in `code`. If you find one, look at the sentence.

## Contents
1. Structural tells
2. Word-level tells
3. Punctuation and formatting tells
4. Chat-residue tells

---

## 1. Structural tells

**Significance inflation.** `stands as` `serves as` `is a testament` `marks a
pivotal` `underscores the importance` `reflects broader` `setting the stage`
`represents a shift` `key turning point` `evolving landscape`

> The 2024 launch marked a pivotal moment in the evolution of coaching software.

> Harlen launched in 2024.

**Superficial -ing analysis.** A participle phrase bolted onto the end to fake
depth. `highlighting` `underscoring` `emphasizing` `ensuring` `reflecting`
`showcasing` `fostering` `contributing to`

> The dashboard shows HRV trends, highlighting the athlete's recovery patterns and
> reflecting their overall readiness.

> The dashboard shows HRV trends over the last 30 days.

**Rule of three.** Forced triads. "faster, cleaner, and more reliable." Cut to
one or two, or restructure.

**Negative parallelism.** `not just X, it's Y` `not only ... but also` `not a
tool, but a partner`. Delete the negation, keep the positive claim.

**False range.** `from X to Y` where X and Y aren't on a scale. "from solo
coaches to enterprise teams" is fine; "from data to insight" is not.

**Challenges-and-future-prospects section.** `Despite these challenges`
`Looking ahead` `Future Outlook`. Delete the section. Say the specific problem
and the specific next step, or say nothing.

**Vague attribution.** `Industry reports suggest` `Experts argue` `Observers have
noted` `research shows`. Name the study and the year or cut the claim.

**Elegant variation.** Cycling synonyms for the same noun across sentences
(the coach / the trainer / the practitioner / the professional). Repeat the word.

**Generic uplift close.** `The future looks bright` `Exciting times ahead` `a
major step forward` `this is just the beginning`. End on the last real fact.

## 2. Word-level tells

Delete or replace on sight, unless technically required:

`additionally` `align with` `crucial` `delve` `robust` `seamless` `holistic`
`leverage` (verb) `utilize` `enhance` `foster` `garner` `intricate` `interplay`
`key` (adj) `landscape` (abstract) `pivotal` `showcase` `tapestry` `testament`
`underscore` (verb) `vibrant` `nestled` `boasts` `renowned` `groundbreaking`
`transformative` `empowers` `unlock` `journey` `ecosystem` (figurative)
`comprehensive` `streamline` `game-changing` `cutting-edge` `state-of-the-art`

**Copula avoidance.** `serves as` `functions as` `stands as` `features` `boasts`
→ `is` `has`.

**Filler.**
- "in order to" → "to"
- "due to the fact that" → "because"
- "at this point in time" → "now"
- "has the ability to" → "can"
- "it is important to note that" → delete
- "in terms of" → usually delete

**Hedge stacking.** "could potentially possibly indicate that it might" → "may
indicate". One hedge maximum, and prefer a flat "I don't know" over a soft verb.

## 3. Punctuation and formatting tells

- **Em dash.** Zero tolerance. Comma, period, parens, or rewrite.
- **Curly quotes.** Convert to straight.
- **Title Case Headings.** Sentence case.
- **Bold-header bullet lists.** `- **Speed:** it is faster`. Write prose instead.
- **Emoji** in headings or bullets.
- **Every paragraph the same length.** Vary it.
- **Bold used more than once or twice a page.** Cut most of it.

## 4. Chat-residue tells

Never survives into a deliverable:

`Great question!` `Certainly!` `Of course!` `You're absolutely right` `I hope
this helps` `Let me know if you'd like` `Here's a...` `I'd be happy to`
`As an AI` `As of my last update` `While specific details are limited`
`Based on available information`

Also: an opening sentence that restates the request back to the reader.

---

## Final gate

After fixing everything above, ask literally: **"what still reads like a model
wrote this?"** Name specific sentences. Then rewrite those. The checklist catches
words; this catches rhythm, and rhythm is what gives it away once the words are
clean.
