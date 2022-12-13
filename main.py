import sys
import csv

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.display_results()
        self.le_search.textChanged.connect(self.display_results)

    def display_results(self):
        substring = self.le_search.text()
        if len(substring) < 3:
            substring = ''
        ans = []
        with open('titanic.csv', 'r', encoding='utf8') as f:
            reader = csv.DictReader(f, delimiter=',', quotechar='"')
            headers = reader.fieldnames
            for d in reader:
                if substring.lower() in d['Name'].lower():
                    ans.append(tuple(d[i] for i in d))
        self.table.setRowCount(len(ans))
        self.table.setColumnCount(len(ans[0]))
        self.table.setHorizontalHeaderLabels(headers)
        for i, row in enumerate(ans):
            for j, col in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(col)))
        self.table.resizeColumnsToContents()
        colors = [QColor(255, 0, 0), QColor(0, 255, 0)]
        for i in range(self.table.rowCount()):
            k = int(self.table.item(i, 5).text())
            for j in range(self.table.columnCount()):
                self.table.item(i, j).setBackground(colors[k])


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
