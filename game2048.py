# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2048.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys

board=[[0 for w in range(4)] for h in range(4)]
score=0
NNl=[[0 for w in range(2)] for h in range(16)]
NNc=0

def game_newmap():
    global board
    i=0
    while i<2:
        x=random.randrange(0,4)
        y=random.randrange(0,4)
        v=random.randrange(0,2)
        if board[x][y]==0:
            i+=1
            if v==0: board[x][y]=2
            else: board[x][y]=4;
        else: continue

def game_blankchecker():
    global NNc
    global NNl
    NNc=0
    countn=0
    for i in range(4):
        for j in range(4):
            if board[i][j]==0:
                countn+=1
                NNl[NNc][0]=i
                NNl[NNc][1]=j
                NNc+=1
    return countn

def game_overcheck():
    if game_blankchecker()>0: return 0
    global board
    d=[[0 for w in range(2)] for h in range(4)]
    d[0][0]=-1
    d[0][1]=0
    d[1][0]=1
    d[1][1]=0
    d[2][0]=0
    d[2][1]=-1
    d[3][0]=0
    d[3][1]=1
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if i+d[k][0]<0 or i+d[k][0]>3: continue
                if j+d[k][1]<0 or j+d[k][1]>3: continue
                if board[i][j]==board[i+d[k][0]][j+d[k][1]]: return 0
    return 1

def gamechecker(game_over):
    if game_over and game_overcheck():
        ui.gameover()
    elif game_over==False:
        global NNl
        global NNc
        global board
        t=game_blankchecker()
        n=0
        if t==0: n=0
        elif t==1: n=1
        else: n=random.randrange(1,3)
        for i in range(n):
            p=random.randrange(0,NNc)
            x=NNl[p][0]
            y=NNl[p][1]
            if n==1:
                submin=999999
                if x+1<4 and submin>board[x+1][y]: submin=board[x+1][y]
                if x-1>0 and submin>board[x-1][y]: submin=board[x-1][y]
                if y+1<4 and submin>board[x][y+1]: submin=board[x][y+1]
                if y-1>0 and submin>board[x][y-1]: submin=board[x][y-1]
                board[x][y]=submin
            else:
                v=random.randrange(2)
                if v==0: board[x][y]=2
                else:board[x][y]=4
    #Next game displayboard
    ui.displayboard()

def btn_event_up():
    global board, score
    game_over=True
    for i in range(4):
        for j in range(3):
            if board[j][i]==0: continue
            for k in range(j+1,4):
                if board[k][i]==0: continue
                if board[j][i]==board[k][i]:
                    board[j][i]+=board[k][i]
                    score+=board[j][i]
                    board[k][i]=0
                    game_over=False
                    break
                if board[j][i]!=board[k][i]: break
        for j in range(3):
            if board[j][i]!=0: continue
            for k in range(j+1,4):
                if board[k][i]!=0:
                    board[j][i]=board[k][i]
                    board[k][i]=0
                    game_over=False
                    break
    gamechecker(game_over)

def btn_event_left():
    global board, score
    game_over=True
    for i in range(4):
        for j in range(3):
            if board[i][j]==0: continue
            for k in range(j+1,4):
                if board[i][k]==0: continue
                if board[i][j]==board[i][k]:
                    board[i][j]+=board[i][k]
                    score+=board[i][j]
                    board[i][k]=0
                    game_over=False
                    break
                if board[i][j]!=board[i][k]: break
        for j in range(3):
            if board[i][j]!=0:continue
            for k in range(j+1,4):
                if board[i][k]!=0:
                    board[i][j]=board[i][k]
                    board[i][k]=0
                    game_over=False
                    break
    gamechecker(game_over)

def btn_event_down():
    global board, score
    game_over=True
    for i in range(4):
        j=3
        while j>0:
            if board[j][i]==0:
                j-=1
                continue
            k=j-1
            while k>=0:
                if board[k][i]==0:
                    k-=1
                    continue
                if board[j][i]==board[k][i]:
                    board[j][i]+=board[k][i]
                    score+=board[j][i]
                    board[k][i]=0
                    game_over=False
                    break
                if board[j][i]!=board[k][i]: break
                k-=1
            j-=1
        j=3
        while j>0:
            if board[j][i]!=0:
                j-=1
                continue
            k=j-1
            while k>=0:
                if board[k][i]!=0:
                    board[j][i]=board[k][i]
                    board[k][i]=0
                    game_over=False
                    break
                k-=1
            j-=1
    gamechecker(game_over)

def btn_event_right():
    global board, score
    game_over=True
    for i in range(4):
        j=3
        while j>0:
            if board[i][j]==0:
                j-=1
                continue
            k=j-1
            while k>=0:
                if board[i][k]==0:
                    k-=1
                    continue
                if board[i][j]==board[i][k]:
                    board[i][j]+=board[i][k]
                    score+=board[i][j]
                    board[i][k]=0
                    game_over=False
                    break
                if board[i][j]!=board[i][k]: break
                k-=1
            j-=1
        j=3
        while j>0:
            if board[i][j]!=0:
                j-=1
                continue
            k=j-1
            while k>=0:
                if board[i][k]!=0:
                    board[i][j]=board[i][k]
                    board[i][k]=0
                    game_over=False
                    break
                k-=1
            j-=1
    gamechecker(game_over)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(181, 302)
        MainWindow.setMinimumSize(QtCore.QSize(181, 302))
        MainWindow.setMaximumSize(QtCore.QSize(181, 302))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_down = QtWidgets.QPushButton(self.centralwidget)
        self.btn_down.setGeometry(QtCore.QRect(70, 260, 41, 23))
        self.btn_down.setObjectName("btn_down")
        self.btn_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_up.setGeometry(QtCore.QRect(70, 220, 41, 23))
        self.btn_up.setObjectName("btn_up")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(30, 240, 41, 23))
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(110, 240, 41, 23))
        self.btn_right.setObjectName("btn_right")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 160, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.display_score = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.display_score.setObjectName("display_score")
        self.horizontalLayout_3.addWidget(self.display_score)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 50, 161, 161))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_1.setGeometry(QtCore.QRect(0, 0, 41, 41))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 0, 41, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 0, 41, 41))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_4.setGeometry(QtCore.QRect(120, 0, 41, 41))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 40, 41, 41))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_6.setGeometry(QtCore.QRect(40, 40, 41, 41))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_7.setGeometry(QtCore.QRect(80, 40, 41, 41))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_8.setGeometry(QtCore.QRect(120, 40, 41, 41))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_9.setGeometry(QtCore.QRect(0, 80, 41, 41))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_10.setGeometry(QtCore.QRect(40, 80, 41, 41))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_11.setGeometry(QtCore.QRect(80, 80, 41, 41))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_12.setGeometry(QtCore.QRect(120, 80, 41, 41))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_13.setGeometry(QtCore.QRect(0, 120, 41, 41))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_14.setGeometry(QtCore.QRect(40, 120, 41, 41))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_15.setGeometry(QtCore.QRect(80, 120, 41, 41))
        self.textBrowser_15.setObjectName("textBrowser_15")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.frame)
        self.textBrowser_16.setGeometry(QtCore.QRect(120, 120, 41, 41))
        self.textBrowser_16.setObjectName("textBrowser_16")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.btn_up.clicked.connect(btn_event_up)
        self.btn_left.clicked.connect(btn_event_left)
        self.btn_down.clicked.connect(btn_event_down)
        self.btn_right.clicked.connect(btn_event_right)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textBrowser_1, self.textBrowser_2)
        MainWindow.setTabOrder(self.textBrowser_2, self.textBrowser_3)
        MainWindow.setTabOrder(self.textBrowser_3, self.textBrowser_4)
        MainWindow.setTabOrder(self.textBrowser_4, self.textBrowser_5)
        MainWindow.setTabOrder(self.textBrowser_5, self.textBrowser_6)
        MainWindow.setTabOrder(self.textBrowser_6, self.textBrowser_7)
        MainWindow.setTabOrder(self.textBrowser_7, self.textBrowser_8)
        MainWindow.setTabOrder(self.textBrowser_8, self.textBrowser_9)
        MainWindow.setTabOrder(self.textBrowser_9, self.textBrowser_10)
        MainWindow.setTabOrder(self.textBrowser_10, self.textBrowser_11)
        MainWindow.setTabOrder(self.textBrowser_11, self.textBrowser_12)
        MainWindow.setTabOrder(self.textBrowser_12, self.textBrowser_13)
        MainWindow.setTabOrder(self.textBrowser_13, self.textBrowser_14)
        MainWindow.setTabOrder(self.textBrowser_14, self.textBrowser_15)
        MainWindow.setTabOrder(self.textBrowser_15, self.textBrowser_16)
        MainWindow.setTabOrder(self.textBrowser_16, self.btn_up)
        MainWindow.setTabOrder(self.btn_up, self.btn_left)
        MainWindow.setTabOrder(self.btn_left, self.btn_down)
        MainWindow.setTabOrder(self.btn_down, self.btn_right)

    def displayboard(self):
        global board
        self.display_score.setText(str(score))
        if board[0][0]!=0:self.textBrowser_1.setText(str(board[0][0]))
        else:self.textBrowser_1.setText(" ")
        if board[0][1]!=0:self.textBrowser_2.setText(str(board[0][1]))
        else:self.textBrowser_2.setText(" ")
        if board[0][2]!=0:self.textBrowser_3.setText(str(board[0][2]))
        else:self.textBrowser_3.setText(" ")
        if board[0][3]!=0:self.textBrowser_4.setText(str(board[0][3]))
        else:self.textBrowser_4.setText(" ")
        if board[1][0]!=0:self.textBrowser_5.setText(str(board[1][0]))
        else:self.textBrowser_5.setText(" ")
        if board[1][1]!=0:self.textBrowser_6.setText(str(board[1][1]))
        else:self.textBrowser_6.setText(" ")
        if board[1][2]!=0:self.textBrowser_7.setText(str(board[1][2]))
        else:self.textBrowser_7.setText(" ")
        if board[1][3]!=0:self.textBrowser_8.setText(str(board[1][3]))
        else:self.textBrowser_8.setText(" ")
        if board[2][0]!=0:self.textBrowser_9.setText(str(board[2][0]))
        else:self.textBrowser_9.setText(" ")
        if board[2][1]!=0:self.textBrowser_10.setText(str(board[2][1]))
        else:self.textBrowser_10.setText(" ")
        if board[2][2]!=0:self.textBrowser_11.setText(str(board[2][2]))
        else:self.textBrowser_11.setText(" ")
        if board[2][3]!=0:self.textBrowser_12.setText(str(board[2][3]))
        else:self.textBrowser_12.setText(" ")
        if board[3][0]!=0:self.textBrowser_13.setText(str(board[3][0]))
        else:self.textBrowser_13.setText(" ")
        if board[3][1]!=0:self.textBrowser_14.setText(str(board[3][1]))
        else:self.textBrowser_14.setText(" ")
        if board[3][2]!=0:self.textBrowser_15.setText(str(board[3][2]))
        else:self.textBrowser_15.setText(" ")
        if board[3][3]!=0:self.textBrowser_16.setText(str(board[3][3]))
        else:self.textBrowser_16.setText(" ")

    def gameover(self):
        sys.exit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Py2048"))
        self.btn_down.setText(_translate("MainWindow", "Down"))
        self.btn_up.setText(_translate("MainWindow", "Up"))
        self.btn_left.setText(_translate("MainWindow", "Left"))
        self.btn_right.setText(_translate("MainWindow", "Right"))
        self.label_3.setText(_translate("MainWindow", "Score"))
        self.display_score.setText(_translate("MainWindow", "0"))
        self.textBrowser_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_15.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_16.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.displayboard()

if __name__ == "__main__":
    game_newmap()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
