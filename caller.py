import requests
import schedule
import threading
import concurrent.futures
from datetime import datetime

times_to_ping = ("17:58:25", "17:58:25", "09:15:25","11:58:23","13:45:09","13:45:09","13:45:09","17:22:00")

thread_local = threading.local()

def num_of_ping(times):
    ping_times = {}
    for i in times_to_ping:
        if i in ping_times:
            ping_times[i] += 1
        else:
            ping_times[i] = 1
    return ping_times

def ping_api(pings:int):
    for i in range(pings):
        cur_date = datetime.today()
        print(cur_date)
        url = 'https://ifconfig.co'
        response = requests.get(url)
    #print(response.content)


def scheduler(ping_times):
    for time,ping in ping_times.items():
        schedule.every().day.at(time).do(ping_api,ping)
    while True:
        schedule.run_pending()

def threads(ping_times):
    print(ping_times)
    max_workers = max(ping_times.values())
    print(max_workers)
    with concurrent.futures.ThreadPoolExecutor(max_workers) as executor:
        executor.map(scheduler,ping_times)
        
if __name__ == '__main__':
    times_to_ping = ("18:01:30", "18:01:30", "09:15:25","11:58:23","13:45:09","13:45:09","13:45:09","17:22:00")
    ping_times = num_of_ping(times_to_ping)
        threads(ping_times)
