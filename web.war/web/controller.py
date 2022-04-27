from flask import Flask, jsonify, request, render_template, redirect
from flask_restful import Resource, Api
import requests
import json

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
api = Api(app)

@app.route('/')
def entry():
    return redirect('/simulate')

@app.route('/simulate', methods=['GET'])
def simulate():

    return render_template('simulate.html')

@app.route('/simulationresults', methods=['POST'])
def simulationresults():

    package = {
        "playerOne": request.form['playerOne'],
        "playerTwo": request.form['playerTwo']
    }    

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    r = requests.post( "http://gameapi:5001/simulate", data=json.dumps(package), headers=headers)
    result = json.loads(r.text)

    return render_template('simulationresults.html', result=result)

@app.route('/stats', methods=['GET'])
def stats():
  return render_template('stats.html')

@app.route('/statsresults', methods=['POST'])
def statsresults():
    package = {
        "player": request.form['player']
    }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    r = requests.post( "http://gamehistoryapi:5002/get", data=json.dumps(package), headers=headers)
    result = r.text

    data = {"player": request.form['player'], "wins": result}

    return render_template('statsresults.html', result=data)


def run():
  app.run(debug=True, port=5000, host='0.0.0.0')