from flask import Flask, render_template_string

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
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: #080808;
            color: white;
            line-height: 1.6;
        }

        nav {
            position: sticky;
            top: 0;
            z-index: 100;
            background: rgba(8,8,8,0.95);
            border-bottom: 1px solid #292929;
            padding: 18px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 28px;
            font-weight: 900;
            letter-spacing: 3px;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 25px;
            font-weight: bold;
        }

        nav a:hover {
            color: #00e5ff;
        }

        .hero {
            min-height: 90vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 60px 20px;
            background:
                radial-gradient(circle at center, #17252b 0%, #080808 55%);
        }

        .hero h1 {
            font-size: clamp(60px, 12vw, 150px);
            font-weight: 1000;
            letter-spacing: 10px;
        }

        .hero p {
            font-size: 22px;
            color: #bbb;
            margin: 10px 0 30px;
        }

        .button {
            display: inline-block;
            padding: 14px 28px;
            margin: 8px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            background: white;
            color: black;
        }

        .button.secondary {
            background: transparent;
            color: white;
            border: 1px solid #555;
        }

        section {
            padding: 80px 7%;
        }

        .section-title {
            text-align: center;
            font-size: 42px;
            margin-bottom: 45px;
        }

        .games {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 20px;
        }

        .card {
            background: #111;
            border: 1px solid #292929;
            border-radius: 14px;
            padding: 25px;
            transition: 0.25s;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: #00e5ff;
        }

        .card h3 {
            font-size: 25px;
            margin-bottom: 10px;
        }

        .card p {
            color: #aaa;
        }

        .info {
            margin-top: 18px;
            font-size: 14px;
            color: #ddd;
        }

        .cta {
            text-align: center;
            background: #101010;
        }

        footer {
            padding: 30px;
            text-align: center;
            color: #777;
            border-top: 1px solid #222;
        }

        @media (max-width: 700px) {
            nav {
                padding: 15px 4%;
            }

            nav a {
                margin-left: 10px;
                font-size: 13px;
            }

            section {
                padding: 60px 5%;
            }
        }
    </style>
</head>

<body>

<nav>
    <div class="logo">CLUTCH</div>

    <div>
        <a href="#games">Games</a>
        <a href="#workshop">Workshop</a>
        <a href="#rules">Rules</a>
    </div>
</nav>

<section class="hero">
    <div>
        <h1>CLUTCH</h1>
        <p>THE ULTIMATE GAME</p>

        <a class="button" href="#games">EXPLORE EVENTS</a>
        <a class="button secondary" href="#rules">VIEW RULES</a>
    </div>
</section>

<section id="games">
    <h2 class="section-title">EVENTS</h2>

    <div class="games">

        <div class="card">
            <h3>VALORANT</h3>
            <p>5-player competitive PC tournament.</p>
            <div class="info">
                Classes 8–12<br>
                Single Elimination • BO1
            </div>
        </div>

        <div class="card">
            <h3>BGMI</h3>
            <p>Squad TPP mobile battle royale.</p>
            <div class="info">
                4 players per team<br>
                24 teams • 7 matches
            </div>
        </div>

        <div class="card">
            <h3>CHESS</h3>
            <p>Competitive online chess tournament.</p>
            <div class="info">
                1 player per team<br>
                Blitz & Rapid rounds
            </div>
        </div>

        <div class="card">
            <h3>MINECRAFT PvP</h3>
            <p>Fight your way through the PvP arena.</p>
            <div class="info">
                1 player per team<br>
                10-minute matches
            </div>
        </div>

        <div class="card">
            <h3>MINECRAFT BUILDING</h3>
            <p>Turn creativity into a winning build.</p>
            <div class="info">
                1 player per team<br>
                2-hour time limit
            </div>
        </div>

    </div>
</section>

<section id="workshop">
    <h2 class="section-title">GAME BUILDING WORKSHOP</h2>

    <div class="card">
        <p>
            A hands-on game development workshop with Microsoft Campus
            Ambassadors from BHU.
        </p>

        <br>

        <p>
            Learn game concepts, mechanics, controls, design and basic
            development through a guided demonstration and build your
            own game or prototype.
        </p>
    </div>
</section>

<section id="rules">
    <h2 class="section-title">QUICK RULES</h2>

    <div class="games">

        <div class="card">
            <h3>VALORANT</h3>
            <p>5 per team • PC • Classes 8–12 • Single Elimination BO1</p>
        </div>

        <div class="card">
            <h3>BGMI</h3>
            <p>4 per team • Mobile • Classes 8–12 • Single Elimination BO1</p>
        </div>

        <div class="card">
            <h3>CHESS</h3>
            <p>1 per team • PC • Chess.com • Blitz and Rapid formats</p>
        </div>

        <div class="card">
            <h3>MINECRAFT PvP</h3>
            <p>1 per team • PC • 10-minute matches • PvP kit</p>
        </div>

        <div class="card">
            <h3>MINECRAFT BUILDING</h3>
            <p>1 per team • PC • Theme-based building • 2-hour limit</p>
        </div>

    </div>
</section>

<section class="cta">
    <h2 class="section-title">READY TO CLUTCH?</h2>
    <p>Bring your team. Bring your skill. Make your play.</p>
    <br>
    <a class="button" href="#games">VIEW EVENTS</a>
</section>

<footer>
    © 2026 CLUTCH — The Ultimate Game
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
