import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.con = sqlite3.connect('films_db.sqlite')
        self.btn_find.clicked.connect(self.display_result)
        self.btn_change.clicked.connect(self.save_results)
        self.modified = {}

    def display_result(self):
        cur = self.con.cursor()
        item_id = self.mask.toPlainText()
        result = cur.execute(f"SELECT * FROM films WHERE {item_id}").fetchall()
        self.table.setRowCount(len(result))
        if not result:
            return
        self.table.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            self.modified['title'] = elem[1][::-1]
            self.modified['year'] = str(int(elem[2]) + 1000)
            self.modified['duration'] = str(int(elem[4]) * 2)
            for j, val in enumerate(elem):
                self.table.setItem(i, j, QTableWidgetItem(str(val)))

    def save_results(self):
        cur = self.con.cursor()
        item_id = self.mask.toPlainText()
        que = "UPDATE films SET\n"
        que += ", ".join([f"{key}='{self.modified.get(key)}'"
                          for key in self.modified.keys()])
        que += f"WHERE {item_id}"
        cur.execute(que)
        self.con.commit()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
