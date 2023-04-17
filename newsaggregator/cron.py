import schedule, os , time


def task():
    os.system("python3 manage.py scrape")

schedule.every(10).minutes.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
