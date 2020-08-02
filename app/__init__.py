from flask import Flask

app = Flask(__name__)

from app import controller

app.static_folder = 'static'
