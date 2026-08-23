# Banned words

The authoritative list. `check.py` enforces it, so this file and the scanner
move together. Three lists used to disagree with each other: the `HYPE` array in
`check.py`, section 2 of `ai-tells.md`, which nothing enforced, and the absence
list in `voice-dna.md`. This replaces all three as the source of truth, and
the product repo's own `BRAND.md` still wins for product copy.

## Contents
- Protected words
- Hard bans
- Soft bans
- Exemptions

---

## Protected words

Measured in his own corpus, so these are never bans no matter how they read to a
model: *like*, *just*, *really*, *actually*, *honestly*, *to be honest*, *maybe*,
*kind of*, *kinda*, *okay*, *yeah*, *alright*, *idk*, *bro*, *wait*, and
profanity in the private register.

A model editing his prose will reach for these as cuts, because they scan as
filler in general-purpose writing advice. They are his diction. Leave them.

## Hard bans

Never in anything, including private notes. `check.py` reports these as
`BANNED WORD`.

**Significance inflation.** crucial, pivotal, vital, paramount, invaluable,
indispensable, profound, myriad, plethora, testament, underscore, groundbreaking,
transformative, revolutionary, revolutionize, disrupt, disruptive, unparalleled,
unprecedented.

**Corporate and product slop.** leverage (verb), utilize, streamline,
seamless, seamlessly, frictionless, turnkey, bespoke, curated, world-class,
best-in-class, industry-leading, next-generation, cutting-edge,
state-of-the-art, game-changing, game changer, supercharge, robust,
comprehensive, holistic, scalable, empower, elevate, unlock, showcase, foster,
garner, boasts, renowned, nestled, vibrant, intricate, interplay, ship.

*Ship* is banned only as the release verb, meaning to push something out. His
corpus says *push* and *push to prod* every time, so that is the replacement,
along with *out*, *live* and *released*. The literal senses are exempt, as are
`/ship` and other command names.

**Health and fitness marketing.** This is the register his product sits closest
to and the one no previous list covered. actionable, actionable insights, insights (as
a standalone noun), data-driven, science-backed, peak performance, optimize your,
maximize your, unlock your potential, transform your, dial in, next level, level
up, biohacking, wellness journey, personalized experience.

**Figurative abstractions.** journey, landscape, ecosystem, tapestry, realm,
arena, sphere, fabric, backbone, cornerstone, bedrock, north star, secret sauce,
superpower, dna (of a company), delve.

**Copula avoidance.** serves as, functions as, stands as, represents (when it
means *is*), embodies, encapsulates, exemplifies, underpins, facilitates,
harnesses, spearheads, taps into, lends itself to, speaks to (figurative),
navigates (figurative).

**Discourse filler.** that said, having said that, that being said, with that in
mind, to that end, in essence, at its core, simply put, put simply, needless to
say, suffice it to say, it is important to note, it is worth noting, when it
comes to, in terms of, in order to, due to the fact that, at this point in time,
has the ability to, firstly, secondly, in conclusion.

**Closing slop.** the future looks bright, exciting times, this is just the
beginning, watch this space, stay tuned, the possibilities are endless, only
time will tell, at the end of the day, a major step forward.

**Hedge stacking.** may potentially, could possibly, might suggest, would seem
to, it could be argued, one might argue, there is a case to be made. One hedge
maximum, and a flat "I don't know" beats all of them.

## Soft bans

Legitimate in a technical or measured sense and slop everywhere else, so
`check.py` reports these as `WEAK WORD` for a look rather than an automatic cut.
The test is whether the word is doing measurement or decoration.

**Measured senses.** critical, essential, key (adjective), significant, notable,
noteworthy, integral, optimize, optimization.

**Product adjectives.** powerful, innovative, intuitive, effortless, delightful,
magical, compelling, remarkable, striking, meaningful, personalized, tailored.

**Product nouns and verbs.** solution, offering, platform, enables, drives
(figurative).

**Adverb inflation.** fundamentally, ultimately, essentially, effectively,
arguably, undoubtedly, certainly, truly, genuinely, incredibly, remarkably,
surprisingly, notably, particularly, especially, relatively, somewhat, fairly.

## Exemptions

Applied automatically, since the same string is a term of art in the writing he
actually does:

- *statistically significant*, *significance*, *significantly* next to a number
  or a p-value
- *critical value*, *critical path*, *criterion*
- *key* as a noun, including *API key* and *primary key*
- *platform* naming a real one, as in *the iOS platform*
- *solution* in a chemical or mathematical sense
- *optimize* naming a real optimizer or an actual optimization problem
- anything inside a direct quotation, which the scanner already strips

Add an exemption rather than rewriting around a word that is genuinely the right
one. If a hard ban is the right word in some real case, it belongs in soft bans
instead, so move it and say why here.
