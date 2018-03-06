import os
import os.path
import zipfile
import hashlib
import requests

from launcher_globals import *
from game_starter import GameStarter
from link_parser import LinkParser



class Launcher(LinkParser, GameStarter):

    def __init__(self):
        print ('Starting launcher!')
  
        # Initalize our objects
        LinkParser.__init__(self)
        GameStarter.__init__(self)
    

    def checkCredentials(self):
        print (self.uiCallback.uName)
        if self.uiCallback.uName and self.uiCallback.pWord:
            self.wantUpdates()
        else:
            self.uiCallback.enterCredentials()



    def wantUpdates(self):
        # Setup the UI for the update in progress screen
        self.uiCallback.setUpdateUI()
        self.uiCallback.setProgressZero()
        self.refreshUI()

        # Build our folder structure FIRST
        self.createDirectory(BASE_FILEPATH_S)
        # Downlaod the resource update file
        self.downloadFile(RESOURCE_FILE, RESOURCE_FILE, RESOURCE_LINK)
        # Extract the data from the resource file 
        self.extractLinks(RESOURCE_FILE)

        # Parse through the links and put them into the appropriate lists
        self.parseLinks()

        # Start the download manager
        self.downloadManager()
        
        # Extract any archived files we may have
        self.archiveManager()

        return



    def downloadManager(self):
        if self.download_list:
            # We have files to download

            for lists in self.download_list:

                self.uiCallback.countProgress()
                self.refreshUI()

                # Grab the data out of the current list
                file_url = lists[0]
                file_path = lists[1]
                file_name = lists[2]
                file_type = lists[3]
                file_r_hash = lists[4]

                # Have we downloaded the file or not?
                if os.path.exists(file_path):
                    # File already exists, lets check the hash

                    # Get local hash of the file
                    file_l_hash = self.getMD5Sum(file_path)
                    if not file_l_hash:
                        self.setFailedLauncher()
                        break

                    # Check if the file hashes match
                    if file_l_hash != file_r_hash:
                        # Hashes didnt match, download it
                         if not self.downloadFile(file_name, file_path, file_url):
                            self.setFailedLauncher()
                            break
                    else:
                        # The file was up to date!
                        print (FILE_CURRENT % file_name)

                        if ZIPPED_FILE in lists:
                        # If the file is up to date, remove it from the unzip list
                            self.unzip_list.remove(lists)

                else:
                    # The file does not exist, we MUST download it
                    if not self.downloadFile(file_name, file_path, file_url):
                        self.setFailedLauncher()
                        break
            return

    # Download a file with the requests library
    def downloadFile(self, file_name, file_path, file_url):
        try:
            self.ui.launcher_status.setText(DOWNLOADING_FILE % file_name)
            self.refreshUI()
            print (DOWNLOADING_FILE % file_name)

            response = requests.get(file_url)
            with open(file_path, 'wb') as file_data:  
                file_data.write(response.content)
            
            print (DOWNLOAD_COMPLETE_FILE % file_name)

        except:
            # PUT A CALLBACK HERE TO CANCEL THE UPDATE PROCESS!!!
            print (FILE_DOWNLOAD_FAILED % file_name)
            return False
        return



    def archiveManager(self):
        if self.unzip_list:
            # We have files to extract...
            for lists in self.unzip_list:

                self.refreshUI()

                # Grab the data out of the current list
                file_url = lists[0]
                file_path = lists[1]
                file_name = lists[2]
                file_r_hash = lists[3]

                if not self.extractArchive(file_name):
                    self.setFailedLauncher()
                    break
        return



    # Extract a file
    def extractArchive(self, file_name, directory=''):
        try:

            self.ui.launcher_status.setText(ARCHIVE_EXTRACTING % file_name)
            self.refreshUI()
            print (ARCHIVE_EXTRACTING % file_name)

            zip_data = zipfile.ZipFile(file_name)
            zip_data.extractall(directory)
            zip_data.close()
            print (ARCHIVE_COMPLETE % file_name)
        except:
            # PUT CALL BACK HERE TO CANCEL THE UPDATE PROCESS!!!
            print (ARCHIVE_FAILED % file_name)
            return False
        return



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
            print (MD5_FAILED % file_name)
            return False



    def setUICallbacks(self, callback):
        self.uiCallback = callback
        self.ui = callback.ui



    def setApp(self, qApp):
        self.APP_UI = qApp



    # CALL BACK THE UI
    def refreshUI(self):
        self.APP_UI.processEvents()



    def setFailedLauncher(self):
        self.link_data = []
        self.download_list = []
        self.unzip_list = []
        self.setFailedUI()



    def setFailedUI(self):
        self.uiCallback.setFailedUI()
        self.refreshUI()



