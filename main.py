import os
import sqlite3
import sys

from PyQt5.QtWidgets import *

from endVictorin import EndVictorin
from history import HistoryWindow
from mainWindow import MainWindow
from tecVictorin import TecVictorin
from victorins import Victorins

global mainWindow, historyWindow, tecVictorian, victorins, endVictorian

app = QApplication(sys.argv)

mainWindow = MainWindow()
historyWindow = HistoryWindow()
victorins = Victorins()
tecVictorian = TecVictorin()
endVictorian = EndVictorin()

mainWindow.setWindows(mainWindow, historyWindow, tecVictorian, victorins, endVictorian)
historyWindow.setWindows(mainWindow, historyWindow, tecVictorian, victorins, endVictorian)
victorins.setWindows(mainWindow, historyWindow, tecVictorian, victorins, endVictorian)
tecVictorian.setWindows(mainWindow, historyWindow, tecVictorian, victorins, endVictorian)
endVictorian.setWindows(mainWindow, historyWindow, tecVictorian, victorins, endVictorian)

mainWindow.show()
sys.exit(app.exec_())
