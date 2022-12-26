from datetime import datetime


class Session:
    def __init__(self, name, begin_datetime, duration, w_seats, h_seats):
        self.name = name
        self.time = begin_datetime
        self.duration = duration
        self.w, self.h = w_seats, h_seats
        self.seats = [[0] * w_seats for _ in range(h_seats)]

    def take_seat(self, x, y):
        if 0 <= x < self.w and 0 <= y < self.h:
            if not self.seats[y][x]:
                self.seats[y][x] = 1
                return True
            return False

    def __str__(self):
        return f'{self.time} {self.duration}'

    def all_seats(self):
        return '\n'.join(''.join(str(seat) for seat in row) for row in self.seats)


class CinemaHall:
    def __init__(self, number, w_seats, h_seats):
        self.number = number
        self.sessions = []
        self.w, self.h = w_seats, h_seats

    def add_session(self, name, year, month, day, hour, minute, duration):
        begin_datetime = datetime(year, month, day, hour, minute)
        new_session = Session(name, begin_datetime, duration, self.w, self.h)
        if all(new_session.time + new_session.duration < session.time or
               new_session.time > session.time + session.duration for session in self.sessions):
            self.sessions.append(new_session)

    def __str__(self):
        return f'{self.number}'


class Cinema:
    def __init__(self, name):
        self.name = name
        self.cinema_halls = []

    def add_cinema_hall(self, number, w_seats, h_seats):
        if any(number == cinema_hall.number for cinema_hall in self.cinema_halls):
            return False
        self.cinema_halls.append(CinemaHall(number, w_seats, h_seats))
        return True

    def __str__(self):
        return f'{self.name}'


'''
Строка для теста:
6
t1
8
1
5
5
10
s1
10
6
t2
8
1
5
5
10
s1
10
11
s1
1
0 0
11
s1
1
'''


cinemas = []
run = True
current_year = 2022
current_month = 12
current_day = 25
current_hour = 12
current_minute = 0
current_cinema = None
current_cinema_hall = None

while run:
    print('''Выберите один из пунктов:
0. Выйти
1. Указать год
2. Указать месяц
3. Указать день
4. Указать час
5. Указать минуты
6. Добавить кинотеатр
7. Выбрать кинотеатр
8. Добавить зал в текущий кинотеатр
9. Выбрать зал в текущем кинотеатре
10. Добавить сеанс в текущий зал в текущем кинотеатре в текущую дату
11. Купить билет на сеанс
12. Найти ближайший сеанс (относительно текущей даты) на фильм
''')
    s = input('Выберите пункт: ')
    if s == '0':
        run = False
    if s == '1':
        try:
            current_year = int(input('Введите год: '))
        except Exception:
            print('Ошибка!')
    if s == '2':
        try:
            current_month = int(input('Введите месяц: '))
        except Exception:
            print('Ошибка!')
    if s == '3':
        try:
            current_day = int(input('Введите день: '))
        except Exception:
            print('Ошибка!')
    if s == '4':
        try:
            current_hour = int(input('Введите час: '))
        except Exception:
            print('Ошибка!')
    if s == '5':
        try:
            current_minute = int(input('Введите минуту: '))
        except Exception:
            print('Ошибка!')
    if s == '6':
        cinema_name = input('Введите название: ')
        cinemas.append(Cinema(cinema_name))
        current_cinema = cinemas[-1]
        current_cinema_hall = None
    if s == '7':
        print('Выберите один из вариантов:')
        for i, cinema in enumerate(cinemas, 1):
            print(i, cinema.name)
        try:
            n = int(input('Номер из списка: ')) - 1
            current_cinema = cinemas[n]
            current_cinema_hall = None
        except Exception:
            print('Ошибка!')
    if s == '8':
        if current_cinema is None:
            print('Нет кинотеатров')
        else:
            try:
                n = int(input('Номер зала: '))
                w = int(input('Ширина ряда (в местах): '))
                h = int(input('Количество рядов: '))
                result = current_cinema.add_cinema_hall(n, w, h)
                if result:
                    current_cinema_hall = current_cinema.cinema_halls[-1]
                else:
                    print('Номер повторился')
            except Exception:
                print('Ошибка')
    if s == '9':
        if current_cinema is None:
            print('Нет кинотеатров')
        elif not current_cinema.cinema_halls:
            print('Нет залов')
        else:
            for i, cinema_hall in enumerate(current_cinema.cinema_halls, 1):
                print(i, cinema_hall.number, f'{cinema_hall.w}x{cinema_hall.h}')
            try:
                n = int(input('Выберите один из пунктов: ')) - 1
                current_cinema_hall = current_cinema.cinema_halls[n]
            except Exception:
                print('Ошибка!')
    if s == '10':
        if current_cinema is None:
            print('Нет кинотеатров')
        elif not current_cinema.cinema_halls:
            print('Нет залов')
        else:
            session_name = input('Введите название сеанса: ')
            session_duration = input('Введите продолжительность сеанса: ')
            current_cinema_hall.add_session(session_name, current_year, current_month, current_day, current_hour,
                                            current_minute, session_duration)
    if s == '11':
        movie_title = input('Введите название фильма: ')
        result = []
        for cinema in cinemas:
            for cinema_hall in cinema.cinema_halls:
                for session in cinema_hall.sessions:
                    if session.name == movie_title:
                        result.append([cinema, cinema_hall, session])
        for i, res in enumerate(result, 1):
            print(i, res[0], res[1].number, res[2])
        try:
            n = int(input('Введите один из пунктов: '))
            res = result[n]
            print('Выберите место:')
            print(res[2].all_seats())
            x, y = map(int, input('x y: ').split())
            res[2].take_seat(x, y)
        except Exception:
            print('Ошибка!')
