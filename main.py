import sys
import csv

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.load_schools()
        self.load_grades()
        self.btn_results.clicked.connect(self.display_results)
        self.cb_schools.currentIndexChanged.connect(self.load_grades)

    def load_schools(self):
        ans = []
        with open('rez.csv', 'r', encoding='utf8') as f:
            reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for d in reader:
                login = d['login']
                a = login.split('-')
                school = int(a[2])
                ans.append(school)
        ans = sorted(set(ans))
        self.cb_schools.clear()
        self.cb_schools.addItem('Все')
        for school in ans:
            self.cb_schools.addItem(str(school))

    def load_grades(self):
        ans = []
        school = self.cb_schools.currentText()
        selected_school = int(school) if school != 'Все' else school
        with open('rez.csv', 'r', encoding='utf8') as f:
            reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for d in reader:
                login = d['login']
                a = login.split('-')
                school, grade = map(int, (a[2], a[3]))
                if selected_school == school or selected_school == 'Все':
                    ans.append(grade)
        ans = sorted(set(ans))
        self.cb_grades.clear()
        self.cb_grades.addItem('Все')
        for grade in ans:
            self.cb_grades.addItem(str(grade))

    def display_results(self):
        school = self.cb_schools.currentText()
        selected_school = int(school) if school != 'Все' else school
        grade = self.cb_grades.currentText()
        selected_grade = int(grade) if grade != 'Все' else grade
        ans = []
        with open('rez.csv', 'r', encoding='utf8') as f:
            reader = csv.DictReader(f, delimiter=',', quotechar='"')
            for d in reader:
                name, login, score = d['user_name'], d['login'], d['Score']
                a = login.split('-')
                school, grade = map(int, (a[2], a[3]))
                if (school == selected_school or selected_school == 'Все') and \
                        (grade == selected_grade or selected_grade == 'Все'):
                    ans.append((name.split()[3], int(score)))
        ans.sort(key=lambda item: (item[1], item[0]), reverse=True)
        self.table_results.setRowCount(len(ans))
        for i, row in enumerate(ans):
            for j, col in enumerate(row):
                self.table_results.setItem(i, j, QTableWidgetItem(str(col)))
        self.table_results.resizeColumnsToContents()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
