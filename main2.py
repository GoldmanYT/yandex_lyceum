import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.con = sqlite3.connect('library_db.sqlite')
        self.btn.clicked.connect(self.find_result)
        self.lw.itemActivated.connect(self.show_info)
        cur = self.con.cursor()
        self.genres = dict(cur.execute('''SELECT id, title FROM genres''').fetchall())
        self.authors = dict(cur.execute('''SELECT id, title FROM authors''').fetchall())
        self.images = dict(cur.execute('''SELECT id, img_path FROM images''').fetchall())
        self.results = []
        self.info_widget = None

    def show_info(self, item):
        index = None
        for i, result in enumerate(self.results):
            if result[0] == item.text():
                index = i
                break
        if index is None:
            return
        title, author_id, year, genre_id, img_id = self.results[index]
        author = self.authors.get(author_id)
        genre = self.genres.get(genre_id)
        img_path = self.images.get(img_id, self.images.get(1))
        self.info_widget = InfoWidget(title, author, year, genre, img_path)
        self.info_widget.show()

    def find_result(self):
        cur = self.con.cursor()
        text = self.le.text()
        if self.cb.currentText() == 'Автор':
            data = cur.execute(f'''SELECT title, author, year, genre, img FROM books
                                   WHERE author IN (
                                   SELECT id FROM authors
                                   WHERE title LIKE "{text}%"
                                   )
                                   ''').fetchall()
        else:
            data = cur.execute(f'''SELECT title, author, year, genre, img FROM books
                                   WHERE title LIKE "{text}%"
                                   ''').fetchall()
        self.results = data
        self.lw.clear()
        for result in data:
            self.lw.addItem(result[0])


class InfoWidget(QWidget):
    def __init__(self, title, author, year, genre, img_path):
        super().__init__()
        uic.loadUi('info.ui', self)
        self.lb_title.setText(title)
        self.lb_author.setText(author)
        self.lb_year.setText(str(year))
        self.lb_genre.setText(genre)
        self.img_pixmap = QPixmap(img_path)
        self.img.setPixmap(self.img_pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
