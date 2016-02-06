__author__ = 'assaneesukatham'

#The program copy all text files in the source folder to the destination folder (automatically create the 'folder_name'_CSV directory)
#and rename the extension to ".csv"
#Enter folder name (containing text files) into the console to complete the directory path

import glob, os
from shutil import copyfile

#Directory refers to where text files are stored
#Directory default is /senior_project/Resources/
#Put the folder containing text files under /senior_project/Resources/
current_directory = os.getcwd() + "/Resources/"
folder_name = input("Please enter the folder name:")

if not os.path.exists(current_directory + "/Resources/" + folder_name):
    raise Exception("The directory does not exist, please rerun the program and enter a proper directory.")

source_directory = current_directory + folder_name + "/"
#Create a new directory 'folder_name'_CSV, ignore if the directory exists
if not os.path.exists(current_directory + folder_name + "_CSV/"):
    os.makedirs(current_directory + folder_name + "_CSV/")
destination_directory = current_directory + folder_name + "_CSV/"
for filedir in glob.glob(source_directory + "*.txt"):
    #filename without the extension
    filename = filedir[filedir.rindex("/")+1 : filedir.rindex(".")]
    #Check if the destination exists a file with the extension ".csv"
    #Delete the file if the file exists
    if os.path.exists(destination_directory + filename + ".csv"):
        os.remove(destination_directory + filename + ".csv")
    #Copy the source file to the destination, rename the ex
    copyfile(source_directory + filename + ".txt", destination_directory + filename + ".csv")



