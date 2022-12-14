import sys
import csv

from random import randint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.load_table()
        self.compute()
        self.update_colors()
        self.table.itemSelectionChanged.connect(self.compute)
        self.btn_update.clicked.connect(self.update_colors)

    def load_table(self):
        ans = []
        with open('price.csv', 'r', encoding='utf8') as f:
            reader = csv.DictReader(f, delimiter=';', quotechar='"')
            for d in reader:
                ans.append(tuple([d[i] for i in d] + [0]))
        ans.sort(key=lambda x: x[1], reverse=True)
        self.table.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, col in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(col)))
        self.table.resizeColumnsToContents()

    def compute(self):
        s = 0
        for i in range(self.table.rowCount()):
            p, c = map(int, (self.table.item(i, 1).text(), self.table.item(i, 2).text()))
            s += p * c
        self.result.setText(str(s))

    def update_colors(self):
        for i in range(min(5, self.table.rowCount())):
            color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            for j in range(self.table.columnCount()):
                self.table.item(i, j).setBackground(color)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
