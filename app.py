from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment
from api.TestApiHandler import TestApiHandler

# Use the second line to serve the front end with the back end
# app = Flask(__name__, static_url_path='', static_folder='')
app = Flask(__name__, static_url_path='', static_folder='frontend/build')

CORS(app) #comment this on deployment
api = Api(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(str(app.static_folder),'index.html')

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


# if __name__ == '__main__':
#     app.run(debug=True)

api.add_resource(TestApiHandler, '/flask/test')