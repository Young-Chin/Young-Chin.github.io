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
  <div class="notion-columns">
    <div class="notion-column">
      <h1 class="notion-hero-title" dir="auto">Yang Chin</h1>
      <h3 class="notion-hero-subtitle">AI Engineer passionate about Multimodality and AIGC.</h3>
      <p class="notion-hero-text">
        Currently an <em>AI Engineer</em> at <a href="https://www.allvoicelab.cn/" class="notion-link">All Voice Lab</a>, focusing on Multimodality (text, speech, vision) for film and drama understanding and editing.
      </p>
      <p class="notion-hero-text">
        Previously at <a href="https://www.magiclight.ai/official-website" class="notion-link">MagicLight</a>, working on AIGC (text, image, video) for long story video generation.
      </p>
      <p class="notion-hero-text">
        Master's from <a href="https://www.must.edu.mo" class="notion-link">Macau University of Science and Technology</a> (Applied Mathematics and Data Science). Bachelor's from <a href="https://www.fosu.edu.cn" class="notion-link">Foshan University</a> (Data Science and Big Data Technology).
      </p>
    </div>
    <div class="notion-column">
      <div class="notion-image">
        <img class="notion-hero-image" src="{{ base_path }}/images/personal photo.jpeg" alt="Yang Chin">
      </div>
    </div>
  </div>

  <hr class="notion-divider">

  <!-- Projects Section -->
  <h2 class="notion-h2">Projects</h2>

  <div class="notion-project-list">
    {% for post in site.portfolio %}
      <div class="notion-project-item">
        <a href="{{ base_path }}{{ post.url }}">
          <span class="notion-project-icon">⭐</span>
          <span>{{ post.title }}</span>
        </a>
      </div>
    {% endfor %}
  </div>

  <p class="notion-section-link">
    <a href="{{ base_path }}/year-archive/" class="notion-link">View all blog posts →</a>
  </p>

  <hr class="notion-divider">

  <!-- Expertise Section -->
  <h2 class="notion-h2">Expertise</h2>

  <div class="notion-columns">
    <div class="notion-column">
      <h3 class="notion-h3">Multimodality</h3>
      <ul class="notion-expertise-list">
        <li>Vision Language Model</li>
        <li>Alignment for Speech and Vision</li>
      </ul>

      <h3 class="notion-h3">AIGC and Its Applications</h3>
      <ul class="notion-expertise-list">
        <li>Prompt Engineering for story script and image/video generation</li>
        <li>ID Preserving and Face Swap</li>
        <li>Regionally controlled image generation</li>
        <li>Subject-consistent video generation</li>
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

  <hr class="notion-divider">

  <!-- News Section -->
  <h2 class="notion-h2">News</h2>

  <div class="notion-news-list">
    <p class="notion-news-item"><span class="notion-news-date">[Sep 2025]</span> Joining <a href="https://www.allvoicelab.cn/" class="notion-link">AllVoiceLab</a> at <a href="https://www.quwangroup.com/" class="notion-link">Quwan Technology</a> for film and drama understanding and editing.</p>
    <p class="notion-news-item"><span class="notion-news-date">[Sep 2024]</span> Invited interview as <em>Outstanding Postgraduate Students</em> in MUST. <a href="https://www.youtube.com/watch?si=aU1BVE1TQiOXAV9W&v=KoJ63k_ffKs&feature=youtu.be" class="notion-link">Watch video</a>.</p>
    <p class="notion-news-item"><span class="notion-news-date">[Jun 2024]</span> Joining <strong><a href="https://www.magiclight.ai" class="notion-link">MagicLight</a></strong> to build AIGC platform. Try <a href="https://aibrm.com" class="notion-link">白日梦AI</a> or <a href="https://magiclight.ai" class="notion-link">MagiclightAI</a>.</p>
    <p class="notion-news-item"><span class="notion-news-date">[Feb 2024]</span> Joining <a href="https://www.afirstsoft.cn" class="notion-link">软牛科技</a> as AI Intern for vision generation.</p>
    <p class="notion-news-item"><span class="notion-news-date">[Nov 2023]</span> <strong>MAPS</strong> won <strong>Bronze Award</strong> and <strong>Best Application Award</strong> at The 8th Guangdong-Hong Kong-Macao GBA IT Application Competition.</p>
    <p class="notion-news-item"><span class="notion-news-date">[Nov 2023]</span> Awarded <a href="https://www.must.edu.mo/student-affairs-office/student-services/scholarships/company" class="notion-link">YuanGuang Software Scholarship 2023</a> (only 7 postgraduates in MUST).</p>
    <p class="notion-news-item"><span class="notion-news-date">[Oct 2023]</span> Project MAPS advanced to national competition of The 9th China International College Students' "Internet+" Innovation and Entrepreneurship Competition.</p>
    <p class="notion-news-item"><span class="notion-news-date">[Jun 2023]</span> Project MAPS won <strong>Winner Award (Top 3)</strong> at The 8th GBA IT Application Development Competition 2023 Macau Sub-Competition.</p>
  </div>

  <hr class="notion-divider">

  <!-- Publications & CV Section -->
  <h2 class="notion-h2">Publications & CV</h2>

  <div class="notion-columns">
    <div class="notion-column">
      <h3 class="notion-h3">Publications</h3>
      <p class="notion-text">
        <a href="{{ base_path }}/publications/" class="notion-link">View all publications →</a>
      </p>
    </div>
    <div class="notion-column">
      <h3 class="notion-h3">Curriculum Vitae</h3>
      <p class="notion-text">
        <a href="{{ base_path }}/cv/" class="notion-link">View full CV →</a>
      </p>
    </div>
  </div>

  <hr class="notion-divider">

  <!-- Contact Section -->
  <h2 class="notion-h2">Contact</h2>

  <div class="notion-columns">
    <div class="notion-column">
      <h3 class="notion-h3">Get in Touch</h3>
      <p class="notion-contact-item">📍 SZ, China</p>
      <p class="notion-contact-item">📧 <a href="mailto:yangqinbob@gmail.com" class="notion-link">yangqinbob@gmail.com</a></p>
      <p class="notion-contact-item">🏢 <a href="https://www.allvoicelab.cn/" class="notion-link">All Voice Lab</a></p>
    </div>
    <div class="notion-column">
      <h3 class="notion-h3">Socials</h3>
      <p class="notion-contact-item">
        <a href="https://github.com/Young-Chin" class="notion-social-link" target="_blank" rel="noopener">GitHub</a>
      </p>
      <p class="notion-contact-item">
        <a href="mailto:yangqinbob@gmail.com" class="notion-social-link">Email</a>
      </p>
    </div>
  </div>

  <hr class="notion-divider">

  <!-- CTA -->
  <h2 class="notion-cta">Let's create something amazing together!</h2>

  <div class="notion-callout notion-callout-blue">
    <span class="notion-callout-icon">💡</span>
    <div class="notion-callout-content">
      <p><strong>Feel free to reach out for collaborations or just to say hi.</strong></p>
      <p>I'm always open to discussing new projects, creative ideas, or opportunities to be part of your vision.</p>
    </div>
  </div>

</div>
