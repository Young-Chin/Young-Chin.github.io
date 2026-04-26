# Young Chin Personal Homepage

A Notion-styled personal portfolio built with Jekyll and hosted on GitHub Pages.

Originally forked from [academicpages](https://github.com/academicpages/academicpages.github.io), then fully redesigned into a clean, minimal Notion-inspired layout.

**Live site:** https://young-chin.github.io/

---

## Architecture

```
.
├── _config.yml              # Site configuration (title, defaults, plugins)
├── _pages/
│   └── about.md             # Homepage content (Hero, Expertise, News, Blog, CV modal)
├── _posts/                  # Blog posts (6 articles)
├── _layouts/
│   ├── notion.html          # Homepage layout
│   └── notion-post.html     # Blog post layout
├── _sass/
│   └── notion.scss          # All custom Notion-style CSS
├── _includes/
│   └── head.html            # HTML head template
├── assets/css/main.scss     # SCSS entry (imports notion.scss + theme base)
├── images/                  # Images used by the site
│   ├── personal photo.jpeg  # Hero profile photo
│   └── Optimization.png     # Used by a blog post
├── files/                   # Static files (PDFs, etc.)
│   └── SimplexMethod.pdf
└── _data/
    └── navigation.yml       # Nav links (currently unused by Notion layout)
```

### Key files to edit

| File | Purpose |
|------|---------|
| `_pages/about.md` | **Main homepage**. Edit your bio, work experience, news, expertise cards, blog gallery, and CV modal content here. |
| `_posts/*.md` | **Blog articles**. Add or edit posts. Front matter controls permalink, date, and tags. |
| `_sass/notion.scss` | **All custom styles**. Colors, fonts, spacing, card hover effects, modal animations, responsive breakpoints. |
| `_config.yml` | Site-wide config. `defaults` section sets `layout: notion-post` for blog posts. |

---

## How to modify content

### Edit homepage text

Open `_pages/about.md` and edit the HTML/Liquid directly. The page is divided into sections:

- **Hero** — name, location, social icons, bio paragraph
- **Expertise** — 2x2 skill cards. Hover reveals bullet list
- **News** — timeline items with date tags
- **Blog** — auto-generated card gallery from `_posts/`
- **CV Modal** — inline CV content shown in a popup
- **Footer** — closing quote + copyright

> The site uses Jekyll + GitHub Pages. After pushing changes, wait 1–2 minutes for the site to rebuild.

### Add or edit a blog post

Create a new file in `_posts/` with the naming convention `YYYY-MM-DD-title.md`:

```markdown
---
title: 'Your Post Title'
date: 2024-01-15
permalink: /posts/category/permalink-name
tags:
  - Tag1
  - Tag2
---

Your markdown content here.
```

The homepage blog gallery auto-picks up new posts (latest 6). If you want a custom card color/emoji for the new post, edit the `{% if post.title contains ... %}` block in `_pages/about.md`.

### Modify styles

All custom styles live in `_sass/notion.scss`. The original academicpages SASS files are kept in `_sass/` but overridden or hidden by the Notion layout.

Common tweaks:
- Page width: `.notion-page { max-width: ... }`
- Hero title size: `.notion-hero-title { font-size: ... }`
- Card colors: CSS variables `--card-bg` / `--card-border` set inline on each card in `about.md`
- Hover animation: `.notion-expertise-card:hover` and `.notion-blog-card:hover`

### Add images or files

- Images → `images/`, reference with `{{ base_path }}/images/filename.jpg`
- PDFs/downloads → `files/`, reference with `{{ base_path }}/files/filename.pdf`

---

## Deployment

The site is deployed via **GitHub Pages** automatically on every push to `master`.

No local build required. Just push and wait 1–2 minutes.

If you want to preview locally:

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

---

## License

The original academicpages theme is © Michael Rose, MIT License.
Custom Notion-style redesign and content are personal.
