from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine
from gamehistoryapi import database
from pathlib import Path
import json
import yaml

config = yaml.safe_load(open( Path(__file__).parent / "config.yaml"))

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
db = database.initDB(app, config)
api = Api(app)

class PlayedGame(db.Document):
    gameID = db.StringField()
    players = db.ListField()
    winner = db.StringField()
    handsHistory = db.ListField()

@app.route('/test', methods=['GET'])
def test():
  result1 = str(PlayedGame.objects(winner="john").count())
  result2 = str(PlayedGame.objects(winner="mary").count())
  results = result1+result2
  return results, 200

@app.route('/get', methods=['POST'])
def get():
  player = json.loads(request.data)
  print(player)
  result = str(PlayedGame.objects(winner=player['player']).count())

  return result, 200

@app.route('/insert', methods=['POST'])
def insert_record():

  record = json.loads(request.data)
  game = PlayedGame(
    gameID=record['gameID'],
    players=record['players'],
    winner=record['winner'],
    handsHistory=record['handsHistory'])
  game.save()
  return "OK", 200

def run():
  app.run(debug=True, port=5002, host='0.0.0.0')
