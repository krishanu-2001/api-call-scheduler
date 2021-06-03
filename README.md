## Api scheduler  
<hr>  
Run a cron job every 30 seconds on heroku  
### Steps  
      heroku ps:scale clock=1
      git push heroku HEAD:master
      heroku logs --tail  
### Information  
      **main.py** - main scheduled task
      **cronjob.py** - scheduler
      *pipenv* - virtual environment
