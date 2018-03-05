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
        # This still needs work but I guess this is slightly better
        cmd_00 = (CMD_00 % self.user_name)
        cmd_01 = (CMD_01)
        cmd_02 = (CMD_02 % self.user_name)
        cmd_03 = (CMD_03 % GAME_SERVER)
        cmd_04 = (CMD_04)
        cmd_05 = (CMD_05 % self.python_path)

        cmd_list = [cmd_00, cmd_01, cmd_02, cmd_03, cmd_05, cmd_05]

        for command in cmd_list:
            subprocess.call(command, shell=True)




