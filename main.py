import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btns = [self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8,
                     self.btn_9, self.btn_10, self.btn_11, self.btn_12, self.btn_13, self.btn_14, self.btn_15,
                     self.btn_16, self.btn_17, self.btn_18, self.btn_19, self.btn_20, self.btn_21, self.btn_22,
                     self.btn_23, self.btn_24, self.btn_25, self.btn_26, self.btn_27, self.btn_28, self.btn_29,
                     self.btn_30, self.btn_31, self.btn_32, self.btn_33]
        self.get_data()
        for btn in self.btns:
            btn.clicked.connect(self.get_data)

    def get_data(self):
        try:
            upper_letter = self.sender().text()
        except Exception:
            upper_letter = 'А'
        lower_letter = upper_letter.lower()
        connection = sqlite3.connect('films_db.sqlite')
        cursor = connection.cursor()
        result = cursor.execute(f'''
        SELECT id, title, year, genre, duration FROM films
        WHERE title LIKE "{upper_letter}%" OR title LIKE "{lower_letter}%"
        ''').fetchall()
        genres = dict(cursor.execute('''
        SELECT id, title FROM genres
        ''').fetchall())
        self.table.setRowCount(len(result))
        if result:
            self.lb_info.setText(f'Нашлось {len(result)} записей')
            self.table.setColumnCount(len(result[0]))
        else:
            self.lb_info.setText(f'Ничего не найдено')
        for i, row in enumerate(result):
            for j, col in enumerate(row):
                if j == 3:
                    col = genres.get(col)
                self.table.setItem(i, j, QTableWidgetItem(str(col)))
        self.table.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
