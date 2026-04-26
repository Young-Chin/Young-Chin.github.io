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
  <section class="notion-section notion-hero">
    <div class="notion-columns">
      <div class="notion-column">
        <h1 class="notion-hero-title" dir="auto">Young Chin|Bob|秦洋</h1>
        <p class="notion-hero-location">SZ/GZ China</p>
        <div class="notion-hero-social">
          <a href="mailto:yangqinbob@gmail.com" class="notion-social-icon" title="Email" target="_blank" rel="noopener">
            <i class="fas fa-envelope"></i>
          </a>
          <a href="https://github.com/Young-Chin" class="notion-social-icon" title="GitHub" target="_blank" rel="noopener">
            <i class="fab fa-github"></i>
          </a>
          <a href="https://x.com/Young_Chin_Bob" class="notion-social-icon" title="X" target="_blank" rel="noopener">
            <i class="fab fa-twitter"></i>
          </a>
        </div>
        <div class="notion-hero-body">
          <p>Currently a Senior AI Engineer in <a href="https://www.quwangroup.com" class="notion-link">Quwan</a>, focusing on Multimodality and AI Agent.</p>
          <p>Previously at <a href="https://www.magiclight.ai" class="notion-link">MagicLight</a>, working on AIGC (text, image, video) for long story video generation.</p>
        </div>
      </div>
      <div class="notion-column notion-column-shrink">
        <div class="notion-hero-photo">
          <img src="{{ base_path }}/images/personal photo.jpeg" alt="Yang Chin">
        </div>
      </div>
    </div>
  </section>

  <!-- Expertise Section -->
  <section class="notion-section">
    <h2 class="notion-h2">Expertise</h2>
    <div class="notion-expertise-grid">
      <div class="notion-expertise-card" style="--card-bg: rgba(229, 242, 252, 0.45); --card-border: rgba(186, 218, 244, 0.5);">
        <h3 class="notion-expertise-card-title">Multimodality</h3>
        <ul class="notion-expertise-card-list">
          <li>Vision Language Model</li>
          <li>Speech-Vision Alignment</li>
        </ul>
      </div>
      <div class="notion-expertise-card" style="--card-bg: rgba(243, 235, 249, 0.45); --card-border: rgba(220, 204, 232, 0.5);">
        <h3 class="notion-expertise-card-title">AIGC</h3>
        <ul class="notion-expertise-card-list">
          <li>Prompt Engineering</li>
          <li>ID Preserving & Face Swap</li>
          <li>Regional Controlled Generation</li>
          <li>Subject-Consistent Video Gen</li>
        </ul>
      </div>
      <div class="notion-expertise-card" style="--card-bg: rgba(250, 233, 241, 0.45); --card-border: rgba(232, 196, 216, 0.5);">
        <h3 class="notion-expertise-card-title">AI Security</h3>
        <ul class="notion-expertise-card-list">
          <li>Multimedia Forensics</li>
          <li>Deepfake Detection</li>
        </ul>
      </div>
      <div class="notion-expertise-card" style="--card-bg: rgba(232, 241, 236, 0.45); --card-border: rgba(192, 220, 204, 0.5);">
        <h3 class="notion-expertise-card-title">Smart City</h3>
        <ul class="notion-expertise-card-list">
          <li>Urban Data Analytics</li>
          <li>IoT Applications</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- News Section -->
  <section class="notion-section">
    <h2 class="notion-h2">News</h2>
    <div class="notion-news-list">
      <div class="notion-news-item">
        <span class="notion-news-date">Sep 2025</span>
        <span class="notion-news-text">Joining <a href="https://www.allvoicelab.cn/" class="notion-link">AllVoiceLab</a> at <a href="https://www.quwangroup.com/" class="notion-link">Quwan Technology</a> for film and drama understanding and editing.</span>
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
    <h2 class="notion-h2">Blog</h2>
    <div class="notion-blog-grid">
      {% for post in site.posts limit:6 %}
        {% assign card_bg = '' %}
        {% assign card_icon = '' %}
        {% assign short_title = post.title %}
        {% if post.title contains '05/24' %}
          {% assign card_bg = 'linear-gradient(135deg, #e5f2fc 0%, #cce0f5 100%)' %}
          {% assign card_icon = '🚀' %}
          {% assign short_title = 'AIGC Weekly 05/24' %}
        {% elsif post.title contains '05/17' %}
          {% assign card_bg = 'linear-gradient(135deg, #f3ebf9 0%, #e4d6f0 100%)' %}
          {% assign card_icon = '✨' %}
          {% assign short_title = 'AIGC Weekly 05/17' %}
        {% elsif post.title contains 'Missing Semester' %}
          {% assign card_bg = 'linear-gradient(135deg, #f9f3dc 0%, #f0e6c0 100%)' %}
          {% assign card_icon = '🎓' %}
          {% assign short_title = 'The Missing Semester' %}
        {% elsif post.title contains 'Simplex' %}
          {% assign card_bg = 'linear-gradient(135deg, #e8f1ec 0%, #d0e4db 100%)' %}
          {% assign card_icon = '📐' %}
          {% assign short_title = 'Simplex Method' %}
        {% elsif post.title contains 'Synthetic Image Detection' %}
          {% assign card_bg = 'linear-gradient(135deg, #fae9f1 0%, #f0d4e4 100%)' %}
          {% assign card_icon = '🔍' %}
          {% assign short_title = 'Synthetic Image Detection' %}
        {% elsif post.title contains 'Watermark' %}
          {% assign card_bg = 'linear-gradient(135deg, #f5ede9 0%, #e8ddd0 100%)' %}
          {% assign card_icon = '💧' %}
          {% assign short_title = 'Watermark Removal' %}
        {% endif %}
        <a href="{{ base_path }}{{ post.url }}" class="notion-blog-card" title="{{ post.title }}">
          <div class="notion-blog-card-image" style="background: {{ card_bg }};">
            <span class="notion-blog-card-icon">{{ card_icon }}</span>
          </div>
          <div class="notion-blog-card-content">
            <h3 class="notion-blog-card-title">{{ short_title }}</h3>
          </div>
        </a>
      {% endfor %}
    </div>
    <p class="notion-section-link">
      <a href="{{ base_path }}/year-archive/" class="notion-link">View all posts →</a>
    </p>
  </section>

  <!-- CV Section -->
  <section class="notion-section">
    <h2 class="notion-h2">Curriculum Vitae</h2>
    <p class="notion-text" style="margin-bottom: 1em;">A quick overview of my education, experience, and projects.</p>
    <button class="notion-button" onclick="openCvModal()">View CV</button>
  </section>

  <!-- Footer -->
  <footer class="notion-footer">
    <p>Let's create something amazing together.</p>
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
        <p><strong>Senior Engineer</strong> · AllVoiceLab, Quwan Technology · Sep 2025 – Present</p>
        <ul>
          <li>Focus on multimodal understanding and editing of film and television dramas (text, speech, vision).</li>
        </ul>

        <p><strong>AI Engineer</strong> · MagicLight · Jun 2024 – Aug 2025</p>
        <ul>
          <li>Built AIGC platform for long story video generation (text / image / video).</li>
        </ul>

        <p><strong>AI Intern</strong> · AFS Ltd., Digital AI Group · Feb 2024 – May 2024</p>
        <ul>
          <li>Human Portrait Generation and Pose-driven Video Generation.</li>
        </ul>

        <p><strong>Research Intern</strong> · Zhuhai UM Research Institute · 2022 – 2023</p>
        <ul>
          <li>Synthetic Image Detection, Advanced AIGC Technology, and AI Security.</li>
        </ul>
      </div>

      <div class="notion-cv-section">
        <h3>Leadership</h3>
        <ul>
          <li>A key founder of the <strong>MAPS</strong> project.</li>
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
