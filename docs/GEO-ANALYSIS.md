# GEO / AI Search Analysis — epochdigital.ai

**Analysed:** 2026-08-10 · **Target:** https://www.epochdigital.ai/ · **Pages:** 1

> **Framing.** Per [Google's AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide),
> optimizing for generative AI search *is* SEO. AI Overviews and AI Mode are grounded in the same
> ranking and quality systems as classic Search, and the eligibility floor is being **indexed and
> snippet-eligible**. Nothing below is a separate "GEO discipline" — it is SEO fundamentals viewed
> through AI-search surfaces. Where community GEO advice contradicts Google, this report defers to
> Google and says so.

---

## GEO Readiness Score: 32 / 100

| Criterion | Weight | Score | Notes |
|---|---:|---:|---|
| Citability | 25% | 15 | 408 words site-wide; nothing self-contained enough to quote |
| Structural readability | 20% | 35 | Short paragraphs, but two broken heading levels, no tables, no FAQ |
| Multi-modal content | 15% | 20 | One stock photo, one decorative 3D iframe, no video/chart/tool |
| Authority & brand signals | 20% | 8 | No author, no dates, no `sameAs`, no third-party presence |
| Technical accessibility | 20% | 85 | Fully server-rendered, all AI crawlers allowed, schema in place |

The technical layer is now genuinely strong. Everything else is close to a floor, and the score is
held down almost entirely by two things: **there is not enough content to cite**, and **the brand
name does not resolve to this company**.

### Platform breakdown

| Surface | Score | Why |
|---|---:|---|
| Google AI Overviews | 10 | 92% of AIO citations come from top-10 ranking pages. This site does not yet rank for anything. |
| Google AI Mode | 12 | Broader pool and less ranking-dependent, but leans on freshness + entity authority — both absent. |
| ChatGPT | 8 | Its citation mix is ~47.9% Wikipedia, ~11.3% Reddit. Zero presence on either. |
| Perplexity | 7 | ~46.7% Reddit-sourced. Zero presence. |
| Bing Copilot | 15 | Static HTML crawls cleanly, but the domain is not verified in Bing and no IndexNow ping exists. |

Treat AI Mode and AI Overviews as **two separate engines**: they agree on the answer ~86% of the
time but cite the same URL only ~13.7% of the time.

---

## 1. The finding that outranks everything else: the brand name does not resolve to you

This is the single largest GEO problem on the property, and no amount of markup fixes it.

Searching the brand returns **at least seven distinct organizations**, none of them this one:

| Entity | Domain | What they are |
|---|---|---|
| **Epoch Digital Media** | `epochdm.com` | **AI automation for mid-market operators — voice agents, booking, lead qual** |
| Epoch Digital | `epochdigital.org` | Asia-Pacific data centre platform, backed by Actis, has a newsroom |
| Epoch AI | `epoch.ai` | High-authority AI research nonprofit |
| Epoch AI Consulting | `epochaiconsulting.com` | AI strategy + automation, ex-CTO founding team |
| Epoch Digital Marketing | `epochdigital.co` | Digital marketing agency |
| Epoch Digital | `epochdigital.in` | Web design / marketing, India |
| Epoch Technology | `epochtechnology.co` | RPA / AI solutions |

Two consequences:

**a) `epochdm.com` is a near-collision, not a coincidence.** Epoch Digital Media sells AI voice
agents that "answer every call, qualify leads, and book appointments 24/7" to home services, med
spas, dental groups and auto dealerships. That is your positioning, your service line, and
substantially your name. They run a dedicated product subdomain (`voice.epochdm.com`), roughly 11
navigation pages including Results, About, Podcast and API docs. When an AI is asked about "Epoch"
+ "AI receptionist," they are the entity with enough surface area to describe.

**b) `linkedin.com/company/epoch-digital` is already occupied** by a different Epoch Digital. The
canonical LinkedIn slug for your name is gone, which matters because `sameAs` entity-linking is the
main mechanism for telling engines which "Epoch Digital" you are.

**Also confirmed: no search surface currently returns epochdigital.ai for any brand query.** That is
expected — `robots.txt` and `sitemap.xml` both 404'd until 2026-08-09 — but it means you are starting
entity-building from zero against six incumbents, one of them a direct competitor.

This is a **business decision before it is an SEO one**. Realistically: either commit to a
disambiguating entity strategy (always "Epoch Digital · epochdigital.ai", founder-forward, tight
vertical + geography), or reconsider whether the name is defensible against `epochdm.com` before
more equity accrues to it.

---

## 2. Citability — 15/100

**408 words of rendered body text on the entire site.** For comparison, the optimal *single* citable
passage is 134–167 words. There is roughly enough text here for two of them, and neither is written
to be extracted.

Section-by-section:

| Section | Words | Verdict |
|---|---:|---|
| Hero + service cards | 170 | Only block in citable range — but it is positioning copy, not an answer |
| `#services` ("Built for Revenue") | 82 | Too thin |
| `#use-cases` ("Infinite Receptionist") | 77 | Too thin |
| `#contact` | 48 | Too thin |

What's missing structurally:

- **Zero question-form headings.** AI retrieval matches heading text against query phrasing. Not one
  heading on the site is phrased as a question.
- **Zero definitions.** No "An AI receptionist is…" pattern anywhere. Definition sentences are among
  the most-extracted passage types.
- **Two statistics, both uncited** — the "391%" lead-conversion figure and the "20–30%" revenue
  recovery range. Uncited numbers on a commercial page are a liability, not a citability asset: they
  are exactly what a quality rater flags. (I documented both in `llms.txt` as general industry
  figures rather than your measured results, so assistants don't attribute them to you.)
- **No original data.** Google's stated test is *unique, non-commodity, first-hand* content. Their
  own example contrasts a generic listicle against lived experience with specifics. You run
  automation deployments — that is first-hand material nobody else has.

Also worth noting: **~44% of AI citations come from the first 30% of a page.** Your first 30% is the
hero — a headline, a subhead, and a drag-to-explore card stack. It front-loads *brand*, not *answer*.

---

## 3. Structural readability — 35/100

Two confirmed heading-hierarchy breaks:

1. **The four service cards are orphaned `H3`s.** `AI Website Receptionist`, `Booking & Scheduling`,
   `AI Voice Agent` and `Follow-Up & Review Engine` sit directly under the `H1` with no governing
   `H2`. These are the four things you actually sell, and structurally they belong to nothing.
2. **`#use-cases` jumps `H2` → `H4`**, skipping `H3` entirely.

Element inventory: 22 `<p>`, **1** list with **2** `<li>`, **0** tables, **0** FAQ blocks,
**0** question headings. Paragraphs are short (good) but there is no scannable structure for a
retriever to segment.

A comparison table is the highest-value missing element — comparative data is disproportionately
extracted, and "AI receptionist vs. answering service vs. voicemail" is a question your buyers
genuinely have.

---

## 4. Multi-modal content — 20/100

Multi-modal pages see materially higher selection rates. Current inventory:

- 2 × logo image (same file)
- 1 × Unsplash stock photo (now with descriptive alt text)
- 1 × Spline 3D iframe — **decorative**, contributes nothing extractable, and is the heaviest thing on the page
- 1 × cal.com booking embed

No video, no diagram, no chart, no calculator. For an automation agency the obvious plays are a
**short screen recording of a voice agent handling a live call**, and an **architecture diagram** of
what a deployed system actually looks like. Both are first-hand, neither exists elsewhere.

---

## 5. Authority & brand signals — 8/100

The weakest area, and the one with the most mechanical fixes available.

| Signal | Status |
|---|---|
| Author / founder byline | **Absent** — zero mentions of a person anywhere on the site |
| `Person` schema | **Absent** |
| `sameAs` entity links | **Absent** — nothing to link to |
| Publication / updated dates | **Absent** — no `<time>`, no `datePublished`, no `dateModified` |
| Copyright year | **`© 2025`** — stale by a year, and the only date signal on the page |
| Wikipedia / Wikidata | None |
| Reddit | None |
| YouTube | None |
| LinkedIn | Slug taken by another entity |

Two things to weigh here. **Recency is roughly a 3× citation multiplier**, and pages left stale 6+
months lose eligibility — yet this site has no date at all, and its one visible year marker is
wrong. And **brand mentions correlate ~3× more strongly with AI citation than backlinks do**
(YouTube ~0.737, Domain Rating ~0.266). Your link profile is not the lever; your absence from
third-party platforms is.

**Important caveat, per Google's myth list:** do *not* read that as licence to chase inauthentic
mentions across blogs, forums and videos — Google explicitly rejects mention-farming. The play is
genuine participation and genuine artefacts, not seeding.

---

## 6. Technical accessibility — 85/100

This is the part that is working, and most of it shipped in the last two days.

| Check | Status |
|---|---|
| Server-side rendering | **Pass** — all 408 words are in the raw HTML. AI crawlers don't execute JS; nothing here depends on it. |
| AI crawler access | **Pass** — GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, Claude-SearchBot, PerplexityBot, Perplexity-User, Google-Extended, Applebot-Extended, Bingbot, CCBot all explicitly `Allow: /` |
| `sitemap.xml` | Present, referenced from `robots.txt` |
| Canonical | Self-referential, present |
| Structured data | `Organization`, `WebSite`, `WebPage`, `ImageObject`, 4 × `Service` — parses clean |
| `llms.txt` | Present, well-formed — **but see below** |
| `llms-full.txt` | Absent |
| RSL 1.0 licensing | Absent (`/license.xml` 404, no `License` directives in robots.txt) |

### On `llms.txt` — honest correction to my own work

I built you an `llms.txt` two days ago. **It is not a citation lever and I should not have implied
it might be.** The evidence:

- **John Mueller (Google), 2025:** no AI system currently uses `llms.txt`; compared it to meta keywords.
- **Gary Illyes (Google), July 2025:** Google has no plans to support it.
- **SE Ranking, 300k-domain study:** of the 50 most AI-cited domains, exactly **one** had an `llms.txt`.
- **OtterlyAI server-log audit:** `/llms.txt` accounted for **0.1%** of AI-bot traffic (84 of 62,100 requests).
- Google's AI optimization guide lists creating `llms.txt` under **myths** explicitly.

Keep the file — it costs nothing and buys optionality if a provider adopts the standard. But score it
at zero, and don't let it substitute for the content work. The genuinely useful part of what I wrote
is the "Notes for AI assistants" block that tells assistants what you *don't* claim.

---

## Top 5 highest-impact changes

**1. Decide the entity question.** (Business decision, blocks everything else.)
Either commit to disambiguation — founder-forward positioning, a tight vertical + geography, and a
consistent `Epoch Digital · epochdigital.ai` lockup everywhere — or reassess the name against
`epochdm.com` now, while the brand has near-zero accrued equity. Every downstream GEO investment
compounds into whichever answer you pick, so pick first.

**2. Publish first-hand content that only you have.**
Google's stated test is unique, non-commodity, lived experience. You deploy these systems; write up
actual deployments — what the voice agent got wrong in week one, the real call-volume numbers, what
integration broke. Three or four honest 800–1,200 word build logs would move citability further than
every markup change on this list combined. 408 words cannot be cited.

**3. Put a person on the site.**
Founder byline, a real bio with specific background, and `Person` schema with `sameAs` pointing at
whatever profiles you own. This simultaneously fixes the E-E-A-T floor *and* is the strongest
available entity-disambiguation signal — "the Epoch Digital founded by ___" is a much easier thing
for a retriever to resolve than a bare company name shared by seven organizations.

**4. Fix dates, starting with the stale one.**
`© 2025` → current year, and add real `datePublished` / `dateModified` to any content you publish.
Recency is ~3× on citation likelihood; right now you have no date signal at all and the one visible
year is wrong, which reads as abandoned.

**5. Clear the eligibility floor.**
Verify in Google Search Console and submit the sitemap; verify in Bing Webmaster Tools and enable
IndexNow. There is no separate "AI index" — a page must be indexed and snippet-eligible to appear in
any AI surface. This is a prerequisite, not an optimization.

---

## Schema recommendations

Ordered by value, and deliberately restrained — Google explicitly warns against over-investing in
structured data specifically for AI features.

1. **`Person` (founder)** with `jobTitle`, `description`, `worksFor` → the existing Organization
   `@id`, and `sameAs`. Highest-value addition available.
2. **`Organization.sameAs`** — populate the moment any owned profile exists. This is the entity
   disambiguation mechanism.
3. **`Organization.foundingDate`** and **`areaServed`** — both currently omitted because nothing on
   the page states them. Adding them to the page first, then the schema, narrows the entity.
4. **`Article` / `BlogPosting`** with `author` → the `Person` `@id`, plus `datePublished` and
   `dateModified`, on each build log from change #2.
5. **FAQ content — but not `FAQPage` schema.** Build the Q&A section, since question-form headings
   and self-contained answers are what actually get retrieved. Don't expect rich results: Google
   restricted FAQ rich results to government and health sites.

Do **not** add `aggregateRating`, `review`, or `award` markup. You have no reviews to represent, and
fabricated rating markup is a manual-action risk.

---

## Content reformatting — specific changes

| # | Where | Change |
|---|---|---|
| 1 | Hero, first 60 words | Add a definition block: "An AI receptionist is …" — the highest-extraction sentence pattern, placed in the first 30% of the page where ~44% of citations originate |
| 2 | Service cards | Give the four orphaned `H3`s a governing `H2` (e.g. "What Epoch Digital automates"), fixing the hierarchy break |
| 3 | `#use-cases` | Promote the two `H4`s to `H3` to close the skipped level |
| 4 | Each of the 4 services | Expand from ~20 words to a self-contained 134–167 word block that answers the service's question without needing surrounding context |
| 5 | New section | Comparison table: AI receptionist vs. human answering service vs. voicemail, across cost / coverage / booking / escalation |
| 6 | New section | 5–7 question-form `H2`s with direct 40–60 word answers ("How long does setup take?", "What happens when the AI can't answer?") |
| 7 | The two statistics | Either cite the primary source inline or cut them. Uncited numbers on a commercial page are a quality-rater flag |
| 8 | Footer | `© 2025` → current year |

---

## What not to do

Google's AI optimization guide explicitly rejects these, and they circulate widely as GEO advice:

- Creating AI-specific markup files as a ranking play (including `llms.txt`)
- "Chunking" content into small pieces for AI consumption
- Rewriting copy with AI-specific phrasings or long-tail keyword variations
- Chasing inauthentic mentions across blogs, forums and videos
- Over-investing in structured data specifically for AI features

---

## Method / limitations

- Content, heading, schema and crawler analysis run against the live HTML at
  `https://www.epochdigital.ai/` on 2026-08-10.
- Brand-presence findings come from live web search across general, Reddit and YouTube queries.
  **Absence of evidence is not proof of zero presence** — a private LinkedIn page or an unindexed
  profile would not surface.
- Indexation status is inferred from search visibility, not confirmed. **Verify in Search Console**
  before treating "not indexed" as fact.
- No DataForSEO / SE Ranking API access in this session, so no live LLM-mention tracking or AI
  Share-of-Voice measurement. Scores are criterion-based, not measured citation rates.
