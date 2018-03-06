# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'launcher_interface.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LauncherWindow(object):
    def setupUi(self, LauncherWindow):
        LauncherWindow.setObjectName("LauncherWindow")
        LauncherWindow.setEnabled(True)
        LauncherWindow.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LauncherWindow.sizePolicy().hasHeightForWidth())
        LauncherWindow.setSizePolicy(sizePolicy)
        LauncherWindow.setMinimumSize(QtCore.QSize(800, 500))
        LauncherWindow.setMaximumSize(QtCore.QSize(800, 500))
        LauncherWindow.setStyleSheet("background-image: url(:/images/images/toontown_bg.png);")
        self.centralwidget = QtWidgets.QWidget(LauncherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QFrame(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-10, 0, 821, 501))
        self.bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bg.setObjectName("bg")
        self.login = QtWidgets.QFrame(self.bg)
        self.login.setGeometry(QtCore.QRect(60, 50, 701, 391))
        self.login.setStyleSheet("background: #f9f9f9;\n"
"border-radius: 25;\n"
"border: 5px solid white;\n"
"padding: 5px;\n"
"")
        self.login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.login.setLineWidth(0)
        self.login.setObjectName("login")
        self.pass_input = QtWidgets.QLineEdit(self.login)
        self.pass_input.setGeometry(QtCore.QRect(50, 130, 171, 27))
        self.pass_input.setStyleSheet("background: white;\n"
"border-radius: 5;\n"
"border: 1px solid grey;\n"
"padding: 0px;\n"
"font: 12pt \"Arial\";")
        self.pass_input.setFrame(False)
        self.pass_input.setObjectName("pass_input")
        self.user_input = QtWidgets.QLineEdit(self.login)
        self.user_input.setGeometry(QtCore.QRect(50, 80, 171, 27))
        self.user_input.setStyleSheet("background: white;\n"
"border-radius: 5;\n"
"border: 1px solid grey;\n"
"padding: 0px;\n"
"font: 12pt \"Arial\";")
        self.user_input.setText("")
        self.user_input.setFrame(False)
        self.user_input.setObjectName("user_input")
        self.launcher_state = QtWidgets.QLabel(self.login)
        self.launcher_state.setGeometry(QtCore.QRect(60, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Anton")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.launcher_state.setFont(font)
        self.launcher_state.setStyleSheet("border-radius: 5;\n"
"border: 0px solid #ffffff;\n"
"padding: 0px;\n"
"font: 14pt \"Anton\";")
        self.launcher_state.setObjectName("launcher_state")
        self.launcher_status = QtWidgets.QLabel(self.login)
        self.launcher_status.setGeometry(QtCore.QRect(60, 280, 621, 31))
        self.launcher_status.setStyleSheet("border-radius: 0;\n"
"border: 0px solid #ffffff;\n"
"padding: 0px;\n"
"font: 14pt \"Anton\";")
        self.launcher_status.setObjectName("launcher_status")
        self.progress_bar = QtWidgets.QProgressBar(self.login)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setGeometry(QtCore.QRect(50, 320, 631, 31))
        self.progress_bar.setAutoFillBackground(False)
        self.progress_bar.setStyleSheet("QProgressBar:horizontal {\n"
"border-radius: 5;\n"
"border: 1px solid grey;\n"
"padding: 0px;\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk:horizontal {\n"
"background: #0a496d;\n"
"}")
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setInvertedAppearance(False)
        self.progress_bar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progress_bar.setObjectName("progress_bar")
        self.pushButton = QtWidgets.QPushButton(self.login)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(50, 180, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bowlby One SC")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton { \n"
"    color: white;\n"
"    background: #cc3018;\n"
"    border-radius: 5;\n"
"    border: 1px solid grey;\n"
"    padding: 0px;\n"
"    font: 12pt \"Bowlby One SC\";\n"
"}\n"
"\n"
"QPushButton:hover { \n"
"    background: #dd3d23;\n"
"}")
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.LOGO = QtWidgets.QLabel(self.login)
        self.LOGO.setGeometry(QtCore.QRect(390, 60, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.LOGO.setFont(font)
        self.LOGO.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LOGO.setStyleSheet("border-radius: 5;\n"
"border: 0px solid #ffffff;\n"
"padding: 0px;")
        self.LOGO.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGO.setWordWrap(True)
        self.LOGO.setObjectName("LOGO")
        LauncherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LauncherWindow)
        QtCore.QMetaObject.connectSlotsByName(LauncherWindow)

    def retranslateUi(self, LauncherWindow):
        _translate = QtCore.QCoreApplication.translate
        LauncherWindow.setWindowTitle(_translate("LauncherWindow", "Launcher"))
        self.pass_input.setPlaceholderText(_translate("LauncherWindow", "password"))
        self.user_input.setPlaceholderText(_translate("LauncherWindow", "username"))
        self.launcher_state.setText(_translate("LauncherWindow", "Login"))
        self.launcher_status.setText(_translate("LauncherWindow", "Launcher status"))
        self.progress_bar.setFormat(_translate("LauncherWindow", "%p%"))
        self.pushButton.setText(_translate("LauncherWindow", "Play Now!"))
        self.LOGO.setText(_translate("LauncherWindow", "Toontown Test"))

import launcher_resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LauncherWindow = QtWidgets.QMainWindow()
    ui = Ui_LauncherWindow()
    ui.setupUi(LauncherWindow)
    LauncherWindow.show()
    sys.exit(app.exec_())

