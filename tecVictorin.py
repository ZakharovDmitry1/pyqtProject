import csv
import time
from pprint import pprint

from PyQt5 import uic
from PyQt5.QtWidgets import *

from mainWindow import MainWindow


class TecVictorin(QDialog):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.listVictorin = []
        self.sum = 0
        uic.loadUi('resurses/Uic_files/tecVictorin.ui', self)
        self.btnNext.clicked.connect(self.setTextVidgets)
        self.run()

    def run(self):
        pass

    def fillList(self, name):
        with open('victorins/' + name + '.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            for i in reader:
                self.listVictorin.append(i)
        pprint(self.listVictorin)

    def setTextVidgets(self):
        self.start_time = time.time()
        if self.count == self.listVictorin.__len__():
            self.endVictorian.set_res(self.sum, len(self.listVictorin))
            self.go_to_endWindow()
            self.btnNext.setText("Далее")
            return
        self.label.setText(self.listVictorin[self.count][0])
        self.rad1.setText(self.listVictorin[self.count][1].replace('+ ', ''))
        self.rad2.setText(self.listVictorin[self.count][2].replace('+ ', ''))
        self.rad3.setText(self.listVictorin[self.count][3].replace('+ ', ''))
        n = QRadioButton()
        if self.count == 6:
            q = 0
        if self.rad1.isChecked() and self.listVictorin[self.count][1].find('+ ') != -1:
            self.sum += 1
        elif self.rad2.isChecked() and self.listVictorin[self.count][2].find('+ ') != -1:
            self.sum += 1
        elif self.rad3.isChecked() and self.listVictorin[self.count][3].find('+ ') != -1:
            self.sum += 1
        self.count += 1
        if self.count == self.listVictorin.__len__():
            self.btnNext.setText("Завершить викторину")

    def go_to_endWindow(self):
        self.tecVictorian.hide()
        self.endVictorian.show()
        #self.endVictorian.setRes()


    def play(self):
        ...

    def setVictorin(self, victorin: str):
        self.sum = 0
        self.count = 0
        self.listVictorin = []
        self.victorin = victorin
        self.fillList(victorin)
        self.setTextVidgets()
        self.play()

    def setWindows(self, mainWindow, historyWindow, tecVictorian, victorins, endVictorian):
        self.mainWindow = mainWindow
        self.historyWindow = historyWindow
        self.tecVictorian = tecVictorian
        self.victorins = victorins
        self.endVictorian = endVictorian
