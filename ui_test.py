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


        # Give the launcher a hook so it can update the interface    
        self.Launcher.setApp(qApp)
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
        self.ui.progress_bar.hide()
        self.ui.launcher_state.setText(LAUNCHER_STATE_WAITING)
        self.ui.launcher_status.setText(LAUNCHER_STATUS_LOGIN)
        self.ui.pushButton.setEnabled(True)
        self.ui.username_text.show()
        self.ui.password_text.show()
        self.ui.user_input.show()
        self.ui.pass_input.show()



    def setUpdateUI(self):
        self.ui.progress_bar.show()
        self.ui.launcher_state.setText(LAUNCHER_STATE_UPDATING)
        self.ui.launcher_status.setText('Updating...')
        self.ui.username_text.hide()
        self.ui.password_text.hide()
        self.ui.user_input.hide()
        self.ui.pass_input.hide()
        self.ui.pushButton.setEnabled(False)



    # Reset all of our local variables to zero and reset the UI
    def setFailedUI(self):
        self.setDefaultUI()
        self.ui.launcher_state.setText(LAUNCHER_STATE_FAILURE)
        self.counter = 0
        self.uName = False
        self.pWord = False



    def enterCredentials(self):
        self.ui.launcher_status.setText(LAUNCHER_STATUS_GIVE_INPUT)



    def setProgressZero(self):
        self.counter = 0
        self.ui.progress_bar.setValue(self.counter)
        complete = len(self.Launcher.download_list)
        self.ui.progress_bar.setMaximum(complete)



    def countProgress(self):
        self.counter +1
        self.ui.progress_bar.setValue(self.counter)



def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow(app)
    application.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
