# skills

Agent skills for [Claude Code](https://claude.com/claude-code).

## iara

**"I ain't reading allat."** A standing output contract. Roughly 30% of a
typical response is the answer and the rest is packaging, so this deletes the
packaging.

Written as a positive recipe rather than a list of bans, on purpose.
Prohibition-style wording ("don't restate", "never narrate") tests worse than no
guidance at all, because an agent under a competing incentive negotiates with
"don't X". A contract states what a response *is*, which leaves nothing to
negotiate.

The other half is legibility, which took a rewrite to get right. An agent holds
the whole codebase in context while the reader holds one message, so a finding
compressed into `vite.config.ts:12` and a symbol name is unreadable to the
person deciding what to do with it. The contract asks for it in plain
words with the path after that for checking, written the way an engineer briefs
their TPM.

It also refuses to become a shape. Cost and open questions belong in a reply
only when they are real, and ending on the same label every turn rebuilds the
packaging the contract was meant to delete.

Brevity is scoped to prose from the start rather than added as an exemption, so
it cannot reach code blocks, tables, or commands. Those appear in full.

## kai-voice

A voice skill that works by subtraction. Every version of it that tried to *add*
style produced the slop it was built to prevent, so what remains is mostly a
list of what a sentence may not do.

The information gate comes first: a line earns its place by giving the reader
something they need before they can act, since a true fact with no consumer is
still filler. Four constructions are then banned outright, parataxis, negative
parallelism, rule of three, and em dashes. Glaze goes too, meaning anything that
announces importance instead of carrying it.

`scripts/check.py` is the deterministic half, scanning for each of them, plus
a 137-term hard ban list and a 44-term soft list read straight out of
`references/banned-words.md`, content words echoing across two sentences, and
conjunctions that bolt on a clause without stating a relation. Exit status is
non-zero on any finding, so it can gate a commit.

```bash
python3 skills/kai-voice/scripts/check.py draft.md
```

Read `references/failure-modes.md` before anything else. It annotates a real
eval where roughly thirteen spans of this skill's own writing were killed, and
seven of those had arrived in the material handed over for editing. They lived
because an earlier pass treated them as the author's own words, when a previous
model had written them. So the headline is that a pasted draft proves nothing
about voice, and inherited text gets the same bar as new text.

The corpus behind it is one person's and the register table is his. Fork it and
swap `references/voice-dna.md` for your own measurements.

## Install

```bash
git clone https://github.com/kaimorales/skills.git
cp -R skills/skills/iara ~/.claude/skills/iara
cp -R skills/skills/kai-voice ~/.claude/skills/kai-voice
```

Invoke with `/iara` or `/kai-voice`.

To keep it on permanently, add a line to `~/.claude/CLAUDE.md`:

```markdown
Follow `~/.claude/skills/iara/SKILL.md` in every response, without being asked.
Answers in plain language with the packaging deleted, and no fixed shape.
Cost and open questions belong in a response only when they are real, never as
a standing label or a recurring last line.
```

A skill on its own only loads when invoked or when its description matches. `CLAUDE.md` is read every session, which is what makes it standing.

## License

MIT
