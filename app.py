import requests
from flask import Flask, render_template, request
from flask_ngrok import run_with_ngrok
from pprint import pprint
import json

app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when app is run

@app.route('/')
def telaApp():  # put application's code here
    lista = requests.get('http://my-json-server.typicode.com/maujor/livros-json/livros').json()
    # pprint(lista)
    return render_template('index.html', lista=lista) 


if __name__ == '__main__':
    app.run(debug=True)
    # app.run()
