import csv
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        self.w = None
        super().__init__()
        uic.loadUi('resurses/Uic_files/mainWindow.ui', self)
        self.btnPlay.clicked.connect(self.show_victorins)
        self.btnHistory.clicked.connect(self.show_history)
        self.btnAdd.clicked.connect(self.show_add)
        self.run()

    def run(self):
        pass

    def show_add(self):
        fileName = QFileDialog().getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.csv)")[0]
        if fileName == '':
            return
        with open(fileName, 'r', encoding='utf-8') as csvfile2:
            reader = csv.reader(csvfile2, delimiter=';')
            with open(f'victorins/{fileName.split("/")[-1]}', 'w', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"')
                writer.writerows(reader)



    def show_victorins(self):
        self.mainWindow.hide()
        self.victorins.show()

    def show_history(self):
        self.mainWindow.hide()
        self.historyWindow.show()
        self.historyWindow.set_result()

    def setWindows(self, mainWindow, historyWindow, tecVictorian, victorins, endVictorian):
        self.mainWindow = mainWindow
        self.historyWindow = historyWindow
        self.tecVictorian = tecVictorian
        self.victorins = victorins
        self.endVictorian = endVictorian
