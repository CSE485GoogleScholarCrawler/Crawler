import os

pdf2txt = 'pdf2txt.py'


def getText(paperPath):
    os.system("pdftotext" + " " + paperPath)


def getAbstract(paperPath):
    minimumAbstractLength = 500
    getText(paperPath)
    txtFilePath = paperPath[:-4]
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

    outputFilePath = txtFilePath = paperPath[:-4] + "abstract.txt"
    outFile = open(outputFilePath, "w")
    if(foundAbstract):
        print(abstract)
        outFile.write(abstract)
        outFile.close()
        return abstract
    else:
        print(possibleAbstractStored[0])
        outFile.write(possibleAbstractStored[0])
        outFile.close()
        return possibleAbstractStored[0]

    
