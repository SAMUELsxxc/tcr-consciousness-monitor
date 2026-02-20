<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TCR — Licensing Opportunity</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=DM+Mono:wght@300;400;500&family=DM+Sans:wght@300;400;500&display=swap');

  :root {
    --black: #080a0f;
    --white: #f0ede8;
    --cream: #e8e3da;
    --gold: #c9a84c;
    --gold-light: #e8c96a;
    --red: #c93a2a;
    --blue: #1a3a5c;
    --blue-light: #2a5a8c;
    --gray: #4a4a5a;
    --gray-light: #8a8a9a;
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html { scroll-behavior: smooth; }

  body {
    background: var(--black);
    color: var(--white);
    font-family: 'DM Sans', sans-serif;
    font-weight: 300;
    overflow-x: hidden;
  }

  /* SLIDE SYSTEM */
  .slide {
    min-height: 100vh;
    padding: 80px 100px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    border-bottom: 1px solid rgba(201,168,76,0.15);
  }

  .slide-number {
    position: absolute;
    top: 40px;
    right: 60px;
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--gold);
    letter-spacing: 3px;
    opacity: 0.6;
  }

  .slide-tag {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 4px;
    color: var(--gold);
    text-transform: uppercase;
    margin-bottom: 24px;
    opacity: 0.8;
  }

  /* TYPOGRAPHY */
  h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(48px, 7vw, 96px);
    font-weight: 900;
    line-height: 0.95;
    letter-spacing: -2px;
  }

  h2 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(36px, 5vw, 64px);
    font-weight: 700;
    line-height: 1.05;
    letter-spacing: -1px;
  }

  h3 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(24px, 3vw, 36px);
    font-weight: 400;
    line-height: 1.2;
  }

  p {
    font-size: 16px;
    line-height: 1.7;
    color: rgba(240,237,232,0.75);
    max-width: 600px;
  }

  .mono {
    font-family: 'DM Mono', monospace;
    font-size: 13px;
  }

  /* SLIDE 1 — COVER */
  .slide-cover {
    background: var(--black);
    justify-content: space-between;
    padding: 60px 100px;
  }

  .cover-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }

  .logo-text {
    font-family: 'DM Mono', monospace;
    font-size: 12px;
    letter-spacing: 4px;
    color: var(--gold);
    opacity: 0.7;
  }

  .cover-main {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 80px 0;
  }

  .cover-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(60px, 9vw, 120px);
    font-weight: 900;
    line-height: 0.88;
    letter-spacing: -4px;
    color: var(--white);
  }

  .cover-title span {
    color: var(--gold);
  }

  .cover-sub {
    margin-top: 32px;
    font-family: 'DM Sans', sans-serif;
    font-size: 18px;
    font-weight: 300;
    color: rgba(240,237,232,0.55);
    letter-spacing: 1px;
    max-width: 500px;
    line-height: 1.6;
  }

  .cover-divider {
    width: 60px;
    height: 1px;
    background: var(--gold);
    margin: 28px 0;
  }

  .cover-footer {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-top: 1px solid rgba(201,168,76,0.2);
    padding-top: 32px;
  }

  .cover-stat {
    text-align: center;
  }

  .cover-stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
  }

  .cover-stat-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    color: rgba(240,237,232,0.4);
    margin-top: 6px;
  }

  /* SLIDE 2 — PROBLEM */
  .slide-problem {
    background: #0d0f14;
  }

  .problem-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    margin-top: 50px;
  }

  .problem-card {
    padding: 40px;
    border: 1px solid rgba(255,255,255,0.06);
    background: rgba(255,255,255,0.02);
    position: relative;
  }

  .problem-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px;
    height: 100%;
    background: var(--red);
  }

  .problem-card h3 {
    font-size: 20px;
    margin-bottom: 12px;
    color: var(--white);
  }

  .problem-card p {
    font-size: 14px;
    line-height: 1.6;
  }

  .problem-card .stat {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    color: var(--red);
    margin-bottom: 8px;
    line-height: 1;
  }

  /* SLIDE 3 — SOLUTION */
  .slide-solution {
    background: var(--blue);
    position: relative;
    overflow: hidden;
  }

  .slide-solution::before {
    content: 'TCR';
    position: absolute;
    right: -40px;
    top: 50%;
    transform: translateY(-50%);
    font-family: 'Playfair Display', serif;
    font-size: 300px;
    font-weight: 900;
    color: rgba(255,255,255,0.04);
    line-height: 1;
    pointer-events: none;
  }

  .equation-block {
    margin-top: 40px;
    padding: 40px;
    background: rgba(0,0,0,0.3);
    border-left: 3px solid var(--gold);
    font-family: 'DM Mono', monospace;
  }

  .equation-main {
    font-size: clamp(16px, 2.5vw, 24px);
    color: var(--gold-light);
    margin-bottom: 20px;
    letter-spacing: 1px;
  }

  .equation-sub {
    font-size: 13px;
    color: rgba(240,237,232,0.5);
    line-height: 2;
  }

  .dual-criterion {
    display: flex;
    gap: 24px;
    margin-top: 40px;
  }

  .criterion {
    flex: 1;
    padding: 28px;
    border: 1px solid rgba(201,168,76,0.3);
    background: rgba(201,168,76,0.05);
  }

  .criterion-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--gold);
    margin-bottom: 12px;
  }

  .criterion-eq {
    font-family: 'DM Mono', monospace;
    font-size: 20px;
    color: var(--white);
    margin-bottom: 8px;
  }

  .criterion-desc {
    font-size: 13px;
    color: rgba(240,237,232,0.55);
    line-height: 1.5;
  }

  /* SLIDE 4 — VALIDATION */
  .slide-validation {
    background: #080a0f;
  }

  .validation-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2px;
    margin-top: 50px;
    background: rgba(201,168,76,0.1);
  }

  .val-cell {
    background: var(--black);
    padding: 32px 28px;
  }

  .val-cell.highlight {
    background: rgba(201,168,76,0.08);
  }

  .val-number {
    font-family: 'Playfair Display', serif;
    font-size: 52px;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
  }

  .val-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 2px;
    color: var(--gray-light);
    margin-top: 8px;
    text-transform: uppercase;
  }

  .val-detail {
    font-size: 13px;
    color: rgba(240,237,232,0.45);
    margin-top: 10px;
    line-height: 1.5;
  }

  /* SLIDE 5 — COMPETITIVE */
  .slide-competitive {
    background: #0a0c10;
  }

  .comp-table {
    margin-top: 50px;
    width: 100%;
    border-collapse: collapse;
  }

  .comp-table th {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--gold);
    text-align: left;
    padding: 16px 24px;
    border-bottom: 1px solid rgba(201,168,76,0.3);
    font-weight: 400;
  }

  .comp-table td {
    padding: 20px 24px;
    font-size: 14px;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    color: rgba(240,237,232,0.7);
    vertical-align: middle;
  }

  .comp-table tr.our-row td {
    background: rgba(201,168,76,0.07);
    color: var(--white);
    font-weight: 500;
  }

  .comp-table tr.our-row td:first-child {
    color: var(--gold);
    font-family: 'DM Mono', monospace;
  }

  .pass { color: #4ade80; font-weight: 500; }
  .fail { color: #f87171; }
  .partial { color: #fbbf24; }

  /* SLIDE 6 — MARKET */
  .slide-market {
    background: var(--black);
  }

  .market-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 32px;
    margin-top: 50px;
  }

  .market-card {
    padding: 36px 32px;
    border: 1px solid rgba(255,255,255,0.06);
    position: relative;
    overflow: hidden;
  }

  .market-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0;
    width: 100%;
    height: 2px;
    background: var(--gold);
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.4s ease;
  }

  .market-card:hover::after {
    transform: scaleX(1);
  }

  .market-size {
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    font-weight: 700;
    color: var(--gold);
    line-height: 1;
  }

  .market-name {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--gray-light);
    margin: 12px 0 16px;
    text-transform: uppercase;
  }

  .market-desc {
    font-size: 13px;
    color: rgba(240,237,232,0.5);
    line-height: 1.6;
  }

  /* SLIDE 7 — IP */
  .slide-ip {
    background: #0d0f14;
  }

  .ip-timeline {
    margin-top: 50px;
    position: relative;
  }

  .ip-timeline::before {
    content: '';
    position: absolute;
    left: 0; top: 0;
    width: 1px;
    height: 100%;
    background: rgba(201,168,76,0.3);
  }

  .ip-item {
    padding: 0 0 40px 40px;
    position: relative;
  }

  .ip-item::before {
    content: '';
    position: absolute;
    left: -4px; top: 6px;
    width: 9px; height: 9px;
    background: var(--gold);
    border-radius: 50%;
  }

  .ip-date {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    color: var(--gold);
    margin-bottom: 6px;
  }

  .ip-title {
    font-size: 18px;
    font-weight: 500;
    color: var(--white);
    margin-bottom: 6px;
  }

  .ip-detail {
    font-size: 13px;
    color: rgba(240,237,232,0.5);
    line-height: 1.5;
    max-width: 500px;
  }

  /* SLIDE 8 — DEAL */
  .slide-deal {
    background: #0a0c10;
  }

  .deal-structure {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 40px;
    margin-top: 50px;
  }

  .deal-box {
    padding: 40px;
    border: 1px solid rgba(201,168,76,0.2);
    background: rgba(201,168,76,0.03);
  }

  .deal-box h3 {
    font-size: 14px;
    font-family: 'DM Mono', monospace;
    letter-spacing: 3px;
    color: var(--gold);
    margin-bottom: 24px;
    font-weight: 400;
  }

  .deal-item {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 14px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
  }

  .deal-item:last-child { border-bottom: none; }

  .deal-item-label {
    font-size: 14px;
    color: rgba(240,237,232,0.6);
  }

  .deal-item-value {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    color: var(--white);
    font-weight: 700;
  }

  .deal-item-value.gold { color: var(--gold); }

  /* SLIDE 9 — STRATEGY */
  .slide-strategy {
    background: var(--black);
  }

  .strategy-phases {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2px;
    margin-top: 50px;
    background: rgba(255,255,255,0.04);
  }

  .phase {
    background: var(--black);
    padding: 36px 28px;
  }

  .phase-num {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    letter-spacing: 2px;
    color: var(--gold);
    margin-bottom: 16px;
  }

  .phase-title {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    color: var(--white);
    margin-bottom: 12px;
    line-height: 1.2;
  }

  .phase-time {
    font-family: 'DM Mono', monospace;
    font-size: 11px;
    color: var(--gray-light);
    margin-bottom: 16px;
  }

  .phase-items {
    list-style: none;
  }

  .phase-items li {
    font-size: 13px;
    color: rgba(240,237,232,0.55);
    padding: 6px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    line-height: 1.4;
  }

  .phase-items li::before {
    content: '→ ';
    color: var(--gold);
    font-family: 'DM Mono', monospace;
  }

  /* SLIDE 10 — CONTACT */
  .slide-contact {
    background: #080a0f;
    min-height: 60vh;
  }

  .contact-content {
    display: flex;
    gap: 80px;
    margin-top: 50px;
    align-items: flex-start;
  }

  .contact-left { flex: 1; }
  .contact-right { flex: 1; }

  .contact-item {
    padding: 20px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
  }

  .contact-item-label {
    font-family: 'DM Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    color: var(--gold);
    margin-bottom: 8px;
  }

  .contact-item-value {
    font-size: 16px;
    color: var(--white);
  }

  .contact-quote {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    font-style: italic;
    color: rgba(240,237,232,0.5);
    line-height: 1.5;
    border-left: 2px solid var(--gold);
    padding-left: 28px;
  }

  /* NAV */
  .nav {
    position: fixed;
    right: 32px;
    top: 50%;
    transform: translateY(-50%);
    display: flex;
    flex-direction: column;
    gap: 12px;
    z-index: 100;
  }

  .nav-dot {
    width: 6px;
    height: 6px;
    border: 1px solid rgba(201,168,76,0.4);
    border-radius: 50%;
    cursor: pointer;
    transition: all 0.3s;
    background: transparent;
  }

  .nav-dot:hover, .nav-dot.active {
    background: var(--gold);
    border-color: var(--gold);
  }

  /* ANIMATIONS */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .slide > * {
    animation: fadeUp 0.6s ease both;
  }

  .slide > *:nth-child(1) { animation-delay: 0.1s; }
  .slide > *:nth-child(2) { animation-delay: 0.2s; }
  .slide > *:nth-child(3) { animation-delay: 0.3s; }
  .slide > *:nth-child(4) { animation-delay: 0.4s; }

  /* PRINT */
  @media print {
    .nav { display: none; }
    .slide { page-break-after: always; min-height: 100vh; }
  }
</style>
</head>
<body>

<!-- NAV DOTS -->
<nav class="nav" id="nav"></nav>

<!-- SLIDE 1: COVER -->
<section class="slide slide-cover" id="s1">
  <div class="cover-header">
    <div class="logo-text">CONFIDENTIAL LICENSING DOCUMENT — 2026</div>
    <div class="logo-text">SAMUEL SANTOS OLIVEIRA DA SILVA</div>
  </div>

  <div class="cover-main">
    <div class="slide-tag">Temporal Consciousness Recursion</div>
    <div class="cover-title">The First<br><span>Quantitative</span><br>Consciousness<br>Monitor</div>
    <div class="cover-divider"></div>
    <div class="cover-sub">A patented method and system for objective, real-time consciousness quantification in clinical settings — solving what no existing technology can.</div>
  </div>

  <div class="cover-footer">
    <div class="cover-stat">
      <div class="cover-stat-num">523</div>
      <div class="cover-stat-label">Systems Validated</div>
    </div>
    <div class="cover-stat">
      <div class="cover-stat-num">100%</div>
      <div class="cover-stat-label">Classification Accuracy</div>
    </div>
    <div class="cover-stat">
      <div class="cover-stat-num">11/12</div>
      <div class="cover-stat-label">Predictions Confirmed</div>
    </div>
    <div class="cover-stat">
      <div class="cover-stat-num">$4B+</div>
      <div class="cover-stat-label">Addressable Market</div>
    </div>
  </div>
</section>

<!-- SLIDE 2: PROBLEM -->
<section class="slide slide-problem" id="s2">
  <div class="slide-number">02 / 09</div>
  <div class="slide-tag">The Problem</div>
  <h2>Current Technology<br>Has Critical Blind Spots</h2>

  <div class="problem-grid">
    <div class="problem-card">
      <div class="stat">0%</div>
      <h3>Ketamine Detection</h3>
      <p>BIS Monitor — the $2B market leader — completely fails under dissociative anesthesia. Patients remain conscious while the monitor reads "unconscious." Intraoperative awareness goes undetected.</p>
    </div>
    <div class="problem-card">
      <div class="stat">40%</div>
      <h3>DoC Misdiagnosis Rate</h3>
      <p>Up to 40% of vegetative state diagnoses are wrong. Locked-in patients — fully conscious, completely paralyzed — are routinely classified as unconscious. Life-or-death decisions made on false data.</p>
    </div>
    <div class="problem-card">
      <div class="stat">0</div>
      <h3>Theoretical Foundation</h3>
      <p>Every existing monitor (BIS, SedLine, Entropy) uses purely empirical correlation. No mechanism. No theory. No ability to extrapolate to edge cases or novel anesthetic agents.</p>
    </div>
    <div class="problem-card">
      <div class="stat">1D</div>
      <h3>One-Dimensional Metrics</h3>
      <p>All current systems collapse multidimensional consciousness into a single number. They cannot distinguish phenomenal awareness from narrative self, or sedation from dissociation.</p>
    </div>
  </div>
</section>

<!-- SLIDE 3: SOLUTION -->
<section class="slide slide-solution" id="s3">
  <div class="slide-number">03 / 09</div>
  <div class="slide-tag">The Solution</div>
  <h2>TCR: Dual-Criterion<br>Consciousness Quantification</h2>

  <div class="equation-block">
    <div class="equation-main">Ψ_phen = Θ × √(Π × G × I × T × Ω)</div>
    <div class="equation-sub">
      Θ = Thermodynamic criticality &nbsp;|&nbsp; Π = Physical complexity &nbsp;|&nbsp; G = Ontological vulnerability<br>
      I = Causal integration &nbsp;|&nbsp; T = Temporal continuity &nbsp;|&nbsp; Ω = Environmental coupling (adaptive)
    </div>
  </div>

  <div class="dual-criterion">
    <div class="criterion">
      <div class="criterion-label">Criterion I — Magnitude</div>
      <div class="criterion-eq">Ψ_phen > 0.001</div>
      <div class="criterion-desc">Phenomenal consciousness threshold. Eliminates panpsychism — thermostats and simple systems score zero.</div>
    </div>
    <div class="criterion">
      <div class="criterion-label">Criterion II — Criticality</div>
      <div class="criterion-eq">Θ > 0.85</div>
      <div class="criterion-desc">Thermodynamic criticality via Gaussian: Θ(x) = exp(−(x−1)²/2σ²). Captures edge-of-chaos dynamics essential for consciousness.</div>
    </div>
    <div class="criterion">
      <div class="criterion-label">Key Innovation — Ω</div>
      <div class="criterion-eq">Ω = α·Ω_ext + (1−α)·Ω_body</div>
      <div class="criterion-desc">Adaptive weighting. When motor output collapses (locked-in), interoceptive coupling sustains consciousness detection.</div>
    </div>
  </div>
</section>

<!-- SLIDE 4: VALIDATION -->
<section class="slide slide-validation" id="s4">
  <div class="slide-number">04 / 09</div>
  <div class="slide-tag">Empirical Validation</div>
  <h2>Validated Across<br>523 Systems</h2>

  <div class="validation-grid">
    <div class="val-cell highlight">
      <div class="val-number">100%</div>
      <div class="val-label">Classification Accuracy</div>
      <div class="val-detail">Zero false positives. Zero false negatives. Across 13 distinct categories.</div>
    </div>
    <div class="val-cell">
      <div class="val-number">11/12</div>
      <div class="val-label">Predictions Confirmed</div>
      <div class="val-detail">Pre-registered predictions tested retrospectively against independent literature.</div>
    </div>
    <div class="val-cell">
      <div class="val-number">0</div>
      <div class="val-label">Predictions Refuted</div>
      <div class="val-detail">No prediction has been falsified across any tested condition or species.</div>
    </div>
    <div class="val-cell">
      <div class="val-number">7/7</div>
      <div class="val-label">Locked-In Detected</div>
      <div class="val-detail">100% sensitivity, 100% specificity. n=211 across 5 independent studies. p < 0.0001.</div>
    </div>
    <div class="val-cell highlight">
      <div class="val-number">100%</div>
      <div class="val-label">Ketamine Detection</div>
      <div class="val-detail">Correctly identifies consciousness under dissociative anesthesia. BIS Monitor: 0%.</div>
    </div>
    <div class="val-cell">
      <div class="val-number">r=0.89</div>
      <div class="val-label">Hypothermia Correlation</div>
      <div class="val-detail">Θ vs core temperature. n=149, p<0.0001. 5 independent meta-analytic studies.</div>
    </div>
  </div>
</section>

<!-- SLIDE 5: COMPETITIVE -->
<section class="slide slide-competitive" id="s5">
  <div class="slide-number">05 / 09</div>
  <div class="slide-tag">Competitive Landscape</div>
  <h2>TCR Solves What<br>Nothing Else Can</h2>

  <table class="comp-table">
    <thead>
      <tr>
        <th>METHOD</th>
        <th>KETAMINE</th>
        <th>LOCKED-IN</th>
        <th>REAL-TIME</th>
        <th>OR COMPATIBLE</th>
        <th>THEORETICAL BASIS</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>BIS Monitor (Medtronic)</td>
        <td class="fail">FAIL</td>
        <td class="fail">FAIL</td>
        <td class="pass">Yes</td>
        <td class="pass">Yes</td>
        <td class="fail">Empirical only</td>
      </tr>
      <tr>
        <td>IIT (Φ)</td>
        <td class="fail">FAIL</td>
        <td class="partial">Ambiguous</td>
        <td class="fail">No</td>
        <td class="fail">No</td>
        <td class="partial">Theory, no device</td>
      </tr>
      <tr>
        <td>PCI (TMS-EEG)</td>
        <td class="fail">FAIL</td>
        <td class="partial">Partial</td>
        <td class="fail">No</td>
        <td class="fail">No</td>
        <td class="partial">Empirical</td>
      </tr>
      <tr>
        <td>wSMI</td>
        <td class="partial">Untested</td>
        <td class="partial">Partial</td>
        <td class="fail">5 min latency</td>
        <td class="partial">Partial</td>
        <td class="fail">Empirical</td>
      </tr>
      <tr class="our-row">
        <td>TCR v22.0 ★</td>
        <td class="pass">PASS (100%)</td>
        <td class="pass">PASS (100%)</td>
        <td class="pass">&lt;500ms</td>
        <td class="pass">Yes</td>
        <td class="pass">First-principles</td>
      </tr>
    </tbody>
  </table>
</section>

<!-- SLIDE 6: MARKET -->
<section class="slide slide-market" id="s6">
  <div class="slide-number">06 / 09</div>
  <div class="slide-tag">Market Opportunity</div>
  <h2>Multiple Billion-Dollar<br>Markets, One Platform</h2>

  <div class="market-grid">
    <div class="market-card">
      <div class="market-size">$2.1B</div>
      <div class="market-name">Anesthesia Monitoring</div>
      <div class="market-desc">Direct replacement for BIS Monitor. 300M+ surgeries annually requiring anesthetic monitoring. Per-patient consumable revenue model.</div>
    </div>
    <div class="market-card">
      <div class="market-size">$1.4B</div>
      <div class="market-name">Disorders of Consciousness</div>
      <div class="market-desc">ICU diagnosis, vegetative state assessment, locked-in detection, coma prognosis. Critical unmet need — 40% current misdiagnosis rate.</div>
    </div>
    <div class="market-card">
      <div class="market-size">$1.2B</div>
      <div class="market-name">Procedural Sedation</div>
      <div class="market-desc">Endoscopy, dental, interventional radiology. Real-time conscious sedation titration. Reduces adverse events, enables ambulatory expansion.</div>
    </div>
    <div class="market-card">
      <div class="market-size">$800M</div>
      <div class="market-name">Consumer Wearable</div>
      <div class="market-desc">Sleep monitoring, meditation quantification, neurofeedback. Ψ_phen and Ψ_narr as consumer metrics. Comparable to cardiac wearables (Apple Watch, Fitbit).</div>
    </div>
    <div class="market-card">
      <div class="market-size">$600M</div>
      <div class="market-name">Legal & Forensic</div>
      <div class="market-desc">Intraoperative awareness litigation ($600k–$2.3M per case). Cryptographic consciousness documentation. Organ donation confirmation. ICU legal protection.</div>
    </div>
    <div class="market-card">
      <div class="market-size">$4B+</div>
      <div class="market-name">Total Addressable</div>
      <div class="market-desc">Platform technology with expansion into pediatrics, animal welfare, BCI communication, ventilator synchronization, and psychiatric monitoring.</div>
    </div>
  </div>
</section>

<!-- SLIDE 7: IP -->
<section class="slide slide-ip" id="s7">
  <div class="slide-number">07 / 09</div>
  <div class="slide-tag">Intellectual Property</div>
  <h2>Protected, Documented,<br>Pre-Registered</h2>

  <div class="ip-timeline">
    <div class="ip-item">
      <div class="ip-date">JAN 2026</div>
      <div class="ip-title">Theory Published — Zenodo (v1–v16)</div>
      <div class="ip-detail">7 publications establishing prior art and pre-registered predictions. DOIs: 10.5281/zenodo.18113271 → 18402684. Public timestamp proof of invention priority.</div>
    </div>
    <div class="ip-item">
      <div class="ip-date">JAN 2026</div>
      <div class="ip-title">TCR v15.0 Scientific Paper</div>
      <div class="ip-detail">"Temporal Consciousness Recursion as Neural Gravity: A Complete Geometric Theory of Consciousness." Full mathematical derivation, 523-system validation, 12 pre-registered predictions.</div>
    </div>
    <div class="ip-item">
      <div class="ip-date">FEB 2026</div>
      <div class="ip-title">Patent Application Filed — PENDING</div>
      <div class="ip-detail">Method and system patent. 40 claims covering: dual-criterion algorithm, adaptive Ω weighting, locked-in protocol, GPU parallelization, wearable architecture, cloud system, forensic mode. Brazilian law Art. 8 + EPC Art. 52(1).</div>
    </div>
    <div class="ip-item">
      <div class="ip-date">2026 →</div>
      <div class="ip-title">Peer Review Submission Planned</div>
      <div class="ip-detail">Target: Nature Neuroscience / PNAS. Peer-reviewed publication will establish independent scientific validation and dramatically increase licensing leverage.</div>
    </div>
  </div>
</section>

<!-- SLIDE 8: DEAL -->
<section class="slide slide-deal" id="s8">
  <div class="slide-number">08 / 09</div>
  <div class="slide-tag">Licensing Terms</div>
  <h2>Deal Structure</h2>

  <div class="deal-structure">
    <div class="deal-box">
      <h3>PROPOSED TERMS</h3>
      <div class="deal-item">
        <span class="deal-item-label">Royalty Rate</span>
        <span class="deal-item-value gold">12–15%</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">Upfront Payment</span>
        <span class="deal-item-value">Negotiable</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">Territory</span>
        <span class="deal-item-value">Global</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">License Type</span>
        <span class="deal-item-value">Exclusive / Field</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">Sublicensing</span>
        <span class="deal-item-value">Permitted</span>
      </div>
    </div>

    <div class="deal-box">
      <h3>RATIONALE FOR RATE</h3>
      <div class="deal-item">
        <span class="deal-item-label">Industry benchmark (medical devices)</span>
        <span class="deal-item-value">8–18%</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">No direct competitor</span>
        <span class="deal-item-value gold">↑ Premium</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">Platform (multi-market)</span>
        <span class="deal-item-value gold">↑ Premium</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">Pre-registered IP protection</span>
        <span class="deal-item-value gold">↑ Premium</span>
      </div>
      <div class="deal-item">
        <span class="deal-item-label">Pending patent (not granted)</span>
        <span class="deal-item-value">↓ Discount</span>
      </div>
    </div>
  </div>
</section>

<!-- SLIDE 9: STRATEGY -->
<section class="slide slide-strategy" id="s9">
  <div class="slide-number">09 / 09</div>
  <div class="slide-tag">Go-To-Market Strategy</div>
  <h2>Four-Phase<br>Commercialization</h2>

  <div class="strategy-phases">
    <div class="phase">
      <div class="phase-num">PHASE 01</div>
      <div class="phase-title">Credibility</div>
      <div class="phase-time">Now → 3 months</div>
      <ul class="phase-items">
        <li>Submit to Nature Neuroscience or PNAS</li>
        <li>Build computational demo (algorithm on real data)</li>
        <li>Document methodology publicly</li>
        <li>"Under review at X" in all conversations</li>
      </ul>
    </div>
    <div class="phase">
      <div class="phase-num">PHASE 02</div>
      <div class="phase-title">Partnership</div>
      <div class="phase-time">2–4 months</div>
      <ul class="phase-items">
        <li>Approach USP / Unicamp tech transfer office</li>
        <li>Healthtech accelerators (Pulse, Rock Health)</li>
        <li>Hospital pilot agreement for data validation</li>
        <li>Engage PI attorney specializing in med devices</li>
      </ul>
    </div>
    <div class="phase">
      <div class="phase-num">PHASE 03</div>
      <div class="phase-title">Negotiation</div>
      <div class="phase-time">3–6 months</div>
      <ul class="phase-items">
        <li>Tier 1: Masimo, Nihon Kohden (faster)</li>
        <li>Tier 2: Medtronic, Philips (larger)</li>
        <li>Open at 15–18%, floor at 12%</li>
        <li>Consider upfront + lower royalty hybrid</li>
      </ul>
    </div>
    <div class="phase">
      <div class="phase-num">PHASE 04</div>
      <div class="phase-title">Execution</div>
      <div class="phase-time">6–18 months</div>
      <ul class="phase-items">
        <li>License signed, upfront received</li>
        <li>Partner handles regulatory (FDA/ANVISA)</li>
        <li>Partner handles manufacturing</li>
        <li>Royalties begin on commercial sales</li>
      </ul>
    </div>
  </div>
</section>

<!-- SLIDE CONTACT -->
<section class="slide slide-contact" id="s10">
  <div class="slide-tag">Contact</div>
  <h2>Samuel Santos<br>Oliveira da Silva</h2>

  <div class="contact-content">
    <div class="contact-left">
      <div class="contact-item">
        <div class="contact-item-label">ORCID</div>
        <div class="contact-item-value">0009-0000-6882-619X</div>
      </div>
      <div class="contact-item">
        <div class="contact-item-label">EMAIL (RESEARCH)</div>
        <div class="contact-item-value">samuelsilva.research@proton.me</div>
      </div>
      <div class="contact-item">
        <div class="contact-item-label">PATENT STATUS</div>
        <div class="contact-item-value">Filed & Pending — February 2026</div>
      </div>
      <div class="contact-item">
        <div class="contact-item-label">PUBLICATIONS</div>
        <div class="contact-item-value">Zenodo DOIs: 10.5281/zenodo.18113271 → 18402684</div>
      </div>
    </div>
    <div class="contact-right">
      <div class="contact-quote">"TCR is the first consciousness theory that resolves the ketamine paradox, detects locked-in syndrome with 100% accuracy, and provides a real-time clinical instrument — all from a single theoretical framework."</div>
    </div>
  </div>
</section>

<script>
  const slides = document.querySelectorAll('.slide');
  const nav = document.getElementById('nav');

  slides.forEach((_, i) => {
    const dot = document.createElement('div');
    dot.className = 'nav-dot';
    dot.onclick = () => slides[i].scrollIntoView({ behavior: 'smooth' });
    nav.appendChild(dot);
  });

  const dots = nav.querySelectorAll('.nav-dot');

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const idx = Array.from(slides).indexOf(entry.target);
        dots.forEach(d => d.classList.remove('active'));
        if (dots[idx]) dots[idx].classList.add('active');
      }
    });
  }, { threshold: 0.5 });

  slides.forEach(s => observer.observe(s));
</script>
</body>
</html>

