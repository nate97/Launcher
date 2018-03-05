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
        self.centralwidget = QtWidgets.QWidget(LauncherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QFrame(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(439, 130, 311, 201))
        self.login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login.setFrameShadow(QtWidgets.QFrame.Plain)
        self.login.setObjectName("login")
        self.username_text = QtWidgets.QLabel(self.login)
        self.username_text.setGeometry(QtCore.QRect(30, 50, 81, 19))
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLabel(self.login)
        self.password_text.setGeometry(QtCore.QRect(30, 100, 81, 19))
        self.password_text.setObjectName("password_text")
        self.pass_input = QtWidgets.QLineEdit(self.login)
        self.pass_input.setGeometry(QtCore.QRect(120, 100, 171, 27))
        self.pass_input.setObjectName("pass_input")
        self.user_input = QtWidgets.QLineEdit(self.login)
        self.user_input.setGeometry(QtCore.QRect(120, 50, 171, 27))
        self.user_input.setObjectName("user_input")
        self.launcher_state = QtWidgets.QLabel(self.login)
        self.launcher_state.setGeometry(QtCore.QRect(20, 10, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.launcher_state.setFont(font)
        self.launcher_state.setObjectName("launcher_state")
        self.launcher_status = QtWidgets.QLabel(self.login)
        self.launcher_status.setGeometry(QtCore.QRect(20, 170, 271, 21))
        self.launcher_status.setObjectName("launcher_status")
        self.progress_bar = QtWidgets.QProgressBar(self.login)
        self.progress_bar.setEnabled(True)
        self.progress_bar.setGeometry(QtCore.QRect(20, 80, 271, 23))
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.pushButton = QtWidgets.QPushButton(self.login)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 91, 27))
        self.pushButton.setObjectName("pushButton")
        self.news = QtWidgets.QLabel(self.centralwidget)
        self.news.setGeometry(QtCore.QRect(50, 20, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.news.setFont(font)
        self.news.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.news.setStyleSheet("")
        self.news.setAlignment(QtCore.Qt.AlignCenter)
        self.news.setWordWrap(True)
        self.news.setObjectName("news")
        self.news_2 = QtWidgets.QLabel(self.centralwidget)
        self.news_2.setGeometry(QtCore.QRect(460, 20, 281, 91))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.news_2.setFont(font)
        self.news_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.news_2.setStyleSheet("")
        self.news_2.setAlignment(QtCore.Qt.AlignCenter)
        self.news_2.setWordWrap(True)
        self.news_2.setObjectName("news_2")
        LauncherWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LauncherWindow)
        QtCore.QMetaObject.connectSlotsByName(LauncherWindow)

    def retranslateUi(self, LauncherWindow):
        _translate = QtCore.QCoreApplication.translate
        LauncherWindow.setWindowTitle(_translate("LauncherWindow", "Launcher"))
        self.username_text.setText(_translate("LauncherWindow", "Username:"))
        self.password_text.setText(_translate("LauncherWindow", "Password:"))
        self.launcher_state.setText(_translate("LauncherWindow", "Login"))
        self.launcher_status.setText(_translate("LauncherWindow", "Launcher status"))
        self.pushButton.setText(_translate("LauncherWindow", "Play"))
        self.news.setText(_translate("LauncherWindow", "News"))
        self.news_2.setText(_translate("LauncherWindow", "Launcher"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LauncherWindow = QtWidgets.QMainWindow()
    ui = Ui_LauncherWindow()
    ui.setupUi(LauncherWindow)
    LauncherWindow.show()
    sys.exit(app.exec_())

