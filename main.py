import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.load_genres()
        self.btn_update.clicked.connect(self.get_data)

    def load_genres(self):
        connection = sqlite3.connect('films_db.sqlite')
        cursor = connection.cursor()
        result = cursor.execute('''
        SELECT title FROM genres
        ''').fetchall()
        for s in result:
            self.cb_genres.addItem(s[0])

    def get_data(self):
        genre = self.cb_genres.currentText()
        connection = sqlite3.connect('films_db.sqlite')
        cursor = connection.cursor()
        result = cursor.execute(f'''
        SELECT title, genre, year FROM films
        WHERE genre IN (
        SELECT id FROM genres
        WHERE title = "{genre}"
        )
        ''').fetchall()
        self.table.setRowCount(len(result))
        self.table.setColumnCount(len(result[0]))
        for i, row in enumerate(result):
            for j, col in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(col)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
