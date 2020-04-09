import os

pdf2txt = 'pdf2txt.py'


def getText(paperPath):
    os.system("pdftotext " + paperPath)
    


def getAbstract():
    minimumAbstractLength = 500
    path = input("Input the name of the paper in this directory including the .pdf: ")
    getText(path)
    txtFilePath = path[:-4]
    txtFile = open(txtFilePath + ".txt", 'r')

    fileLines = txtFile.readlines()

    abstract = ""
    possibleAbstract = ""
    possibleAbstractStored = []
    foundAbstract = False
    for x in fileLines:
        if(~foundAbstract):
            if(x != "\n"):
                possibleAbstract += x
        if(x == "\n" and ~foundAbstract and len(possibleAbstract) > minimumAbstractLength and len(possibleAbstractStored) < 3):
            possibleAbstractStored.append(possibleAbstract)
        elif(x == "\n" and ~foundAbstract and len(possibleAbstract) < minimumAbstractLength):
            possibleAbstract = ""
        if(x.lower() == "abstract"):
            foundAbstract = True
        if(foundAbstract):
            abstract += x
        
        if(x == "\n" and foundAbstract):
            break

    outputFilePath = txtFilePath + "abstract.txt"
    print(outputFilePath)
    outFile = open(outputFilePath, "w")
    if(foundAbstract):
        print(abstract)
        outFile.write(abstract)
        outFile.close()
    else:
        print(possibleAbstractStored[0])
        outFile.write(possibleAbstractStored[0])
        outFile.close()
        
def main():
    getAbstract()
    
main()
