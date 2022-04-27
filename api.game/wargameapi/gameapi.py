from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from wargameapi import game, models
from pathlib import Path
import requests
import json
import yaml

config = yaml.safe_load(open( Path(__file__).parent / "config.yaml"))

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

@app.route('/test', methods=['GET'])
def test():
  result = game.SimulateGame("john", "mary")

  package = {
    "gameID": result["game"].gameID,
    "winner": result["winner"],
    "players": [result["game"].playerOne.name, result["game"].playerTwo.name],
    "handsHistory": result["game"].handHistory
  }
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
  #should be a thread or try/catch so that results still get sent to end user
  #even if records db is down
  r = requests.post( config["gamehistory"]["url"], data=json.dumps(package), headers=headers)

  return package, 200

@app.route('/simulate', methods=['POST'])
def simulate():
  record = json.loads(request.data)
  result = game.SimulateGame(record["playerOne"], record["playerTwo"])

  package = {
    "gameID": result["game"].gameID,
    "winner": result["winner"],
    "players": [result["game"].playerOne.name, result["game"].playerTwo.name],
    "handsHistory": result["game"].handHistory
  }
  headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
  #should be a thread or try/catch so that results still get sent to end user
  #even if records db is down
  r = requests.post( config["gamehistory"]["url"], data=json.dumps(package), headers=headers)

  return package, 200

def run():
  app.run(debug=True, port=5001, host='0.0.0.0')
