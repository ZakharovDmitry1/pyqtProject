import os

from PyQt5 import uic
from PyQt5.QtWidgets import *


class Victorins(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('resurses/Uic_files/victorins.ui', self)
        self.array = []
        self.run()

    def run(self):
        self.listWidget.clear()
        self.files = os.listdir(path=r"victorins")
        self.listWidget.itemDoubleClicked.connect(self.go_to_victorin)
        for i in range(len(self.files)):
            self.listWidget.addItem(self.files[i].split('.')[0])

    def go_to_victorin(self, lstItem):
        print(s := self.listWidget.currentItem().text())
        self.endVictorian.set_name(s)
        self.victorins.hide()
        self.tecVictorian.show()
        self.tecVictorian.setVictorin(s)



    def setWindows(self, mainWindow, historyWindow, tecVictorian, victorins, endVictorian):
        self.mainWindow = mainWindow
        self.historyWindow = historyWindow
        self.tecVictorian = tecVictorian
        self.victorins = victorins
        self.endVictorian = endVictorian
