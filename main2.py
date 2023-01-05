import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.car1 = QPixmap('car1.png')
        self.car2 = QPixmap('car2.png')
        self.car.setPixmap(self.car1)
        self.setMouseTracking(True)
        self.state = False
        self.w, self.h = self.width(), self.height()

    def mouseMoveEvent(self, event):
        x, y = event.x(), event.y()
        if self.w - self.car1.width() >= x >= 0 <= y <= self.h - self.car1.height():
            self.car.move(x, y)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.state = not self.state
            if self.state:
                self.car.setPixmap(self.car2)
            else:
                self.car.setPixmap(self.car1)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
