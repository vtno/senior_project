__author__ = 'assaneesukatham'

directory = "/Users/assaneesukatham/PycharmProjects/senior_project/Resources/CR92/";
import glob
def countCourses():
    count = 0
    sName = set()
    sID = set()
    for filename in glob.glob(directory+"*.txt"):
        input = open(filename,"r")
        for line in input:
            nline = line.split()
            print(nline)
            subjID = nline[0]
            subjName = getSubjectName(nline)
            sName.add(subjName)
            sID.add(subjID)
    print(len(sName))
    print(sName)
    print(len(sID))
    print(sID)
    numberOfSubject = str(len(sID))

    out = open("subject stats.txt",'w')
    out.write("Total Number of Subject is: "+numberOfSubject)

def getSubjectName(nline):
        index = indexOfCredit()
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
        filename = filedir.split("/")[-1].split(".")[0];
        print(filename);
        out = open(filename+".csv","w");
        for line in input:
            col = line.split();
            print("contain "+str(len(col))+" columns");
            for word in col:
                out.write(word+",");
            out.write("\n");

countCourses();
