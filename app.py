from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>CLUTCH | The Ultimate Game</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background: #050505;
    color: #ffffff;
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.6;
}

/* =========================
   NAVIGATION
========================= */

nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 76px;
    z-index: 1000;

    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 0 7%;

    background: rgba(5,5,5,0.88);
    backdrop-filter: blur(12px);

    border-bottom: 1px solid rgba(255,193,7,0.15);
}

.logo {
    font-size: 28px;
    font-weight: 900;
    letter-spacing: 5px;
    color: #ffffff;
}

.nav-links {
    display: flex;
    gap: 35px;
}

.nav-links a {
    color: #ffffff;
    text-decoration: none;
    font-weight: 700;
    font-size: 14px;
    transition: 0.25s;
}

.nav-links a:hover {
    color: #ffc400;
}

/* =========================
   HERO
========================= */

.hero {
    min-height: 100vh;
    position: relative;

    display: flex;
    align-items: center;
    justify-content: center;

    overflow: hidden;
}

.hero-video {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    object-fit: cover;

    z-index: 0;
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            180deg,
            rgba(0,0,0,0.78) 0%,
            rgba(0,0,0,0.48) 45%,
            rgba(0,0,0,0.94) 100%
        );

    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;

    text-align: center;
    padding: 30px;
}

.hero-small {
    color: #ffc400;
    font-size: 14px;
    letter-spacing: 6px;
    font-weight: 800;
    margin-bottom: 15px;
}

.hero-title {
    font-size: clamp(70px, 13vw, 180px);
    font-weight: 1000;
    letter-spacing: 12px;
    line-height: 0.9;

    text-shadow:
        0 0 10px rgba(255,196,0,0.15),
        0 0 35px rgba(255,196,0,0.08);
}

.hero-title span {
    color: #ffc400;
}

.hero-subtitle {
    margin-top: 28px;
    font-size: clamp(15px, 2vw, 22px);
    letter-spacing: 5px;
    color: #dddddd;
}

.hero-buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 42px;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;

    padding: 15px 30px;

    border-radius: 4px;

    text-decoration: none;

    font-weight: 900;
    letter-spacing: 1px;

    transition: 0.3s;
}

.btn-primary {
    background: #ffc400;
    color: #050505;
}

.btn-primary:hover {
    background: #ffffff;
    transform: translateY(-3px);
    box-shadow: 0 10px 35px rgba(255,196,0,0.25);
}

.btn-secondary {
    color: #ffffff;
    border: 1px solid rgba(255,255,255,0.4);
}

.btn-secondary:hover {
    border-color: #ffc400;
    color: #ffc400;
}

/* =========================
   GENERAL
========================= */

section {
    padding: 110px 7%;
}

.section-label {
    color: #ffc400;
    font-size: 12px;
    font-weight: 900;
    letter-spacing: 5px;
    text-align: center;
    margin-bottom: 10px;
}

.section-title {
    font-size: clamp(35px, 5vw, 65px);
    text-align: center;
    font-weight: 900;
    margin-bottom: 60px;
}

.section-title span {
    color: #ffc400;
}

/* =========================
   GAMES
========================= */

.games-section {
    background:
        radial-gradient(
            circle at center top,
            rgba(255,196,0,0.08),
            transparent 45%
        ),
        #050505;
}

.games-grid {
    max-width: 1250px;
    margin: auto;

    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.game-card {
    position: relative;

    padding: 35px;

    min-height: 280px;

    background:
        linear-gradient(
            145deg,
            #151515,
            #090909
        );

    border: 1px solid #242424;

    overflow: hidden;

    transition: 0.35s;
}

.game-card::before {
    content: "";

    position: absolute;
    top: 0;
    left: 0;

    width: 4px;
    height: 100%;

    background: #ffc400;

    transform: scaleY(0);
    transform-origin: bottom;

    transition: 0.35s;
}

.game-card:hover {
    transform: translateY(-8px);
    border-color: rgba(255,196,0,0.55);

    box-shadow:
        0 15px 50px rgba(0,0,0,0.5),
        0 0 30px rgba(255,196,0,0.06);
}

.game-card:hover::before {
    transform: scaleY(1);
}

.game-number {
    color: #666;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 3px;
}

.game-name {
    font-size: 32px;
    font-weight: 900;
    margin-top: 30px;
}

.game-name span {
    color: #ffc400;
}

.game-description {
    color: #999;
    margin-top: 12px;
    font-size: 14px;
}

.game-info {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;

    margin-top: 25px;
}

.tag {
    border: 1px solid #333;
    padding: 6px 9px;

    font-size: 11px;
    font-weight: 700;

    color: #ccc;
}

.game-card button {
    margin-top: 25px;

    background: transparent;
    border: none;

    color: #ffc400;

    font-weight: 900;
    cursor: pointer;
}

/* =========================
   DETAILS
========================= */

.details {
    max-width: 1250px;
    margin: 45px auto 0;

    display: none;

    background: #0d0d0d;
    border: 1px solid #292929;

    padding: 35px;
}

.details.active {
    display: block;
    animation: fadeIn 0.35s ease;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.details h3 {
    color: #ffc400;
    font-size: 25px;
    margin-bottom: 20px;
}

.details-grid {
    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 15px;
}

.detail-box {
    background: #141414;
    padding: 18px;
    border-left: 2px solid #ffc400;
}

.detail-box strong {
    display: block;
    color: #ffffff;
    margin-bottom: 4px;
}

.detail-box span {
    color: #999;
}

/* =========================
   RULES
========================= */

.rules-section {
    background: #080808;
}

.rules-container {
    max-width: 1050px;
    margin: auto;
}

.rule-tabs {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;

    margin-bottom: 35px;
}

.rule-tab {
    background: #111;
    border: 1px solid #292929;

    color: #aaa;

    padding: 12px 20px;

    cursor: pointer;

    font-weight: 800;

    transition: 0.25s;
}

.rule-tab:hover,
.rule-tab.active {
    background: #ffc400;
    color: #050505;
    border-color: #ffc400;
}

.rule-content {
    display: none;

    background: #101010;
    border: 1px solid #242424;

    padding: 35px;
}

.rule-content.active {
    display: block;
}

.rule-content h3 {
    font-size: 30px;
    margin-bottom: 20px;
}

.rule-content h3 span {
    color: #ffc400;
}

.rule-content ul {
    padding-left: 20px;
}

.rule-content li {
    margin-bottom: 12px;
    color: #bdbdbd;
}

.rule-warning {
    margin-top: 25px;
    padding: 15px;

    background: rgba(255,196,0,0.07);
    border-left: 3px solid #ffc400;

    color: #ddd;
}

/* =========================
   WORKSHOP
========================= */

.workshop {
    max-width: 1050px;
    margin: auto;

    background:
        linear-gradient(
            135deg,
            #111111,
            #080808
        );

    border: 1px solid #292929;

    padding: 55px;

    position: relative;
    overflow: hidden;
}

.workshop::after {
    content: "CLUTCH";

    position: absolute;

    right: -40px;
    bottom: -45px;

    font-size: 130px;
    font-weight: 1000;

    color: rgba(255,196,0,0.025);
}

.workshop h3 {
    font-size: 38px;
}

.workshop h3 span {
    color: #ffc400;
}

.workshop p {
    color: #aaa;
    max-width: 800px;
    margin-top: 18px;
}

.workshop-list {
    margin-top: 25px;
    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 10px;
}

.workshop-item {
    padding: 13px 15px;
    background: #151515;
    color: #ccc;
}

.workshop-item::before {
    content: "◆";
    color: #ffc400;
    margin-right: 10px;
}

/* =========================
   CARDS
========================= */

.cards-section {
    background: #050505;
}

.cards-grid {
    max-width: 1050px;
    margin: auto;

    display: grid;
    grid-template-columns: repeat(2,1fr);
    gap: 30px;
}

.id-card {
    width: 100%;

    border: 1px solid #292929;

    transition: 0.35s;
}

.id-card:hover {
    transform: scale(1.015);
    border-color: #ffc400;
    box-shadow: 0 15px 50px rgba(0,0,0,0.6);
}

.id-card img {
    width: 100%;
    display: block;
}

/* =========================
   LIVE
========================= */

.live-section {
    background:
        radial-gradient(
            circle at center,
            rgba(255,196,0,0.07),
            transparent 50%
        ),
        #080808;
}

.live-box {
    max-width: 1050px;
    margin: auto;

    border: 1px solid #292929;
    background: #0d0d0d;

    padding: 45px;

    text-align: center;
}

.live-status {
    display: inline-flex;
    align-items: center;
    gap: 9px;

    color: #ff3d3d;

    font-weight: 900;
    letter-spacing: 3px;
    font-size: 12px;
}

.live-dot {
    width: 9px;
    height: 9px;
    background: #ff3d3d;
    border-radius: 50%;
    animation: pulse 1.2s infinite;
}

@keyframes pulse {
    50% {
        opacity: 0.25;
        transform: scale(0.7);
    }
}

.live-box h3 {
    margin-top: 20px;
    font-size: 38px;
}

.live-box p {
    color: #888;
    margin: 12px auto 30px;
}

/* =========================
   FOOTER
========================= */

footer {
    padding: 55px 7%;

    background: #030303;

    border-top: 1px solid #191919;

    text-align: center;
}

.footer-logo {
    font-size: 32px;
    font-weight: 1000;
    letter-spacing: 7px;
}

.footer-tagline {
    color: #777;
    margin-top: 8px;
}

.footer-line {
    width: 70px;
    height: 2px;

    background: #ffc400;

    margin: 25px auto;
}

.copyright {
    color: #444;
    font-size: 12px;
}

/* =========================
   MOBILE
========================= */

@media (max-width: 900px) {

    .games-grid {
        grid-template-columns: repeat(2,1fr);
    }

    .cards-grid {
        grid-template-columns: 1fr;
    }

}

@media (max-width: 650px) {

    nav {
        padding: 0 5%;
    }

    .nav-links {
        gap: 12px;
    }

    .nav-links a {
        font-size: 11px;
    }

    .hero-title {
        letter-spacing: 5px;
    }

    section {
        padding: 80px 5%;
    }

    .games-grid {
        grid-template-columns: 1fr;
    }

    .details-grid {
        grid-template-columns: 1fr;
    }

    .workshop {
        padding: 30px;
    }

    .workshop-list {
        grid-template-columns: 1fr;
    }

    .live-box {
        padding: 30px 20px;
    }

}

</style>
</head>

<body>

<!-- =========================
     NAVIGATION
========================= -->

<nav>

    <div class="logo">
        CLUTCH
    </div>

    <div class="nav-links">
        <a href="#games">GAMES</a>
        <a href="#rules">RULES</a>
        <a href="#workshop">WORKSHOP</a>
        <a href="#live">LIVE</a>
    </div>

</nav>


<!-- =========================
     HERO
========================= -->

<header class="hero">

    <video
        class="hero-video"
        autoplay
        muted
        loop
        playsinline
        preload="auto">

        <source src="/static/bd.mp4" type="video/mp4">

    </video>

    <div class="hero-overlay"></div>

    <div class="hero-content">

        <div class="hero-small">
            ESPORTS • GAMING • COMPETITION
        </div>

        <h1 class="hero-title">
            CLU<span>T</span>CH
        </h1>

        <div class="hero-subtitle">
            THE ULTIMATE GAME
        </div>

        <div class="hero-buttons">

            <a href="#games" class="btn btn-primary">
                EXPLORE EVENTS
            </a>

            <a href="#rules" class="btn btn-secondary">
                VIEW RULES
            </a>

        </div>

    </div>

</header>


<!-- =========================
     GAMES
========================= -->

<section id="games" class="games-section">

    <div class="section-label">
        THE BATTLEGROUND
    </div>

    <h2 class="section-title">
        CHOOSE YOUR <span>GAME</span>
    </h2>


    <div class="games-grid">


        <!-- VALORANT -->

        <div class="game-card">

            <div class="game-number">01 / FPS</div>

            <div class="game-name">
                VALO<span>RANT</span>
            </div>

            <div class="game-description">
                Tactical competitive FPS tournament.
            </div>

            <div class="game-info">
                <div class="tag">5v5</div>
                <div class="tag">PC</div>
                <div class="tag">BO1</div>
                <div class="tag">SINGLE ELIMINATION</div>
            </div>

            <button onclick="showGame('valorant')">
                VIEW DETAILS →
            </button>

        </div>


        <!-- BGMI -->

        <div class="game-card">

            <div class="game-number">02 / BATTLE ROYALE</div>

            <div class="game-name">
                <span>BGMI</span>
            </div>

            <div class="game-description">
                Squad-based mobile battle royale competition.
            </div>

            <div class="game-info">
                <div class="tag">4 PLAYER</div>
                <div class="tag">MOBILE</div>
                <div class="tag">24 TEAMS</div>
                <div class="tag">TPP</div>
            </div>

            <button onclick="showGame('bgmi')">
                VIEW DETAILS →
            </button>

        </div>


        <!-- CHESS -->

        <div class="game-card">

            <div class="game-number">03 / STRATEGY</div>

            <div class="game-name">
                <span>CHESS</span>
            </div>

            <div class="game-description">
                Competitive Chess.com tournament.
            </div>

            <div class="game-info">
                <div class="tag">1v1</div>
                <div class="tag">PC</div>
                <div class="tag">BLITZ</div>
                <div class="tag">RAPID</div>
            </div>

            <button onclick="showGame('chess')">
                VIEW DETAILS →
            </button>

        </div>


        <!-- MINECRAFT PVP -->

        <div class="game-card">

            <div class="game-number">04 / COMBAT</div>

            <div class="game-name">
                MINECRAFT <span>PvP</span>
            </div>

            <div class="game-description">
                One-on-one Minecraft combat.
            </div>

            <div class="game-info">
                <div class="tag">1v1</div>
                <div class="tag">PC</div>
                <div class="tag">10 MIN</div>
                <div class="tag">SINGLE ELIMINATION</div>
            </div>

            <button onclick="showGame('pvp')">
                VIEW DETAILS →
            </button>

        </div>


        <!-- MINECRAFT BUILDING -->

        <div class="game-card">

            <div class="game-number">05 / CREATIVE</div>

            <div class="game-name">
                MINECRAFT <span>BUILD</span>
            </div>

            <div class="game-description">
                Build, design and create under pressure.
            </div>

            <div class="game-info">
                <div class="tag">1 PER TEAM</div>
                <div class="tag">PC</div>
                <div class="tag">2 HOURS</div>
                <div class="tag">CREATIVE</div>
            </div>

            <button onclick="showGame('building')">
                VIEW DETAILS →
            </button>

        </div>

    </div>


    <!-- DETAILS -->

    <div id="valorant" class="details">

        <h3>VALO<span>RANT</span></h3>

        <div class="details-grid">

            <div class="detail-box">
                <strong>Participants</strong>
                <span>5 per team — Classes 8–12</span>
            </div>

            <div class="detail-box">
                <strong>Platform</strong>
                <span>PC</span>
            </div>

            <div class="detail-box">
                <strong>Format</strong>
                <span>Single Elimination — Best of 1</span>
            </div>

            <div class="detail-box">
                <strong>Devices</strong>
                <span>Tournament devices will be provided</span>
            </div>

            <div class="detail-box">
                <strong>Account</strong>
                <span>Participants use personal IDs</span>
            </div>

            <div class="detail-box">
                <strong>Match Mode</strong>
                <span>Swiftplay up to Semifinals; Finals in Unrated</span>
            </div>

            <div class="detail-box">
                <strong>Map Pool</strong>
                <span>Ascent, Breeze, Haven, Lotus, Split, Summit, Sunset</span>
            </div>

            <div class="detail-box">
                <strong>Map Selection</strong>
                <span>Tournament officials or map veto depending on availability</span>
            </div>

        </div>

    </div>


    <div id="bgmi" class="details">

        <h3><span>BGMI</span></h3>

        <div class="details-grid">

            <div class="detail-box">
                <strong>Participants</strong>
                <span>4 per team — Classes 8–12</span>
            </div>

            <div class="detail-box">
                <strong>Platform</strong>
                <span>Mobile</span>
            </div>

            <div class="detail-box">
                <strong>Format</strong>
                <span>Single Elimination — Best of 1</span>
            </div>

            <div class="detail-box">
                <strong>Teams</strong>
                <span>24 teams — First come, first served</span>
            </div>

            <div class="detail-box">
                <strong>Total Matches</strong>
                <span>7</span>
            </div>

            <div class="detail-box">
                <strong>Match Type</strong>
                <span>Squad TPP</span>
            </div>

            <div class="detail-box">
                <strong>Maps</strong>
                <span>Erangle, Miramar, Rondo and Livik</span>
            </div>

            <div class="detail-box">
                <strong>Scoring</strong>
                <span>Official PUBGM EWC 2026 points system</span>
            </div>

        </div>

    </div>


    <div id="chess" class="details">

        <h3><span>CHESS</span></h3>

        <div class="details-grid">

            <div class="detail-box">
                <strong>Participants</strong>
                <span>1 per team — Classes 8–12</span>
            </div>

            <div class="detail-box">
                <strong>Platform</strong>
                <span>PC — Chess.com</span>
            </div>

            <div class="detail-box">
                <strong>Format</strong>
                <span>Single Elimination — Best of 1</span>
            </div>

            <div class="detail-box">
                <strong>Accounts</strong>
                <span>Accounts will be provided</span>
            </div>

            <div class="detail-box">
                <strong>Rounds up to Semifinals</strong>
                <span>Blitz — 5|0</span>
            </div>

            <div class="detail-box">
                <strong>Semifinals & Finals</strong>
                <span>Rapid — 10|0</span>
            </div>

            <div class="detail-box">
                <strong>Blitz Tiebreak</strong>
                <span>3|0 Bullet</span>
            </div>

            <div class="detail-box">
                <strong>Rapid Tiebreak</strong>
                <span>5|0 Blitz, then 3|0 Bullet if needed</span>
            </div>

        </div>

        <div class="rule-warning">
            Any form of external assistance will lead to immediate disqualification.
        </div>

    </div>


    <div id="pvp" class="details">

        <h3>MINECRAFT <span>PvP</span></h3>

        <div class="details-grid">

            <div class="detail-box">
                <strong>Participants</strong>
                <span>1 per team — Classes 8–12</span>
            </div>

            <div class="detail-box">
                <strong>Platform</strong>
                <span>PC</span>
            </div>

            <div class="detail-box">
                <strong>Format</strong>
                <span>Single Elimination — Best of 1</span>
            </div>

            <div class="detail-box">
                <strong>Accounts</strong>
                <span>Accounts will be provided</span>
            </div>

            <div class="detail-box">
                <strong>PvP Kit</strong>
                <span>Provided by the tournament</span>
            </div>

            <div class="detail-box">
                <strong>Match Timer</strong>
                <span>10 minutes</span>
            </div>

            <div class="detail-box">
                <strong>Draw Rule</strong>
                <span>Player with the most hearts after 10 minutes wins</span>
            </div>

        </div>

    </div>


    <div id="building" class="details">

        <h3>MINECRAFT <span>BUILDING</span></h3>

        <div class="details-grid">

            <div class="detail-box">
                <strong>Participants</strong>
                <span>1 per team — Classes 8–12</span>
            </div>

            <div class="detail-box">
                <strong>Platform</strong>
                <span>PC</span>
            </div>

            <div class="detail-box">
                <strong>Format</strong>
                <span>Single Elimination — Best of 1</span>
            </div>

            <div class="detail-box">
                <strong>Accounts</strong>
                <span>Accounts will be provided</span>
            </div>

            <div class="detail-box">
                <strong>Theme</strong>
                <span>Theme will be given for the build</span>
            </div>

            <div class="detail-box">
                <strong>Time Limit</strong>
                <span>2 hours</span>
            </div>

            <div class="detail-box">
                <strong>Mods</strong>
                <span>Mods such as Litematica are not allowed</span>
            </div>

        </div>

    </div>

</section>


<!-- =========================
     RULES
========================= -->

<section id="rules" class="rules-section">

    <div class="section-label">
        OFFICIAL REGULATIONS
    </div>

    <h2 class="section-title">
        TOURNAMENT <span>RULEBOOK</span>
    </h2>


    <div class="rules-container">

        <div class="rule-tabs">

            <button class="rule-tab active"
                    onclick="showRules('r-valorant', this)">
                VALORANT
            </button>

            <button class="rule-tab"
                    onclick="showRules('r-bgmi', this)">
                BGMI
            </button>

            <button class="rule-tab"
                    onclick="showRules('r-chess', this)">
                CHESS
            </button>

            <button class="rule-tab"
                    onclick="showRules('r-pvp', this)">
                MINECRAFT PvP
            </button>

            <button class="rule-tab"
                    onclick="showRules('r-building', this)">
                MINECRAFT BUILDING
            </button>

        </div>


        <div id="r-valorant" class="rule-content active">

            <h3>VALO<span>RANT</span></h3>

            <ul>
                <li>5 participants per team.</li>
                <li>Participants are from Classes 8–12.</li>
                <li>The tournament follows single elimination.</li>
                <li>Matches are Best of 1.</li>
                <li>Tournament devices will be provided.</li>
                <li>Participants will use their personal in-game IDs.</li>
                <li>Matches up to the Top 2 / Semifinals and below will use Swiftplay.</li>
                <li>The Finals will be played in Unrated mode.</li>
                <li>The tournament follows the current competitive map pool specified by the organisers.</li>
                <li>Map selection will be decided by tournament officials or through map veto depending on time availability.</li>
            </ul>

        </div>


        <div id="r-bgmi" class="rule-content">

            <h3><span>BGMI</span></h3>

            <ul>
                <li>4 participants per team.</li>
                <li>Participants are from Classes 8–12.</li>
                <li>The tournament follows single elimination.</li>
                <li>24 teams will be accepted on a first-come, first-served basis.</li>
                <li>The tournament consists of 7 matches.</li>
                <li>Matches are Squad TPP.</li>
                <li>Maps include Erangle, Miramar, Rondo and Livik.</li>
                <li>Devices are allowed for the BGMI tournament.</li>
                <li>Participants will use their personal in-game IDs.</li>
                <li>The official PUBGM EWC 2026 points system will be used for scoring.</li>
            </ul>

        </div>


        <div id="r-chess" class="rule-content">

            <h3><span>CHESS</span></h3>

            <ul>
                <li>1 participant per team.</li>
                <li>Participants are from Classes 8–12.</li>
                <li>All matches are played on Chess.com using tournament devices.</li>
                <li>The tournament follows single elimination.</li>
                <li>Rounds up to the semifinals are played in Blitz format — 5|0.</li>
                <li>Semifinals and Finals are played in Rapid format — 10|0.</li>
                <li>For a draw in a Blitz round, the tiebreak is 3|0 Bullet.</li>
                <li>For a draw in a Rapid round, the tiebreak is 5|0 Blitz.</li>
                <li>If required, the Rapid tiebreak proceeds to 3|0 Bullet.</li>
            </ul>

            <div class="rule-warning">
                Any form of external assistance will lead to immediate disqualification.
            </div>

        </div>


        <div id="r-pvp" class="rule-content">

            <h3>MINECRAFT <span>PvP</span></h3>

            <ul>
                <li>1 participant per team.</li>
                <li>Participants are from Classes 8–12.</li>
                <li>The tournament follows single elimination.</li>
                <li>Matches are Best of 1.</li>
                <li>Tournament devices will be provided.</li>
                <li>Accounts will be provided.</li>
                <li>A PvP kit will be provided.</li>
                <li>Every matchup has a 10-minute timer.</li>
                <li>In case of a draw, the player with the most hearts after the 10-minute mark wins.</li>
            </ul>

        </div>


        <div id="r-building" class="rule-content">

            <h3>MINECRAFT <span>BUILDING</span></h3>

            <ul>
                <li>1 participant per team.</li>
                <li>Participants are from Classes 8–12.</li>
                <li>The tournament follows single elimination.</li>
                <li>Matches are Best of 1.</li>
                <li>Tournament devices will be provided.</li>
                <li>Accounts will be provided.</li>
                <li>A theme will be provided for the build.</li>
                <li>Each team receives 2 hours to complete the build.</li>
                <li>Mods such as Litematica are not allowed.</li>
            </ul>

        </div>

    </div>

</section>


<!-- =========================
     WORKSHOP
========================= -->

<section id="workshop">

    <div class="section-label">
        LEARN • CREATE • BUILD
    </div>

    <h2 class="section-title">
        GAME BUILDING <span>WORKSHOP</span>
    </h2>


    <div class="workshop">

        <h3>
            BUILD YOUR <span>GAME</span>
        </h3>

        <p>
            The Game Building Workshop is a hands-on game development
            session conducted in collaboration with Microsoft Campus
            Ambassadors from Banaras Hindu University (BHU).
        </p>

        <p>
            Participants will be introduced to the basics of creating
            a game, including concepts, mechanics, controls, design and
            basic development.
        </p>

        <div class="workshop-list">

            <div class="workshop-item">
                Game Concepts
            </div>

            <div class="workshop-item">
                Game Mechanics
            </div>

            <div class="workshop-item">
                Controls
            </div>

            <div class="workshop-item">
                Game Design
            </div>

            <div class="workshop-item">
                Basic Development
            </div>

            <div class="workshop-item">
                Guided Demonstration
            </div>

            <div class="workshop-item">
                Build Your Own Prototype
            </div>

            <div class="workshop-item">
                Mentor Guidance
            </div>

        </div>

    </div>

</section>


<!-- =========================
     EVENT CARDS
========================= -->

<section class="cards-section">

    <div class="section-label">
        OFFICIAL ACCESS
    </div>

    <h2 class="section-title">
        CLUTCH <span>CREDENTIALS</span>
    </h2>


    <div class="cards-grid">

        <div class="id-card">

            <img
                src="/static/organiser.png"
                alt="CLUTCH Organiser Card">

        </div>


        <div class="id-card">

            <img
                src="/static/participant.png"
                alt="CLUTCH Participant Card">

        </div>

    </div>

</section>


<!-- =========================
     LIVE
========================= -->

<section id="live" class="live-section">

    <div class="section-label">
        THE ACTION GOES LIVE
    </div>

    <h2 class="section-title">
        WATCH <span>CLUTCH</span>
    </h2>


    <div class="live-box">

        <div class="live-status">

            <div class="live-dot"></div>

            LIVE STREAM

        </div>

        <h3>
            THE ULTIMATE GAME
        </h3>

        <p>
            Follow the action, matches and tournament moments
            on the official CLUTCH YouTube channel.
        </p>

        <!--
        Replace YOUR_YOUTUBE_LINK below with your actual
        YouTube channel or livestream link.
        -->

        <a
            href="https://www.youtube.com/"
            target="_blank"
            class="btn btn-primary">

            WATCH ON YOUTUBE

        </a>

    </div>

</section>


<!-- =========================
     FOOTER
========================= -->

<footer>

    <div class="footer-logo">
        CLUTCH
    </div>

    <div class="footer-tagline">
        THE ULTIMATE GAME
    </div>

    <div class="footer-line"></div>

    <div class="copyright">
        © 2026 CLUTCH. All rights reserved.
    </div>

</footer>


<script>

/* =========================
   GAME DETAILS
========================= */

function showGame(game) {

    const allDetails =
        document.querySelectorAll(".details");

    allDetails.forEach(function(item) {
        item.classList.remove("active");
    });

    const selected =
        document.getElementById(game);

    if (selected) {

        selected.classList.add("active");

        setTimeout(function() {

            selected.scrollIntoView({
                behavior: "smooth",
                block: "center"
            });

        }, 50);

    }

}


/* =========================
   RULE TABS
========================= */

function showRules(rule, button) {

    const contents =
        document.querySelectorAll(".rule-content");

    contents.forEach(function(content) {
        content.classList.remove("active");
    });


    const tabs =
        document.querySelectorAll(".rule-tab");

    tabs.forEach(function(tab) {
        tab.classList.remove("active");
    });


    document
        .getElementById(rule)
        .classList.add("active");


    button.classList.add("active");

}

</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
