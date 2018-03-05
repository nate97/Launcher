import os
import os.path
import zipfile
import hashlib
import requests

from launcher_globals import *
from game_starter import GameStarter
from link_parser import LinkParser



class ToontownLauncher(LinkParser, GameStarter):

    def __init__(self):
        print ('Starting launcher!')
  
        # Initalize our objects
        LinkParser.__init__(self)
        GameStarter.__init__(self)

        # Call the update process
        self.wantUpdates()
        


    def wantUpdates(self):        
        # Build our folder structure FIRST
        self.createDirectory(BASE_FILEPATH_S)
        # Downlaod the resource update file
        self.downloadFile(RESOURCE_FILE, RESOURCE_FILE, RESOURCE_LINK)
        # Extract the data from the resource file 
        self.extractLinks(RESOURCE_FILE)

        self.parseLinks()

        self.downloadManager()
        
        self.archiveManager()

        return



    def downloadManager(self):
        for lists in self.download_list:
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

                # Check if the file hashes match
                if file_l_hash != file_r_hash:
                    print (file_l_hash)
                    print (file_r_hash)

                    # Hashes didnt match, download it
                    self.downloadFile(file_name, file_path, file_url)

                else:
                    # The file was up to date!
                    print (FILE_CURRENT % file_name)

                    if ZIPPED_FILE in lists:
                    # If the file is up to date, remove it from the unzip list
                        self.unzip_list.remove(lists)

            else:
                # The file does not exist, we MUST download it
                self.downloadFile(file_name, file_path, file_url)



    # Download a file with the requests library
    def downloadFile(self, file_name, file_path, file_url):
        try:
            print (DOWNLOADING_FILE % file_name)

            response = requests.get(file_url)
            with open(file_path, 'wb') as file_data:  
                file_data.write(response.content)


            print (DOWNLOAD_COMPLETE_FILE % file_name)
            return

        except:
            print (FILE_DOWNLOAD_FAILED % file_name)
            # PUT A CANCEL CALL BACK HERE????
            return



    def archiveManager(self):
        if self.unzip_list:
            # We have files to extract...
            for lists in self.unzip_list:
                # Grab the data out of the current list
                file_url = lists[0]
                file_path = lists[1]
                file_name = lists[2]
                file_r_hash = lists[3]

                self.extractArchive(file_name)



    # Extract a file
    def extractArchive(self, file_name, directory=''):
        try:
            print (ARCHIVE_EXTRACTING % file_name)
            zip_data = zipfile.ZipFile(file_name)
            zip_data.extractall(directory)
            zip_data.close()
            print (ARCHIVE_COMPLETE % file_name)
        except:
            print (ARCHIVE_FAILED % file_name)
        return



    # Creates directory structure if it hasn't already been built, or deleted
    def createDirectory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return



    # Gets the local MD5 hash of a file
    def getMD5Sum(self, file_name, block_size = 65536):
        hash = hashlib.md5()

        with open(file_name, 'rb') as file_data:
            for block in iter(lambda: file_data.read(block_size), b''):
                hash.update(block)

        return hash.hexdigest()



launcher = ToontownLauncher()
