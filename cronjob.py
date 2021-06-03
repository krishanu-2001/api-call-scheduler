from apscheduler.schedulers.blocking import BlockingScheduler

from main import cronjob

scheduler = BlockingScheduler()
scheduler.add_job(cronjob, "interval", seconds=30)

scheduler.start()