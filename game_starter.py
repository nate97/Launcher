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

        ### Game starting commands ###
        if CURRENT_PLATFORM == 'Linux':
            cmd_00 = 'export ttiUsername=' + self.uiCallback.uName + ' && export ttiPassword=' + self.uiCallback.pWord + ' && export TTI_GAMESERVER=' + GAME_SERVER + ' && cd src/ && ' + self.python_path + ' -O -m toontown.toonbase.ClientStart ' + cookie
        else:
            cmd_00 = 'set ttiUsername=' + self.uiCallback.uName + ' && set ttiPassword=' + self.uiCallback.pWord + ' && set TTI_GAMESERVER=' + GAME_SERVER + ' && cd "src" && ' + self.python_path + ' -O -m toontown.toonbase.ClientStart ' + cookie

        # Before we run the command lets set the username variables to null
        self.uiCallback.uName = False
        self.uiCallback.pWord = False
        cookie = False

        subprocess.call(cmd_00, shell=True)

        return



