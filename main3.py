import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.ufo_pixmap = QPixmap('ufo.png')
        self.ufo.setPixmap(self.ufo_pixmap)
        self.w, self.h = self.width() - self.ufo_pixmap.width(), self.height() - self.ufo_pixmap.height()

    def keyPressEvent(self, event):
        x, y = self.ufo.x(), self.ufo.y()
        if event.key() == Qt.Key_Up:
            y -= 10
        if event.key() == Qt.Key_Down:
            y += 10
        if event.key() == Qt.Key_Left:
            x -= 10
        if event.key() == Qt.Key_Right:
            x += 10
        x %= self.w
        y %= self.h
        self.ufo.move(x, y)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
