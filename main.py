from apscheduler.schedulers.blocking import BlockingScheduler

from reptile_task import reptile_task


def job():
    reptile_task()


scheduler = BlockingScheduler()
scheduler.add_job(job, 'interval', seconds=10)  # 每隔10秒执行一次任务
scheduler.start()
