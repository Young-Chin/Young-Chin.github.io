# Blog Card Editorial Covers Design

## Summary

Refresh the homepage blog gallery so each card feels like a lightweight editorial cover instead of a gradient tile with a centered emoji.

This redesign is visual only. It does not change post content, card count, post ordering, metadata requirements, or homepage information architecture.

## Design Read

Reading this as: a personal homepage blog section for fast-scanning visitors, with a restrained editorial language, leaning toward a clean Notion-like system with more cover-like visual hierarchy.

## Dials

- `DESIGN_VARIANCE: 6`
- `MOTION_INTENSITY: 4`
- `VISUAL_DENSITY: 3`

These values fit an editorial/blog subsection inside an already minimal homepage. The layout should feel more intentional, but not more experimental than the rest of the page.

## Goals

- Replace emoji-as-image with a more refined cover treatment
- Keep the blog section visually aligned with the rest of the homepage
- Increase distinction between posts through composition, color, and abstract motifs
- Improve perceived quality without requiring real thumbnails or new CMS fields

## Non-Goals

- No changes to post content or markdown files
- No new fields in front matter
- No changes to the number of posts shown
- No new interactive behavior beyond current hover polish
- No shift to image-heavy cards or external illustration assets

## Current Problems

- The card image area depends almost entirely on a single emoji, so every card reads as the same template with a different background
- The visual weight sits in the emoji instead of the composition
- The title and image area feel disconnected, which weakens the sense of each card as a distinct piece of writing
- The current cards are tidy, but not memorable

## Chosen Direction

Use an "Editorial Covers" direction for the blog cards.

Each card should resemble a compact magazine or notebook cover:

- A cover area with low-saturation color, abstract geometric motifs, and subtle texture
- The post title treated as part of the cover composition rather than as a separate caption-only block
- A restrained footer/content strip that anchors the card and preserves scanability
- A unified radius, border, and shadow system across all cards

This keeps the page calm and structured while making the blog area feel more designed.

## Visual System

### Color

- Keep one calm neutral family that already matches the homepage
- Use soft per-post cover palettes with muted contrast
- Avoid neon gradients, AI-purple glow, or high-saturation accents

### Shape

- Preserve the existing rounded card language
- Use simple geometric motifs such as blocks, lines, circles, frames, and soft highlight overlays
- Keep motif scale intentional and sparse so the cards still feel editorial rather than playful

### Typography

- Title becomes the hero element inside the cover area
- Cover typography should feel compact and poster-like, not oversized
- Supporting text remains minimal and secondary

### Motion

- Keep hover movement subtle
- Add polish through light shadow and highlight changes instead of stronger displacement
- Preserve reduced-motion-safe behavior by relying on simple transitions only

## Content and Data Handling

The homepage will continue using the existing loop over `site.posts`.

Per-post mapping remains lightweight and local to the homepage template:

- Replace `card_icon` usage with visual tokens such as a palette class and motif class
- Keep the existing short-title overrides where needed
- Do not require dates, tags, or summaries to render the card

## Layout Strategy

The card remains a single-column object inside the existing 3-column grid on desktop and existing responsive collapse on smaller screens.

Within each card:

1. The top cover area becomes the primary visual zone
2. The title sits inside that zone with better hierarchy
3. The lower strip remains restrained and mostly structural

This avoids changing the section architecture while improving card presence.

## Implementation Outline

### Template changes

Update [`_pages/about.md`](/Users/gechin/Code/Young-Chin.github.io/_pages/about.md) to:

- Remove emoji output
- Map each known post to a cover palette and motif variant
- Render the title inside the cover section
- Keep the card markup simple and maintainable

### Styling changes

Update [`_sass/notion.scss`](/Users/gechin/Code/Young-Chin.github.io/_sass/notion.scss) to:

- Redesign `.notion-blog-card-image` into a cover composition surface
- Add motif variants using pseudo-elements and layered shapes
- Rebalance padding, hierarchy, and hover polish
- Preserve current responsiveness and theme compatibility

## Risks and Guardrails

- The new cards must not outshine the rest of the page to the point that the homepage feels visually inconsistent
- Decorative motifs must stay abstract and lightweight, otherwise the section will feel busy
- Because no real images are being added, the title composition has to carry enough identity on its own
- The implementation should avoid brittle inline styling that becomes hard to extend when new posts are added

## Verification

- Check the homepage section on desktop and mobile widths
- Confirm that the cards still read clearly in both light and dark color-scheme contexts currently supported by the site
- Verify that all six cards feel related but not identical
- Verify that hover polish remains smooth and restrained
- Confirm that no emoji remains in the visible card covers

## Scope Summary

This work is intentionally narrow:

- Files expected to change: [`_pages/about.md`](/Users/gechin/Code/Young-Chin.github.io/_pages/about.md), [`_sass/notion.scss`](/Users/gechin/Code/Young-Chin.github.io/_sass/notion.scss)
- No post markdown changes
- No navigation, layout, or CV section changes
