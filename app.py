from flask import Flask, render_template_string, url_for
import os

app = Flask(__name__)

HTML = """
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
            overflow-x: hidden;
        }

        /* =========================
           NAVIGATION
        ========================= */

        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 74px;
            z-index: 1000;

            display: flex;
            justify-content: space-between;
            align-items: center;

            padding: 0 7%;

            background: rgba(0, 0, 0, 0.72);
            backdrop-filter: blur(15px);

            border-bottom: 1px solid rgba(255, 193, 7, 0.15);
        }

        .logo {
            font-size: 27px;
            font-weight: 900;
            letter-spacing: 4px;
            color: #ffd21c;
        }

        .logo span {
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 32px;
            list-style: none;
        }

        .nav-links a {
            color: #ffffff;
            text-decoration: none;
            font-size: 14px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s;
        }

        .nav-links a:hover {
            color: #ffd21c;
        }

        /* =========================
           HERO
        ========================= */

        .hero {
            position: relative;
            min-height: 100vh;
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
            z-index: 1;

            background:
                linear-gradient(
                    90deg,
                    rgba(0,0,0,0.95),
                    rgba(0,0,0,0.58),
                    rgba(0,0,0,0.88)
                );
        }

        .hero-overlay::after {
            content: "";
            position: absolute;
            inset: 0;

            background:
                radial-gradient(
                    circle at center,
                    transparent 15%,
                    rgba(0,0,0,0.65) 100%
                );
        }

        .hero-content {
            position: relative;
            z-index: 2;
            width: 90%;
            max-width: 1200px;
            text-align: center;
            padding-top: 60px;
        }

        .eyebrow {
            color: #ffd21c;
            font-size: 15px;
            font-weight: 800;
            letter-spacing: 5px;
            text-transform: uppercase;
            margin-bottom: 20px;
        }

        .hero h1 {
            font-size: clamp(65px, 12vw, 150px);
            line-height: 0.85;
            font-weight: 1000;
            letter-spacing: -7px;
            text-transform: uppercase;

            color: #ffffff;

            text-shadow:
                0 0 15px rgba(255,210,28,0.15),
                0 0 45px rgba(255,210,28,0.08);
        }

        .hero h1 span {
            color: #ffd21c;
        }

        .hero-subtitle {
            margin-top: 28px;
            color: #d4d4d4;
            font-size: 19px;
            letter-spacing: 2px;
        }

        .hero-buttons {
            margin-top: 40px;

            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .btn {
            display: inline-block;
            padding: 15px 30px;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 13px;
            font-weight: 900;
            letter-spacing: 1.5px;

            transition: 0.3s;
        }

        .btn-primary {
            background: #ffd21c;
            color: #000000;
        }

        .btn-primary:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 30px rgba(255,210,28,0.25);
        }

        .btn-secondary {
            border: 1px solid rgba(255,255,255,0.5);
            color: white;
            background: rgba(0,0,0,0.3);
        }

        .btn-secondary:hover {
            border-color: #ffd21c;
            color: #ffd21c;
        }

        /* =========================
           GENERAL SECTIONS
        ========================= */

        section {
            padding: 110px 7%;
        }

        .section-header {
            max-width: 850px;
            margin-bottom: 55px;
        }

        .section-label {
            color: #ffd21c;
            text-transform: uppercase;
            font-size: 12px;
            font-weight: 900;
            letter-spacing: 4px;
            margin-bottom: 14px;
        }

        .section-title {
            font-size: clamp(38px, 6vw, 70px);
            line-height: 0.95;
            text-transform: uppercase;
            font-weight: 950;
        }

        .section-description {
            margin-top: 20px;
            color: #999999;
            max-width: 700px;
            line-height: 1.7;
        }

        /* =========================
           GAMES
        ========================= */

        #games {
            background:
                linear-gradient(#050505, #080808);
        }

        .games-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .game-card {
            position: relative;
            min-height: 300px;
            padding: 35px;

            background:
                linear-gradient(
                    135deg,
                    #111111,
                    #080808
                );

            border: 1px solid #202020;

            overflow: hidden;
            transition: 0.35s;
        }

        .game-card::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 5px;
            height: 100%;
            background: #ffd21c;
        }

        .game-card::after {
            content: "";
            position: absolute;
            width: 250px;
            height: 250px;
            right: -100px;
            bottom: -100px;

            border-radius: 50%;
            background: rgba(255,210,28,0.07);
        }

        .game-card:hover {
            transform: translateY(-7px);
            border-color: rgba(255,210,28,0.5);
        }

        .game-number {
            color: #555555;
            font-size: 13px;
            font-weight: 900;
            letter-spacing: 2px;
        }

        .game-card h3 {
            margin-top: 35px;
            font-size: 32px;
            text-transform: uppercase;
        }

        .game-card p {
            margin-top: 15px;
            color: #999999;
            line-height: 1.6;
        }

        .game-info {
            margin-top: 25px;

            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .game-info span {
            padding: 8px 11px;
            background: #151515;
            border: 1px solid #292929;

            color: #cfcfcf;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }

        /* =========================
           CARDS
        ========================= */

        #cards {
            background: #090909;
        }

        .cards-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 35px;
            max-width: 1050px;
            margin: auto;
        }

        .role-card {
            background: #050505;
            border: 1px solid #252525;
            padding: 18px;
            transition: 0.35s;
        }

        .role-card:hover {
            transform: translateY(-8px);
            border-color: #ffd21c;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
        }

        .role-card img {
            display: block;
            width: 100%;
            height: auto;
        }

        .role-title {
            text-align: center;
            margin-top: 18px;
            color: #ffd21c;
            font-size: 13px;
            font-weight: 900;
            letter-spacing: 2px;
            text-transform: uppercase;
        }

        /* =========================
           WORKSHOP
        ========================= */

        #workshop {
            background:
                linear-gradient(
                    135deg,
                    #080808,
                    #111111
                );
        }

        .workshop-box {
            max-width: 1000px;
            padding: 50px;

            border: 1px solid #292929;
            background: rgba(0,0,0,0.35);

            position: relative;
            overflow: hidden;
        }

        .workshop-box::before {
            content: "";
            position: absolute;
            width: 400px;
            height: 400px;
            right: -200px;
            top: -200px;

            border-radius: 50%;
            background: rgba(255,210,28,0.08);
        }

        .workshop-box h3 {
            font-size: 38px;
            text-transform: uppercase;
        }

        .workshop-box p {
            margin-top: 20px;
            color: #a5a5a5;
            line-height: 1.8;
            max-width: 750px;
        }

        .workshop-points {
            margin-top: 30px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
        }

        .workshop-point {
            padding: 15px;
            border-left: 3px solid #ffd21c;
            background: #111111;
            color: #cccccc;
        }

        /* =========================
           RULES
        ========================= */

        #rules {
            background: #050505;
        }

        .rules-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 20px;
        }

        .rule {
            padding: 28px;
            border: 1px solid #222222;
            background: #0b0b0b;
        }

        .rule-number {
            color: #ffd21c;
            font-size: 13px;
            font-weight: 900;
        }

        .rule h4 {
            margin-top: 14px;
            font-size: 19px;
        }

        .rule p {
            margin-top: 10px;
            color: #888888;
            line-height: 1.6;
        }

        /* =========================
           STREAM
        ========================= */

        #stream {
            background: #090909;
        }

        .stream-box {
            padding: 70px 30px;
            text-align: center;

            border: 1px solid #292929;
            background:
                linear-gradient(
                    135deg,
                    #0c0c0c,
                    #111111
                );
        }

        .stream-box h2 {
            font-size: clamp(35px, 5vw, 60px);
            text-transform: uppercase;
        }

        .stream-box p {
            margin: 20px auto 30px;
            max-width: 600px;
            color: #999999;
        }

        /* =========================
           FOOTER
        ========================= */

        footer {
            padding: 45px 7%;
            border-top: 1px solid #1c1c1c;
            background: #030303;

            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            flex-wrap: wrap;
        }

        footer strong {
            color: #ffd21c;
            letter-spacing: 2px;
        }

        footer p {
            color: #666666;
            font-size: 12px;
        }

        /* =========================
           ANIMATIONS
        ========================= */

        @keyframes fadeUp {
            from {
                opacity: 0;
                transform: translateY(25px);
            }

            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-content > * {
            animation: fadeUp 1s ease forwards;
        }

        .hero h1 {
            animation-delay: 0.15s;
        }

        .hero-subtitle {
            animation-delay: 0.3s;
        }

        .hero-buttons {
            animation-delay: 0.45s;
        }

        /* =========================
           MOBILE
        ========================= */

        @media (max-width: 800px) {

            nav {
                padding: 0 5%;
            }

            .nav-links {
                gap: 12px;
            }

            .nav-links a {
                font-size: 10px;
            }

            .logo {
                font-size: 21px;
                letter-spacing: 2px;
            }

            section {
                padding: 80px 5%;
            }

            .games-grid,
            .cards-grid,
            .rules-grid {
                grid-template-columns: 1fr;
            }

            .workshop-points {
                grid-template-columns: 1fr;
            }

            .hero h1 {
                letter-spacing: -3px;
            }

            .hero-subtitle {
                font-size: 14px;
            }

            .workshop-box {
                padding: 30px;
            }

            footer {
                text-align: center;
                justify-content: center;
            }
        }

        @media (prefers-reduced-motion: reduce) {
            html {
                scroll-behavior: auto;
            }

            * {
                animation: none !important;
                transition: none !important;
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
        CLUTCH<span>.</span>
    </div>

    <ul class="nav-links">
        <li><a href="#games">Games</a></li>
        <li><a href="#cards">Cards</a></li>
        <li><a href="#workshop">Workshop</a></li>
        <li><a href="#rules">Rules</a></li>
        <li><a href="#stream">Live</a></li>
    </ul>
</nav>


<!-- =========================
     HERO
========================= -->

<header class="hero">

    <video class="hero-video"
           autoplay
           muted
           loop
           playsinline>
        <source src="{{ url_for('static', filename='bd.mp4') }}"
                type="video/mp4">
    </video>

    <div class="hero-overlay"></div>

    <div class="hero-content">

        <div class="eyebrow">
            The Ultimate Game
        </div>

        <h1>
            CLUT<span>CH</span>
        </h1>

        <p class="hero-subtitle">
            COMPETE. CREATE. CONQUER.
        </p>

        <div class="hero-buttons">
            <a href="#games" class="btn btn-primary">
                Explore Games
            </a>

            <a href="#stream" class="btn btn-secondary">
                Watch Live
            </a>
        </div>

    </div>

</header>


<!-- =========================
     GAMES
========================= -->

<section id="games">

    <div class="section-header">

        <div class="section-label">
            The Arena
        </div>

        <h2 class="section-title">
            Choose Your<br>
            Battlefield
        </h2>

        <p class="section-description">
            Five competitive experiences. One ultimate gaming event.
            Step into the arena and prove what you can do.
        </p>

    </div>


    <div class="games-grid">

        <div class="game-card">
            <div class="game-number">01 / FPS</div>

            <h3>VALORANT</h3>

            <p>
                Tactical competitive PC tournament.
                Teamwork, precision and clutch plays decide
                who survives.
            </p>

            <div class="game-info">
                <span>5 Players</span>
                <span>Classes 8–12</span>
                <span>Single Elimination</span>
                <span>BO1</span>
            </div>
        </div>


        <div class="game-card">
            <div class="game-number">02 / BATTLE ROYALE</div>

            <h3>BGMI</h3>

            <p>
                Squad-based mobile battle royale where
                strategy, positioning and survival matter.
            </p>

            <div class="game-info">
                <span>4 Players / Team</span>
                <span>24 Teams</span>
                <span>TPP</span>
                <span>7 Matches</span>
            </div>
        </div>


        <div class="game-card">
            <div class="game-number">03 / STRATEGY</div>

            <h3>CHESS</h3>

            <p>
                Competitive online chess where calculation,
                patience and tactical decisions determine
                the winner.
            </p>

            <div class="game-info">
                <span>1 Player</span>
                <span>Blitz</span>
                <span>Rapid</span>
                <span>Knockout</span>
            </div>
        </div>


        <div class="game-card">
            <div class="game-number">04 / PVP</div>

            <h3>MINECRAFT PVP</h3>

            <p>
                Enter the arena, fight your opponents and
                survive the battle.
            </p>

            <div class="game-info">
                <span>1 Player</span>
                <span>10 Minutes</span>
                <span>PVP Arena</span>
            </div>
        </div>


        <div class="game-card">
            <div class="game-number">05 / CREATIVE</div>

            <h3>MINECRAFT BUILDING</h3>

            <p>
                Turn imagination into reality in a timed
                creative building challenge.
            </p>

            <div class="game-info">
                <span>1 Player</span>
                <span>2 Hours</span>
                <span>Creative</span>
            </div>
        </div>

    </div>

</section>


<!-- =========================
     ORGANISER / PARTICIPANT
========================= -->

<section id="cards">

    <div class="section-header">

        <div class="section-label">
            Official Access
        </div>

        <h2 class="section-title">
            CLUTCH<br>
            ID Cards
        </h2>

        <p class="section-description">
            Official identification cards for the CLUTCH event
            organising committee and participants.
        </p>

    </div>


    <div class="cards-grid">

        <div class="role-card">

            <img
                src="{{ url_for('static', filename='Org-Card.png') }}"
                alt="CLUTCH Organiser Event Crew Card"
            >

            <div class="role-title">
                Organiser / Event Crew
            </div>

        </div>


        <div class="role-card">

            <img
                src="{{ url_for('static', filename='Part-Card.png') }}"
                alt="CLUTCH Player Event Participant Card"
            >

            <div class="role-title">
                Player / Event Participant
            </div>

        </div>

    </div>

</section>


<!-- =========================
     WORKSHOP
========================= -->

<section id="workshop">

    <div class="section-header">

        <div class="section-label">
            Learn & Create
        </div>

        <h2 class="section-title">
            Game<br>
            Development
        </h2>

    </div>


    <div class="workshop-box">

        <h3>
            Game Development Workshop
        </h3>

        <p>
            Learn the foundations of game development with
            Microsoft Campus Ambassadors from BHU.
            Explore how games are designed, built and brought
            to life.
        </p>


        <div class="workshop-points">

            <div class="workshop-point">
                Game Concepts & Mechanics
            </div>

            <div class="workshop-point">
                Controls & Gameplay
            </div>

            <div class="workshop-point">
                Game Design
            </div>

            <div class="workshop-point">
                Basic Game Development
            </div>

        </div>

    </div>

</section>


<!-- =========================
     RULES
========================= -->

<section id="rules">

    <div class="section-header">

        <div class="section-label">
            Play Fair
        </div>

        <h2 class="section-title">
            Quick<br>
            Rules
        </h2>

        <p class="section-description">
            Every player is expected to compete fairly,
            respect opponents and follow the rules of their
            respective game.
        </p>

    </div>


    <div class="rules-grid">

        <div class="rule">
            <div class="rule-number">RULE 01</div>
            <h4>Fair Play</h4>
            <p>
                No cheating, exploits or unfair external
                advantages are permitted.
            </p>
        </div>


        <div class="rule">
            <div class="rule-number">RULE 02</div>
            <h4>Respect</h4>
            <p>
                Players must maintain respectful behaviour
                toward opponents, organisers and staff.
            </p>
        </div>


        <div class="rule">
            <div class="rule-number">RULE 03</div>
            <h4>Match Timing</h4>
            <p>
                Players must be ready before their scheduled
                match. Delays may affect participation.
            </p>
        </div>


        <div class="rule">
            <div class="rule-number">RULE 04</div>
            <h4>Organiser Decision</h4>
            <p>
                Organisers have the final authority regarding
                match disputes and event decisions.
            </p>
        </div>

    </div>

</section>


<!-- =========================
     LIVE STREAM
========================= -->

<section id="stream">

    <div class="stream-box">

        <div class="section-label">
            Live Coverage
        </div>

        <h2>
            Watch CLUTCH Live
        </h2>

        <p>
            Follow the action, watch the biggest plays and
            experience the CLUTCH tournament live on YouTube.
        </p>

        <a
            href="https://www.youtube.com/"
            target="_blank"
            class="btn btn-primary"
        >
            YouTube Live
        </a>

    </div>

</section>


<!-- =========================
     FOOTER
========================= -->

<footer>

    <strong>CLUTCH</strong>

    <p>
        © 2026 CLUTCH — The Ultimate Game
    </p>

</footer>


</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
