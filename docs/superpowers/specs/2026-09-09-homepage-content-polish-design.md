# Homepage Content Polish Design

## Goal

Polish the first-version homepage content supplied in `Desktop/info.txt` and
apply it to the existing personal homepage without changing the current
Notion-inspired visual design or information architecture. Provide a standalone
HTML preview that can be opened locally without Jekyll.

## Scope

- Update the homepage hero copy, location, expertise cards, and CV modal in
  `_pages/about.md`.
- Keep the existing news timeline, blog loop, card mappings, navigation, and
  interaction behavior unless a wording correction is required for consistency.
- Update site-level author metadata in `_config.yml` where the existing values
  conflict with the revised homepage content.
- Create `preview/homepage-preview.html`, a static browser preview using the
  same page structure, content, image, responsive behavior, and CV modal.

## Content Decisions

- Use polished English throughout the homepage.
- Hero positioning: Yang Chin is currently seeking roles in multimodal/omni
  models, AI agents, and AIGC.
- Experience summary: one year as a Senior Engineer at Quwan Technology in
  Guangzhou, preceded by work at MagicLight on long-form story video generation.
- Expertise categories: Multimodality, AIGC, AI Agents, and AI Security.
- Correct the CV timeline to AllVoiceLab/Quwan Technology ending in August
  2026, and clarify responsibilities without inventing metrics.
- Preserve project names, external URLs, and the existing footer message.

## Preview Requirements

- The file must render by opening it directly from the filesystem.
- Use relative asset paths so the existing profile image displays.
- Include responsive desktop/mobile layout, social links, expertise cards, news,
  blog cards, and a working CV modal with close and Escape behavior.

## Verification

- Check the edited homepage for stale role/company wording and malformed HTML.
- Validate the standalone preview with a local browser/server and confirm the
  profile image, responsive sections, links, and CV modal render.
