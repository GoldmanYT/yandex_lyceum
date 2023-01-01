import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.con = sqlite3.connect('films_db.sqlite')
        self.genres = self.get_genres()
        self.display_result()
        self.btn_add.clicked.connect(self.open_dialog)
        self.dialog = None

    def get_genres(self):
        cur = self.con.cursor()
        return dict(cur.execute('''SELECT id, title FROM genres''').fetchall())

    def open_dialog(self):
        cur = self.con.cursor()
        genres = [i[0] for i in cur.execute('''SELECT title FROM genres''').fetchall()]
        self.dialog = Dialog(genres, self.con, self)
        self.dialog.show()

    def display_result(self):
        cur = self.con.cursor()
        result = cur.execute(f"SELECT * FROM films").fetchall()
        self.table.setRowCount(len(result))
        if not result:
            return
        self.table.setColumnCount(len(result[0]))
        for i, elem in enumerate(result[::-1]):
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(self.genres.get(val) if j == 3 else str(val)))


class Dialog(QWidget):
    def __init__(self, genres, con, main_window):
        super().__init__()
        uic.loadUi('dialog.ui', self)
        for genre in genres:
            self.cb_genre.addItem(genre)
        self.con = con
        self.btn_add.clicked.connect(self.add)
        self.main_window = main_window

    def add(self):
        title = self.le_title.text()
        year = self.le_year.text()
        genre = self.cb_genre.currentText()
        duration = self.le_duration.text()
        if not year.isdigit() or not duration.isdigit():
            self.lb_error.setText('Неверно заполнена форма')
            return
        year = int(year)
        if year > 2022:
            self.lb_error.setText('Неверно заполнена форма')
            return
        cur = self.con.cursor()
        genre_id = cur.execute(f'''SELECT id FROM genres
                                   WHERE title = "{genre}"''').fetchall()[0][0]
        cur.execute(f'''INSERT INTO films(title, year, genre, duration) 
                        VALUES("{title}", {year}, {genre_id}, {duration})''')
        self.con.commit()
        self.main_window.display_result()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
