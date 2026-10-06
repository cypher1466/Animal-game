from flask import Flask, render_template, request, redirect, url_for, session
import random
import string

app = Flask(__name__)
app.secret_key = "change-this-to-a-random-secret-key"

# Animal list based on your original Python code
animals = [
    "Lion", "Tiger", "Elephant", "Giraffe", "Zebra",
    "Leopard", "Cheetah", "Hippopotamus", "Rhinoceros",
    "Gorilla", "Chimpanzee", "Monkey", "Baboon",
    "Kangaroo", "Koala", "Panda", "Bear", "Wolf", "Fox",
    "Deer", "Horse", "Donkey", "Cow", "Goat", "Sheep",
    "Pig", "Dog", "Cat", "Rabbit", "Mouse", "Rat",
    "Squirrel", "Camel", "Buffalo", "Antelope", "Hyena",
    "Crocodile", "Alligator", "Snake", "Lizard", "Turtle",
    "Tortoise", "Frog", "Toad", "Eagle", "Hawk", "Parrot",
    "Owl", "Penguin", "Ostrich", "Peacock", "Chicken",
    "Duck", "Goose", "Swan", "Dolphin", "Whale", "Shark",
    "Octopus", "Crab"
]


def start_game():
    word = random.choice(animals).lower()

    session["word"] = word
    session["guessed"] = []
    session["wrong"] = []
    session["message"] = "Guess a letter to reveal the animal!"
    session["status"] = "playing"


@app.route("/")
def index():
    if "word" not in session:
        start_game()

    word = session["word"]
    guessed = session["guessed"]

    display_word = [
        letter if letter in guessed else "_"
        for letter in word
    ]

    won = all(letter in guessed for letter in word)

    if won:
        session["status"] = "won"

    return render_template(
        "index.html",
        display_word=display_word,
        guessed=guessed,
        wrong=session["wrong"],
        message=session["message"],
        status=session["status"],
        alphabet=list(string.ascii_lowercase),
        score=max(0, 100 - len(session["wrong"]) * 10)
    )


@app.route("/guess", methods=["POST"])
def guess():
    if "word" not in session:
        start_game()

    if session["status"] != "playing":
        return redirect(url_for("index"))

    letter = request.form.get("letter", "").strip().lower()

    if len(letter) != 1 or letter not in string.ascii_lowercase:
        session["message"] = "Please enter one valid letter."

    elif letter in session["guessed"] or letter in session["wrong"]:
        session["message"] = "You have already guessed that letter!"

    elif letter in session["word"]:
        session["guessed"].append(letter)
        session["message"] = "Correct! That letter is in the animal name."

        if all(
            char in session["guessed"]
            for char in session["word"]
        ):
            session["status"] = "won"
            session["message"] = "Amazing! You guessed the animal! 🎉"

    else:
        session["wrong"].append(letter)
        session["message"] = "Oops! That letter is not in the word."

    return redirect(url_for("index"))


@app.route("/new-game", methods=["POST"])
def new_game():
    start_game()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)