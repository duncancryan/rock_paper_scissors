from flask import render_template, request
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/play-game', methods=['POST'])