from flask import Flask
from random import randint
app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Witaj świecie!</p><a href='/druga'>Przejdź do drugiej strony</a>"


@app.route("/druga")
def druga():
    return f"<p>Jakaś podstrona. Losowa liczba: {randint(1, 100)}</p><a href='/'>Wróć do strony głównej</a>"


app.run(debug=True)