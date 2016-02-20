__author__ = 'assaneesukatham'

#The code separates CR92 txt files with the \t delimeter
#With the absence of "," , toCSV.py fails to convert the CR92 text files to csv (by renaming the extension) with separated values

import glob, os
script_directory = os.path.dirname(__file__)
source_directory = os.path.abspath(os.path.join(script_directory, os.pardir, os.pardir, "Resources", "CR92"))
destination_directory = os.path.abspath(os.path.join(script_directory, os.pardir, os.pardir, "Resources", "CR92_CSV"))
c = os.path.join(destination_directory, "*.txt")

for filedir in glob.glob(os.path.join(source_directory, "*.txt")):
    input = open(filedir,'r')
    filename = filedir[filedir.rindex(os.sep)+1 : filedir.rindex(".")]
    #Check if the destination directory exists
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    output = open(os.path.join(destination_directory, filename + ".csv",), "w")
    for line in input:
        split_line = line.split("\t")
        for i in range(0, len(split_line)-1):
            output.write(split_line[i] + ",")
        output.write(split_line[-1])
