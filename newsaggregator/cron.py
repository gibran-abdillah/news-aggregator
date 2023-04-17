import schedule, os , time


print("do something")

def task():
    print("running the task...")
    os.system("python3 manage.py scrape")

schedule.every(1).minutes.do(task)

while True:
    print("pending task...")
    schedule.run_pending()
    time.sleep(1)
