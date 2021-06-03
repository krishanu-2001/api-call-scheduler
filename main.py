from datetime import datetime
import requests
import json

def cronjob():
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    response = requests.get("https://mernstackestore.herokuapp.com/items")
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(text)
