# course-planner-agent

**Status: work in progress — active side project, not yet functional end-to-end.**

A degree-planning agent for College of Charleston's School of Computing. Goal: take a
student's completed coursework and target major, and produce a valid semester-by-semester
plan that satisfies gen-ed, major, and first-year requirements — with an LLM handling
natural-language input/output and a solver owning the actual correctness of the plan.

## Motivation

As a student, I mapped out every class I'll take through graduation. It wasn't
difficult, but it was time-consuming: requirements are spread across many catalog pages,
and every choice affects what has to happen in later semesters. Most students don't do
this, so they go semester to semester hoping everything adds up and that they'll
graduate on time. Advisors help, but they work with a lot of students and, like anyone,
occasionally make mistakes. This tool aims to do that mapping for every student: it lays
out the decisions they actually have and finds a path to graduation that fits their
situation, with the correctness checked by a solver instead of by hand.

## The technical problem

Degree requirements are published as web pages that mix structured course lists with
narrative policy text, and the requirement logic (e.g. "take A and B, OR take C") is
written for humans rather than programs. Turning that into something a program can
reason about — and then solving the scheduling constraints — is the core problem.

## Design

```
fetch  ->  parse  ->  walk (extract structure)  ->  JSON  ->  solver
                                                               ^
                                                               |
                                                       LLM (interpreter only)
```

- **Data pipeline** — fetches catalog pages, caches them locally, and extracts structured
  requirement data from them.
- **Solver (planned)** — owns all hard-constraint correctness (prerequisites, term
  offerings, requirement options, credit limits). This is deliberate: the LLM never
  decides whether a plan is valid, it only turns messy student input into structured
  preferences and explains solver output conversationally. Keeping "is this plan correct"
  out of the LLM's hands is the main architectural bet of this project. One shared
  constraint model supports two modes:
  - **On-time plan** — graduate within 8 total semesters while fitting the student's
    preferences (classes per semester, course balance, ranked course choices with
    backups). Only the remaining semesters are planned, so a student with 2 semesters
    completed gets a 6-semester plan.
  - **Fastest plan** — fewest remaining semesters possible (A\* search with a
    prerequisite-chain heuristic), with preferences used to break ties.

  When a student's preferences can't be met, the solver reports which constraint causes
  the conflict and what would fix it.
- **LLM interface (planned)** — conversational layer on top of the solver.

Requirement logic is designed to be modeled as a tree end to end, so that "pick one
complete option" choices aren't lost by flattening requirements into a simple list.

## Current state

Working:
- Fetching and local caching of the catalog pages for the 10 School of Computing majors.
- Parsing cached pages and grouping courses under their requirement sections (currently
  a flat list of sections, not yet a tree).

In progress:
- Extracting the "choose one of these" logic from the pages into the requirement tree.
- Fetching the general policy pages (gen eds, first-year experience, academic
  regulations, etc.) — URLs are in `main.py` but not yet wired in.

Not started:
- JSON output (`data.json` is a placeholder), solver, LLM layer, tests.

## Running it

```
pip install playwright beautifulsoup4
playwright install chromium
python main.py
```

This currently fetches (or loads from `cache/`) each major's catalog page and prints the
number of courses found. It does not write any output yet.

## Roadmap

1. Finish the data pipeline and emit the requirement tree as JSON.
2. Handle the special-case requirements that don't fit the standard course-list format.
3. Build the constraint model and both solver modes (on-time and fastest) over the
   emitted JSON.
4. Add the LLM interpreter layer on top.
5. Add tests.

## Stack

Python, Playwright, BeautifulSoup.
