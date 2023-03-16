import datetime
import schedule


def koo():
    hour = datetime.datetime.now().hour
    print('Ку' * ((hour - 1) % 12 + 1))


schedule.every().hour.at('00:00').do(koo)

while True:
    schedule.run_pending()
