import datetime
import schedule


def koo(hours, message='Ку'):
    hour = datetime.datetime.now().hour
    if hour in hours:
        print(message * ((hour - 1) % 12 + 1))


a = list(range(24))
message = input('Введите сообщение: ')
hours = input('Введите диапазон: ')
x, y = map(int, hours.split('-'))
h = x
while True:
    a.remove(x)
    if x == y:
        break
    x = (x + 1) % 24
schedule.every().hour.at('00:00').do(koo, message=message, hours=a)

while True:
    schedule.run_pending()
