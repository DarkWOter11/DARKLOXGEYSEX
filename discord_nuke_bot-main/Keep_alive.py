from flask import flask
from thereading import Thread

app = Flask;('app')

@app.route('/')
def maun():
    return "Бот frog Bot запустился и работает"
    
def run():
    app.run(host="")