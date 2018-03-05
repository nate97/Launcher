import os
import os.path
import zipfile
import hashlib

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
        self.downloadFile(RESOURCE_FILE, RESOURCE_LINK)

        # Extract the data from the resource file 
        self.extractLinks(RESOURCE_FILE)

        self.parseLinks()

        print (self.zipped_files)


        return




















    def manageLinkData(self, file_url, file_path, file_name, file_format, file_r_hash):
        # Have we downloaded the file or not?
        if os.path.exists(file_path):
            # File already exists, lets check the hash

            # Get local hash of the file
            file_l_hash = self.getLocalMD5Sum(file_path)

            # Check if the file hashes match
            if file_l_hash != file_r_hash:
                print (file_l_hash)
                print (file_r_hash)

                # Hashes didnt match, download it
                #self.downloadFile(directory, file_name, file_url)

            else:
                print (file_name +': file up to date!\n')

        else:
            # The file does not exist, we MUST to download it

            self.downloadFile(file_path, file_url)
            print ("DOWNLOAD IT")



































    #
    def downloadFile(self, file_path, file_url):
        return
        try:
            if TESTING_NF:
                print (DOWNLOADING_FILE % file_name)


            response = urllib2.urlopen(file_url)
            data = response.read()
            file_data = open(file_path, 'w')
            file_data.write(data)
            file_data.close()


            if TESTING_NF:
                print (DOWNLOAD_COMPLETE_FILE % file_name)
            return

        except:
            if TESTING_NF:
                print (FILE_DOWNLOAD_FAILED % file_name)
            return




    # Extract a file
    def extractZip(self, file_name, directory=''):
        try:
            file_path = directory + file_name
            zip_data = zipfile.ZipFile(file_path)
            zip_data.extractall(path = directory)

            return
        except:
            print ('Error extracting file: ' + file_name + '\n')
            return



























    # Creates directory structure if it hasn't already been built, or deleted
    def createDirectory(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        return


    # Gets the local MD5 hash of a file
    def getLocalMD5Sum(self, file_name, block_size = 65536):
        hash = hashlib.md5()

        with open(file_name, 'rb') as file_data:

            for block in iter(lambda: file_data.read(block_size), b''):
                hash.update(block)

        return hash.hexdigest()

























    # Split string on specified dilimeter X amount of times
    def stringSplitter(self, link_data, delimimeter, occurrence):
        return link_data.split(delimimeter, occurrence)



launcher = ToontownLauncher()
