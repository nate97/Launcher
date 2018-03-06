import platform
import os



### DEBUG VARIABLE ###

TESTING_NF = True
LOCAL_GAME = True

CURRENT_PLATFORM = platform.system()
CURRENT_PATH = os.getcwd()

if TESTING_NF:
    print ('Host operating system: ' + CURRENT_PLATFORM)



####################################
########## For the parser ##########
####################################

### DEBUGGING PURPOSES FOR LOCAL AND REMOTE FILE NAMES ###
if LOCAL_GAME:
    RESOURCE_FILE = 'local_file_links.txt'
    RESOURCE_LINK = 'http://10.0.0.29/index.php/s/YEpPZvza2jfISz1/download'
else:
    RESOURCE_FILE = 'remote_file_links.txt'
    RESOURCE_LINK = 'https://cloud.com/file1.txt'

### PARSE VARIABLES ###
VALID_LINE = 'link'
DILIMETER = ' | '
OCCURENCE = 5

### FILE TYPE VARIABLES ###
ZIPPED_FILE = 'archive'
NORMAL_FILE = 'file'

### DECLERATION TO PATH ###
BASE_FILEPATH_D = 'base'
RESOURCE_FILEPATH_D = 'resource'

if CURRENT_PLATFORM == 'Linux':
    BASE_FILEPATH_S = './'
    RESOURCE_FILEPATH_S = '/resources/'
else:
    BASE_FILEPATH_S = ''
    RESOURCE_FILEPATH_S = 'resources\\'



####################################
########## For the client ##########
####################################

### Phrases ###
DOWNLOADING_FILE = 'Downloading: %s'
DOWNLOAD_COMPLETE_FILE = '%s has completed.'
FILE_UPTODATE = '%s is up to date.'
FILE_DOWNLOAD_FAILED = 'Could not download %s !'
LINK_INVALID = 'WARNING!!! Something went wrong while parsing: %s !'

UPDATED_STARTED = 'Update has begun! Please wait...'
FILE_CURRENT = 'File %s is already up to date.'
UPDATE_COMPLETE = 'The game is up to date!'
UPDATE_FAILED = 'Update has failed!'

ARCHIVE_EXTRACTING = 'Extracting: %s'
ARCHIVE_COMPLETE = 'Finished extracting %s'
ARCHIVE_FAILED = 'Could not extract %s'

MD5_FAILED = 'Failed retriving MD5 hash for %s !'

LAUNCHER_STATE_WAITING = 'Login'
LAUNCHER_STATE_UPDATING = 'Please wait...'
LAUNCHER_STATE_FAILURE = 'Something went wrong while updating.'

LAUNCHER_STATUS_LOGIN = 'Please login...'
LAUNCHER_STATUS_GIVE_INPUT = 'You must enter a username and password.'

##########################################
########## For the game starter ##########
##########################################

### Game server ###
if TESTING_NF:
    GAME_SERVER = '127.0.0.1'
else:
    GAME_SERVER = 'disguisedpenguin.onmypc.net'

### Relative paths to python install ###
if CURRENT_PLATFORM == 'Linux':
    PYTHON_PATH = '/usr/bin/python2'
else:
    PYTHON_PATH = '\panda3d\python\ppython.exe'

### Game starting commands ###
if CURRENT_PLATFORM == 'Linux':
    CMD_00 = 'set ttiUsername= %s'
    CMD_01 = 'set ttiPassword=password'
    CMD_02 = 'set TTI_PLAYCOOKIE= %s'
    CMD_03 = 'set TTI_GAMESERVER= %s'
    CMD_04 = 'cd src'
    CMD_05 = '%s -m toontown.toonbase.ClientStart'
else:
    # TEMPORARILIY THE SAME!!!
    CMD_00 = 'set ttiUsername= %s'
    CMD_01 = 'set ttiPassword=password'
    CMD_02 = 'set TTI_PLAYCOOKIE= %s'
    CMD_03 = 'set TTI_GAMESERVER= %s'
    CMD_04 = 'cd src'
    CMD_05 = '%s -m toontown.toonbase.ClientStart'

# Possibly loop through a list for doing the appropirate commands for starting the game
GAME_CMD_LIST = [CMD_00, CMD_01, CMD_02, CMD_03, CMD_04, CMD_05]



