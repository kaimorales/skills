# Failure modes

Findings from the trace eval Kai ran on 2026-08-23, annotating a message this
skill drafted to a design partner. Roughly thirteen spans were
flagged. Read this before drafting anything, because these are the failures the
skill itself produced.

## Contents
- The headline: provenance is not a defense
- The additive trap
- The eight modes
- What survived

---

## The headline: an input draft is not a voice sample

Seven of the flagged spans arrived with the draft Kai pasted in, and this skill
preserved them because it read them as his voice. They were Claude output from
an earlier session.

| Span | Verdict |
|---|---|
| "That's you." | "horrible writing" |
| "the part that matters most" | "unnecessary glaze" |
| "deliberately messy" | "such a slop thing to say" |
| "The edits are the interesting part" | "weird glaze" |
| "did I invent a guy who doesn't exist" | "sounds so insecure" |
| "the part I really need you for" | "overstating importance" |
| the three-athlete list | "classic tell, really bad writing" |

So the worst failure was preservation rather than generation. Slop survived two
consecutive Claude passes because the second pass treated the first pass's
output as a voice reference.

Three rules fall out.

**Scan the input before using it as a base.** Run `check.py` over any draft
handed over for editing, before writing a line. That step did not happen here.

**A pasted draft is never evidence of voice**, whoever pasted it. Ask whose
words they are when it matters, and edit as though they are nobody's when it
does not.

**Inherited text gets the same bar as new text.** A phrase earns no protection
from already being in the document.

The corpus in `voice-dna.md` carries a related caveat. It was mined from
messages Kai typed to Claude, which is his lowest-stakes register, so it is
evidence of diction and stance and never of whether a sentence clears his bar
for outbound writing.

## The additive trap

Humanizer works by subtraction. The invariants in this skill are additive, and
the additive layer is what generated the failures:

| Invariant | What it produced |
|---|---|
| Vary the rhythm | empty punches: "That stops working as this grows." |
| Keep comparisons physical | the laboured retest analogy, "same" four times |
| Reasons land as consequences | because-clauses read as glaze |
| Verdict first | setup sentences announcing importance before delivering any |

Treat the invariants as constraints on what a sentence may do, never as moves to
reach for. When in doubt, cut rather than add.

## The eight modes

### 1. Glaze

Telling the reader how to weigh something instead of saying it. Highest
frequency mode in the eval, and Kai used the word three times.

Greppable: "the part that matters", "the interesting part", "what matters
most", "the part I really need", "that's the", "here's the thing", "and that's
the point", "which is the whole point".

Fix: delete the frame and keep the content. Weight comes from the fact, so a
sentence that announces importance is admitting the fact cannot carry it.

### 2. Sentences carrying no new information

The shape is a setup sentence that previews the next one, the real sentence,
then a punch restating it. Three sentences, one fact.

> The part I can't do myself is the part that matters most. I can check whether
> Harlen made up a number or contradicted the data in front of it, because
> that's mechanical, but I can't tell whether the coaching is any good. That's
> you.

Kai's note: "basically a retell of the sentence beforehand, whole paragraph just
to say 1 sentence pretty much."

Fix: every sentence introduces a fact the reader does not have. Delete any
sentence whose content appears in the sentence next to it.

### 3. Empty punches

A short standalone sentence carrying no fact, kept for rhythm. "That's you."
"That stops working as this grows." The skill previously endorsed these as
voice, which was wrong. Short is his average length, and shortness never
justifies a sentence that says nothing.

### 4. Over-explaining and the staged reveal

Building an analogy and then naming the term at the end reads as being dumbed
down. Justifying a request ("because that's mechanical", "because the edits are
the interesting part") reads the same way.

Fix: name the term first and define it in the same breath. Ask for the thing
without explaining why it interests you.

### 5. Word echo and comma-chaining

"Same reason you'd retest a client on the same movements under the same
conditions" put "same" four times inside two sentences, which Kai called
"super unnatural and a classic tell of slop."

Fix: no content word repeats within two sentences unless it is a term of art.
Cap a sentence at two comma-joined clauses.

### 6. Parallel triads that pass the drop test

Three items where every item carries distinct content, still read as cadence:

> One has never worn a tracker at all. Another stopped charging his Garmin for
> eleven days in the middle of a block, and there's one who signed up last week
> with almost nothing on file.

The drop test is necessary and not sufficient. Structural parallelism across
three items is the tell by itself. Give two, or fold them into one sentence
that does not repeat a frame.

### 7. Leading the witness

> Ray is the one I'm least sure about.
>
> Real client, or did I invent a guy who doesn't exist?

Two problems at once. Nominating his own suspicion pre-loads the reviewer's
answer, and the self-deprecating question is performed insecurity, which section
5 of SKILL.md already bans.

This one is not only style. Kai was building a review instrument, so naming the
athlete he doubts makes the reviewer's verdict on that athlete worth less than
their verdict on the other nine. Ask the open question and let the reviewer find
it.

### 8. Clarity sacrificed to ban compliance

Removing Kai's "Not what you'd type into an app, what was actually on your mind"
produced "in the words it actually showed up in?", which does not parse.

Fix: when removing a banned construction breaks the sentence, rewrite the whole
thought from scratch. A banned construction beats a broken sentence, so if only
those two options exist, go back and find a third.

## What survived

Worth knowing, because these are calibration points rather than accidents.

- "Four things, and blunt is more useful than nice:" went unflagged.
- The four numbered questions survived as questions. The damage was in the
  editorial wrapped around them.
- "Right now when I change how Harlen works, I'm guessing whether it got
  better." survived, which is the one sentence in the message that states a
  problem without decorating it.
