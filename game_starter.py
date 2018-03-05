import subprocess
import os

from launcher_globals import *



class GameStarter():

    def __init__(self):
        # Start game internal globals
        self.user_name = ''
        self.python_path = CURRENT_PATH + PYTHON_PATH



    # Ask for username
    def getUsername(self):
        print ('Enter username: ')
        self.user_name = ''



    def launchGame(self):
        # We should really have some type of iterator for this shit
        subprocess.call(CMD_00, shell=True)
        subprocess.call(CMD_01, shell=True)
        subprocess.call(CMD_02, shell=True)
        subprocess.call(CMD_03, shell=True)
        subprocess.call(CMD_04, shell=True)
        subprocess.call(CMD_05, shell=True)



