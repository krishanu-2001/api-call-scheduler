import requests
import json

def func():
  response = requests.get("https://mernstackestore.herokuapp.com/items")
  var = json.loads(response.text)
  print(var[0])


func()