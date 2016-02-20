import csv, glob, os
import re

class CheckCR92Column:

    def __init__(self):
        self.count = 0
        self.row_list = [[]]

    def check_class_time(self, row):
        #check if the the column 8 is either class time (HH.MM - HH.MM) or TDF
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
            return
        self.row_list.append(row)

    def check_seat_amount(self, row):
        #Seat column is row[24]
        matchObj1 = re.match(r'[0-9]*', row[24]) #match a number in format X or XX
        column = 24
        #If the matchObj1 does not match, iterate row (>24) until meet the row that match the matchObj1
        if matchObj1:
            return
        while not matchObj1:
            matchObj1 = re.match(++column)

        #Aggregrate column 21 with any other column after 21 which are not empty
        #TBC...


        return



current_directory = os.path.dirname(__file__) #/senior_project/CR92_Python/FixColumn/
source_directory = os.path.abspath(os.path.join(current_directory, os.pardir, os.pardir, "Resources", "CR92_CSV"))

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

