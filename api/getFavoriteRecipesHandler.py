from flask_restful import Api, Resource, reqparse
from db import start, get_favorites

class getFavoriteRecipesHandler(Resource):
  def get(self):
    conn = start()
    favorites_all = get_favorites(conn, "tester")

    result = []
    for favorite in favorites_all:
        result.append(favorite["recipie"])

    return result