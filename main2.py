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
        self.btn_add_film.clicked.connect(self.open_add_film_dialog)
        self.btn_edit_film.clicked.connect(self.open_edit_film_dialog)
        self.btn_delete_film.clicked.connect(self.delete_film)
        self.btn_add_genre.clicked.connect(self.open_add_genre_dialog)
        self.btn_edit_genre.clicked.connect(self.open_edit_genre_dialog)
        self.btn_delete_genre.clicked.connect(self.delete_genre)
        self.dialog = None

    def get_genres(self):
        cur = self.con.cursor()
        return dict(cur.execute('''SELECT id, title FROM genres''').fetchall())

    def open_add_film_dialog(self):
        cur = self.con.cursor()
        genres = [i[0] for i in cur.execute('''SELECT title FROM genres''').fetchall()]
        self.dialog = AddFilmDialog(genres, self.con, self)
        self.dialog.show()

    def open_edit_film_dialog(self):
        cur = self.con.cursor()
        genres = [i[0] for i in cur.execute('''SELECT title FROM genres''').fetchall()]
        indexes = self.table_films.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            data = [self.table_films.item(row, i).text() for i in range(5)]
            self.dialog = EditFilmDialog(genres, self.con, self, data)
            self.dialog.show()

    def delete_film(self):
        cur = self.con.cursor()
        indexes = self.table_films.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            _id = self.table_films.item(row, 0).text()
            cur.execute(f'''DELETE FROM films
                            WHERE id = {_id}''')
            self.display_result()

    def open_add_genre_dialog(self):
        self.dialog = AddGenreDialog(self.con, self)
        self.dialog.show()

    def open_edit_genre_dialog(self):
        indexes = self.table_genres.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            data = [self.table_genres.item(row, i).text() for i in range(2)]
            self.dialog = EditGenreDialog(self.con, self, data)
            self.dialog.show()

    def delete_genre(self):
        cur = self.con.cursor()
        indexes = self.table_genres.selectedIndexes()
        if indexes:
            row = indexes[0].row()
            _id = self.table_genres.item(row, 0).text()
            cur.execute(f'''DELETE FROM genres
                            WHERE id = {_id}''')
            self.display_result()

    def display_result(self):
        cur = self.con.cursor()
        result = cur.execute(f"SELECT * FROM films").fetchall()
        self.table_films.setRowCount(len(result))
        if result:
            self.table_films.setColumnCount(len(result[0]))
            for i, elem in enumerate(result[::-1]):
                for j, val in enumerate(elem):
                    self.table_films.setItem(i, j, QTableWidgetItem(self.genres.get(val) if j == 3 else str(val)))
        result = cur.execute(f"SELECT * FROM genres").fetchall()
        self.table_genres.setRowCount(len(result))
        if result:
            self.table_genres.setColumnCount(len(result[0]))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.table_genres.setItem(i, j, QTableWidgetItem(self.genres.get(val) if j == 3 else str(val)))


class AddFilmDialog(QWidget):
    def __init__(self, genres, con, main_window):
        super().__init__()
        uic.loadUi('add_film.ui', self)
        for genre in genres:
            self.cb_genre.addItem(genre)
        self.con = con
        self.btn_save.clicked.connect(self.save)
        self.main_window = main_window

    def save(self):
        title = self.le_title.text()
        year = self.le_year.text()
        genre = self.cb_genre.currentText()
        duration = self.le_duration.text()
        if not year.isdigit() or not duration.isdigit():
            return
        year = int(year)
        if year > 2022:
            return
        cur = self.con.cursor()
        genre_id = cur.execute(f'''SELECT id FROM genres
                                   WHERE title = "{genre}"''').fetchall()[0][0]
        cur.execute(f'''INSERT INTO films(title, year, genre, duration) 
                        VALUES("{title}", {year}, {genre_id}, {duration})''')
        self.con.commit()
        self.main_window.display_result()
        self.close()


class EditFilmDialog(QWidget):
    def __init__(self, genres, con, main_window, data):
        super().__init__()
        uic.loadUi('edit_film.ui', self)
        for genre in genres:
            self.cb_genre.addItem(genre)
        self.con = con
        self.btn_save.clicked.connect(self.save)
        self.main_window = main_window
        self.id, title, year, genre, duration = data
        self.le_title.setText(title)
        self.le_year.setText(str(year))
        self.cb_genre.setCurrentIndex(genres.index(genre))
        self.le_duration.setText(str(duration))

    def save(self):
        title = self.le_title.text()
        year = self.le_year.text()
        genre = self.cb_genre.currentText()
        duration = self.le_duration.text()
        if not year.isdigit() or not duration.isdigit():
            return
        year = int(year)
        if year > 2022:
            return
        cur = self.con.cursor()
        genre_id = cur.execute(f'''SELECT id FROM genres
                                   WHERE title = "{genre}"''').fetchall()[0][0]
        cur.execute(f'''UPDATE films
                        SET title = "{title}",
                        year = "{year}",
                        genre = "{genre_id}",
                        duration = "{duration}"
                        WHERE id = {self.id}''')
        self.con.commit()
        self.main_window.display_result()
        self.close()


class AddGenreDialog(QWidget):
    def __init__(self, con, main_window):
        super().__init__()
        uic.loadUi('add_genre.ui', self)
        self.con = con
        self.btn_save.clicked.connect(self.save)
        self.main_window = main_window

    def save(self):
        title = self.le_title.text()
        cur = self.con.cursor()
        cur.execute(f'''INSERT INTO genres(title) 
                        VALUES("{title}")''')
        self.con.commit()
        self.main_window.genres = self.main_window.get_genres()
        self.main_window.display_result()
        self.close()


class EditGenreDialog(QWidget):
    def __init__(self, con, main_window, data):
        super().__init__()
        uic.loadUi('edit_genre.ui', self)
        self.con = con
        self.btn_save.clicked.connect(self.save)
        self.main_window = main_window
        self.id, title = data
        self.le_title.setText(title)

    def save(self):
        title = self.le_title.text()
        cur = self.con.cursor()
        cur.execute(f'''UPDATE genres
                        SET title = "{title}"
                        WHERE id = {self.id}''')
        self.con.commit()
        self.main_window.genres = self.main_window.get_genres()
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
