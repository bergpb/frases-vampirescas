import requests
from random import randrange
from flask import Flask, jsonify, g

app = Flask(__name__)

__url__ = "https://gist.githubusercontent.com/bergpb/76f23a2aab91ff09660ae1319e0b6f56/raw/frases_christian_profanus.txt"

@app.before_request
def before_request_func():
    frases = requests.get(__url__).text
    list_frases = frases.split('\n')
    g.frase = list_frases[randrange(len(list_frases))]


@app.route('/', methods=['GET'])
def index():
    data = {
        "success": True,
        "frase": g.frase,
        "autor": "Profanus, Christian Cardoso"
    }
    return jsonify(data = data)
