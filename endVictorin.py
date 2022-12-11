import sqlite3
import time

from PyQt5 import uic
from PyQt5.QtWidgets import *

from mainWindow import MainWindow


class EndVictorin(QDialog):
    def __init__(self):
        super().__init__()
        self.w = None
        uic.loadUi('resurses/Uic_files/endVictorin.ui', self)
        self.btnEnd.clicked.connect(self.show_main_window)
        self.run()
        self.e = 0

    def run(self):
        pass

    def show_main_window(self):
        self.endVictorian.hide()
        self.mainWindow.show()

    def setWindows(self, mainWindow, historyWindow, tecVictorian, victorins, endVictorian):
        self.mainWindow = mainWindow
        self.historyWindow = historyWindow
        self.tecVictorian = tecVictorian
        self.victorins = victorins
        self.endVictorian = endVictorian

    def set_name(self, name):
        self.name = name

    def set_res(self, sum: int, chisl: int):
        self.label_2.setText(f'Вы ответили правильно на {sum} вопросов из {chisl}!!!')
        t = int(sum / chisl * 100)
        self.e += 1
        con = sqlite3.connect("MyDB.db")
        cur = con.cursor()
        print(self.name)
        print(time.time() - self.tecVictorian.start_time)
        cur.execute(
            f"""INSERT INTO history(name, correct_answers, number_of_correct_answers, percent) VALUES ("{self.name}", {sum},{chisl},{t})""")
        con.commit()
        con.close()
