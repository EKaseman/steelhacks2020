# coding: utf-8

import os
import json
import pickle
import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

querystring = {"number": "100", "instructionsRequired": "true", "query": "soup"}

headers = {
    "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "x-rapidapi-key": os.environ["API_KEY"],
}

response = requests.request("GET", url, headers=headers, params=querystring)

response_100_soup = response
r[0] = response
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

querystring = {
    "number": "100",
    "instructionsRequired": "true",
    "offset": "100",
    "query": "soup",
}

headers = {
    "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "x-rapidapi-key": os.environ["API_KEY"],
}

response = requests.request("GET", url, headers=headers, params=querystring)

response_100_soup_2 = response
r[1] = response_100_soup_2
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

querystring = {
    "number": "100",
    "instructionsRequired": "true",
    "offset": "200",
    "query": "soup",
}

headers = {
    "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "x-rapidapi-key": os.environ["API_KEY"],
}

response = requests.request("GET", url, headers=headers, params=querystring)

response_100_soup_3 = response
r[2] = response
id_list = (
    [result["id"] for result in r[0].json()["results"]]
    + [result["id"] for result in r[1].json()["results"]]
    + [result["id"] for result in r[2].json()["results"]]
)

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/informationBulk"

querystring = {"ids": ",".join([str(i) for i in id_list])}

headers = {
    "x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    "x-rapidapi-key": os.environ["API_KEY"],
}

response = requests.request("GET", url, headers=headers, params=querystring)

response_big = response
with open("data.pickle", "wb") as f:
    pickle.dump(response_big.json(), f, protocol=pickle.HIGHEST_PROTOCOL)
