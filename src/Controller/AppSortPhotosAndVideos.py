import glob
import sys
import getopt
import os
from builtins import FileExistsError
from zipfile import ZipFile, ZIP_DEFLATED


class AppSortPhotosAndVideos:

    def __init__(self):
        self.str_full_argv = sys.argv
        self.str_opt_argv = self.str_full_argv[1:]
        self.str_path_extension = self.str_opt_argv[0]

    def main(self, param1=None):
        txtfiles = []
        nameOnly = []
        originalPathOnlyList = []
        originalPathOnly = "/"


        for file in glob.glob(self.str_path_extension):
            txtfiles.append(file)
            nameOnly.append(file.split(os.sep)[-1])
            originalPathOnlyList= file.split(os.sep)[0:-1]

        originalPathOnly = originalPathOnly.join(originalPathOnlyList)

        print(txtfiles)
        print(nameOnly)

        for i in range(len(txtfiles)):
            year = nameOnly[i][0:4]
            month = nameOnly[i][4:6]
            day = nameOnly[i][6:8]

            print("year:{0}, month:{1}, day:{2}\n".format(year, month, day))

            #Create the year/month/day directory
            dir_to_create = originalPathOnly + os.sep + year + os.sep + month + os.sep + day
            print("Creating ... " + dir_to_create + "\n")
            os.makedirs(dir_to_create, exist_ok=True)

            old_file = txtfiles[i]
            new_file = dir_to_create + os.sep + nameOnly[i]

            print("Moving ... " + old_file + " ... to ..." + new_file + "\n")
            os.rename(old_file, new_file)
