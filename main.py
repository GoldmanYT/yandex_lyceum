import sys
import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.load_table()
        self.compute()
        self.table.itemSelectionChanged.connect(self.compute)

    def load_table(self):
        ans = []
        with open('price.csv', 'r', encoding='utf8') as f:
            reader = csv.DictReader(f, delimiter=';', quotechar='"')
            for d in reader:
                ans.append(tuple([d[i] for i in d] + [0]))
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


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
