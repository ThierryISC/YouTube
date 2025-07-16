import string

from flask import Flask, request, render_template, redirect
import sqlite3
import os
import random

DB_FILE = 'urls.db'

app = Flask(__name__)

def init_database():
    if not os.path.exists(DB_FILE):
        with sqlite3.connect(DB_FILE) as conn:
            conn.execute("CREATE TABLE urls (short TEXT PRIMARY KEY, original TEXT)")


def genere_code_court():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def index():
    short_url = None
    if request.method == 'POST':
        original = request.form['url'].strip()
        if not original.startswith(('http://', 'https://')):
            original = 'http://' + original
        code_court = genere_code_court()
        with sqlite3.connect(DB_FILE) as conn:
            cur = conn.cursor()
            while True:
                cur.execute("SELECT * FROM urls WHERE short = ?", (code_court,))
                if not cur.fetchone():
                    break
                code_court = genere_code_court()
            conn.execute("INSERT INTO urls (short, original) VALUES (?, ?)", (code_court, original))
            short_url = request.host_url + code_court
    return render_template('index.html', short_url=short_url)


@app.route('/<short_code>')
def redirecteur(short_code):
    with sqlite3.connect(DB_FILE) as conn:
        cur = conn.cursor()
        cur.execute("SELECT original FROM urls WHERE short = ?", (short_code,))
        resultat = cur.fetchone()
        if resultat:
            return redirect(resultat[0])
    return "INTROUVABLE", 404


if __name__ == '__main__':
    init_database()
    app.run(debug=True)