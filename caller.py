import requests
import schedule
import threading

def ping_api():
    url = 'https://ifconfig.co'
    response = requests.get(url)

def scheduler(ping_times):
    for time,ping in ping_times.items():
        schedule.every().day.at(time).do(run_threaded,ping_api)


def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()
        
if __name__ == '__main__':
    times_to_ping = ("18:01:30", "18:01:30", "09:15:25","11:58:23","13:45:09","13:45:09","13:45:09","17:22:00")
    scheduler(times_to_ping)
    while True:
        schedule.run_pending()

