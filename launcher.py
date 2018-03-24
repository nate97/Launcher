import os
import sys
import os.path
import zipfile
import hashlib
import requests

from launcher_globals import *
from launcher_parser import LauncherParser
from game_starter import GameStarter

class Launcher(LauncherParser, GameStarter):

    def __init__(self):
        if TESTING_NF:
            print ('Starting launcher!')
  
        # Initalize our objects
        LauncherParser.__init__(self)
        GameStarter.__init__(self)

        self.launch = False    


    def checkCredentials(self):
        if self.uiCallback.uName and self.uiCallback.pWord:
            # Implement mechanism to check to see if account is valid
            self.updateManager()
        else:
            self.uiCallback.setEnterCredsUI()


    def updateManager(self):
        # Setup the UI for the update in progress screen
        self.uiCallback.setUpdateUI()
        self.refreshUI()

        # Build our folder structure FIRST
        self.createDirectory(RESOURCE_FILEPATH_S)

        # Downlaod the resource update file
        self.downloadFile(RESOURCE_NAME, RESOURCE_FILE, RESOURCE_LINK)

        # Extract the data from the resource file 
        self.extractLinks(RESOURCE_FILE)

        # Parse through the links and put them into the appropriate lists
        self.parseLinks()

        # Update the UI's progress bar AFTER the file list has been populated
        self.uiCallback.setProgressZero()
        self.refreshUI()

        # Start the download manager
        self.downloadManager()
        
        # Extract any archived files we may have
        self.archiveManager()

        self.uiCallback.ui.launcher_status.setText(UPDATE_COMPLETE)
        self.uiCallback.ui.launcher_state.setText(LAUNCHER_STATE_LAUNCHING)
        self.refreshUI()

        self.launch = True

        #self.setFailedLauncher()
        #self.launch = False

        self.launchGame()
        sys.exit()


    def downloadManager(self):
        if self.download_list:
            # We have files to download

            for lists in self.download_list:

                # Grab the data out of the current list
                file_url = lists[0]
                file_path = lists[1]
                file_name = lists[2]
                file_extension = lists[3]
                file_archive = lists[4]
                file_r_hash = lists[5]
                file_path_extension = file_path + file_extension

                # Have we downloaded the file or not?
                if os.path.exists(file_path_extension):
                    # File already exists, lets check the hash

                    # Get local hash of the file
                    file_l_hash = self.getMD5Sum(file_path_extension)
                    if not file_l_hash:
                        self.setFailedLauncher()
                        break

                    # Check if the file hashes match
                    if file_l_hash != file_r_hash:
                        # Hashes didnt match, download it
                         if not self.downloadFile(file_name, file_path_extension, file_url):
                            self.setFailedLauncher()
                            break

                    elif file_l_hash == file_r_hash:
                        # The file was up to date!
                        if file_archive == True and os.path.exists(file_path):
                        # If the file is up to date, and the directory already exists,
                        # remove the file from the list to be extracted
                            self.unzip_list.remove(lists)
                            # Tell the progress bar that the maximum is less now
                            self.uiCallback.subtractProgressZIP()

                else:
                    # The file does not exist, we MUST download it
                    if not self.downloadFile(file_name, file_path_extension, file_url):
                        self.setFailedLauncher()
                        break

                # Add progress to the UI's progress bar
                self.uiCallback.countProgress()
                self.refreshUI()

            return True


    # Download a file with the requests library
    def downloadFile(self, file_name, file_path, file_url):
        try:
            self.ui.launcher_status.setText(DOWNLOADING_FILE % file_name)
            self.refreshUI()
            if TESTING_NF:
                print (DOWNLOADING_FILE % file_name)
            
            response = requests.get(file_url, stream=True)
            handle = open(file_path, "wb")
            for chunk in response.iter_content(chunk_size=512):

                # Call back so that the UI doesn't freeze
                self.refreshUI()

                if chunk:  # filter out keep-alive new chunks
                    handle.write(chunk)

            self.ui.launcher_status.setText(DOWNLOAD_COMPLETE_FILE % file_name)
            self.refreshUI()
            if TESTING_NF:
                print (DOWNLOAD_COMPLETE_FILE % file_name)

        except:
            # CALL BACK AND KILL THE PROCESS
            if TESTING_NF:
                print (FILE_DOWNLOAD_FAILED % file_name)
            return False
        return True


    def archiveManager(self):
        if self.unzip_list:
            # We have files to extract...
            for lists in self.unzip_list:

                self.refreshUI()

                # Grab the data out of the current list
                file_url = lists[0]
                file_path = lists[1]
                file_name = lists[2]
                file_extension = lists[3]
                file_archive = lists[4]
                file_r_hash = lists[5]
                directory = lists[6]
                file_path_extension = file_path + file_extension


                if not self.extractArchive(file_path_extension, file_name, directory):
                    self.setFailedLauncher()
                    break

                # Add progress to the UI's progress bar
                self.uiCallback.countProgress()
                self.refreshUI()

        return True


    # Extract a file
    def extractArchive(self, file_path, file_name, directory):
        try:
            self.ui.launcher_status.setText(ARCHIVE_EXTRACTING % file_name)
            self.refreshUI()
            if TESTING_NF:
                print (ARCHIVE_EXTRACTING % file_name)

            zip_data = zipfile.ZipFile(file_path)
            zip_data.extractall(directory)
            zip_data.close()

            self.ui.launcher_status.setText(ARCHIVE_COMPLETE % file_name)
            self.refreshUI()
            if TESTING_NF:
                print (ARCHIVE_COMPLETE % file_name)
        except:
            # PUT CALL BACK HERE TO CANCEL THE UPDATE PROCESS!!!
            if TESTING_NF:
                print (ARCHIVE_FAILED % file_name)
            return False
        return True


    # Creates directory structure if it hasn't already been built, or deleted
    def createDirectory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return


    # Gets the local MD5 hash of a file
    def getMD5Sum(self, file_name, block_size = 65536):
        try:
            hash = hashlib.md5()
            with open(file_name, 'rb') as file_data:
                for block in iter(lambda: file_data.read(block_size), b''):
                    hash.update(block)

            return hash.hexdigest()
        except:
            # CALL BACK FOR CANCELING THE UPDATE PROGRESS!!!!!
            if TESTING_NF:
                print (MD5_FAILED % file_name)
            return False


    # This is so we can make calls to the UI class
    def setUICallbacks(self, callback):
        self.uiCallback = callback
        self.ui = callback.ui


    # Calls the function to update the UI while we're processing data
    def refreshUI(self):
        self.uiCallback.APP.processEvents()


    # Set our variables the the defaults since the update failed
    def setFailedLauncher(self):
        self.link_data = []
        self.download_list = []
        self.unzip_list = []
        self.setFailedUI()


    # Tell the UI that updates have failed
    def setFailedUI(self):
        self.uiCallback.setFailedUI()
        self.refreshUI()

