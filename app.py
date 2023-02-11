from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.TestApiHandler import TestApiHandler

# Use the second line to serve the front end with the back end
app = Flask(__name__, static_url_path='', static_folder='')
# app = Flask(__name__, static_url_path='', static_folder='frontend/build')

CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'index.html')

api.add_resource(TestApiHandler, '/flask/test')