# course-planner-agent

**Status: work in progress — active side project, not yet functional end-to-end.**

A degree-planning agent for College of Charleston's School of Computing. Goal: take a
student's completed coursework and target major, and produce a valid semester-by-semester
plan that satisfies gen-ed, major, and First-Year Experience requirements — with an LLM
handling natural-language input/output and a solver owning the actual correctness of the plan.

## Why

CofC's course catalog (an Acalog CMS instance) mixes structured course lists with narrative
policy text, sits behind bot protection that blocks plain HTTP fetches, and encodes
requirement logic (e.g. "take A and B, OR take C") in prose rather than data. Turning that
into something a program can reason about — and then actually solving the scheduling
constraints — is the core problem.

## Design

```
fetch (Playwright)  ->  parse (BeautifulSoup)  ->  walk (extract structure)  ->  JSON  ->  solver
                                                                                      ^
                                                                                      |
                                                                              LLM (interpreter only)
```

- **fetch.py** — headless-browser fetch of catalog pages, cached to disk so parsing/dev
  work doesn't refetch on every run.
- **parse.py** — parses cached HTML with BeautifulSoup, pulls out course list elements.
- **walker.py** — walks the parsed tree to group requirements by section.
- **Solver (not started)** — will own all hard/soft constraint correctness (prerequisites,
  credit minimums, AND/OR requirement trees). This is deliberate: the LLM never decides
  whether a plan is valid, it only normalizes messy student input and explains solver output
  conversationally. Keeping "is this plan correct" out of the LLM's hands is the main
  architectural bet of this project.
- **LLM interface (not started)** — conversational layer on top of the solver.

Requirement logic (e.g. "lecture AND lab, OR an alternate course") is modeled as an AND/OR
tree end to end so that "pick one complete branch" logic isn't lost by flattening it into a
simple list.

## Current state

Working:
- Fetches and locally caches all target catalog pages (6 policy/gen-ed pages, 10 major
  program pages) through Playwright, with basic validation that a fetch actually returned
  real content instead of a bot-block page.
- Parses cached pages and extracts course list elements.

Not working yet:
- Walker currently logs the elements it matches but doesn't group them into structured
  output or return anything usable.
- No JSON emission, no solver, no LLM layer. These are designed (see above) but unbuilt.
- No tests.

## Next steps

1. Finish the walker: group matched elements by section header, emit the AND/OR requirement
   tree as JSON.
2. Model the FYE (First-Year Experience) requirement, which has real branching logic:
   students either take a First-Year Seminar, a themed stand-alone course, or a Learning
   Community, each paired with a synthesis seminar corequisite — plus transfer/age-based
   waivers.
3. Build a solver over the emitted JSON.
4. Add the LLM interpreter layer on top.

## Stack

Python, Playwright, BeautifulSoup.
