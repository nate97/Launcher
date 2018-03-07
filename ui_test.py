from PyQt5 import QtCore, QtGui, QtWidgets
from launcher_interface import Ui_LauncherWindow
import sys

from launcher import Launcher
from launcher_globals import *


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self, qApp):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_LauncherWindow()
        self.ui.setupUi(self)
        self.Launcher = Launcher()
    
        ### UI Globals ###
        self.counter = 0
        self.uName = False
        self.pWord = False
        # This is defined so that we can call back the UI from the main application
        self.APP = qApp

        # So we can implement hooks to control the UI
        self.Launcher.setUICallbacks(self)
        # Set the startup state of the UI
        self.setDefaultUI()
        # Attatch functions to buttons
        self.ui.pushButton.clicked.connect(self.setCredentials)



    def setCredentials(self):
        self.uName = self.ui.user_input.text()
        self.pWord = self.ui.pass_input.text()

        self.Launcher.checkCredentials()



    def setDefaultUI(self):
        self.ui.launcher_state.setText(LAUNCHER_STATE_WAITING)
        self.ui.launcher_status.setText(LAUNCHER_STATUS_LOGIN)
        self.ui.pushButton.setEnabled(True)
        self.ui.user_input.setDisabled(False)
        self.ui.pass_input.setDisabled(False)
        self.ui.user_input.setText('')
        self.ui.pass_input.setText('')
        self.ui.progress_bar.setValue(self.counter)
        self.ui.progress_bar.setMaximum(100)



    def setUpdateUI(self):
        self.ui.launcher_state.setText(LAUNCHER_STATE_UPDATING)
        self.ui.user_input.setDisabled(True)
        self.ui.pass_input.setDisabled(True)
        self.ui.pushButton.setEnabled(False)



    # Reset all of our local variables to zero and reset the UI
    def setFailedUI(self):
        self.setDefaultUI()
        self.counter = 0
        self.uName = False
        self.pWord = False
        self.ui.launcher_state.setText(LAUNCHER_STATE_WAITING)
        self.ui.launcher_status.setText(LAUNCHER_STATUS_FAILURE)
        self.ui.progress_bar.setValue(self.counter)
        self.ui.progress_bar.setMaximum(100)



    def enterCredentials(self):
        self.ui.launcher_status.setText(LAUNCHER_STATUS_GIVE_INPUT)



    def setProgressZero(self):
        self.counter = 0
        self.ui.progress_bar.setValue(self.counter)
        complete = len(self.Launcher.download_list)
        print (complete)
        self.ui.progress_bar.setMaximum(complete)



    def countProgress(self):
        print (self.counter)
        self.ui.progress_bar.setValue(self.counter)
        self.counter +1


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow(app)
    application.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
