import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn_search.clicked.connect(self.get_data)

    def get_data(self):
        param = self.cb.currentText()
        k = {
            'Год выпуска': ('year', int),
            'Название': ('title', str),
            'Продолжительность': ('duration', int)
        }
        param, param_type = k.get(param)
        value = self.le_search.text()
        connection = sqlite3.connect('films_db.sqlite')
        cursor = connection.cursor()
        try:
            if type(value) != param_type:
                value = param_type(value)
            result = cursor.execute(f'''
            SELECT id, title, year, genre, duration FROM films
            WHERE {param} = "{value}"
            ''').fetchall()
            if not result:
                self.lb_error.setText('Ничего не найдено')
            else:
                self.lb_error.setText('')
                data = result[0]
                for s, widget in zip(data, (self.le_id, self.le_name, self.le_year, self.le_genre, self.le_duration)):
                    widget.setText(str(s))
        except Exception:
            self.lb_error.setText('Неправильный запрос')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
