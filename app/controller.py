from flask import render_template, request
from app import app
from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/play-game', methods=['POST'])
def play_game():
    pass
    player_1 = Player(request.form['player-1'], request.form['player-1-choice'])
    player_2 = Player(request.form['player-2'], request.form['player-2-choice'])
    new_game = Game(player_1, player_2)
    result = new_game.determine_winner()
    return render_template('index.html', title='Home')