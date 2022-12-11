import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import *


class HistoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.w = None
        self.historyList = []
        self.result = []
        uic.loadUi('resurses/Uic_files/history.ui', self)
        self.run()
        self.btnBack.clicked.connect(self.show_main_window)
        self.btnClear.clicked.connect(self.clear_db)

    def clear_db(self):
        con = sqlite3.connect("MyDB.db")
        cur = con.cursor()
        cur.execute(
            f"""DELETE FROM history""")
        con.commit()
        con.close()
        self.set_result()

    def run(self):
        pass

    def set_result(self):
        con = sqlite3.connect("MyDB.db")
        cur = con.cursor()
        result = cur.execute(
            f"""SELECT * FROM history""").fetchall()
        con.close()
        n = QTableWidget()
        self.tableWidget.setRowCount(result.__len__())
        x = 0
        for q, w, e, r, t in result:
            self.tableWidget.setItem(x, 0, QTableWidgetItem(str(w)))
            self.tableWidget.setItem(x, 1, QTableWidgetItem(str(e)))
            self.tableWidget.setItem(x, 2, QTableWidgetItem(str(r)))
            self.tableWidget.setItem(x, 3, QTableWidgetItem(str(t)))
            x += 1

        print(result)


    def show_main_window(self):
        self.historyWindow.hide()
        self.mainWindow.show()

    def setWindows(self, mainWindow, historyWindow, tecVictorian, victorins, endVictorian):
        self.mainWindow = mainWindow
        self.historyWindow = historyWindow
        self.tecVictorian = tecVictorian
        self.victorins = victorins
        self.endVictorian = endVictorian


