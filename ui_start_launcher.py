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
    
        ### Import UI Fonts ###
        self.fontDB = QtGui.QFontDatabase()
        self.fontDB.addApplicationFont(":/fonts/fonts/Anton-Regular.ttf")
        self.fontDB.addApplicationFont(":/fonts/fonts/BowlbyOneSC-Regular.ttf")

        ### Set special case fonts ###
        self.ui.launcher_state.setFont(QtGui.QFont("Anton", 14))
        self.ui.launcher_status.setFont(QtGui.QFont("Anton", 14))
        self.ui.pushButton.setFont(QtGui.QFont("BowlbyOneSC", 12))

        ### UI Globals ###
        self.counter = 0
        self.complete_progress = 0
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
        self.uName = str(self.ui.user_input.text())
        self.pWord = str(self.ui.pass_input.text())
        # Check to see if we have credentials
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
        self.complete_progress = 0
        self.uName = False
        self.pWord = False
        self.ui.launcher_state.setText(LAUNCHER_STATE_WAITING)
        self.ui.launcher_status.setText(LAUNCHER_STATUS_FAILURE)
        self.ui.progress_bar.setValue(self.counter)
        self.ui.progress_bar.setMaximum(100)


    def setEnterCredsUI(self):
        self.ui.launcher_status.setText(LAUNCHER_STATUS_GIVE_INPUT)


    def setInvalidUserPassUI(self):
        self.ui.launcher_status.setText(LAUNCHER_STATUS_INVALID_UP)


    def setProgressZero(self):
        self.counter = 0
        self.ui.progress_bar.setValue(self.counter)
        self.complete_progress = len(self.Launcher.download_list) + len(self.Launcher.unzip_list)
        self.ui.progress_bar.setMaximum(self.complete_progress )


    def countProgress(self):
        self.counter = self.counter +1
        self.ui.progress_bar.setValue(self.counter)


    def subtractProgressZIP(self):
        self.complete_progress = self.complete_progress -1
        self.ui.progress_bar.setMaximum(self.complete_progress)


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow(app)
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

