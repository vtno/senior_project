import csv, glob, os
import re

class CheckCR92Column:

    def __init__(self):
        self.count = 0
        self.row_list = [[]]

    def check_class_time(self, row):
        self.row_list.append(row)
        #check if the the column 8 is either class time (HH:MM - HH:MM) or TDF
        column_7 = row[7]
        matchObj1 = re.match(r'.*-.*', column_7)
        matchObj2 = re.match(r'TDF', column_7)
        if not (matchObj1 or matchObj2):
            row[3] = row[3] + row[4]
            for i in range(4, len(row)-1):
                row[i] = row[i+1]
            #row now is the data to be written
            #append the data to the row
            self.row_list.append(row)


current_directory = os.getcwd() #/senior_project/CR92_Python/FixColumn/
os.chdir("../../Resources/CR92_CSV")
source_directory = os.getcwd()

for filedir in glob.glob(source_directory + "/*.csv"):
    with open(filedir, 'r', newline='') as csvfile:
        CSV_Reader = csv.reader(csvfile)
        check_cr92_column = CheckCR92Column()
        del check_cr92_column.row_list[0]
        for row in CSV_Reader:
            check_cr92_column.check_class_time(row)

        with open(filedir, 'w', newline='') as csvfile:
            CSV_writer = csv.writer(csvfile)
            for each_row in check_cr92_column.row_list:
                    CSV_writer.writerow(each_row)

