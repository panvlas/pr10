import time
import sys

from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.timer1 = QTimer()
        loadUi('form.ui', self)
        self.setWindowTitle('Работа с таймерами Python')
        self.setWindowIcon(QtGui.QIcon('img/logo.png'))

        backgr = QPixmap('img/background.png')
        self.background.setPixmap(backgr)
        self.background.setScaledContents(True)

        pixmap_bus = QPixmap('img/bus2.png')
        self.bus.setPixmap(pixmap_bus)
        self.bus.setScaledContents(True)

        self.x = self.bus.pos().x()
        self.y = self.bus.pos().y()

        self.startBtn.clicked.connect(self.run)

    def run(self):
        if self.startLbl.value() >= self.stopLbl.value():
            self.startBtn.setStyleSheet("color: black;" "background-color: red;")
        else:
            self.startBtn.setEnabled(False)

            self.startBtn.setStyleSheet("color: black;" "background-color: none;")

            if self.startLbl.value() == 1:
                self.x = 100
                self.y = 30
                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus1.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.stopLbl.value() >= 1:
                    self.timer1 = QTimer()
                    self.timer1.timeout.connect(self.from_the_first_to_the_second)
                    self.timer1.start(5)

            # Начинаем движение со второй остановки
            elif self.startLbl.value() == 2:

                self.x = 40
                self.y = 230

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.stopLbl.value() >= 3:
                    self.timer2 = QTimer()
                    self.timer2.timeout.connect(self.from_the_second_to_the_third)
                    self.timer2.start(5)

            # Начинаем движение с третьй остановкие
            elif self.startLbl.value() == 3:

                self.x = 160
                self.y = 210

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.stopLbl.value() >= 4:
                    self.timer3 = QTimer()
                    self.timer3.timeout.connect(self.from_the_third_to_the_fourth)
                    self.timer3.start(5)

            # Начинаем движение с четвертой остановки
            elif self.startLbl.value() == 4:

                self.x = 210
                self.y = 430

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.stopLbl.value() >= 5:
                    self.timer4_1 = QTimer()
                    self.timer4_1.timeout.connect(self.from_the_fourth_to_the_fifth)
                    self.timer4_1.start(5)

            # Начинаем движение с пятой остановки
            elif self.startLbl.value() == 5:

                self.x = 230
                self.y = 150

                self.bus.setGeometry(self.x, self.y, 141, 71)

                pixmap_bus = QPixmap('img/bus.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.stopLbl.value() >= 6:
                    self.timer5_1 = QTimer()
                    self.timer5_1.timeout.connect(self.from_the_fifth_to_the_sixth)
                    self.timer5_1.start(5)

            # Начинаем движение с шестой остановки
            elif self.startLbl.value() == 6:

                self.x = 440
                self.y = 150

                self.bus.setGeometry(self.x, self.y, 71, 141)

                pixmap_bus = QPixmap('img/bus3.png')
                self.bus.setPixmap(pixmap_bus)
                self.bus.setScaledContents(True)

                if self.stopLbl.value() >= 7:
                    self.timer6 = QTimer()
                    self.timer6.timeout.connect(self.from_the_sixth_to_the_seventh)
                    self.timer6.start(5)

    # С первой до второй (лево)
    def from_the_first_to_the_second(self):
        self.startBtn.setEnabled(False)
        self.x -= 1
        self.bus.move(self.x, self.y)

        if self.x == 50:
            self.x -= 10

            self.bus.setGeometry(self.x, self.y, 71, 141)

            pixmap_bus = QPixmap('img/bus1.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer1.stop()

            self.timer2_1 = QTimer()
            self.timer2_1.timeout.connect(self.from_the_first_to_the_second_two)
            self.timer2_1.start(5)

    # С первой до второй (вниз)
    def from_the_first_to_the_second_two(self):
        self.startBtn.setEnabled(False)
        self.y += 1
        self.bus.move(self.x, self.y)

        if self.y == 200:
            self.y += 30
            self.bus.setGeometry(self.x, self.y, 141, 71)

            pixmap_bus = QPixmap('img/bus.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer2_1.stop()

            if self.stopLbl.value() >= 3:
                self.timer2 = QTimer()
                self.timer2.timeout.connect(self.from_the_second_to_the_third)
                self.timer2.start(5)
            else:
                # Делаем кнопку активной
                self.startBtn.setEnabled(True)

    # Со второй до третей (право)
    def from_the_second_to_the_third(self):
        self.startBtn.setEnabled(False)

        self.x += 1
        self.bus.move(self.x, self.y)

        if self.x == 140:

            self.x -= 30

            self.bus.setGeometry(self.x, self.y, 141, 71)

            pixmap_bus = QPixmap('img/bus.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer2.stop()

            self.timer3_1 = QTimer()
            self.timer3_1.timeout.connect(self.from_the_second_to_the_third_two)
            self.timer3_1.start(5)

    # со второй до третей (вниз)

    def from_the_second_to_the_third_two(self):
        self.startBtn.setEnabled(False)
        self.y += 1
        self.bus.move(self.x, self.y)
        if self.y == 290:
            self.y += 10
            self.x += 20
            self.bus.setGeometry(self.x, self.y, 71, 141)

            pixmap_bus = QPixmap('img/bus1.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer3_1.stop()
            if self.stopLbl.value() >= 4:
                self.timer3 = QTimer()
                self.timer3.timeout.connect(self.from_the_third_to_the_fourth)
                self.timer3.start(5)
            else:
                self.startBtn.setEnabled(True)

    # Движемся до четвертой (вниз)
    def from_the_third_to_the_fourth(self):
        self.startBtn.setEnabled(False)
        self.bus.move(self.x, self.y)
        self.y += 1

        if self.y == 400:
            self.y += 10
            self.timer3.stop()

            self.bus.setGeometry(self.x, self.y, 141, 71)

            pixmap_bus = QPixmap('img/bus.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer4_1 = QTimer()
            self.timer4_1.timeout.connect(self.from_the_third_to_the_fourth_two)
            self.timer4_1.start(5)


    # До четвертой (право)

    def from_the_third_to_the_fourth_two(self):
        self.startBtn.setEnabled(False)
        self.bus.move(self.x, self.y)
        self.x += 1

        if self.x == 200:
            self.y += 10
            self.timer4_1.stop()

            self.bus.setGeometry(self.x, self.y, 71, 141)

            pixmap_bus = QPixmap('img/bus3.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            if self.stopLbl.value() >= 5:
                self.timer4 = QTimer()
                self.timer4.timeout.connect(self.from_the_fourth_to_the_fifth)
                self.timer4.start(5)
            else:
                self.startBtn.setEnabled(True)

    # До пятой
    def from_the_fourth_to_the_fifth(self):
        self.startBtn.setEnabled(False)

        self.y -= 1
        self.bus.move(self.x, self.y)
        if self.y == 150:
            self.bus.setGeometry(self.x, self.y, 141, 71)

            pixmap_bus = QPixmap('img/bus.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)

            self.timer4.stop()
            if self.stopLbl.value() >= 6:
                self.timer4_2 = QTimer()
                self.timer4_2.timeout.connect(self.from_the_fifth_to_the_sixth)
                self.timer4_2.start(5)
            else:
                self.startBtn.setEnabled(True)

    # С пятой до шестой
    def from_the_fifth_to_the_sixth(self):
        self.startBtn.setEnabled(False)

        self.x += 1
        self.bus.move(self.x, self.y)

        if self.x == 420:
            self.x += 10
            self.bus.setGeometry(self.x, self.y, 71, 141)

            pixmap_bus = QPixmap('img/bus3.png')
            self.bus.setPixmap(pixmap_bus)
            self.bus.setScaledContents(True)
            self.timer4_2.stop()
            if self.stopLbl.value() == 7:
                self.timer6 = QTimer()
                self.timer6.timeout.connect(self.from_the_sixth_to_the_seventh)
                self.timer6.start(5)
            else:
                self.startBtn.setEnabled(True)

    def from_the_sixth_to_the_seventh(self):
        self.startBtn.setEnabled(False)

        self.y -= 1
        self.bus.move(self.x, self.y)

        if self.y == 30:
            self.bus.setGeometry(self.x, self.y, 71, 141)

            self.timer6.stop()
            self.startBtn.setEnabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())