__author__ = 'assaneesukatham'

#The code separates CR92 txt files with the \t delimeter
#With the absence of "," , toCSV.py fails to convert the CR92 text files to csv (by renaming the extension) with separated values

import glob, os

current_directory = os.getcwd() + "/Resources/CR92/"
destination_directory = os.getcwd() + "/Resources/CR92_CSV"

for filedir in glob.glob(current_directory + "*.txt"):
    input = open(filedir,'r')
    filename = filedir[filedir.rindex("/")+1 : filedir.rindex(".")]
    #Check if the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    output = open(os.getcwd() + "/Resources/CR92_CSV/" + filename + ".csv", "w")
    for line in input:
        split_line = line.split("\t")
        for column in split_line:
            output.write(column + ",")
        output.write("\n")
