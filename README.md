# gioiazheng.github.io

[![Deploy](https://github.com/GioiaZheng/GioiaZheng.github.io/actions/workflows/deploy.yml/badge.svg)](https://github.com/GioiaZheng/GioiaZheng.github.io/actions/workflows/deploy.yml)

Source for [gioiazheng.github.io](https://gioiazheng.github.io/) — personal
technical site. Static, content-first, no analytics, no trackers.

## Stack

- [Astro](https://astro.build/) v7, content collections + Markdown
- Vanilla CSS, no UI framework
- Deployed to GitHub Pages via the official `actions/deploy-pages` action

## Quickstart

Requires Node `>=22.23.4` (pinned to `22.23.4` in `.nvmrc`).

```sh
git clone https://github.com/GioiaZheng/GioiaZheng.github.io.git
cd GioiaZheng.github.io

npm install
npm run dev      # local server on http://localhost:4321
npm run build    # production build into ./dist
npm run check:links # validate links in the built site without network access
npm run preview  # serve ./dist locally
```

Expected output:

```text
Local: http://localhost:4321/
```

## Editing content

Content lives under [`src/content/`](src/content/) as Markdown with
frontmatter — the schema is in
[`src/content.config.ts`](src/content.config.ts).

- **Projects** → `src/content/projects/<slug>.md`. Required fields:
  `title`, `summary`, `order`, `status`, optional `repo` / `featured` / `tags`.
- **Writing** → `src/content/writing/<slug>.md`. Required fields:
  `title`, `summary`, `status` (`draft` / `planned` / `published`).

Adding a file is enough — the routes at `/projects/<slug>/` and
`/writing/<slug>/` are generated from the collection.

## Site structure

```
src/
  layouts/Base.astro           # html wrapper, header, footer
  components/                  # Nav, Footer
  pages/
    index.astro                # home
    projects/index.astro       # projects list
    projects/[slug].astro      # one project per markdown file
    writing/index.astro        # writing list
    writing/[slug].astro       # one note per markdown file
    contact.astro
  content.config.ts            # collection schemas
  content/
    projects/*.md
    writing/*.md
  styles/global.css            # all site styles
public/
  cv/Gioia_Zheng_CV.pdf        # served at /cv/Gioia_Zheng_CV.pdf
```

## Deployment

Push to `main`. The workflow in
[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) builds the
site and publishes the `dist/` artifact to Pages.

Before upload, CI runs Astro's type/content checks and a post-build link
integrity check. Internal pages, assets, and anchors must resolve. External
project URLs keep their schema validation, but transient network responses do
not block deployment.

Repository setting required once: **Settings → Pages → Source → GitHub Actions**.


## CV versions

See [CV version guide](docs/cv-versions.md). The default CV is the general research version; robotics applications use a separate file.
