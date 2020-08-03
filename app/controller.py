from flask import render_template, request
from app import app
from app.models.game import Game, generate_ai
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play-game', methods=['POST'])
def play_game():
    player_1 = Player(request.form['player-1'], request.form['player-1-choice'])
    player_2 = Player(request.form['player-2'], request.form['player-2-choice'])
    new_game = Game(player_1, player_2)
    result = new_game.determine_winner()
    return render_template('result.html', result=result)

@app.route('/welcome')
def welcome_page():
    return render_template('welcome.html')

@app.route('/computer')
def computer_opponent():
    return render_template('computer.html')

@app.route('/play-computer', methods=['POST'])
def play_computer():
    player_1 = Player(request.form['player'], request.form['player-choice'])
    computer = generate_ai()
    new_game = Game(player_1, computer)
    result = new_game.determine_winner()
    return render_template('computer-result.html', result=result)
