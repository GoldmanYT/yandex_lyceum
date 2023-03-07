import os
import shutil
import datetime


def make_reserve_arc(source, dest):
    if not os.path.exists(source):
        print('Нет такой папки')
        return
    if not os.path.isdir(source):
        print('Это не папка')
        return
    time = datetime.datetime.now()
    year, month, day, hour, minute, second = map(
        str, (time.year, time.month, time.day, time.hour, time.minute, time.second))
    file_name = f'{year.rjust(4, "0")}{month.rjust(2, "0")}{day.rjust(2, "0")}_' \
                f'{hour.rjust(2, "0")}{minute.rjust(2, "0")}{second.rjust(2, "0")}.zip'
    shutil.make_archive(source, 'zip', root_dir=source)
    path = source.replace('\\', '/').split('/')[-1] + '.zip'
    os.rename(path, file_name)
    shutil.move(file_name, dest)


if __name__ == '__main__':
    s = input('Введите путь к каталогу, который надо архивировать: ')
    d = input('Введите путь к каталогу, в который необходимо поместить результат: ')
    make_reserve_arc(s, d)
