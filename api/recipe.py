#getRecipeSearch(ingredients)
# Given an array of ingredients (e.g. ["carrot", "onion", "celery"]),
#    return a json of the most relevent recipes
#
#getSingleRecipe(name)
# Given a string name of ingredients or a recipe name: ("Carrot Onion Celery") or ("Fettucine Alfredo")
#    return a json of the most relevent recipes.
#    
#    Can search for a single recipe by setting name to the recipe name and accessing the first recipe returned
#    Alternatively, can use like getRecipeSearch, but instead of having the ingredients in array, they are in a string name seperated by spaces.
#
# EDAMAM SCHEMA
# Application ID: f84dab47
# Application Key: bcf804f39e847197f4849e1050fb1d49
# https://developer.edamam.com/edamam-docs-recipe-api

# Model Schema 
#{
#  "from": 0,
#  "to": 0,
#  "count": 0,
#  "_links": {
#    "self": {
#      "href": "string",
#      "title": "string"
#    },
#    "next": {
#      "href": "string",
#      "title": "string"
#    }
#  },
#  "hits": [
#    {
#      "recipe": {
#        "uri": "string",
#        "label": "string",
#        "image": "string",
#        "images": {
#          "THUMBNAIL": {
#            "url": "string",
#            "width": 0,
#            "height": 0
#          },
#          "SMALL": {
#            "url": "string",
#            "width": 0,
#            "height": 0
#          },
#          "REGULAR": {
#            "url": "string",
#            "width": 0,
#            "height": 0
#          },
#          "LARGE": {
#            "url": "string",
#            "width": 0,
#            "height": 0
#          }
#        },
#        "source": "string",
#        "url": "string",
#        "shareAs": "string",
#        "yield": 0,
#        "dietLabels": [
#          "string"
#        ],
#        "healthLabels": [
#          "string"
#        ],
#        "cautions": [
#          "string"
#        ],
#        "ingredientLines": [
#          "string"
#        ],
#        "ingredients": [
#          {
#            "text": "string",
#            "quantity": 0,
#            "measure": "string",
#            "food": "string",
#            "weight": 0,
#            "foodId": "string"
#          }
#        ],
#        "calories": 0,
#        "glycemicIndex": 0,
#        "totalCO2Emissions": 0,
#        "co2EmissionsClass": "A+",
#        "totalWeight": 0,
#        "cuisineType": [
#          "string"
#        ],
#        "mealType": [
#          "string"
#        ],
#        "dishType": [
#          "string"
#        ],
#        "instructions": [
#          "string"
#        ],
#        "tags": [
#          "string"
#        ],
#        "externalId": "string",
#        "totalNutrients": {},
#        "totalDaily": {},
#        "digest": [
#          {
#            "label": "string",
#            "tag": "string",
#            "schemaOrgTag": "string",
#            "total": 0,
#            "hasRDI": true,
#            "daily": 0,
#            "unit": "string",
#            "sub": {}
#          }
#        ]
#      },
#      "_links": {
#        "self": {
#          "href": "string",
#          "title": "string"
#        },
#        "next": {
#          "href": "string",
#          "title": "string"
#        }
#      }
#    }
#  ]
#}

from flask import Flask
from urllib.request import urlopen
app = Flask(__name__)

def getRecipeSearch(ingredients):
    ingList = ""
    if ingredients:
        ingList += ingredients[0]
    for x in range(1, len(ingredients)):
        ingList += "%2C"
        ingList += ingredients[x]
    with urlopen("https://api.edamam.com/api/recipes/v2?type=public&q=" + ingList + "&app_id=f84dab47&app_key=bcf804f39e847197f4849e1050fb1d49") as response:
        return response.read()
def getSingleRecipe(name):
    with urlopen("https://api.edamam.com/api/recipes/v2?type=public&q=" + name.replace(" ", "%2C") + "&app_id=f84dab47&app_key=bcf804f39e847197f4849e1050fb1d49") as response:
        return response.read()

@app.route("/", methods=["GET", "POST"])
def index():
    #This is not fully integrated, I don't know
    #how to yet.
    return "index.html"