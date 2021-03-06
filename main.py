# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import QImage, QPainter, QPixmap, QPalette
from PyQt5.QtWidgets import (QApplication, QMainWindow, QMenuBar, QMenu, QAction,
                             QFileDialog, QMessageBox, QLabel, QScrollArea, QSizePolicy)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter

import random
import time
from _thread import start_new_thread
import threading

from game.run import GamblingContext, PlayerState

threadLock = threading.Lock()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(950, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.roundlabel = QtWidgets.QLabel(self.centralwidget)
        self.roundlabel.setGeometry(QtCore.QRect(30, 0, 131, 61))
        self.roundlabel.setObjectName("roundlabel")
        self.declarebutton = QtWidgets.QPushButton(self.centralwidget)
        self.declarebutton.setGeometry(QtCore.QRect(630, 500, 90, 61))
        self.declarebutton.setObjectName("declarebutton")
        self.passbutton = QtWidgets.QPushButton(self.centralwidget)
        self.passbutton.setGeometry(QtCore.QRect(740, 500, 90, 61))
        self.passbutton.setObjectName("passbutton")
        self.declaredsum = QtWidgets.QLabel(self.centralwidget)
        self.declaredsum.setGeometry(QtCore.QRect(480, 40, 231, 41))
        self.declaredsum.setObjectName("declaredsum")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(450, 110, 351, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 410, 331, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.playername3 = QtWidgets.QLabel(self.groupBox_3)
        self.playername3.setGeometry(QtCore.QRect(40, 10, 101, 41))
        self.playername3.setObjectName("playername3")
        self.declare_label3 = QtWidgets.QLabel(self.groupBox_3)
        self.declare_label3.setGeometry(QtCore.QRect(20, 60, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.declare_label3.setFont(font)
        self.declare_label3.setObjectName("label_3")
        self.playerstate3 = QtWidgets.QLabel(self.groupBox_3)
        self.playerstate3.setGeometry(QtCore.QRect(210, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playerstate3.setFont(font)
        self.playerstate3.setObjectName("playerstate3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 220, 331, 161))
        self.groupBox_2.setObjectName("groupBox_2")
        self.playername2 = QtWidgets.QLabel(self.groupBox_2)
        self.playername2.setGeometry(QtCore.QRect(40, 10, 101, 41))
        self.playername2.setObjectName("playername2")
        self.declare_label2 = QtWidgets.QLabel(self.groupBox_2)
        self.declare_label2.setGeometry(QtCore.QRect(20, 60, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.declare_label2.setFont(font)
        self.declare_label2.setObjectName("label_2")
        self.playerstate2 = QtWidgets.QLabel(self.groupBox_2)
        self.playerstate2.setGeometry(QtCore.QRect(210, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playerstate2.setFont(font)
        self.playerstate2.setObjectName("playerstate2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 331, 141))
        self.groupBox.setObjectName("groupBox")
        self.playername1 = QtWidgets.QLabel(self.groupBox)
        self.playername1.setGeometry(QtCore.QRect(40, 10, 101, 41))
        self.playername1.setObjectName("playername1")
        self.declare_label1 = QtWidgets.QLabel(self.groupBox)
        self.declare_label1.setGeometry(QtCore.QRect(20, 60, 180, 51))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.declare_label1.setFont(font)
        self.declare_label1.setObjectName("label")
        self.playerstate1 = QtWidgets.QLabel(self.groupBox)
        self.playerstate1.setGeometry(QtCore.QRect(210, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playerstate1.setFont(font)
        self.playerstate1.setObjectName("playerstate1")
        self.restart_button = QtWidgets.QPushButton(self.centralwidget)
        self.restart_button.setGeometry(QtCore.QRect(680, 40, 191, 41))
        self.restart_button.setObjectName("restart_button")
        self.valuetext = QtWidgets.QTextEdit(self.centralwidget)
        self.valuetext.setGeometry(QtCore.QRect(450, 500, 171, 61))
        self.valuetext.setObjectName("valuetext")

        self.review_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.review_groupBox.setGeometry(QtCore.QRect(30, 600, 800, 150))
        self.review_groupBox.setObjectName("review_groupBox")
        self.review_label = QtWidgets.QLabel(self.review_groupBox)
        self.review_label.setGeometry(QtCore.QRect(20, 30, 180, 51))
        self.review_label.setFont(font)
        self.review_label.setObjectName("review_label")

        self.imagebox = QLabel()
        self.imagebox.setGeometry(500, 1000, 300, 300)
        self.imagebox.setScaledContents(True)
        self.verticalLayout.addWidget(self.imagebox)
        self.declarebutton.clicked.connect(self.click_declare)
        self.restart_button.clicked.connect(self.click_restart)
        self.passbutton.clicked.connect(self.click_pass)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.roundlabel.setText(_translate("MainWindow", "TextLabel"))
        self.declarebutton.setText(_translate("MainWindow", "Declare"))
        self.passbutton.setText(_translate("MainWindow", "Pass"))
        self.declaredsum.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.playername3.setText(_translate("MainWindow", "????????????"))
        self.declare_label3.setText(_translate("MainWindow", "Declared Number:"))
        self.playerstate3.setText(_translate("MainWindow", "State"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.playername2.setText(_translate("MainWindow", "????????????"))
        self.declare_label2.setText(_translate("MainWindow", "Declared Number:"))
        self.review_label.setText(_translate("MainWindow", "Game review: "))
        self.playerstate2.setText(_translate("MainWindow", "State"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.playername1.setText(_translate("MainWindow", "????????????"))
        self.declare_label1.setText(_translate("MainWindow", "Declared Number:"))
        self.playerstate1.setText(_translate("MainWindow", "State"))
        self.restart_button.setText(_translate("MainWindow", "Restart"))

    def click_declare(self):
        self.decided = True
        self.human_declared_value = int(self.valuetext.toPlainText())
        self.valuetext.setText("")
        self.run_game(True)

    def click_pass(self):
        self.decided = True
        self.human_declared_value = -1
        self.run_game(True)

    def run_game(self, is_continue = False):
        if is_continue:
            i = self.current_index
            self.current_index = 0
            self.context.player_declare(i)
        else:
            for i in range(self.current_index, len(self.players)):
                if self.context.is_waiting() or self.context.is_running():
                    player = self.players[i]
                    card_value = self.context.get_card(i)
                    if isinstance(player, HumanPlayer):
                        self.show_card(card_value)
                        if is_continue:
                            self.current_index = 0
                            self.context.player_declare(i)
                        else:
                            self.current_index = i
                            return
                    else:
                        self.context.player_declare(i)
                    self.act_callback(player)
                    self.declaredsum.setText("Declared sum: %d" % (self.context.declare_sum))
                else:
                    break

        if not self.context.is_waiting() and not self.context.is_running():
            self.context.next_round()
            for i in range(len(self.players)):
                player = self.players[i]
                if i == 0:
                    self.playerstate1.setText("Winner" if player.win else "Loser")
                if i == 1:
                    self.playerstate2.setText("Winner" if player.win else "Loser")
                if i == 2:
                    self.playerstate3.setText("Winner" if player.win else "Loser")
            return

        self.context.next_round()
        self.roundlabel.setText("Round: %d"%self.context.round_num)
        self.run_game(False)

    def click_restart(self):
        self.context.restart()
        self.decided = False
        self.current_index = 0
        self.roundlabel.setText("Round: 1")
        self.run_game(False)

    def act_callback(self, player):
        for i in range(len(self.players)):
            if player.name == self.players[i].name:
                if i == 0:
                    self.playerstate1.setText(str(player.state).split('.')[-1])
                    self.declare_label1.setText("Declared Number: " + str(player.declared_value)
                                                if player.declared_value > 0
                                                else "Declared Number: --------")
                elif i == 1:
                    self.playerstate2.setText(str(player.state).split('.')[-1])
                    self.declare_label2.setText("Declared Number: " + str(player.declared_value)
                                                if player.declared_value > 0
                                                else "Declared Number: --------")
                elif i == 2:
                    self.playerstate3.setText(str(player.state).split('.')[-1])
                    self.declare_label3.setText("Declared Number: " + str(player.declared_value)
                                                if player.declared_value > 0
                                                else "Declared Number: --------")
    def show_card(self, card_value):
        image = QPixmap("./game/assets/pukeImage/%d(%d).jpg"%(card_value, random.randint(1,4)))
        self.imagebox.setPixmap(image)
        # self.imagebox.show()
        # time.sleep(1.5)

    def human_callback(self):
        return self.human_declared_value

    def init_context(self, players):
        self.players = players
        self.context = GamblingContext(self.players)
        self.playername1.setText(players[0].name)
        self.playername2.setText(players[1].name)
        self.playername3.setText(players[2].name)
        self.playerstate1.setText(str(players[0].state).split('.')[-1])
        self.playerstate2.setText(str(players[1].state).split('.')[-1])
        self.playerstate3.setText(str(players[2].state).split('.')[-1])
        self.roundlabel.setText(str(self.context.round_num))
        self.declaredsum.setText("Declared sum: %d"%(self.context.declare_sum))

        self.decided = False # a flag used to see if the human player has manipulated in a round
        self.human_declared_value = 0
        self.current_index = 0

class HumanPlayerThread (threading.Thread):
    def __init__(self, threadID, name, ui, player):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.ui = ui
        self.human_player = player

        self.__flag = threading.Event()  # ???????????????????????????
        self.__flag.set()  # ?????????True
        self.__running = threading.Event()  # ???????????????????????????
        self.__running.set()  # ???running?????????True

    def run(self):
       # ???????????????????????????????????????True
       # ?????????timeout????????????????????????????????????????????????
       # ????????????????????????False
        threadLock.acquire()
        self.pause()
        self.__flag.wait()
        for i in range(len(self.ui.players)):
            if self.human_player.name == self.ui.players[i].name:
                if i == 0:
                    self.ui.playerstate1.setText(self.human_player.state)
                    self.ui.declare_label1.setText("Declared Number: %d" % (self.ui.human_declared_value)
                                                if self.ui.human_declared_value > 0
                                                else "Declared Number: ---")
                elif i == 1:
                    self.ui.playerstate2.setText(self.human_player.state)
                    self.ui.declare_label2.setText("Declared Number: %d" % (self.ui.human_declared_value)
                                                if self.ui.human_declared_value > 0
                                                else "Declared Number: ---")
                elif i == 2:
                    self.ui.playerstate3.setText(self.human_player.state)
                    self.ui.declare_label3.setText("Declared Number: %d" % (self.ui.human_declared_value)
                                                if self.ui.human_declared_value > 0
                                                else "Declared Number: ---")
        self.ui.decided = False
        # ?????????
        threadLock.release()

    def pause(self):
        self.__flag.clear()     # ?????????False, ???????????????

    def resume(self):
        self.__flag.set()    # ?????????True, ?????????????????????

    def stop(self):
        self.__flag.set()       # ??????????????????????????????, ????????????????????????
        self.__running.clear()        # ?????????False

from game.players.random_bot import RandomBot
from game.players.human import HumanPlayer

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    players = [RandomBot("RandomBot1"),
               RandomBot("RandomBot2"),
               HumanPlayer("You", ui.human_callback)]
    ui.init_context(players)

    MainWindow.show()
    sys.exit(app.exec_())