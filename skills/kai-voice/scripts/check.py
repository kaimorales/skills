#!/usr/bin/env python3
"""Deterministic scan for Kai's banned constructions.

Usage:
    python3 check.py FILE [FILE ...]
    python3 check.py -            # read stdin

Flags em dashes, negative parallelism, paratactic double-taps, rule-of-three
fragments, curly quotes, hype vocabulary, bold-header bullets and chat residue.
Fenced code blocks are skipped. Exit status is 1 when anything is found, so this
can gate a commit.
"""
import pathlib
import re
import sys

CONJ = (
    "and but or so because although though while when if unless after before "
    "since which that then also plus yet however whereas as for nor once until "
    "whenever wherever whether given despite"
).split()


GLAZE = [
    r"the part that (?:matters|really matters)",
    r"the (?:most )?interesting part",
    r"what matters most",
    r"the part I (?:really )?need you for",
    r"that'?s the part",
    r"here'?s the thing",
    r"that'?s the point",
    r"the (?:key|real) (?:insight|point|question)",
    r"most importantly",
    r"the important part",
    r"which is the whole point",
    r"the thing that matters",
    r"\b(?:matters|counts)\s+(?:just\s+)?as much\b",
    r"\b(?:this|that|it|which)\s+matters\b",
    r"\bmatters\s+more than\b",
    r"\bis\s+(?:specific|clear|explicit|direct)\s+about\b",
    r"\bworth\s+(?:paying attention to|noting|remembering|acting on)\b",
    r"\bcannot be overstated\b",
]

RESIDUE = [
    "great question", "i hope this helps", "i hope this email finds you well",
    "let me know if you'd like", "happy to help", "i'd be happy to",
    "certainly!", "of course!", "you're absolutely right", "as an ai",
    "as of my last update", "based on available information",
    "it is important to note", "it's worth noting", "in conclusion",
    "firstly", "secondly", "at this point in time", "due to the fact that",
    "in order to", "has the ability to",
]

NEG_PARALLEL = [
    (r"\bnot\s+(?:just|only|merely|simply)\b[^.?!;]{0,90}?[,;]?\s*(?:but|it'?s|its|it is|this is|they are|these are)\b",
     "negative parallelism: not just X, but Y"),
    (r"\bnot\s+(?:a|an|the)\b[^.?!;]{0,60}?\bbut\s+(?:a|an|the)\b",
     "negative parallelism: not a X, but a Y"),
    (r"\b(?:isn'?t|aren'?t|wasn'?t|is not|are not)\b[^.?!;]{0,70}?\b(?:it's|it is|they're|they are|this is)\b",
     "negative parallelism: it isn't X, it's Y"),
    (r",\s*not\s+(?:a|an|the|just|merely)?\s*[\w-]+\s*[.!?\n]",
     "negative parallelism: X, not Y"),
    (r"\brather\s+than\s+(?:a|an|the)\b[^.?!;]{0,40}?\b,\s*(?:it|this|we)\b",
     "negative parallelism: rather than X, it Y"),
    (r"\b(I|we|it|this)\s+can\b[^.?!]{0,90}[.!?]\s+\1\s+can'?(?:no)?t\b",
     "negative parallelism across sentences: capability set up as a foil"),
    (r"\b(I|we|it|this)\s+can\b[^.?!;]{0,70}?,?\s+but\s+\1\s+can'?(?:no)?t\b",
     "negative parallelism: capability set up as a foil"),
    (r"^\s*(?:No|Not)\s+[\w\s'-]{2,30}\.\s*(?:No|Not)\s+[\w\s'-]{2,30}\.",
     "rule of three by negation"),
]

SPLIT = re.compile(r"(?<=[.!?])\s+")
WORD = re.compile(r"[A-Za-z0-9'’-]+")


HYPE = [
    "delve", "robust", "seamless", "seamlessly", "holistic", "tapestry",
    "testament", "underscore", "underscores", "underscoring", "pivotal",
    "vibrant", "nestled", "boasts", "renowned", "groundbreaking",
    "transformative", "empowers", "empowering", "unlock", "unlocks",
    "cutting-edge", "state-of-the-art", "game-changing", "game changer",
    "landscape", "ecosystem", "journey", "leverage", "leveraging", "utilize",
    "utilizing", "streamline", "streamlining", "comprehensive", "elevate",
    "elevates", "foster", "fostering", "garner", "intricate", "interplay",
    "showcase", "showcases", "showcasing", "crucial", "myriad", "plethora",
]

def _load_wordlist():
    """Parse references/banned-words.md so the doc and the scanner cannot drift.

    Only the comma runs that follow a bold category lead are read. Prose inside
    those sections starts on a capital letter, and every list entry is
    lowercase, which is what separates them.
    """
    md = pathlib.Path(__file__).resolve().parent.parent / "references" / "banned-words.md"
    hard, soft, bucket = set(), set(), None
    if not md.exists():
        return hard, soft
    for para in re.split(r"\n\s*\n", md.read_text(encoding="utf-8")):
        head = para.strip().lower()
        if head.startswith("## hard bans"):
            bucket = hard
        elif head.startswith("## soft bans"):
            bucket = soft
        elif head.startswith("## "):
            bucket = None
        flat = " ".join(para.split())
        if bucket is None or not flat.startswith("**"):
            continue          # explanatory prose, not a comma run of terms
        body = re.sub(r"^\*\*[^*]+\*\*", "", flat)
        for raw in re.split(r"[,.]", body):
            term = re.sub(r"\([^)]*\)", "", raw).strip()
            if not term or not term[0].islower():
                continue          # a capital starts a prose sentence, not a term
            term = term.lower()
            if len(term.split()) > 5 or '"' in term or "*" in term or "#" in term:
                continue
            bucket.add(term)
    return hard, soft


HARD_WORDS, SOFT_WORDS = _load_wordlist()
if not HARD_WORDS:          # reference file missing, fall back to the old array
    HARD_WORDS = set(HYPE)

# same string, term of art in the writing he actually does
EXEMPT = [
    r"statistical(?:ly)?\s+significan",
    r"significan\w*\s+(?:at\s+)?(?:p\s*[<=>]|difference|effect)",
    r"\bcritical\s+(?:value|path|region|point)\b",
    r"\bcriterion\b",
    r"\b(?:api|primary|foreign|encryption|private|public)\s+key\b",
    r"\bkeys?\b(?!\s+(?:insight|point|question|takeaway|factor|driver))",
    r"\b(?:ios|android|web|cloud)\s+platform\b",
    r"\b(?:saline|buffer|aqueous)\s+solution\b",
    r"\bvitals\b",
    r"[-_/.]dna|dna[-_/.]",
    r"\bvital\s+(?:signs|capacity)\b",
    r"\bship(?:ping)?\s+(?:address|cost|costs|label|date|carrier|container)\b",
    r"[/:`]\s*ship",
    r"\b(?:cruise|cargo|container|sailing)\s+ship\b",
]
QUOTED = re.compile(r'"[^"]*"|\u201c[^\u201d]*\u201d')


def banned_words(line):
    """Yield (tier, term) for banned vocabulary outside quotation marks."""
    bare = QUOTED.sub(" ", line).lower()
    if not bare.strip():
        return
    hits = []
    for tier, words in (("BANNED WORD", HARD_WORDS), ("WEAK WORD", SOFT_WORDS)):
        for term in words:
            parts = term.split()
            # a silent-e stem has to reach utilizing, streamlining, leveraging
            tail = parts[-1]
            stem = re.escape(tail[:-1]) + r"(?:e|es|ed|ing)?" if tail.endswith("e") \
                else re.escape(tail) + r"(?:s|es|ed|ing|d)?"
            pat = r"\b" + r"\s+".join(
                [re.escape(w) for w in parts[:-1]] + [stem]) + r"\b"
            for m in re.finditer(pat, bare):
                lo, hi = max(0, m.start() - 24), m.end() + 24
                if any(re.search(x, bare[lo:hi]) for x in EXEMPT):
                    continue
                hits.append((m.start(), m.end(), tier, m.group(0)))
                break
    # a single word inside a longer banned phrase is one finding, not two,
    # and stem matching means two list entries can land on the same span
    seen = set()
    for a, b, tier, txt in hits:
        if any(x <= a and b <= y and (y - x) > (b - a) for x, y, _, _ in hits):
            continue
        if (a, b) in seen:
            continue
        seen.add((a, b))
        yield tier, txt


def strip_fences(lines):
    """Return (lineno, text) pairs with fenced code blocks and frontmatter removed."""
    out, fenced = [], False
    start = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                start = j + 1
                break
    lines = lines[start:]
    for i, raw in enumerate(lines, start + 1):
        if raw.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        out.append((i, raw.rstrip("\n")))
    return out


def clause_words(s):
    return WORD.findall(s)


def phrase_triads(text):
    """Yield (snippet, reason) for triads of parallel phrases.

    A triad only counts when it is shaped for cadence: three consecutive short
    segments that either all open with the same word (anaphora) or land at
    matching lengths and close on a conjunction. Ordinary three-clause
    sentences are left alone.
    """
    for sent in SPLIT.split(text):
        sent = sent.strip().rstrip(".!?")
        if not sent or sent.startswith(("|", "#", "-", "*", ">")):
            continue
        segs = [x.strip() for x in re.split(r"[,;:]", sent) if x.strip()]
        if len(segs) < 3:
            continue
        # four or more clipped segments is an enumeration, not a cadence triad
        if sum(1 for x in segs if len(clause_words(x)) <= 4) >= 4:
            continue
        for i in range(len(segs) - 2):
            trio = segs[i:i + 3]
            counts = [len(clause_words(x)) for x in trio]
            if not all(1 <= c <= 10 for c in counts):
                continue
            heads = []
            for x in trio:
                w = clause_words(x)
                if w and w[0].lower() in ("and", "or") and len(w) > 1:
                    w = w[1:]
                heads.append(w[0].lower().split("'")[0] if w else "")
            ratio = max(counts) / min(counts)
            snip = ", ".join(trio)
            if len(set(heads)) == 1:
                yield snip, f"anaphoric triad (each opens '{heads[0]}')"
                break
            closes = re.match(r"^(and|or)\b", trio[-1].strip(), re.I)
            if ratio <= 2.2 and closes:
                yield snip, "isocolon triad"
                break
            # asyndetic triad: three clipped fragments, no conjunction at all
            if max(counts) <= 4 and not any(
                    re.search(r"\b(and|or|but)\b", x, re.I) for x in trio):
                yield snip, "asyndetic triad"
                break


def paratactic_pairs(text):
    """Yield (sentence_a, sentence_b, reason) for suspected double-taps."""
    parts = [p.strip() for p in SPLIT.split(text) if p.strip()]
    for a, b in zip(parts, parts[1:]):
        wa, wb = clause_words(a), clause_words(b)
        if not (2 <= len(wa) <= 9 and 2 <= len(wb) <= 9):
            continue
        if wb[0].lower() in CONJ:
            continue
        if b.rstrip().endswith("?") or a.rstrip().endswith("?"):
            continue
        ratio = len(wa) / len(wb)
        if not 0.6 <= ratio <= 1.67:
            continue
        overlap = len({w.lower() for w in wa} & {w.lower() for w in wb})
        reason = "isocolon" if abs(len(wa) - len(wb)) <= 1 else "asyndeton"
        if overlap >= 2:
            reason += " + synonymia (repeats itself)"
        yield a, b, reason


LOCAL_STOP = (
    "about above after again against along among around because before below "
    "beneath beside between beyond could during either every first from into "
    "itself least less like made make many might more most much must never "
    "next nothing often once only other over own perhaps rather same since "
    "some still such than that their them then there these they thing things "
    "this those though through under until upon using very well were what "
    "when where whether which while will with within without would your "
    "already always another anything back come does done else even ever "
    "given goes going here just kind know look need part place point right "
    "said says seen sits stay take tell tells thats want ways "
    # his own habitual vocabulary, per voice-dna.md, so repeats are not echo
    "like just really actually honestly maybe kind kinda okay yeah yeah alright "
    "idk think thing gonna wanna sure guess feel feels"
).split()
LOCAL_STOP = set(LOCAL_STOP)


def content_repeats(blocks, terms):
    """Yield (word, sent_a, sent_b) for a content word reused within two sentences.

    Four suppressions keep this to real echo. Quoted material is stripped, since
    a source's wording is not the writer's. Pairs never cross a heading, since
    a new section is a real break. A word appearing in three or more paragraphs
    is domain vocabulary
    rather than echo. A word repeating as part of a repeated phrase is a term of
    art ("coefficient of variation"), so only lone repeats survive. Anything
    still slipping through goes in --terms.
    """
    quoted = re.compile(r'"[^"]*"')
    clean = [[quoted.sub(" ", p) for p in blk] for blk in blocks]
    paras = [p for blk in clean for p in blk]

    def bag(s):
        out = []
        for w in WORD.findall(s):
            lw = w.lower()
            if re.search(r"n't$|'(?:re|ll|ve|d|m|s)$", lw) and not lw.endswith("'s"):
                continue                      # contraction, not a content word
            lw = re.sub(r"'s$", "", lw).rstrip("'")
            if len(lw) < 4 or lw in LOCAL_STOP or lw in CONJ or lw in terms:
                continue
            out.append(lw)
        return out

    spread = {}
    for i, para in enumerate(paras):
        for w in set(bag(para)):
            spread.setdefault(w, set()).add(i)

    for blk in clean:
        sents = [x.strip() for x in SPLIT.split(" ".join(blk))
                 if len(x.strip()) > 3]
        for i, a in enumerate(sents):
            for j in (i + 1, i + 2):
                if j >= len(sents):
                    continue
                wa, wb = bag(a), bag(sents[j])
                shared = set(wa) & set(wb)
                if not shared:
                    continue
                # a repeated adjacent pair is a multi-word term, not an echo
                def bigrams(ws):
                    return {(x, y) for x, y in zip(ws, ws[1:])}
                phrase = set()
                for x, y in bigrams(wa) & bigrams(wb):
                    phrase.update((x, y))
                for w in sorted(shared - phrase):
                    if len(spread.get(w, ())) >= 3:
                        continue
                    yield w, a, sents[j]


HOLLOW_AND = re.compile(
    r"[^,.;:!?]{25,},\s+and\s+(?:the|a|an)\s+\w+[^,.;:!?]{10,}[.!?]")


def hollow_conjunction(text):
    """Yield sentences where ', and' bolts on a clause with a fresh subject.

    Section 1.2 says to connect sentences, and 'and' is the connective that
    states no relation. Joining two independent clauses with it leaves the
    parataxis intact under a conjunction, which the sentence-pair pass cannot
    see. A back-referring subject (that, this, it, which) is fine, since the
    reference is the relation.
    """
    for sent in SPLIT.split(text):
        sent = " ".join(sent.split())
        if len(clause_words(sent)) < 16:
            continue
        m = HOLLOW_AND.search(sent)
        if m:
            yield sent


def scan(name, raw, terms=frozenset()):
    findings = []
    lines = strip_fences(raw.splitlines(keepends=True))

    for n, line in lines:
        low = line.lower()

        if "—" in line:
            findings.append((n, "EM DASH", line.strip()))
        if "“" in line or "”" in line or "’" in line:
            findings.append((n, "curly quote", line.strip()))

        for pat, label in NEG_PARALLEL:
            m = re.search(pat, line, re.I)
            if m:
                findings.append((n, label.upper(), m.group(0).strip()))

        if re.match(r"^\s*[-*]\s+\*\*[^*]+:\*\*", line):
            findings.append((n, "bold-header bullet", line.strip()[:70]))

        m = re.match(r"^#{1,6}\s+(.*)$", line)
        if m:
            words = [w for w in m.group(1).split() if w.isalpha()]
            rest = [w for w in words[1:] if w.lower() not in CONJ]
            caps = [w for w in rest if w[:1].isupper()]
            if len(words) > 2 and rest and len(caps) == len(rest):
                findings.append((n, "Title Case heading", m.group(1)[:60]))

        m = re.search(r"\b([\w-]+),\s+([\w-]+),?\s+and\s+([\w-]+)\b", line)
        if m and all(len(g) > 3 for g in m.groups()):
            findings.append((n, "possible rule of three", m.group(0)))

        # repeated connector triads: "X plus Y plus Z", "with A with B with C"
        for conn, floor in (("plus", 2), ("with", 3), ("about", 3), ("through", 3)):
            if len(re.findall(r"\b" + conn + r"\b", low)) >= floor:
                findings.append((n, f"triad via repeated '{conn}'", line.strip()[:70]))

        for pat in GLAZE:
            m = re.search(pat, low)
            if m:
                findings.append((n, "GLAZE (tells reader how to weigh it)", m.group(0)))

        # trailing evaluative tag: noun phrase, comma or dash, judgement adjective
        for sent in SPLIT.split(line):
            m = re.search(r"[,\u2014-]\s*((?:\w+ly\s+)?\w+)\s*[.!?]\s*$", sent.strip())
            if m and re.match(r"^(?:\w+ly\s+\w+|very\s+\w+|quite\s+\w+)$",
                              m.group(1), re.I):
                findings.append((n, "trailing evaluative tag", m.group(0).strip()))

        for tier, term in banned_words(line):
            findings.append((n, tier, term))
        for phrase in RESIDUE:
            if phrase in low:
                findings.append((n, "chat residue / filler", phrase))

    # second pass over unwrapped paragraphs, so line wrapping cannot hide a
    # construction that spans a newline
    seen = {(n, lbl, snip) for n, lbl, snip in findings}
    para_start, buf = None, []

    def flush(buf, start):
        if not buf:
            return
        joined = " ".join(buf)
        for pat, label in NEG_PARALLEL:
            for m in re.finditer(pat, joined, re.I):
                frag = " ".join(m.group(0).split())
                key = (start, label.upper(), frag)
                if not any(frag in s2 or s2 in frag for n2, l2, s2 in seen
                           if l2 == label.upper()):
                    findings.append(key)
                    seen.add(key)

    for n, line in lines:
        if not line.strip() or line.lstrip().startswith(("-", "*", "|", "#", ">", "```")):
            flush(buf, para_start)
            buf, para_start = [], None
            continue
        if para_start is None:
            para_start = n
        buf.append(line.strip())
    flush(buf, para_start)

    body = "\n".join(t for _, t in lines)
    for para in re.split(r"\n\s*\n", body):
        rows = para.splitlines()
        listy = any(r.lstrip().startswith((">", "-", "*", "|", "#"))
                    or re.match(r"^\s*\d+[.)]\s", r) for r in rows)
        joined = " ".join(re.sub(r"^\s*(?:[-*>|]|\d+[.)])\s*", "", r) for r in rows)
        # quoted material and lists are usually examples, so only the paratactic
        # pass skips them; triads inside a list item still count
        if not listy:
            for a, b, reason in paratactic_pairs(joined):
                findings.append((None, f"PARATAXIS ({reason})", f"{a} {b}"))
        for snip, reason in phrase_triads(joined):
            findings.append((None, f"RULE OF THREE ({reason})", snip))
        for sent in hollow_conjunction(joined):
            findings.append((None, "HOLLOW 'AND' (relation not stated)", sent))

    blocks, cur = [], []
    for _, t in lines:
        if t.lstrip().startswith("#"):
            if cur:
                blocks.append(cur)
            cur = []
            continue
        if t.lstrip().startswith(("|", ">", "-", "*")):
            continue
        cur.append(t)
    if cur:
        blocks.append(cur)
    blocks = [[" ".join(p.split()) for p in re.split(r"\n\s*\n", "\n".join(blk))
               if p.strip()] for blk in blocks]
    for w, a, b in content_repeats([b for b in blocks if b], terms):
        findings.append((None, f"WORD ECHO ('{w}' inside two sentences)",
                         f"{a[:44]} ... {b[:44]}"))

    return findings


def main(argv):
    argv = argv[1:]
    terms = set()
    while "--terms" in argv:
        i = argv.index("--terms")
        terms |= {w.strip().lower() for w in argv[i + 1].split(",") if w.strip()}
        del argv[i:i + 2]
    targets = argv or ["-"]
    total = 0
    for t in targets:
        raw = sys.stdin.read() if t == "-" else open(t, encoding="utf-8").read()
        found = scan(t, raw, terms)
        total += len(found)
        print(f"\n=== {t}: {len(found)} finding(s) ===")
        for n, label, snippet in found:
            loc = f"L{n}" if n else "  "
            print(f"  {loc:>6}  {label:<34} {snippet[:88]}")
        if not found:
            print("  clean")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
