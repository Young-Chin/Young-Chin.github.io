# Blog Card Editorial Covers Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the homepage blog card emoji covers with restrained editorial-style abstract covers while keeping the existing data model and section structure intact.

**Architecture:** Keep the existing homepage post loop in [`_pages/about.md`](/Users/gechin/Code/Young-Chin.github.io/_pages/about.md), but swap the per-post mapping from inline gradient-plus-emoji values to semantic cover palette and motif classes. Rebuild the blog card presentation in [`_sass/notion.scss`](/Users/gechin/Code/Young-Chin.github.io/_sass/notion.scss) so the title lives inside the cover composition and the lower card strip becomes structural rather than primary.

**Tech Stack:** Jekyll, Liquid templates, Sass, Minimal Mistakes theme overrides

---

### Task 1: Prepare workspace and plan artifacts

**Files:**
- Modify: `.gitignore`
- Create: `docs/superpowers/plans/2026-06-14-blog-card-editorial-covers.md`
- Create: `.worktrees/codex/blog-editorial-cards/` via git worktree

- [ ] **Step 1: Ensure project-local worktrees are ignored**

```gitignore
.worktrees/
```

- [ ] **Step 2: Verify ignore rule**

Run: `git check-ignore -v .worktrees`
Expected: output references `.gitignore` and `.worktrees/`

- [ ] **Step 3: Create isolated worktree on a codex branch**

Run: `git worktree add .worktrees/codex/blog-editorial-cards -b codex/blog-editorial-cards`
Expected: worktree created and checked out on new branch

- [ ] **Step 4: Record the implementation plan in the repo**

This file is the plan artifact and should remain committed with the work.

- [ ] **Step 5: Commit setup artifacts**

```bash
git add .gitignore docs/superpowers/plans/2026-06-14-blog-card-editorial-covers.md
git commit -m "chore: prepare blog card redesign workspace"
```

### Task 2: Replace emoji cover mapping with editorial cover tokens

**Files:**
- Modify: `_pages/about.md`

- [ ] **Step 1: Write the failing expectation checklist**

Manually verify the current blog loop still contains:

```liquid
{% assign card_icon = '' %}
...
<span class="notion-blog-card-icon">{{ card_icon }}</span>
```

Failure condition: the old emoji-based structure is still present, which proves the redesign has not been applied yet.

- [ ] **Step 2: Remove emoji-specific assignments and add semantic cover tokens**

Replace the blog loop mapping with semantic values such as:

```liquid
{% assign card_palette = 'palette-sand' %}
{% assign card_motif = 'motif-frame' %}
{% assign card_label = 'Notes' %}
```

Per known post, override these tokens with lightweight, human-readable variants rather than inline icon strings.

- [ ] **Step 3: Move title into the cover area**

Render the card with a structure like:

```liquid
<a href="{{ base_path }}{{ post.url }}" class="notion-blog-card notion-blog-card--{{ card_palette }} notion-blog-card--{{ card_motif }} reveal" title="{{ post.title }}">
  <div class="notion-blog-card-image">
    <div class="notion-blog-card-cover-meta">{{ card_label }}</div>
    <h3 class="notion-blog-card-title">{{ short_title }}</h3>
    <div class="notion-blog-card-mark" aria-hidden="true"></div>
  </div>
  <div class="notion-blog-card-content">
    <span class="notion-blog-card-link">Read article</span>
  </div>
</a>
```

- [ ] **Step 4: Verify old emoji markup is gone**

Run: `rg -n "card_icon|notion-blog-card-icon" _pages/about.md`
Expected: no matches

- [ ] **Step 5: Commit template changes**

```bash
git add _pages/about.md
git commit -m "feat: redesign blog card markup"
```

### Task 3: Build editorial cover styling

**Files:**
- Modify: `_sass/notion.scss`

- [ ] **Step 1: Confirm the existing card styles are still the emoji-driven baseline**

Manually verify the current style block includes:

```scss
.notion-blog-card-icon {
  font-size: 2rem;
}
```

Failure condition: old icon-dependent styling is still in place.

- [ ] **Step 2: Redesign the card shell and cover composition**

Update the blog card styles so they include:

```scss
.notion-blog-card {
  display: grid;
  grid-template-rows: minmax(210px, auto) auto;
}

.notion-blog-card-image {
  padding: 1rem;
  align-items: flex-start;
  justify-content: flex-start;
}
```

Add unified shell polish, calmer shadows, and a restrained lower strip.

- [ ] **Step 3: Add title, meta, and decorative motif layers**

Implement classes for:

```scss
.notion-blog-card-cover-meta { ... }
.notion-blog-card-title { ... }
.notion-blog-card-mark { ... }
```

Use pseudo-elements and the `.notion-blog-card--<palette>` / `.notion-blog-card--<motif>` modifiers to create sparse editorial motifs such as frames, circles, vertical bars, and soft highlight overlays.

- [ ] **Step 4: Update responsive behavior**

Preserve the existing two-column mobile/tablet collapse, and reduce cover/title sizing where needed so the cards remain readable at smaller widths.

- [ ] **Step 5: Verify old icon styles are gone**

Run: `rg -n "notion-blog-card-icon" _sass/notion.scss`
Expected: no matches

- [ ] **Step 6: Commit styling changes**

```bash
git add _sass/notion.scss
git commit -m "feat: add editorial blog card styles"
```

### Task 4: Verify the redesign end-to-end and prepare final commit

**Files:**
- Verify: `_pages/about.md`
- Verify: `_sass/notion.scss`
- Verify: homepage rendering

- [ ] **Step 1: Install missing Jekyll dependency if needed**

Run: `bundle install`
Expected: installs `jekyll (~> 4.3)` and project dependencies without errors

- [ ] **Step 2: Build the site**

Run: `bundle exec jekyll build`
Expected: exit code 0 and generated site without Liquid or Sass errors

- [ ] **Step 3: Serve the site locally for browser inspection**

Run: `bundle exec jekyll serve --host 127.0.0.1 --port 4000`
Expected: local preview available at `http://127.0.0.1:4000`

- [ ] **Step 4: Inspect the homepage blog section**

Use the in-app browser to confirm:

```text
- No emoji visible in blog cards
- Each card has a distinct but related abstract cover
- Title hierarchy reads clearly inside the cover
- Hover polish remains subtle
- Desktop and narrow widths remain balanced
```

- [ ] **Step 5: Review diff and create final commit**

```bash
git status --short
git diff -- _pages/about.md _sass/notion.scss .gitignore docs/superpowers/plans/2026-06-14-blog-card-editorial-covers.md
git add .gitignore docs/superpowers/plans/2026-06-14-blog-card-editorial-covers.md _pages/about.md _sass/notion.scss
git commit -m "feat: refresh blog cards with editorial covers"
```
