import random
from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pgp")
def pgp():
    return send_from_directory("static", "pgp.txt")


@app.route("/resume")
def resume():
    return render_template("file.html", title="/static/resume.pdf")


@app.route("/coop")
def coop():
    return render_template("file.html", title="/static/coop.pdf")


@app.route("/projects")
def projects():
    featured_projects = [
        {
            "name": "anthony-new",
            "info": "Responsive portfolio website built with industry-standard frameworks. Previously PHP-based, now runs on Flask. Hosted on a GCP instance.",
            "url": "https://github.com/0foxes/anthony-new",
            "img": url_for("static", filename="img/website.webp"),
            "tags": ["css", "flask", "html", "python", "website"],
        },
        {
            "name": "bookmark-archiver",
            "info": "Script to archive all of a browser's (Chromium-based or Firefox) bookmarks to the Internet Archive. Does not require registration, up to 100k pages/day.",
            "url": "https://github.com/0foxes/bookmarkarchiver",
            "img": url_for("static", filename="img/bmar.webp"),
            "tags": [
                "python",
                "backups",
                "web",
                "wayback-machine",
                "bookmark-archiver",
            ],
        },
        {
            "name": "dogecoin-unofficial",
            "info": "Linux Snap for Dogecoin Core (the official Dogecoin wallet), available on the Snap Store. Packages official binaries for easy installation.",
            "url": "https://github.com/0foxes/dogecoin-unofficial",
            "img": url_for("static", filename="img/dogecoin.webp"),
            "tags": ["linux", "snap", "cryptocurrency", "bash", "dogecoin"],
        },
        {
            "name": "file-visualiser",
            "info": "Visualises any computer file as an image using a variety of data extraction and rendering algorithms. Applications include forensics, CTF, and art.",
            "url": "https://github.com/0foxes/file-visualiser",
            "img": url_for("static", filename="img/filev.webp"),
            "tags": ["visualization", "art", "security", "forensics", "ctf"],
        },
        {
            "name": "simple-markov",
            "info": "Performant natural language generator using Markov chains. Can also be used to generate sequences of letters. Includes a Flask-based web frontend.",
            "url": "https://github.com/0foxes/simple-markov",
            "img": url_for("static", filename="img/markov.webp"),
            "tags": ["flask", "ai", "cpp", "markov-chain", "nlg"],
        },
        {
            "name": "superlumic",
            "info": "Secure command-line password manager written in C++. Allows users to create, save, and load encrypted (AES-256) password lists locally.",
            "url": "https://github.com/0foxes/superlumic",
            "img": url_for("static", filename="img/super.webp"),
            "tags": ["aes", "security", "cpp", "make", "password-manager"],
        },
    ]
    [project["tags"].sort() for project in featured_projects]
    random.shuffle(featured_projects)
    all_projects = [
        {
            "name": "visuals",
            "info": "Cross-platform OpenGL audio visualiser written with GLFW, including several GLSL shaders. Audio data retrieved with SFML and downsampled programmatically.",
            "url": "https://github.com/0foxes/visuals",
            "img": url_for("static", filename="img/vis.webp"),
            "tags": ["opengl", "glsl", "glfw", "sfml", "music"],
        },
        {
            "name": "actually-uwu",
            "info": "Web app that intelligently analyses weather conditions to provide suggestions about outfits, commutes, and sun protection while taking user preferences into account.",
            "url": "https://github.com/0foxes/actually-uwu",
            "img": url_for("static", filename="img/uwu.webp"),
            "tags": ["react", "node", "next", "mongodb", "vercel"],
        },
        {
            "name": "snakewhisper",
            "info": "Proof-of-concept of a simple end-to-end encrypted chat program. Currently supports two-way communication with elliptic curve key exchange.",
            "url": "https://github.com/0foxes/snakewhisper",
            "img": url_for("static", filename="img/snake.webp"),
            "tags": [
                "python",
                "cryptography",
                "privacy",
                "encryption",
                "chat-application",
            ],
        },
        {
            "name": "mersenne-twister-tools",
            "info": "A collection of scripts that implement and attack the famous Mersenne Twister PRNG (included in many standard libraries) and several variants.",
            "url": "https://github.com/0foxes/mersenne-twister-tools",
            "img": url_for("static", filename="img/mt.webp"),
            "tags": ["python", "cpp", "prng", "ctf", "mersenne-twister"],
        },
        {
            "name": "divoc",
            "info": "COVID-19 tracker that uses public APIs to calculate how many cases are within a certain distance of any address in Ontario. Includes self-assessment tool.",
            "url": "https://github.com/0foxes/divoc",
            "img": url_for("static", filename="img/divoc.webp"),
            "tags": ["medicine", "big-data", "cpp", "gps", "covid"],
        },
        {
            "name": "submission-downloader",
            "info": "Tool for archiving code submissions to a wide variety of competitive programming sites in bulk. Available on PyPi. Useful for creating solution archives.",
            "url": "https://github.com/0foxes/submission-downloader",
            "img": url_for("static", filename="img/subdl.webp"),
            "tags": ["python", "scraper", "competitive-programming", "dmoj", "mcpt"],
        },
        {
            "name": "ai-tictactoe",
            "info": "AI-powered tic-tac-toe game with a graphical user interface. Uses the minimax algorithm and alpha-beta pruning. Can be modified to play other games as well.",
            "url": "https://github.com/0foxes/ai-tictactoe",
            "img": url_for("static", filename="img/aittt.webp"),
            "tags": ["python", "ai", "tic-tac-toe", "pygame", "cs50"],
        },
        {
            "name": "cs50x-2021",
            "info": "Coursework for the 2021 CS50x: Introduction to Computer Science course offered by Harvard University. Wide variety of languages and technologies.",
            "url": "https://github.com/0foxes/cs50x-2021",
            "img": url_for("static", filename="img/cs50x.webp"),
            "tags": ["python", "c", "php", "web", "cs50"],
        },
        {
            "name": "cs50ai-2021",
            "info": "Coursework for the 2021 CS50ai: Introduction to Artificial Intelligence with Python course offered by Harvard University. Wide variety of algorithms.",
            "url": "https://github.com/0foxes/cs50ai-2021",
            "img": url_for("static", filename="img/cs50ai.webp"),
            "tags": ["python", "ai", "pygame", "mnist", "cs50"],
        },
        {
            "name": "cs50p-2022",
            "info": "Coursework for the 2022 CS50p: Introduction to Computer Science with Python course offered by Harvard University. Variety of algorithms and libraries.",
            "url": "https://github.com/0foxes/cs50p-2022",
            "img": url_for("static", filename="img/cs50p.webp"),
            "tags": ["python", "regex", "oop", "pytest", "cs50"],
        },
        {
            "name": "zoetrope-game-of-life",
            "info": "Console implementation of the cellular automaton in multiple languages. Being Turing-complete, it can simulate any computer algorithm in existence.",
            "url": "https://github.com/0foxes/zoetrope-game-of-life",
            "img": url_for("static", filename="img/conway.webp"),
            "tags": ["game", "python", "console", "ai", "conways-game-of-life"],
        },
        {
            "name": "stonktrack",
            "info": "Financial tracker that can track stocks, cryptocurrencies, currencies, and other assets with simple configuration and a terminal-based GUI.",
            "url": "https://github.com/0foxes/stonktrack",
            "img": url_for("static", filename="img/stonks.webp"),
            "tags": ["python", "finance", "forex", "cryptocurrency", "stonks"],
        },
        {
            "name": "rc4-variants",
            "info": "Object-oriented implemention of RC4-drop[n], a modification of the simple and speedy RC4 stream cipher that defends against several attacks.",
            "url": "https://github.com/0foxes/rc4-variants",
            "img": url_for("static", filename="img/arc4.webp"),
            "tags": ["python", "security", "cryptography", "encryption", "rc4"],
        },
        {
            "name": "programming-solutions",
            "info": "Archive to hold all of my competitive programming solutions. Contains solutions and some explanations for CCC, Codeforces, DMOJ, CSES, and other sites.",
            "url": "https://github.com/0foxes/programming-solutions",
            "img": url_for("static", filename="img/cp.webp"),
            "tags": ["competitive-programming", "cf", "usaco", "ccc", "dmoj"],
        },
        {
            "name": "cryptopals-solutions",
            "info": "Repository of my solutions to the cryptopals cryptography challenges. Incomplete, but I occasionally work on them for a while. Also contains several useful scripts.",
            "url": "https://github.com/0foxes/cryptopals-solutions",
            "img": url_for("static", filename="img/aesecb.webp"),
            "tags": ["python", "security", "cryptography", "rsa", "cryptopals"],
        },
        {
            "name": "vorldle",
            "info": "Multi-platform Worldle clone implemented with Java's standard library GUI methods. Integrates country database and calculations for distance and bearing.",
            "url": "https://github.com/0foxes/vorldle",
            "img": url_for("static", filename="img/vorldle.webp"),
            "tags": ["game", "java", "swing", "oop", "wordle"],
        },
        {
            "name": "ctfoj",
            "info": "Open-source platform for hosting cybersecurity challenges and contests. Comprehensive test suite included. Used in production by the MGCI CTF Club.",
            "url": "https://github.com/jdabtieu/CTFOJ",
            "img": url_for("static", filename="img/ctfoj.webp"),
            "tags": ["ctf", "security", "pytest", "flask", "python"],
        },
        {
            "name": "gennet",
            "info": 'Innovative social media platform for families. Allows user to create "trees" for their family and populate the "leaves" with knowledge, anecdotes, or media.',
            "url": "https://github.com/AbdulBaseetShabi/GenNet",
            "img": url_for("static", filename="img/gennet.webp"),
            "tags": ["css", "html", "js", "python", "social-media"],
        },
        {
            "name": "the-roller",
            "info": "Reddit bot to roll dice, to be used in online role-playing and simulation games. Rendered prohibitively expensive due to Reddit API pricing changes.",
            "url": "https://github.com/0foxes/the-roller",
            "img": url_for("static", filename="img/roller.webp"),
            "tags": ["python", "dice", "dnd", "reddit", "praw"],
        },
        {
            "name": "classic-pong",
            "info": "Multi-platform Pong created with Java and Swing for a school assignment. The two paddles can be manually controlled, although there is no computer player.",
            "url": "https://github.com/0foxes/classic-pong",
            "img": url_for("static", filename="img/pong.webp"),
            "tags": ["game", "java", "swing", "pong", "ics4u"],
        },
        {
            "name": "0foxes",
            "info": "Repository that appears on my GitHub profile, containing statistics and a short bio for my account. Check it out!",
            "url": "https://github.com/0foxes/0foxes",
            "img": url_for("static", filename="img/github.webp"),
            "tags": ["github", "profile", "bio", "hello-world", "github-readme-stats"],
        },
        {
            "name": "2022-robot",
            "info": "C++ code for my FIRST Robotics Competition team's robot in the 2022-2023 season, with other programmers.",
            "url": "https://github.com/roboticsmgci/2022-robot",
            "img": url_for("static", filename="img/robot.webp"),
            "tags": ["frc", "robot", "cpp", "pid", "gradle"],
        },
        {
            "name": "cosine",
            "info": "Resources collection and ai-assisted interactive story designed to help foster greater understanding.",
            "url": "https://github.com/Lucifersan/COSine",
            "img": url_for("static", filename="img/chatbot.webp"),
            "tags": ["css", "html", "js", "node", "react"],
        },
        {
            "name": "helloworld",
            "info": "Travel planner that allows you to explore global destinations, putting them at your fingertips with slick design.",
            "url": "https://github.com/Lucifersan/helloworld",
            "img": url_for("static", filename="img/helloworld.webp"),
            "tags": ["node", "blender", "nginx", "three", "vite"],
        },
    ]
    # projects that don't have github repos: shad-tile
    [project["tags"].sort() for project in all_projects]
    all_projects.extend(featured_projects)
    random.shuffle(all_projects)
    return render_template(
        "projects.html", featured=featured_projects, all=all_projects
    )


@app.errorhandler(404)
def error_404(e):
    return render_template("default.html", title="Not Found", text="404 Not Found"), 404


@app.errorhandler(500)
def error_500(e):
    return (
        render_template(
            "default.html",
            title="Internal Server Error",
            text="500 Internal Server Error",
        ),
        500,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0")
