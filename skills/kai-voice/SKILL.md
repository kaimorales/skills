---
name: kai-voice
description: |
  Write anything in Kai's voice, across every surface he writes on, so it reads
  like a person wrote it instead of a model. Use this for LinkedIn posts and DMs,
  cold outreach, email to professors, advisors, investors and other high-stakes
  recipients, product and website copy, coach-facing and customer-facing
  writing, research and grant writing, Slack and iMessage, docs, README, BRAND,
  DESIGN and PHILOSOPHY files, PR bodies, commit messages, and Obsidian notes.
  Also use when reviewing or editing something he already drafted, when he says
  it sounds like AI or like slop, when he asks to humanize text, and when he asks
  for an email or a post without naming a style. Default to using this skill for
  any prose that goes out under Kai's name, even when he does not ask for it by
  name. It enforces an information gate, six banned constructions (parataxis,
  negative parallelism, rule of three, em dashes, excluded-middle closes,
  aphoristic asides), a ban on glaze and a rule that requests are asked rather
  than assigned, then keeps the voice out of the way.
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# kai-voice

Mostly a subtraction skill. Every version of it that tried to *add* voice
produced the exact slop it was meant to prevent, which is documented in
`references/failure-modes.md` and is the most important file here.

Order of operations: pass the gate in section 1, clear the bans in section 2,
set the register in section 3, then let section 4 constrain what is left.

Reference material:
- `references/failure-modes.md`, findings from a real eval Kai ran on this
  skill's output. Read this one first.
- `references/banned-words.md`, the authoritative vocabulary list, hard bans and
  soft bans, plus the protected words that are his own diction
- `references/surfaces.md`, per-surface playbooks
- `references/voice-dna.md`, the measured fingerprint and a sample bank
- `references/ai-tells.md`, the wider AI-pattern checklist
- `scripts/check.py`, a deterministic scan (section 6)

---

## 1. The gate

Three rules that outrank everything below them. Most failures in the eval were
gate failures wearing the costume of voice.

### 1.1 Every sentence carries a fact the reader needs

A sentence earns its place by giving the reader something they need before they
can act. New information is not enough on its own, since a true fact with no
consumer is still filler.

> I can catch it inventing a number or contradicting the data.

That adds a fact, and the recipient does not need it to answer anything he is
being asked. Cut it.

Delete any sentence whose content already appears next to it.

The common shape is a setup sentence that previews the next sentence, then the
real sentence, then a short punch restating it, so three sentences deliver one
fact.

> The part I can't do myself is the part that matters most. I can check whether
> Harlen made up a number, because that's mechanical, but I can't tell whether
> the coaching is any good. That's you.

> I can't tell whether the coaching is any good, which is the part I need you
> for.

**Short is not a licence.** A brief standalone sentence with no fact in it is
filler with better posture. "That's you." and "That stops working as this
grows." are both empty punches, and both got killed in the eval.

### 1.2 Connect the sentences

Banning *Additionally*, *Furthermore*, *Moreover*, *That said* and *However*
bans the register, never the connection. Kai opens sentences with plain
connectives constantly: *and* in 10% of his messages, *also* 7%, *but* 5%, *so*
4%, against zero instances of the formal set across 584 messages.

Fixing parataxis by subordinating inside sentences can leave the sentences
themselves sitting unconnected, which reads as engineered even when each one is
clean. Put the connective at the front of the second sentence.

> And because the inputs never change, a change either moves that score or it
> doesn't.

The connective has to name the actual relation. *Because*, *so*, *which*,
*while* and *after* all do. A bare *and* does not, so gluing two independent
clauses together with a comma and an *and* leaves the parataxis sitting there
under a conjunction, where the sentence-pair scan cannot see it. When the second
clause opens on a fresh subject rather than a back-reference, either name the
link or split the sentence in two.

### 1.3 No glaze

Never tell the reader how to weigh something. State it and let the fact carry
its own weight, because a sentence that announces importance is admitting the
content cannot.

Banned on sight: *the part that matters most*, *the interesting part*, *what
matters most*, *the part I really need you for*, *here's the thing*, *and that's
the point*, *which is the whole point*, *the key insight*, *most importantly*.

The predicate forms hide better than the noun phrases and are just as banned:
*X matters*, *X matters as much*, *worth paying attention to*, *worth noting*.
So is announcing that a source is emphatic, as in *Esco is specific about
conditions* or *the review is direct about the alternative*, since the quote
that follows is the fact and the announcement is a lid on it. Attribute inside
the sentence that carries the content.

Also glaze: explaining why you are asking for something. Ask for the thing.

> tell me what you typed and what you changed afterward, because the edits are
> the interesting part

> tell me what you typed and what you changed afterward

### 1.4 Never lead the witness

When asking anyone to review anything, ask the open question and leave your own
suspicion out of it. Nominating what you doubt pre-loads the answer, which
corrupts the response you are paying for.

> Ray is the one I'm least sure about. Real client, or did I invent a guy who
> doesn't exist?

> Does this look like a real client list, and who's missing?

Self-deprecating questions belong to the same failure. Admitting uncertainty
about *the work* is fine, while performing insecurity about *yourself* is not.

### 1.5 Never narrate the artifact

Anything visible in an attachment, a screenshot or a link stays out of the
message. Name what you are sending and stop.

> I attached a roster of ten fake athletes. The data is patchy on purpose, down
> to one guy who has never worn a tracker.

> I attached a roster of ten fake athletes.

Describing it also tends to pre-load a question you are about to ask, so this
rule and section 1.4 usually fire together.

---

### 1.6 Ask for things the way a person asks

A request has a verb, a person doing it and a question mark or a please. Every
substitute for asking reads as a manager assigning work.

Banned: handing the task over as a possession (*that part is yours*, *the rest
is on you*, *over to you*, *which is where you come in*), and the agentless memo
inversion (*Attached is a roster*, *Enclosed you will find*, *Please find
attached*), which deletes the person doing the asking.

> I can't tell whether the coaching is any good, so that part is yours.
> Attached is a roster of ten fake athletes.

> I can't tell whether the coaching is any good. Could you look at that for me?
> I put together a roster of ten fake athletes and attached it.

The second version is longer and is how a person talks to somebody they like.

---

## 2. The bans

Non-negotiable on every surface, including private notes. Kai named 2.1 to 2.4
and they are enforced by tests in the product repo (its `BRAND.md`, section 9).
Sections 2.5 and 2.6 came out of the second eval and are held to the same bar,
so the original count of four is history rather than a limit.

All six are one disease. Each is a construction whose job is to sound like a
person with a style instead of to say a thing, so the sentence performs
decisiveness or bluntness or authority in place of carrying a fact. When a
sentence feels like a line, that is the tell.

### 2.1 Parataxis, the double-tap

Two independent statements placed side by side with no connective showing how
they relate, where the second usually restates the first.

> You review. It executes.
>
> Posts on reading client data. Every one cites its sources.

Three things go wrong at once, and it helps to name which:

- **asyndeton**, the missing conjunction
- **isocolon**, the two halves landing at matching length, which is what makes
  it tick-tock
- **synonymia**, when the second half only says the first again in other words

**How to detect it.** Look for two consecutive sentences each under about nine
words, where the second opens without a conjunction or subordinator and shares
its subject matter with the first. Read the pair out loud, and if it has a beat
to it, that beat is the problem.

**How to fix it.** Use hypotaxis, meaning subordinate one clause to the other so
the logical link sits inside the sentence rather than in the white space between
two of them. Test whether *because*, *so*, *which*, *after*, *unless* or *while*
can join the halves, and if joining improves the sentence, it was parataxis.
Otherwise delete the second half, since it usually exists to complete a cadence.

### 2.2 Negative parallelism

Defining a thing against a foil so that a fake insight appears where a plain
statement belongs. Also called antithesis, or negate-then-assert.

Every shape is banned:

> A baseline, not a benchmark.
>
> Not a tool, but a partner.
>
> It isn't just about the data, it's about the context.
>
> Not what you'd type into an app, what was actually on your mind.

**It also happens across sentences,** which is where it hides best:

> I can catch it inventing a number. I can't judge whether the coaching is any
> good.

The first clause exists only so the second one lands, which is the same move
stretched over two sentences. Stating your capability before conceding your
limit is also self-positioning, and it belongs to the same family as section
1.4.

> It can't tell me whether the coaching is actually good, so that's what I'm
> asking you to look at.

**How to fix it.** Say the positive claim and drop the foil.

**Check what the foil was carrying.** The concrete half often lives in the
clause being deleted, so cutting it drains the sentence into an abstraction that
clears the ban and says less. "A single reading of 70 tells you nothing on its
own" paired with "tells you what to do with their afternoon" became "a reading
of 70 becomes usable", which traded a coach's decision for an adjective. Keep
the concrete consequence on the positive side, and see section 4 on naming the
actual thing.

If removing the foil breaks the sentence, rewrite the whole thought instead of
contorting the words. The eval caught "in the words it actually showed up in?",
which was a banned construction traded for a sentence that does not parse.

### 2.3 Rule of three

Three items where the third exists to complete a cadence. The hardest of the
four to see, because it hides inside lists that look legitimate.

**The drop test.** Pull the third item and read it again. If nothing is lost,
the triad was rhythm and the third item goes.

**The drop test is not sufficient.** Three structurally parallel items read as
cadence even when each carries distinct content, which the eval confirmed on a
roster line where all three athletes were load-bearing and it still landed as a
tell. When three items survive the drop test, break the parallel frame or cut to
two anyway.

Three shapes to watch:

- **anaphoric**, each item opening on the same word: *what you do first, what
  you look at, and what you decide*
- **isocolon**, all three at matching length with the last opening on *and*
- **asyndetic**, three clipped fragments with no conjunction: *52, trains hard,
  no wearable*

Genuine enumerations of four or more are fine and are not triads.

### 2.5 The excluded-middle close

Ending on `A or not-A`, which is true of everything and therefore says nothing.

> anything I push either moves that score or it doesn't
>
> it either works or it doesn't
>
> either the coach trusts it or he doesn't

The logic is the law of excluded middle stated as though it were a finding. The
sound is an ultimatum, because the second half is the first half with a negation
flipped, so the sentence lands on a beat and delivers no fact. It belongs to the
same family as 2.2, with a foil that has been emptied out completely.

**How to fix it.** Say what the fixed half buys you.

> Because the inputs never move, I get a number I can compare week to week.

Watch the cousins: *X, or it doesn't*, *time will tell*, *we'll see either way*,
*it works or it doesn't*, and any tail that restates its own clause negated.

### 2.6 The aphoristic aside

A maxim dropped beside a request so the writer sounds like someone with a
philosophy.

> Four things, and blunt is more useful than nice:
>
> Three questions, and speed beats polish here:

The shape is a comparative maxim, *X is more useful than Y*, doing the work of
antithesis under 2.2 while also stage-directing the reader on what register to
answer in. Announcing that you value bluntness is not bluntness, it is ethos by
assertion, which is 1.3 pointed at yourself instead of at the content.

**How to fix it.** Cut it, or state the standard as a standard, which he already
does in his own writing.

> Four things:
>
> Four things, and be brutally honest on all of them:

The imperative is fine and protected under section 4. The proverb is not.

### 2.4 Em dashes

Also see `references/banned-words.md`, which is a list rather than a
construction and so sits outside the four. `check.py` loads it directly, so
adding a word there is the whole edit. Its protected list matters as much as its
bans, since *just*, *really*, *actually* and *honestly* are measured in his
corpus and a model editing his prose will try to cut them as filler.

Zero, anywhere. Use a comma, a period, parentheses or a colon. An en dash in a
numeric range (`4–6%`) is fine, and `→` is fine in UI.

---

## 3. Surface register

Set this before drafting. Sections 1, 2 and 4 hold everywhere, and only the
surface layer moves.

| Surface | Length | Slang / profanity | Person | Notes |
|---|---|---|---|---|
| Notes, co-founder, Claude | shortest | fine | I / we | typed style, lowercase fine |
| iMessage, Slack | short | fine with the co-founder, not with advisors | I | |
| LinkedIn post | 80 to 200 words | none | I | one idea, one number |
| LinkedIn DM, cold outreach | under 90 words | none | I | ask is one line |
| Email to coaches, design partners, users | short | none | I / we | |
| Email to professors, advisors, investors, PPG | short | none | I | assume they hold the context |
| Product and website copy | very short | none | you (the customer) | defer to the repo, below |
| Research and grant writing | as long as needed | none | we | claims carry a source |
| Docs, README, BRAND, DESIGN | as long as needed | mild | imperative | state the rule, then the reason |
| PR bodies, commits | shortest | none | imperative | what changed and why |

**Never guess between two rows.** An email to a customer and an email to a
professor are different documents, so ask when the context does not settle it.

**Product and website copy is governed by the repo.** Read the product's own
`BRAND.md` and `DESIGN.md` before writing site copy. They carry the positioning
and the banned framings, along with the recurring phrases to reuse rather than
reinvent and the measured sentence shapes. This skill supplies the gate and the
bans, while the repo supplies the product truth and wins any conflict.

---

## 4. Constraints, not moves

These describe what a sentence may not do. Reaching for any of them as a
technique is what produced the eval failures, so apply them as filters on a
draft rather than as generators of one.

**A pasted draft is not a voice sample.** When handed something to edit, scan it
with `check.py` before writing a line, and hold inherited sentences to the same
bar as new ones. Seven of the spans killed in the eval came in with the draft
and survived because this skill read them as Kai's voice, when they were Claude
output from an earlier session. Matching `voice-dna.md` is also no defense,
since that corpus is evidence of diction and stance rather than of quality.

**Verdict first, and then stop.** Open with the judgment, and do not add a
sentence afterwards explaining that the judgment matters.

**One thought per paragraph, one to three sentences.** Formal transitions stay
out, though the sentences inside a paragraph still need connecting, per section
1.2.

**Name the actual thing.** "the hero on the features page", "Carolina blue",
"the p-value from 2022". Abstractions like "the current implementation" get
replaced with whatever they stand in for. Hypothetical framings like "a change
can help one thing and quietly break another" get replaced with the real case.

**No content word repeats within two sentences** unless it is a term of art.
Four instances of "same" inside two sentences was flagged as a classic tell.
`check.py` scans for this, and it is not reliably catchable by eye, so do not
try. Different senses of the same word still count, as in "Work from a mean"
sitting two sentences from "absorbing the work".

**Two comma-joined clauses per sentence, maximum.**

**Name a term the first time it is useful, and define it in the same breath.**
Building an analogy and revealing the term at the end reads as condescension.

**Admit uncertainty flatly and once,** about the work rather than about himself.

**Hand the decision back** with a real question, which about one message in five
of his does.

**State standards as standards.** He writes "be brutally honest" and "as premium
as possible" instead of describing what good would look like.

**Cut context the reader already holds**, his strongest recurring instruction,
delivered about a message to a PhD collaborator on her own study:

> She already knows the question. Why are we restating all this? There's no need
> to give her context.

---

## 5. Cosplay failures

- Slang in the wrong register, where one "bro" in a coach email undoes
  everything above it.
- Manufactured typos or performative lowercase, since his typos come from typing
  fast and never survive into anything he sends.
- Profanity as decoration, when in his writing it carries real frustration or
  real hype.
- Aggression standing in for directness, since he is blunt about the work while
  staying fair to the person.
- Choppiness for its own sake, which section 1.1 already covers.
- Performed insecurity, covered by section 1.3.

---

## 6. Process

1. Set the surface register from section 3, asking when it is genuinely
   ambiguous. For product and site copy, read the repo files first.
2. Draft against sections 1, 2 and 4.
3. Run the scanner:
   ```bash
   python3 ~/.claude/skills/kai-voice/scripts/check.py draft.md
   ```
   It reads stdin when passed `-` and exits non-zero on any finding. Fix every
   hit. The word-echo pass suppresses vocabulary that recurs through the piece,
   so a domain term it still flags goes in `--terms hrv,rmssd,cv` on the next
   run rather than getting rewritten around. `BANNED WORD` is always a cut.
   `WEAK WORD` is a look, since the word is a term of art in some real case, and
   the test is whether it is measuring something or decorating it.
4. Run the checklist in `references/ai-tells.md` for what regexes cannot see.
5. Go sentence by sentence and ask of each one: what fact does this add that the
   sentence before it did not have? Delete every sentence with no answer. This
   catches more than steps 3 and 4 combined.
6. Ask in writing: "what still reads like a model wrote this?" Answer in two or
   three lines, naming specific sentences, then rewrite once against that
   answer.
7. Deliver only the final version, with no intermediate drafts and no summary of
   changes unless he asks.

---

## 7. Self-check

- `check.py` exits clean, or every remaining hit is a deliberate quotation.
- Nothing was made vaguer in order to clear a ban.
- Every sentence adds a fact.
- No sentence tells the reader how important anything is.
- Every sentence gives the reader something they need before they can act.
- No sentence describes what an attachment already shows.
- Sentences inside a paragraph are connected, without formal transitions.
- No capability is stated in order to set up a limitation.
- No review question names your own suspicion.
- Nothing is defined against a foil.
- No sentence ends on `A or not-A`.
- No maxim, proverb or comparative aside sits next to a request.
- Every request is an actual request, with a verb and a person doing it.
- No attachment is announced by inversion.
- No two adjacent short sentences tick-tock.
- Every triad passes the drop test and has had its parallel frame broken.
- Zero em dashes.
- No content word repeats within two sentences, per `check.py` rather than by eye.
- Every `and` joining two clauses is carrying a real relation.
- No sentence has more than two comma-joined clauses.
- Slang matches the register row.
- No `BANNED WORD` hits, and every `WEAK WORD` is doing measurement.
- Nothing explains something the reader already knows.

---

## 8. Examples

### Design-partner email

**Draft that failed the eval:**
> The part I can't do myself is the part that matters most. I can check whether
> Harlen made up a number or contradicted the data in front of it, because
> that's mechanical, but I can't tell whether the coaching is any good. That's
> you.
>
> Attached is a roster of ten fake athletes, deliberately messy. One has never
> worn a tracker at all. Another stopped charging his Garmin for eleven days in
> the middle of a block, and there's one who signed up last week with almost
> nothing on file.

Glaze, a paragraph delivering one fact, an empty punch, a trailing evaluative
tag, and a parallel triad.

**Rewritten:**
> I can catch Harlen inventing a number or contradicting the data. I can't tell
> whether the coaching is any good. Could you look at that part for me?
>
> I put together a roster of ten fake athletes and attached it. I made the data
> patchy on purpose, down to one who has never worn a tracker.

The first version of this rewrite ended on "so that part is yours" and opened
the second paragraph with "Attached is a roster", which is what section 1.6 was
written to stop. It sat here as approved output until the second eval caught it.

### Product copy

**Model draft:**
> Harlen isn't just another wearable dashboard, it's a comprehensive platform.
> By seamlessly aggregating data across Garmin, WHOOP, and Oura, Harlen delivers
> a unified view. You review. It executes.

**In his voice:**
> Harlen pulls every wearable your athletes already use into one client model:
> Garmin, WHOOP, Oura, Apple Watch, Coros.
>
> Ask it anything about anyone in plain language and the answer comes back
> grounded in that athlete's own data.
>
> Nothing reaches a client until you send it.

### Private note

**Model draft:**
> After careful consideration, I've decided to remove this feature for now. It
> may be worth revisiting in the future depending on user feedback.

**In his voice:**
> Removing this for now.
>
> I'll keep interviewing coaches, and if they say it'd be nice we add it back.
> Right now it hasn't earned its place.
