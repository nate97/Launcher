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
        cmd00 = 'set ttiUsername=' + self.user_name
        cmd01 = 'set ttiPassword=password'
        cmd02 = 'set TTI_PLAYCOOKIE=' + self.user_name
        cmd03 = 'set TTI_GAMESERVER=' + self.game_server
        cmd04 = 'cd src && ' + self.python_path + ' -m ' 'toontown.toonbase.ClientStart'

        subprocess.call(cmd00, shell=True)
        subprocess.call(cmd01, shell=True)
        subprocess.call(cmd02, shell=True)
        subprocess.call(cmd03, shell=True)
        subprocess.call(cmd04, shell=True)



