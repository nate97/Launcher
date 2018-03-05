import os

from launcher_globals import *



class LinkParser():

    def __init__(self):
        # Parser globals
        self.link_data = []
        self.all_files = []
        self.zipped_files = []


    # Extract links from our link file
    def extractLinks(self, file_name, directory=''):
        file_path = directory + file_name
        file_data = open(file_path, 'r')
        lines = file_data.readlines()
        file_data.close()

        # Iterate through the lines in the file
        for line in range(len(lines)):

            # Get single line out of resource file
            single_line = lines[line]

            # If the line has the word link in it, we will append it to the links list
            if VALID_LINE in single_line:
                # Get rid of newline dilimeters # HACKY! #
                single_line = single_line.split('\n')[0].split('\r')[0]
                # Append our link data to the list
                self.link_data.append(single_line)
        return


    # This function goes through each item in the links list and parses the data out appropriatly
    def parseLinks(self):
        # Loop through each item in our list
        for link_data in self.link_data:

            link_data = self.stringSplitter(link_data, DILIMETER, OCCURENCE)

            file_url = link_data[1]
            file_path_declar = link_data[2]
            file_name = link_data[3]
            file_format = link_data[4]
            file_r_hash = link_data[5]

            # file_path_declar is a special case, the file only provides a flag as to what the directory should be, not the actual directory
            # So we will convert the flag into a directory string, and then go ahead and combine the directroy and file_name
            if file_path_declar == BASE_FILEPATH_D:
                file_path = BASE_FILEPATH_S + file_name 

            elif file_path_declar == RESOURCE_FILEPATH_D:
                file_path = RESOURCE_FILEPATH_S + file_name

            else:
                # We don't know what happend?! set it to base directory!!!
                file_path = BASE_FILEPATH_S + file_name


            # Another special case is file_format, if the file is a zipped file we need to add it to a list
            # so that we can take care of extracting that file later on.
            if file_format == ZIPPED_FILE:
                self.zipped_files.append([file_path, file_name])


            # Call a different function that does something with the data we have parsed
            # FROM THIS LOOP #
            self.manageLinkData(file_url, file_path, file_name, file_format, file_r_hash)



