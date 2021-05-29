from datetime import datetime
import requests

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    response = requests.get("https://mernstackestore.herokuapp.com/items")
    print(response.status_code)