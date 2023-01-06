import sys

from PyQt5 import uic, QtCore, QtMultimedia
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        abs_path = '/Users/DEXP/PycharmProjects/yandex_lyceum/'
        self.players = {}
        self.keys = {self.a1: 'A', self.a_1: 'A#', self.b1: 'B', self.c1: 'C', self.c_1: 'C#', self.d1: 'D',
                     self.d_1: 'D#', self.e1: 'E', self.f1: 'F', self.f_1: 'F#', self.g1: 'G', self.g_1: 'G#'}
        self.load_media(abs_path)
        self.w1 = QPixmap('data/white1.png')
        self.w2 = QPixmap('data/white2.png')
        self.w3 = QPixmap('data/white3.png')
        self.b = QPixmap('data/black.png')
        self.w1_p = QPixmap('data/white1_p.png')
        self.w2_p = QPixmap('data/white2_p.png')
        self.w3_p = QPixmap('data/white3_p.png')
        self.b_p = QPixmap('data/black_p.png')
        for key in (self.c_1, self.d_1, self.f_1, self.g_1, self.a_1, self.c1, self.f1, self.d1, self.g1, self.a1,
                    self.e1, self.b1):
            self.release(key)
        self.mouse_pressed = False
        self.pressed = None

    def load_media(self, path):
        path += 'data/'
        keys = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        for key in keys:
            media = QtCore.QUrl.fromLocalFile(path + key + '.mp3')
            content = QtMultimedia.QMediaContent(media)
            self.players[key] = QtMultimedia.QMediaPlayer()
            self.players[key].setMedia(content)

    def press(self, key):
        self.players[self.keys.get(key)].stop()
        self.players[self.keys.get(key)].play()
        if key in (self.c1, self.f1):
            key.setPixmap(self.w1_p)
        if key in (self.d1, self.g1, self.a1):
            key.setPixmap(self.w2_p)
        if key in (self.e1, self.b1):
            key.setPixmap(self.w3_p)
        if key in (self.c_1, self.d_1, self.f_1, self.g_1, self.a_1):
            key.setPixmap(self.b_p)

    def release(self, key):
        # self.players[self.keys.get(key)].stop()
        if key in (self.c1, self.f1):
            key.setPixmap(self.w1)
        if key in (self.d1, self.g1, self.a1):
            key.setPixmap(self.w2)
        if key in (self.e1, self.b1):
            key.setPixmap(self.w3)
        if key in (self.c_1, self.d_1, self.f_1, self.g_1, self.a_1):
            key.setPixmap(self.b)

    def mousePressEvent(self, event):
        x, y = event.x(), event.y()
        for key in (self.c_1, self.d_1, self.f_1, self.g_1, self.a_1, self.c1, self.f1, self.d1, self.g1, self.a1,
                    self.e1, self.b1):
            x0, y0, w, h = key.x(), key.y(), key.width(), key.height()
            if x0 <= x <= x0 + w and y0 <= y <= y0 + h:
                self.mouse_pressed = True
                self.pressed = key
                self.press(key)
                break

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Z:
            self.press(self.c1)
        if event.key() == Qt.Key_S:
            self.press(self.c_1)
        if event.key() == Qt.Key_X:
            self.press(self.d1)
        if event.key() == Qt.Key_D:
            self.press(self.d_1)
        if event.key() == Qt.Key_C:
            self.press(self.e1)
        if event.key() == Qt.Key_V:
            self.press(self.f1)
        if event.key() == Qt.Key_G:
            self.press(self.f_1)
        if event.key() == Qt.Key_B:
            self.press(self.g1)
        if event.key() == Qt.Key_H:
            self.press(self.g_1)
        if event.key() == Qt.Key_N:
            self.press(self.a1)
        if event.key() == Qt.Key_J:
            self.press(self.a_1)
        if event.key() == Qt.Key_M:
            self.press(self.b1)

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Z:
            self.release(self.c1)
        if event.key() == Qt.Key_S:
            self.release(self.c_1)
        if event.key() == Qt.Key_X:
            self.release(self.d1)
        if event.key() == Qt.Key_D:
            self.release(self.d_1)
        if event.key() == Qt.Key_C:
            self.release(self.e1)
        if event.key() == Qt.Key_V:
            self.release(self.f1)
        if event.key() == Qt.Key_G:
            self.release(self.f_1)
        if event.key() == Qt.Key_B:
            self.release(self.g1)
        if event.key() == Qt.Key_H:
            self.release(self.g_1)
        if event.key() == Qt.Key_N:
            self.release(self.a1)
        if event.key() == Qt.Key_J:
            self.release(self.a_1)
        if event.key() == Qt.Key_M:
            self.release(self.b1)

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            x, y = event.x(), event.y()
            for key in (self.c_1, self.d_1, self.f_1, self.g_1, self.a_1, self.c1, self.f1, self.d1, self.g1, self.a1,
                        self.e1, self.b1):
                x0, y0, w, h = key.x(), key.y(), key.width(), key.height()
                if x0 <= x <= x0 + w and y0 <= y <= y0 + h:
                    if self.pressed != key:
                        released = self.pressed
                        self.release(released)
                        self.pressed = key
                        self.press(key)
                    break

    def mouseReleaseEvent(self, event):
        self.mouse_pressed = False
        self.release(self.pressed)
        self.pressed = None


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
