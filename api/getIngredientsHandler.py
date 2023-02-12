from flask_restful import Api, Resource, reqparse
from db import start, get_ingredients

class getIngredientsHandler(Resource):
  def get(self):
    conn = start()

    return get_ingredients(conn, "tester")