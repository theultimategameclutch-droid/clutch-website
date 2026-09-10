from flask import Flask, request, redirect, url_for, session, flash, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)

# ============================================================
# SECURITY
# ============================================================

app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")

ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "CLUTCH")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "CHANGE_THIS_PASSWORD")

DATABASE = "clutch.db"


# ============================================================
# GOOGLE FORM LINKS
# ============================================================

EVENTS = [
    {
        "name": "VALORANT",
        "icon": "⚡",
        "players": "5 players per team",
        "classes": "Classes 8–12",
        "platform": "PC",
        "format": "Single Elimination • BO1",
        "details": "Semifinals and below: Swiftplay. Finals: Unrated.",
        "form": "https://forms.gle/9Xpz8wMiSWjBAuCT6"
    },
    {
        "name": "BGMI",
        "icon": "🎯",
        "players": "4 players per team",
        "classes": "Classes 8–12",
        "platform": "Mobile",
        "format": "Single Elimination • BO1",
        "details": "24 teams • 7 matches • Squad TPP • Erangel, Miramar, Rondo, Livik.",
        "form": "https://forms.gle/GmU9MpsuuvhPmEWi6"
    },
    {
        "name": "CHESS",
        "icon": "♟",
        "players": "1 player per team",
        "classes": "Classes 8–12",
        "platform": "PC",
        "format": "Single Elimination • BO1",
        "details": "Blitz 5|0 through semifinals. Semifinals and finals: Rapid 10|0.",
        "form": "https://forms.gle/BXmhHj32V68fZrjw7"
    },
    {
        "name": "MINECRAFT PVP",
        "icon": "⚔️",
        "players": "1 player per team",
        "classes": "Classes 8–12",
        "platform": "PC",
        "format": "Single Elimination • BO1",
        "details": "PvP kit • 10-minute matches • Draw determined by hearts.",
        "form": "https://forms.gle/GWCjyBR6y6H5uE8x6"
    },
    {
        "name": "MINECRAFT BUILDING",
        "icon": "🏗️",
        "players": "1 player per team",
        "classes": "Classes 8–12",
        "platform": "PC",
        "format": "Single Elimination • BO1",
        "details": "Theme given at the event • 2-hour time limit • Litematica not allowed.",
        "form": "https://forms.gle/GWCjyBR6y6H5uE8x6"
    },
    {
        "name": "GAME BUILDING WORKSHOP",
        "icon": "🎮",
        "players": "Participants",
        "classes": "Open to participants",
        "platform": "PC",
        "format": "Hands-on Workshop",
        "details": "Learn game concepts, mechanics, controls, design and basic development with guided demonstrations.",
        "form": "#"
    }
]


# ============================================================
# DATABASE
# ============================================================

def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            class_name TEXT NOT NULL,
            section TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


init_db()


# ============================================================
# COMMON HTML
# ============================================================

BASE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>CLUTCH | The Ultimate Game</title>

<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&display=swap');

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Orbitron', Arial, sans-serif;
    background: #050505;
    color: white;
    min-height: 100vh;
}

/* NAVIGATION */

nav {
    position: sticky;
    top: 0;
    z-index: 1000;

    height: 78px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    padding: 0 7%;

    background: rgba(5,5,5,0.94);
    border-bottom: 1px solid rgba(255,215,0,0.25);
    backdrop-filter: blur(12px);
}

.logo {
    color: #ffd000;
    font-size: 27px;
    font-weight: 900;
    letter-spacing: 5px;
    text-decoration: none;

    text-shadow:
        0 0 8px rgba(255,208,0,.8),
        0 0 25px rgba(255,208,0,.35);
}

.nav-links {
    display: flex;
    gap: 30px;
    align-items: center;
}

.nav-links a {
    color: #ddd;
    text-decoration: none;
    font-weight: 700;
    font-size: 13px;
    transition: .2s;
}

.nav-links a:hover {
    color: #ffd000;
}

.nav-button {
    border: 1px solid #ffd000;
    padding: 11px 17px;
    border-radius: 6px;
    color: #ffd000 !important;
}

.admin-button {
    border-color: #ff4d4d;
    color: #ff4d4d !important;
}

/* HERO */

.hero {
    min-height: calc(100vh - 78px);
    position: relative;
    overflow: hidden;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;
}

.hero-video {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;

    opacity: .34;
    z-index: 0;
}

.hero-overlay {
    position: absolute;
    inset: 0;
    z-index: 1;

    background:
        radial-gradient(circle at center,
        rgba(255,208,0,.12),
        transparent 42%),
        linear-gradient(
        rgba(0,0,0,.65),
        rgba(0,0,0,.92)
        );
}

.hero-content {
    position: relative;
    z-index: 2;
    padding: 30px;
}

.badge {
    display: inline-block;

    border: 1px solid rgba(255,208,0,.55);
    background: rgba(255,208,0,.08);

    color: #ffd000;

    padding: 10px 22px;
    border-radius: 5px;

    font-size: 12px;
    letter-spacing: 2px;

    margin-bottom: 28px;
}

.hero h1 {
    font-size: clamp(65px, 13vw, 170px);
    line-height: .9;
    letter-spacing: 12px;
    font-weight: 900;

    color: #ffd000;

    text-shadow:
        0 0 10px rgba(255,208,0,.8),
        0 0 40px rgba(255,208,0,.35);
}

.hero p {
    margin: 35px auto;

    max-width: 780px;

    color: #ddd;
    font-size: 16px;
    line-height: 1.8;
}

.buttons {
    display: flex;
    justify-content: center;
    gap: 15px;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;

    padding: 15px 28px;

    text-decoration: none;

    font-family: inherit;
    font-weight: 800;
    font-size: 13px;

    border-radius: 6px;

    cursor: pointer;

    transition: .2s;
}

.btn-primary {
    background: #ffd000;
    color: #050505;

    box-shadow: 0 0 25px rgba(255,208,0,.25);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 0 35px rgba(255,208,0,.5);
}

.btn-secondary {
    color: #fff;
    border: 1px solid #555;
}

.btn-secondary:hover {
    border-color: #ffd000;
    color: #ffd000;
}


/* PAGE */

.page {
    padding: 70px 7%;
    max-width: 1400px;
    margin: auto;
}

.page-title {
    font-size: 42px;
    color: #ffd000;
    margin-bottom: 12px;
}

.page-subtitle {
    color: #999;
    margin-bottom: 45px;
    line-height: 1.7;
}


/* EVENTS */

.events-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(290px, 1fr));
    gap: 22px;
}

.event-card {
    background: linear-gradient(
        145deg,
        rgba(255,255,255,.055),
        rgba(255,255,255,.015)
    );

    border: 1px solid #292929;

    border-radius: 12px;

    padding: 28px;

    transition: .25s;
}

.event-card:hover {
    transform: translateY(-5px);
    border-color: rgba(255,208,0,.55);

    box-shadow:
        0 15px 45px rgba(0,0,0,.4),
        0 0 25px rgba(255,208,0,.08);
}

.event-icon {
    font-size: 38px;
    margin-bottom: 18px;
}

.event-card h2 {
    color: #ffd000;
    margin-bottom: 18px;
}

.event-info {
    color: #bbb;
    font-size: 12px;
    line-height: 1.9;
}

.event-info strong {
    color: white;
}

.register-btn {
    display: block;

    text-align: center;

    margin-top: 22px;

    padding: 13px;

    background: #ffd000;
    color: #050505;

    border-radius: 6px;

    text-decoration: none;

    font-weight: 900;
    font-size: 12px;
}

.register-btn:hover {
    box-shadow: 0 0 25px rgba(255,208,0,.35);
}

.disabled {
    background: #333;
    color: #777;
}


/* AUTH */

.auth-container {
    max-width: 520px;
    margin: 30px auto;
}

.auth-box {
    background: #101010;
    border: 1px solid #292929;
    border-radius: 12px;
    padding: 35px;
}

.auth-box h2 {
    color: #ffd000;
    margin-bottom: 25px;
}

input, select {
    width: 100%;

    padding: 14px;

    margin-bottom: 14px;

    background: #080808;

    color: white;

    border: 1px solid #333;

    border-radius: 6px;

    font-family: inherit;
}

input:focus, select:focus {
    outline: none;
    border-color: #ffd000;
}

.form-label {
    display: block;
    color: #aaa;
    font-size: 11px;
    margin-bottom: 7px;
}

.full-btn {
    width: 100%;
    border: none;
}


/* ADMIN */

.admin-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 25px;
    overflow: hidden;
}

.admin-table th,
.admin-table td {
    border-bottom: 1px solid #292929;
    padding: 14px;
    text-align: left;
    font-size: 12px;
}

.admin-table th {
    color: #ffd000;
    background: #111;
}

.admin-table td {
    color: #ccc;
}


/* ALERT */

.alert {
    max-width: 700px;
    margin: 20px auto;
    padding: 14px 18px;
    border-radius: 6px;
    background: rgba(255,208,0,.1);
    border: 1px solid rgba(255,208,0,.4);
    color: #ffd000;
}


/* FOOTER */

footer {
    margin-top: 80px;
    padding: 35px 7%;

    text-align: center;

    border-top: 1px solid #222;

    color: #666;

    font-size: 11px;
}


/* MOBILE */

@media(max-width: 700px) {

    nav {
        padding: 0 5%;
        height: 70px;
    }

    .nav-links {
        gap: 12px;
    }

    .nav-links a {
        font-size: 10px;
    }

    .logo {
        font-size: 19px;
        letter-spacing: 3px;
    }

    .hero h1 {
        letter-spacing: 5px;
    }

    .page {
        padding: 50px 5%;
    }

    .page-title {
        font-size: 32px;
    }

}

</style>
</head>

<body>

<nav>

<a class="logo" href="{{ url_for('home') }}">CLUTCH</a>

<div class="nav-links">

<a href="{{ url_for('home') }}">HOME</a>

<a href="{{ url_for('events') }}">EVENTS</a>

{% if session.get('student_id') %}
<a href="{{ url_for('student_dashboard') }}">MY ACCOUNT</a>
<a href="{{ url_for('logout') }}" class="nav-button">LOGOUT</a>
{% else %}
<a href="{{ url_for('login') }}" class="nav-button">SIGN IN / REGISTER</a>
{% endif %}

<a href="{{ url_for('admin_login') }}" class="nav-button admin-button">
ADMIN
</a>

</div>

</nav>


{% with messages = get_flashed_messages() %}
{% if messages %}
{% for message in messages %}
<div class="alert">{{ message }}</div>
{% endfor %}
{% endif %}
{% endwith %}


{{ content|safe }}


<footer>
    © 2026 CLUTCH — THE ULTIMATE GAME
</footer>

</body>
</html>
"""


# ============================================================
# HELPER
# ============================================================

def render_page(content):
    return render_template_string(
        BASE_HTML,
        content=content
    )


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    content = """
    <section class="hero">

        <video class="hero-video"
               autoplay
               muted
               loop
               playsinline>
            <source src="/static/clutch-video.mp4" type="video/mp4">
        </video>

        <div class="hero-overlay"></div>

        <div class="hero-content">

            <div class="badge">
                OFFICIAL ESPORTS ARENA
            </div>

            <h1>CLUTCH</h1>

            <p>
                Compete in high-stakes esports tournaments,
                explore gaming events, participate in workshops,
                and prove your skills.
            </p>

            <div class="buttons">

                <a href="/events" class="btn btn-primary">
                    EXPLORE EVENTS
                </a>

                <a href="/events" class="btn btn-secondary">
                    VIEW RULES
                </a>

            </div>

        </div>

    </section>
    """

    return render_page(content)


# ============================================================
# EVENTS
# ============================================================

@app.route("/events")
def events():

    cards = ""

    for event in EVENTS:

        if event["form"] == "#":

            register = """
            <span class="register-btn disabled">
                REGISTRATION INFORMATION
            </span>
            """

        else:

            register = f"""
            <a
                href="{event['form']}"
                target="_blank"
                class="register-btn">
                REGISTER NOW
            </a>
            """

        cards += f"""
        <div class="event-card">

            <div class="event-icon">
                {event['icon']}
            </div>

            <h2>
                {event['name']}
            </h2>

            <div class="event-info">

                <div>
                    <strong>Players:</strong>
                    {event['players']}
                </div>

                <div>
                    <strong>Eligibility:</strong>
                    {event['classes']}
                </div>

                <div>
                    <strong>Platform:</strong>
                    {event['platform']}
                </div>

                <div>
                    <strong>Format:</strong>
                    {event['format']}
                </div>

                <br>

                <div>
                    {event['details']}
                </div>

            </div>

            {register}

        </div>
        """

    content = f"""
    <main class="page">

        <h1 class="page-title">
            EVENTS
        </h1>

        <p class="page-subtitle">
            Choose your battlefield. Read the event information
            and register directly through the official registration form.
        </p>

        <div class="events-grid">
            {cards}
        </div>

    </main>
    """

    return render_page(content)


# ============================================================
# STUDENT REGISTER
# ============================================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        class_name = request.form.get("class_name", "").strip()
        section = request.form.get("section", "").strip()
        password = request.form.get("password", "")

        if not all([name, email, class_name, section, password]):

            flash("Please fill all fields.")

            return redirect(url_for("register"))

        connection = get_db()

        try:

            connection.execute(
                """
                INSERT INTO students
                (name, email, class_name, section, password)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    name,
                    email,
                    class_name,
                    section,
                    generate_password_hash(password)
                )
            )

            connection.commit()

            flash("Account created successfully. Please sign in.")

            return redirect(url_for("login"))

        except sqlite3.IntegrityError:

            flash("This email is already registered.")

        finally:

            connection.close()

    content = """
    <main class="page">

        <div class="auth-container">

            <div class="auth-box">

                <h2>STUDENT REGISTER</h2>

                <form method="POST">

                    <label class="form-label">
                        FULL NAME
                    </label>

                    <input
                        type="text"
                        name="name"
                        placeholder="Your full name"
                        required
                    >

                    <label class="form-label">
                        EMAIL
                    </label>

                    <input
                        type="email"
                        name="email"
                        placeholder="your@email.com"
                        required
                    >

                    <label class="form-label">
                        CLASS
                    </label>

                    <input
                        type="text"
                        name="class_name"
                        placeholder="Example: 10"
                        required
                    >

                    <label class="form-label">
                        SECTION
                    </label>

                    <input
                        type="text"
                        name="section"
                        placeholder="Example: A"
                        required
                    >

                    <label class="form-label">
                        PASSWORD
                    </label>

                    <input
                        type="password"
                        name="password"
                        placeholder="Create a password"
                        required
                    >

                    <button class="btn btn-primary full-btn">
                        CREATE ACCOUNT
                    </button>

                </form>

                <br>

                <p style="color:#777;font-size:11px;">
                    Already registered?
                    <a href="/login" style="color:#ffd000;">
                        Sign in
                    </a>
                </p>

            </div>

        </div>

    </main>
    """

    return render_page(content)


# ============================================================
# STUDENT LOGIN
# ============================================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        connection = get_db()

        student = connection.execute(
            "SELECT * FROM students WHERE email = ?",
            (email,)
        ).fetchone()

        connection.close()

        if student and check_password_hash(student["password"], password):

            session["student_id"] = student["id"]

            return redirect(url_for("student_dashboard"))

        flash("Incorrect email or password.")

    content = """
    <main class="page">

        <div class="auth-container">

            <div class="auth-box">

                <h2>STUDENT LOGIN</h2>

                <form method="POST">

                    <label class="form-label">
                        EMAIL
                    </label>

                    <input
                        type="email"
                        name="email"
                        placeholder="Your email"
                        required
                    >

                    <label class="form-label">
                        PASSWORD
                    </label>

                    <input
                        type="password"
                        name="password"
                        placeholder="Your password"
                        required
                    >

                    <button class="btn btn-primary full-btn">
                        SIGN IN
                    </button>

                </form>

                <br>

                <p style="color:#777;font-size:11px;">
                    Don't have an account?
                    <a href="/register" style="color:#ffd000;">
                        Register
                    </a>
                </p>

            </div>

        </div>

    </main>
    """

    return render_page(content)


# ============================================================
# STUDENT DASHBOARD
# ============================================================

@app.route("/student")
def student_dashboard():

    if not session.get("student_id"):

        return redirect(url_for("login"))

    connection = get_db()

    student = connection.execute(
        "SELECT * FROM students WHERE id = ?",
        (session["student_id"],)
    ).fetchone()

    connection.close()

    if not student:

        session.pop("student_id", None)

        return redirect(url_for("login"))

    content = f"""
    <main class="page">

        <h1 class="page-title">
            WELCOME, {student['name'].upper()}
        </h1>

        <p class="page-subtitle">
            Your CLUTCH student account.
        </p>

        <div class="event-card">

            <h2>STUDENT INFORMATION</h2>

            <div class="event-info">

                <p>
                    <strong>Name:</strong>
                    {student['name']}
                </p>

                <p>
                    <strong>Email:</strong>
                    {student['email']}
                </p>

                <p>
                    <strong>Class:</strong>
                    {student['class_name']}
                </p>

                <p>
                    <strong>Section:</strong>
                    {student['section']}
                </p>

            </div>

            <br>

            <a href="/events" class="btn btn-primary">
                BROWSE EVENTS
            </a>

        </div>

    </main>
    """

    return render_page(content)


# ============================================================
# LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    session.pop("student_id", None)
    session.pop("admin", None)

    return redirect(url_for("home"))


# ============================================================
# ADMIN LOGIN
# ============================================================

@app.route("/admin", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if (
            username == ADMIN_USERNAME
            and password == ADMIN_PASSWORD
        ):

            session["admin"] = True

            return redirect(url_for("admin_dashboard"))

        flash("Invalid admin credentials.")

    content = """
    <main class="page">

        <div class="auth-container">

            <div class="auth-box">

                <h2>CLUTCH ADMIN</h2>

                <form method="POST">

                    <label class="form-label">
                        ADMIN ID
                    </label>

                    <input
                        type="text"
                        name="username"
                        placeholder="Admin ID"
                        required
                    >

                    <label class="form-label">
                        PASSWORD
                    </label>

                    <input
                        type="password"
                        name="password"
                        placeholder="Admin password"
                        required
                    >

                    <button class="btn btn-primary full-btn">
                        ADMIN SIGN IN
                    </button>

                </form>

            </div>

        </div>

    </main>
    """

    return render_page(content)


# ============================================================
# ADMIN DASHBOARD
# ============================================================

@app.route("/admin/dashboard")
def admin_dashboard():

    if not session.get("admin"):

        return redirect(url_for("admin_login"))

    connection = get_db()

    students = connection.execute(
        "SELECT id, name, email, class_name, section FROM students ORDER BY id DESC"
    ).fetchall()

    connection.close()

    rows = ""

    for student in students:

        rows += f"""
        <tr>

            <td>{student['id']}</td>

            <td>{student['name']}</td>

            <td>{student['email']}</td>

            <td>{student['class_name']}</td>

            <td>{student['section']}</td>

        </tr>
        """

    if not rows:

        rows = """
        <tr>
            <td colspan="5">
                No students have registered yet.
            </td>
        </tr>
        """

    content = f"""
    <main class="page">

        <h1 class="page-title">
            CLUTCH ADMIN
        </h1>

        <p class="page-subtitle">
            Admin control panel.
        </p>

        <div class="event-card">

            <h2>
                REGISTERED STUDENTS
            </h2>

            <div style="overflow-x:auto;">

                <table class="admin-table">

                    <thead>

                        <tr>
                            <th>ID</th>
                            <th>NAME</th>
                            <th>EMAIL</th>
                            <th>CLASS</th>
                            <th>SECTION</th>
                        </tr>

                    </thead>

                    <tbody>

                        {rows}

                    </tbody>

                </table>

            </div>

        </div>

        <br>

        <a href="/logout" class="btn btn-secondary">
            LOG OUT
        </a>

    </main>
    """

    return render_page(content)


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
