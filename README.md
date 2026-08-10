# skills

Agent skills for [Claude Code](https://claude.com/claude-code).

## iara

**"I ain't reading allat."** A standing output contract: the answer, what it cost, what's still open. Nothing else.

Written as a positive recipe rather than a list of bans, on purpose. Prohibition-style wording ("don't restate", "never narrate") tests worse than no guidance at all, because an agent under a competing incentive negotiates with "don't X". A contract states what the response *is*, which leaves nothing to negotiate.

Brevity is scoped to prose from the start rather than added as an exemption, so it can't reach code blocks, tables, or commands. Those appear in full.

## Install

```bash
git clone https://github.com/kaimorales/skills.git
cp -R skills/iara ~/.claude/skills/iara
```

Invoke with `/iara`.

To keep it on permanently, add a line to `~/.claude/CLAUDE.md`:

```markdown
- Follow `~/.claude/skills/iara/SKILL.md` for every response.
```

A skill on its own only loads when invoked or when its description matches. `CLAUDE.md` is read every session, which is what makes it standing.

## License

MIT
