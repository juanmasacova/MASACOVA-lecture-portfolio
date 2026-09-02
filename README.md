# MEGR 2157 – Design Portfolio Template

This repository is a plain-HTML site built with Jekyll (which GitHub Pages runs natively) with the Analyze / Decide / Communicate framework built into every assignment page. Every page is hand-written HTML — the shared sidebar/header live in `docs/_includes/`, so you get full CSS/JS freedom on each page without duplicating the nav everywhere. The rendered site lives in `docs/`; this README is just for people working with the repo itself.

## Preview locally

Requires Ruby and Bundler.

```bash
bundle install
bundle exec jekyll serve --source docs --destination _site
```

Then open http://127.0.0.1:4000 in your browser. Editing any `.html` file, or `docs/assets/css/style.css`, reloads live.

## Publish

Push to `main` — the included GitHub Actions workflow (`.github/workflows/deploy.yml`) builds the site with Jekyll and publishes it to GitHub Pages automatically.

## Structure

```
MEGR-2156-7-template/
├── .github/
│   └── workflows/
│       └── deploy.yml          <- GitHub Actions: auto-builds and deploys to Pages on every push
├── docs/                       <- Jekyll source root
│   ├── _config.yml             <- site title/description/baseurl
│   ├── _data/nav.yml           <- sidebar nav entries (edit this to add/reorder nav links)
│   ├── _includes/              <- shared head/nav/footer HTML
│   ├── _layouts/default.html   <- page wrapper (head + nav + content + footer)
│   ├── assets/
│   │   ├── css/style.css       <- all site styling — edit freely
│   │   └── js/nav.js           <- mobile nav toggle
│   ├── index.html              <- Portfolio homepage (About Me, Homepage Identity, Decision Standard)
│   ├── portfolio-overview.html <- Running index of all assignments with status
│   ├── aboutme/
│   │   └── index.html          <- About Me page
│   └── assignments/
│       ├── A01/
│       │   └── index.html      <- A1: Build Your Professional Portfolio
│       ├── A02/
│       │   └── index.html      <- A2: Truss Stress Analysis
│       ├── A03/
│       │   └── index.html      <- A3: Parametric Design and FEA
│       ├── A04/
│       │   └── index.html      <- A4: Motor Mount
│       ├── A05/
│       │   └── index.html      <- A5: Bracket Stress
│       ├── A06/
│       │   └── index.html      <- A6: Bracket Drawing
│       ├── A07/
│       │   └── index.html      <- A7: Bracket FEA
│       ├── A08/
│       │   └── index.html      <- A8: Gears
│       ├── A09/
│       │   └── index.html      <- A9: Pulleys
│       ├── A10/
│       │   └── index.html      <- A10: Lead Screw Translating System
│       └── A11/
│           └── index.html      <- A11: Motor Selection
├── templates/
│   └── assignment-template.html <- Blank assignment page for reference (not published)
├── .gitignore
├── Gemfile                     <- Ruby/Jekyll dependency
└── README.md                   <- This file
```

## Adding or renaming an assignment

1. Add a new folder under `docs/assignments/` with an `index.html` (copy `templates/assignment-template.html` as a starting point).
2. Add a matching entry to `docs/_data/nav.yml` under `Assignments: children:` — this is what makes it appear in the sidebar on every page.
