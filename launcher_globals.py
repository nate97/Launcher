import platform
import os


### DEBUG VARIABLE ###

TESTING_NF = False
LOCAL_GAME_DOWNLOAD = False
LOCAL_GAME_SERVER = False


CURRENT_PLATFORM = platform.system()
PLATFORM_ALL = 'all'
CURRENT_PATH = os.getcwd()


if TESTING_NF:
    print ('Host operating system: ' + CURRENT_PLATFORM)



####################################
########## For the parser ##########
####################################

### DEBUGGING PURPOSES FOR LOCAL AND REMOTE FILE NAMES ###
if LOCAL_GAME_DOWNLOAD:
    RESOURCE_FILE = 'LOCAL_RESOURCE_LINKS.yaml'
    RESOURCE_LINK = 'http://10.0.0.29/index.php/s/95etFJlljKx7Fj5/download'
else:
    RESOURCE_FILE = 'REMOTE_RESOURCE_LINKS.yaml'
    RESOURCE_LINK = 'https://dl.dropboxusercontent.com/s/jydre9jhj3m9gci/REMOTE_RESOURCE_LINKS.yaml?dl=0'

RESOURCE_NAME = 'resource-links'

### DECLERATION TO PATH ###
BASE_FILEPATH_D = 'base'
RESOURCE_FILEPATH_D = 'resources'

if CURRENT_PLATFORM == 'Linux':
    BASE_FILEPATH_S = './'
    RESOURCE_FILEPATH_S = './resources/'

elif CURRENT_PLATFORM == 'Darwin':
    BASE_FILEPATH_S = './'
    RESOURCE_FILEPATH_S = './resources/'

else:
    BASE_FILEPATH_S = '.\\'
    RESOURCE_FILEPATH_S = 'resources\\'



####################################
########## For the launcher ##########
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

LAUNCHER_STATE_WAITING = 'Please login...'
LAUNCHER_STATE_UPDATING = 'Please wait...'
LAUNCHER_STATE_LAUNCHING = 'Have fun!'

LAUNCHER_STATUS_LOGIN = 'Welcome!'
LAUNCHER_STATUS_GIVE_INPUT = 'You must enter a username and password.'
LAUNCHER_STATUS_INVALID_UP = 'You have entered an invalid username or password.'
LAUNCHER_STATUS_FAILURE = 'Something went wrong while updating.'



##########################################
########## For the game starter ##########
##########################################

### Game server ###
if LOCAL_GAME_SERVER:
    GAME_SERVER = '127.0.0.1'
else:
    GAME_SERVER = '157.185.125.55'

### Relative paths to python install ###
if CURRENT_PLATFORM == 'Linux':
    PYTHON_PATH = '/usr/bin/python3'
elif CURRENT_PLATFORM == 'Darwin':
    PYTHON_PATH = 'python3.10'
else:
    PYTHON_PATH = '\panda3d\python\ppython.exe'

