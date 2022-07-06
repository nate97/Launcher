import os
import yaml
from launcher_globals import *



class LauncherParser():

    def __init__(self):
        # Parser globals
        self.link_data = []
        self.download_list = []
        self.unzip_list = []


    # Extract the link data and put the dictonaries into a list form the YAML file
    def extractLinks(self, file_name):
        # Read the YAML file
        with open(file_name, 'r') as stream:
            data_loaded = yaml.safe_load(stream)

        for file_data in data_loaded:
            link_line = (data_loaded[file_data])

            self.link_data.append(link_line)

            # Keep the UI active
            self.refreshUI()


    # Parses out the data out of dictionaries inside of our list
    def parseLinks(self):
        for link_data in self.link_data:

            try:
            # If the data isn't corrupted, continuing

                # This is a special case, and will dictate if we continue further with the file we're dealing with
                file_platform = (link_data['platform'])

                # If the file is for our current platform go ahead and process and apend it to the list
                if file_platform == CURRENT_PLATFORM or file_platform == PLATFORM_ALL:

                    # The file is for our platform, continuing
                    file_url = (link_data['url'])
                    file_path_declar = (link_data['path'])
                    file_name = (link_data['name'])
                    file_extension = (link_data['extension'])
                    # File archive can be true or false
                    file_archive = (link_data['archive'])
                    file_hash =  (link_data['hash'])

                    # file_path_declar is a special case, the file only provides a flag to what the directory should be, not an actual path
                    # we will convert the flag into a directory string, and then combine the directroy and file_name
                    # We will also define just the path to the file
                    if file_path_declar == BASE_FILEPATH_D:
                        file_path = BASE_FILEPATH_S + file_name
                        file_dir = BASE_FILEPATH_S
                    elif file_path_declar == RESOURCE_FILEPATH_D:
                        file_path = RESOURCE_FILEPATH_S + file_name
                        file_dir = RESOURCE_FILEPATH_D
                    else:
                        # We don't know what happend?! set it to base directory!!!
                        file_path = BASE_FILEPATH_S + file_name
                        file_dir = BASE_FILEPATH_S

                    # We need to append all files to the download list
                    self.download_list.append(
                        [file_url, file_path, file_name, file_extension, file_archive, file_hash, file_dir])

                    # The file is a special case so we will append to the unzip_list to deal with later
                    if file_archive == True:
                        self.unzip_list.append(
                            [file_url, file_path, file_name, file_extension, file_archive, file_hash, file_dir])

            except:
                if TESTING_NF:
                    print (LINK_INVALID % link_data)
                self.setFailedLauncher()
                break

