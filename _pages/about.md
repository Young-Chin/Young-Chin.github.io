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
        <h1 class="notion-hero-title" dir="auto">Yang Chin</h1>
        <p class="notion-hero-subtitle">AI Engineer passionate about Multimodality and AIGC</p>
        <div class="notion-hero-body">
          <p>Currently an <em>AI Engineer</em> at <a href="https://www.allvoicelab.cn/" class="notion-link">All Voice Lab</a>, focusing on Multimodality (text, speech, vision) for film and drama understanding and editing.</p>
          <p>Previously at <a href="https://www.magiclight.ai/official-website" class="notion-link">MagicLight</a>, working on AIGC (text, image, video) for long story video generation.</p>
          <p>Master's from <a href="https://www.must.edu.mo" class="notion-link">MUST</a> (Applied Mathematics and Data Science). Bachelor's from <a href="https://www.fosu.edu.cn" class="notion-link">Foshan University</a> (Data Science and Big Data Technology).</p>
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
    <div class="notion-columns">
      <div class="notion-column">
        <h3 class="notion-h3">Multimodality</h3>
        <ul class="notion-expertise-list">
          <li>Vision Language Model</li>
          <li>Speech-Vision Alignment</li>
        </ul>

        <h3 class="notion-h3">AIGC</h3>
        <ul class="notion-expertise-list">
          <li>Prompt Engineering</li>
          <li>ID Preserving & Face Swap</li>
          <li>Regional Controlled Generation</li>
          <li>Subject-Consistent Video Gen</li>
        </ul>
      </div>
      <div class="notion-column">
        <h3 class="notion-h3">AI Security</h3>
        <ul class="notion-expertise-list">
          <li>Multimedia Forensics</li>
          <li>Deepfake Detection</li>
        </ul>

        <h3 class="notion-h3">Smart City</h3>
        <ul class="notion-expertise-list">
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

  <!-- Contact Section -->
  <section class="notion-section">
    <h2 class="notion-h2">Contact</h2>
    <div class="notion-columns">
      <div class="notion-column">
        <p class="notion-contact-item">📍 Shenzhen, China</p>
        <p class="notion-contact-item">📧 <a href="mailto:yangqinbob@gmail.com" class="notion-link">yangqinbob@gmail.com</a></p>
        <p class="notion-contact-item">🏢 <a href="https://www.allvoicelab.cn/" class="notion-link">All Voice Lab</a></p>
      </div>
      <div class="notion-column">
        <p class="notion-contact-item">
          <a href="https://github.com/Young-Chin" class="notion-social-link" target="_blank" rel="noopener">GitHub →</a>
        </p>
        <p class="notion-contact-item">
          <a href="mailto:yangqinbob@gmail.com" class="notion-social-link">Email →</a>
        </p>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="notion-footer">
    <p>Let's create something amazing together.</p>
    <p class="notion-footer-copy">© {{ 'now' | date: '%Y' }} Yang Chin. Built with Jekyll.</p>
  </footer>

</div>
