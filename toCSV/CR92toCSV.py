__author__ = 'assaneesukatham'

#Unused code

directory = "/Users/assaneesukatham/PycharmProjects/senior_project/Resources/CR92/"
import glob
def countCourses():
    count = 0
    sName = set()
    sID = set()
    '''
    for filename in glob.glob(directory+"*.txt"):
        input = open(filename,"r")
        for line in input:
            nline = line.split()
            print(nline)
            subjID = nline[0]
            subjName = nline[1]
            sName.add(subjName)
            sID.add(subjID)
    '''
    input = open(directory + "21S20152.txt","r")
    for line in input:
        nline = line.split()
        print(nline)
        subjID = nline[0]
        subjName = nline[1]
        sName.add(subjName)
        sID.add(subjID)
    print(len(sName))
    print(sName)
    print(len(sID))
    print(sID)
    numberOfSubject = str(len(sID))

    out = open("subject stats.txt",'w')
    out.write("Total Number of Subject is: "+numberOfSubject)

def getSubjectID(line):
    index = line.index(" ")
    subjID = line[:index]
    line = line[index:]
    getSubjectName(line)

def getSubjectName(nline):
        index = indexOfCredit(nline)
        subjName = ""
        for i in range(1,index-1):
            subjName += nline[i]
        return subjName

def indexOfCredit(nline):
        strRange = []
        for i in range(0,100):
            strRange[i] = str(i)
        for i in range(0,100):
            index = nline.index(strRange[i])
            if(index != -1):
                return index

def toCsv():
    for filedir in glob.glob(directory+"*.txt"):
        input = open(filedir,'r')
        filename = filedir.split("/")[-1].split(".")[0]
        print(filename)
        subjID = subjName = credit = prerequisite = dateMidterm = timeMidterm = dateFinal = timeFinal = ""
        out = open(filename+".csv","w")
        for line in input:
            col = line.split()
            print("contain "+str(len(col))+" columns")
            for word in col:
                out.write(word+",")
            out.write("\n")

countCourses()
