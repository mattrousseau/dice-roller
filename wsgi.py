from flask import Flask, jsonify
from dice_roller.dice import Dice

app = Flask(__name__)

@app.route('/')
def home():
    dice = Dice()
    roll = dice.roll()
    return jsonify({'roll': roll})

@app.route('/hello')
def hello():
    dice = Dice()
    return jsonify({'message': "Hello there"})
