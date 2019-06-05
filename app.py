from flask import Flask, render_template, request
import codecs
from random import randint

with codecs.open('word_rus.txt', encoding='utf-8') as file:
    words = [row.strip() for row in file]
for i in range(len(words)):
	words[i] = words[i][0].upper() + words[i][1:]
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('main.html', words = words)

if __name__ == "__main__":
    app.run()
