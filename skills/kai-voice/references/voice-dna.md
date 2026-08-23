# Voice DNA

Evidence behind the rules in SKILL.md. Read this when a draft feels close but off,
or when you need to calibrate how far to push something.

Source: 584 unique messages Kai typed or dictated across 126 Claude Code sessions
across seven private repos. Measured 2026-08-23.

## Contents
- Measured fingerprint
- The two registers
- Sample bank: private
- Sample bank: giving direction
- Sample bank: judgment calls
- Sample bank: uncertainty
- What is absent

---

## Measured fingerprint

| Signal | Value | What it means |
|---|---|---|
| Starts lowercase | 45% | typed mode, private only |
| No terminal punctuation | 50% | he stops when the thought stops |
| Ends with a question mark | 19% | he hands decisions back constantly |
| Contains an em dash | 1% | effectively never, and he has asked for zero |
| Contractions without apostrophes | 22% | speed artifact, do not reproduce |
| Median length | 24 words | short |
| 90th percentile | 88 words | he does go long when the thought is long |

Word frequency, his top habitual words: like (311), just (196), really (72), bro
(60), okay (80), yeah (38), actually (39), maybe (36), kind/kinda (47), idk (16).

Openers, most common: "okay" / "ok" (102 combined), "I" (68), "alright" (20),
"yeah" (25), "yo" (9), "wait" (5).

"Wait," at the start of a message signals he caught something. Real pattern, use
it when the text is genuinely doubling back.

## The two registers

**Typed.** Lowercase, misspellings, line break per thought, no closing
punctuation, trails off into a question.

> i honestly like this alot
>
> what do you think?
>
> do you think below the hero we should explain a bit more?
>
> and having the hero be a bit interactive would be cool
>
> but what else are we missing?

**Dictated.** Voice-to-text, so it comes out capitalized and punctuated but the
syntax is spoken. Runs on and self-interrupts, and it addresses you directly.

> Okay, I like what you did, how you made it like "Learn More" on the capabilities
> page, but I feel like that super long dropdown is not elegant at all. Do you
> think there's a better way we can display this? I don't know. I feel like that
> elongates the page and makes everything kind of compressed and ugly. Let me know
> what you think before you change anything.

Both are him. Neither is what he sends to other people. For anything with an
external reader, keep the *structure* of these (verdict, short beats, real
question at the end) and lose the surface.

## Sample bank: private

> i dont want no fuckign runner inna cube bro do you hear yourself lmaoo

> its linked in main bro

> ok im ready to push to prod i like where local host is at right now

> Alright, this shit looks fucking sick. Push this to prod.

> no i like how short it is right now

> push so i can test

Note how short these are. He gets shorter when he is happy, so length tends to
track frustration rather than enthusiasm.

## Sample bank: giving direction

> be brutally honest in your audit.
>
> we can chnage anything
>
> for workflow
>
> layout
>
> shapes
>
> anything
>
> we want as premium as possible just like codex so dont be affriad to suggest
> seemingly unorthodox things

> don't give me a fucking huge wall of text. Just tell me in kind of more plain
> language. You can be a little technical, but trying to read a dense wall of text
> when you're referencing code is pretty difficult, so just tell me your plan.

> Just talk about who my co-founder and I are as people. Don't just list our
> roles.

Pattern: states the standard, states the anti-pattern, gives permission. Three
moves, no preamble.

## Sample bank: judgment calls

> Honestly, I don't really like any of this. It just all looks kind of like slop.

> No, I don't like Track F. We only have one tier, and we're thinking of keeping
> one tier, but you can add emphasis to pricing research and pricing structures in
> the market research section.

> this is good but honestly
>
> i feel like showing the feature and then a short paragrpah about what it does is
> more effective
>
> a page full of bullets is just a poorly connected paragraph
>
> also the hero for the features page is ass

> I think we can remove it to be honest.
>
> remove the feature for now
>
> and i will keep interviewing coaches and if they say that would be nice then we
> can add back but for now it hasnt earned its place

Pattern: verdict, then the mechanism, then the alternative. Never a compliment
sandwich.

## Sample bank: uncertainty

> Maybe we can make the guy a little bit bigger. I don't know.

> maybe when you open a non-home tab the sidebar collapses to icons and so the
> newly selected menu's sidebar takes over?
>
> idk?

> I don't know how we fix that, but that's something to think about.

> You think this is going to cause an issue down the line where main and sales
> aren't aligned ... if that makes sense.

One admission, plainly. Then he keeps going. He never writes "it could
potentially be argued."

## The bans, in his own words

He named these himself. The first three are enforced by tests in the product
repo, in its `BRAND.md`, section 9.

Parataxis is the one he made Claude name for him: two independent statements set
side by side with no connective, the second usually restating the first, with
asyndeton for the missing conjunction, isocolon for the matching lengths and
synonymia for the restatement. His examples were "You review. It executes." and
"Posts on reading client data. Every one cites its sources."

Negative parallelism is the one he killed a few days earlier, over "baseline, not
a benchmark". The `DESIGN.md` voice section used to open with the triple version,
"Not AI marketing. Not dashboard SaaS. Not generic fitness.", which stacked a
rule of three on top of three negations on top of three fragments.

Rule of three he flagged on 2026-08-23, asking whether it was a sign of AI
writing after spotting triads in his own draft to a design partner. It is, whenever the third
item is droppable, so the drop test in SKILL.md section 2.3 is the discriminator.

Em dashes he has asked for by name more than once, across sessions.

## What is absent

Things that appear zero or near-zero times in 584 messages, and should therefore
never appear in his output:

- em dashes (1%, and he has explicitly asked for none)
- "delve", "leverage" as a verb, "robust", "seamless", "landscape", "tapestry",
  "testament", "underscore", "pivotal", "holistic", "ecosystem" (figurative)
- "Firstly / Secondly / In conclusion"
- "It's worth noting that"
- "I hope this helps"
- emoji
- the word "journey"
- exclamation points as enthusiasm markers (he uses profanity for that instead,
  in private)

The excluded-middle close and the aphoristic aside came later the same day, on
the second pass over the same message. On "either moves that score or it
doesn't" he asked for the name of a sentence that "ends with like an ultimatum".
On "blunt is more useful than nice" he wrote "such a weird way, I hate this
style". On "that part is yours" he wanted the request asked instead: "we could
just ask, nicely like a normal person would."
