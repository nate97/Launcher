from PyQt5 import QtCore, QtGui, QtWidgets
from launcher_interface import Ui_LauncherWindow
import sys

from launcher import Launcher
from launcher_globals import *


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_LauncherWindow()
        self.ui.setupUi(self)

        self.Launcher = Launcher()

        # So we can implement hooks to control the UI
        self.Launcher.setUICallback(app)

        # Give the launcher code our UI handle
        self.Launcher.setUi(self.ui)



        self.updatingUI()

        self.ui.pushButton.clicked.connect(self.Launcher.wantUpdates)

        #self.ui.launcher_state.setText(LAUNCHER_STATE_UPDATING)



    def defaultUI(self):
        self.ui.progress_bar.hide()
        self.ui.launcher_status.setText(LAUNCHER_STATUS_LOGIN)



    def updatingUI(self):
        self.ui.progress_bar.show()
        self.ui.launcher_state.setText(LAUNCHER_STATE_UPDATING)
        self.ui.launcher_status.setText('Updating...')
        self.ui.username_text.hide()
        self.ui.password_text.hide()
        self.ui.user_input.hide()
        self.ui.pass_input.hide()



def main():
    global app
    app = QtWidgets.QApplication(sys.argv)

    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()
