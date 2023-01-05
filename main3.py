import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setMouseTracking(True)
        self.w, self.h = self.width() - self.btn.width(), self.height() - self.btn.height()

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        x0, y0 = self.btn.x(), self.btn.y()
        x1, y1 = x0 + self.btn.width(), y0 + self.btn.height()
        if x0 <= x <= x1 and y0 <= y <= y1:
            self.move_btn(x, y)

    def move_btn(self, x, y):
        correct = False
        w, h = self.btn.width(), self.btn.height()
        while not correct:
            x0, y0 = randint(0, 500 - w), randint(0, 500 - h)
            if not (x0 <= x <= x0 + w and y0 <= y <= y0 + h):
                correct = True
        self.btn.move(x0, y0)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
