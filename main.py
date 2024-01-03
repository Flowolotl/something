from flask import Flask, render_template, request, redirect, url_for, jsonify
from voice import Voice, Voices
from config import _config

Config = _config(num_char=2)
Config.add(voice=Voice.Yippee)

app = Flask(__name__)


# Run with "flask --app main run --debugger"
@app.route('/')
def main():
    selection = request.args.get("selection")
    Config.characters[0]
    return render_template("index.html", names=Voices, characters=Config.characters)


@app.route('/data', methods=["POST"])
def selection_data():
    selection = request.form.get("selection")
    Config.voice_selection = Voice[selection]
    print(Voice[selection])
    return selection or ""


@app.route('/add-char', methods=["POST"])
def add_char():
    Config.add(voice=Config.voice_selection)
    return jsonify({'status': 'success'})