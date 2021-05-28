import requests
import schedule
from datetime import datetime

times_to_ping = ("17:58:25", "17:58:25", "09:15:25","11:58:23","13:45:09","13:45:09","13:45:09","17:22:00")

def ping_api():
    cur_date = datetime.today()
    print(cur_date)
    url = 'https://ifconfig.co'
    response = requests.get(url)
    #print(response.content)


if __name__ == '__main__':
    for time in times_to_ping:
        schedule.every().day.at(time).do(ping_api)
    while True:
        schedule.run_pending()
