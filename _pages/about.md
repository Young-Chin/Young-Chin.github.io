---
permalink: /
title: "Home"
layout: notion
redirect_from:
  - /about/
  - /about.html
---

{% include base_path %}

<div class="notion-page">

  <!-- Hero Section -->
  <section class="notion-section notion-hero reveal">
    <div class="notion-columns">
      <div class="notion-column">
        <h1 class="notion-hero-title" dir="auto">Young Chin | Bob | 秦洋</h1>
        <div class="notion-hero-social">
          <p class="notion-hero-location">SZ, China</p>
          <a href="mailto:yangqinbob@gmail.com" class="notion-social-icon" title="Email" target="_blank" rel="noopener">
            <i class="fas fa-envelope"></i>
          </a>
          <a href="https://github.com/Young-Chin" class="notion-social-icon" title="GitHub" target="_blank" rel="noopener">
            <i class="fab fa-github"></i>
          </a>
          <a href="https://x.com/Young_Chin_Bob" class="notion-social-icon" title="X" target="_blank" rel="noopener">
            <i class="fab fa-twitter"></i>
          </a>
          <button class="notion-button" type="button" onclick="openCvModal()">View CV</button>
        </div>
        <div class="notion-hero-body">
          <p>Currently seeking opportunities in multimodal and omni models, AI agents, and AIGC.</p>
          <p>Previously spent one year as a Senior Engineer at <a href="https://www.quwangroup.com" class="notion-link">Quwan Technology</a> in Guangzhou, focusing on multimodal understanding and AI agent systems.</p>
          <p>Started my career at <a href="https://www.magiclight.ai" class="notion-link">MagicLight</a>, working on AIGC for long-form story video generation.</p>
        </div>
      </div>
      <div class="notion-column notion-column-shrink">
        <div class="notion-hero-photo reveal-scale">
          <img src="{{ base_path }}/images/personal photo.jpeg" alt="Yang Chin">
        </div>
      </div>
    </div>
  </section>

  <!-- Expertise Section -->
  <section class="notion-section">
    <h2 class="notion-h2 reveal">Expertise</h2>
    <div class="notion-expertise-grid reveal-stagger">
      <div class="notion-expertise-card reveal">
        <h3 class="notion-expertise-card-title">Multimodality</h3>
        <ul class="notion-expertise-card-list">
          <li>Vision-Language and Omni Models</li>
          <li>VLM-based OCR</li>
          <li>Multimodal Speaker Diarization</li>
          <li>Long Video Understanding</li>
        </ul>
      </div>
      <div class="notion-expertise-card reveal">
        <h3 class="notion-expertise-card-title">AIGC</h3>
        <ul class="notion-expertise-card-list">
          <li>ID Preserving & Face Swap</li>
          <li>Regional Controlled Generation</li>
          <li>Subject-Consistent Video Generation</li>
        </ul>
      </div>
      <div class="notion-expertise-card reveal">
        <h3 class="notion-expertise-card-title">AI Agents</h3>
        <ul class="notion-expertise-card-list">
          <li>Agent Frameworks</li>
          <li>Memory Systems</li>
          <li>Personality and User Modeling</li>
        </ul>
      </div>
      <div class="notion-expertise-card reveal">
        <h3 class="notion-expertise-card-title">AI Security</h3>
        <ul class="notion-expertise-card-list">
          <li>Multimedia Forensics</li>
          <li>Deepfake Detection</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- News Section -->
  <section class="notion-section">
    <h2 class="notion-h2 reveal">News</h2>
    <div class="notion-news-list reveal">
      <div class="notion-news-item">
        <span class="notion-news-date">Jun 2026</span>
        <span class="notion-news-text">Open-sourced <a href="https://github.com/Young-Chin/know-each-other" class="notion-link">Know Each Other</a>, a Claude skill that builds persistent psychological profiles so AI can truly know you across sessions.</span>
      </div>
      <div class="notion-news-item">
        <span class="notion-news-date">May 2026</span>
        <span class="notion-news-text">Open-sourced <a href="https://github.com/Young-Chin/DeepTalk-Agent" class="notion-link">DeepTalk Agent</a>, a fully local voice AI assistant running on macOS Apple Silicon with MLX.</span>
      </div>
      <div class="notion-news-item">
        <span class="notion-news-date">Sep 2025</span>
        <span class="notion-news-text">Joining <a href="https://www.allvoicelab.cn/" class="notion-link">AllVoiceLab</a> at <a href="https://www.quwangroup.com/" class="notion-link">Quwan Technology</a> , All Voice Lab Team.</span>
      </div>
      <div class="notion-news-item">
        <span class="notion-news-date">Sep 2024</span>
        <span class="notion-news-text">Invited interview as <em>Outstanding Postgraduate Students</em> in MUST. <a href="https://www.youtube.com/watch?si=aU1BVE1TQiOXAV9W&v=KoJ63k_ffKs&feature=youtu.be" class="notion-link">Watch video</a>.</span>
      </div>
      <div class="notion-news-item">
        <span class="notion-news-date">Jun 2024</span>
        <span class="notion-news-text">Joining <a href="https://www.magiclight.ai" class="notion-link">MagicLight</a> to build AIGC platform. Try <a href="https://aibrm.com" class="notion-link">白日梦AI</a>.</span>
      </div>
      <div class="notion-news-item">
        <span class="notion-news-date">Nov 2023</span>
        <span class="notion-news-text"><strong>MAPS</strong> won <strong>Bronze Award</strong> and <strong>Best Application Award</strong> at GBA IT Application Competition.</span>
      </div>
      <div class="notion-news-item">
        <span class="notion-news-date">Jun 2023</span>
        <span class="notion-news-text">Project MAPS won <strong>Winner Award (Top 3)</strong> at GBA IT Application Development Competition Macau Sub-Competition.</span>
      </div>
    </div>
  </section>

  <!-- Blog Section -->
  <section class="notion-section">
    <h2 class="notion-h2 reveal">Blog</h2>
    <div class="notion-blog-grid reveal-stagger">
      {% for post in site.posts limit:6 %}
        {% assign card_palette = 'palette-sand' %}
        {% assign card_motif = 'motif-frame' %}
        {% assign card_label = 'Notes' %}
        {% assign short_title = post.title %}
        {% if post.title contains '智能营销' or post.title contains 'Marketing Agent' %}
          {% assign card_palette = 'palette-clay' %}
          {% assign card_motif = 'motif-arc' %}
          {% assign card_label = 'Agent' %}
          {% assign short_title = 'Smart Marketing Agent' %}
        {% elsif post.title contains '字幕 OCR' or post.title contains 'Subtitle OCR' %}
          {% assign card_palette = 'palette-rose' %}
          {% assign card_motif = 'motif-lens' %}
          {% assign card_label = 'OCR' %}
          {% assign short_title = 'Video Subtitle OCR' %}
        {% elsif post.title contains '05/24' %}
          {% assign card_palette = 'palette-sky' %}
          {% assign card_motif = 'motif-orbit' %}
          {% assign card_label = 'AIGC' %}
          {% assign short_title = 'AIGC Weekly 05/24' %}
        {% elsif post.title contains '05/17' %}
          {% assign card_palette = 'palette-lilac' %}
          {% assign card_motif = 'motif-beam' %}
          {% assign card_label = 'AIGC' %}
          {% assign short_title = 'AIGC Weekly 05/17' %}
        {% elsif post.title contains 'Missing Semester' %}
          {% assign card_palette = 'palette-ochre' %}
          {% assign card_motif = 'motif-columns' %}
          {% assign card_label = 'Learning' %}
          {% assign short_title = 'The Missing Semester' %}
        {% elsif post.title contains 'Simplex' %}
          {% assign card_palette = 'palette-moss' %}
          {% assign card_motif = 'motif-grid' %}
          {% assign card_label = 'Math' %}
          {% assign short_title = 'Simplex Method' %}
        {% elsif post.title contains 'Synthetic Image Detection' %}
          {% assign card_palette = 'palette-rose' %}
          {% assign card_motif = 'motif-lens' %}
          {% assign card_label = 'Research' %}
          {% assign short_title = 'Synthetic Image Detection' %}
        {% elsif post.title contains 'Watermark' %}
          {% assign card_palette = 'palette-clay' %}
          {% assign card_motif = 'motif-arc' %}
          {% assign card_label = 'Vision' %}
          {% assign short_title = 'Watermark Removal' %}
        {% elsif post.title contains 'DeepTalk' %}
          {% assign card_palette = 'palette-slate' %}
          {% assign card_motif = 'motif-wave' %}
          {% assign card_label = 'Agent' %}
          {% assign short_title = 'DeepTalk Agent' %}
        {% elsif post.title contains 'Know Each Other' %}
          {% assign card_palette = 'palette-ink' %}
          {% assign card_motif = 'motif-signal' %}
          {% assign card_label = 'Memory' %}
          {% assign short_title = 'Know Each Other' %}
        {% endif %}
        <a href="{{ base_path }}{{ post.url }}" class="notion-blog-card notion-blog-card--{{ card_palette }} notion-blog-card--{{ card_motif }} reveal" title="{{ post.title }}">
          <div class="notion-blog-card-image">
            <span class="notion-blog-card-cover-meta">{{ card_label }}</span>
            <h3 class="notion-blog-card-title">{{ short_title }}</h3>
            <span class="notion-blog-card-mark" aria-hidden="true"></span>
          </div>
          <div class="notion-blog-card-content">
            <span class="notion-blog-card-link">Read article</span>
          </div>
        </a>
      {% endfor %}
    </div>
    <p class="notion-section-link">
      <a href="{{ base_path }}/year-archive/" class="notion-link">View all posts →</a>
    </p>
  </section>

  <!-- Footer -->
  <footer class="notion-footer reveal">
    <p>Be passionate, be creative!</p>
    <p class="notion-footer-copy">© {{ 'now' | date: '%Y' }} Yang Chin. Built with Jekyll.</p>
  </footer>

</div>

<!-- CV Modal -->
<div class="notion-modal" id="cv-modal">
  <div class="notion-modal-overlay" onclick="closeCvModal()"></div>
  <div class="notion-modal-container">
    <button class="notion-modal-close" onclick="closeCvModal()" aria-label="Close">✕</button>
    <div class="notion-modal-content">
      <h2 class="notion-modal-title">Yang Chin</h2>
      <p class="notion-modal-subtitle">AI Engineer · Shenzhen, China</p>

      <div class="notion-cv-section">
        <h3>Education</h3>
        <ul>
          <li>M.S. in Applied Mathematics and Data Science, Macau University of Science and Technology, 2024</li>
          <li>B.E. in Data Science and Big Data Technology, Foshan University, 2022</li>
        </ul>
      </div>

      <div class="notion-cv-section">
        <h3>Experience</h3>
        <p><strong>Senior Engineer</strong> · AllVoiceLab, Quwan Technology · Sep 2025 – Aug 2026</p>
        <ul>
          <li>Developed multimodal solutions for video translation across text, speech, and vision.</li>
          <li>Designed AI agent systems, including agent workflows and memory systems.</li>
        </ul>

        <p><strong>AI Engineer</strong> · MagicLight · Jun 2024 – Aug 2025</p>
        <ul>
          <li>Built an AIGC platform for long-form story video generation across text, image, and video.</li>
          <li>Worked on identity-preserving and regional-controlled image generation, as well as pose-controlled generation.</li>
          <li>Developed prompt-engineering workflows for scripts and image-to-video models.</li>
        </ul>

        <p><strong>AI Intern</strong> · AFS Ltd., Digital AI Group · Feb 2024 – May 2024</p>
        <ul>
          <li>Worked on human portrait generation and pose-driven video generation.</li>
        </ul>

        <p><strong>Research Intern</strong> · Zhuhai UM Research Institute · 2022 – 2023</p>
        <ul>
          <li>Researched synthetic image detection, advanced AIGC technology, and AI security.</li>
        </ul>
      </div>
    </div>
  </div>
</div>

<script>
  function openCvModal() {
    document.getElementById('cv-modal').classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }
  function closeCvModal() {
    document.getElementById('cv-modal').classList.remove('is-open');
    document.body.style.overflow = '';
  }
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeCvModal();
  });
</script>
