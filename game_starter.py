import subprocess
import os
import unicodedata
from string import *

from launcher_globals import *



class GameStarter():

    def __init__(self):
        # Start game internal globals

        if CURRENT_PLATFORM == 'Linux':
            self.python_path = PYTHON_PATH
        else:
            self.python_path = '"'+ CURRENT_PATH + PYTHON_PATH + '"'



    def launchGame(self):
        # This still needs work but I guess this is slightly better
        cookie = (self.uiCallback.uName + self.uiCallback.pWord)

        cookie = cookie.rstrip()

        cmd_00 = (CMD_00 % (self.uiCallback.uName, self.uiCallback.pWord, cookie, GAME_SERVER, self.python_path))

        print (cmd_00)
        # Before we run the command lets set the username variables to null
        self.uiCallback.uName = False
        self.uiCallback.pWord = False

        subprocess.call(cmd_00, shell=True)

        return



