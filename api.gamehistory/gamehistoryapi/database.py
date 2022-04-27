from flask_mongoengine import MongoEngine
from flask import Flask
from pathlib import Path
import yaml

def initDB(app, config):
    uri = "mongodb://{}:{}@{}:{}/{}?authSource={}".format(
        config["dbsettings"]["user"], 
        config["dbsettings"]["password"], 
        config["dbsettings"]["host"], 
        config["dbsettings"]["port"], 
        config["dbsettings"]["database"],
        config["dbsettings"]["database"]
    )

    app.config['MONGODB_SETTINGS'] = {
        'host':uri
    }

    db = MongoEngine()
    db.init_app(app)

    return db

