#
# Copyright Pamela Revuelta 2017
#

from Utils import *

class Terminology(object):
    def __init__(self,name,nameFolder,structures,numberPosition):
        self.name = name
        self.pathFolder = OriginalPath + nameFolder + "/"
        self.structures = structures
        self.allCategoriesParent = {}
        self.allCategoriesChild = []
        self.classNames = []
        self.classNamesBuffer = {}
        self.relationship = []
        self.numberPosition = numberPosition
    def getName(self):
        return self.name

    def fileToMatrix(self,file):
    	document = loadFile(file)
    	data = []
    	for line in document:
    		lineList = line.rsplit('\t')
    		lineListNew =[]
    		for i in lineList:
    			lineListNew.append(i.rstrip().encode('utf-8'))
    		data.append(lineListNew);
    	return data

    def filter(self, data, rank):
        if not rank:
            return data
        dataNew =[];
        for line in data:
            if line[0] in rank:
                dataNew.append(line)
        return dataNew

    def interpret(self,data):
        dataBuff = []
        for line in data:
            code = line[0]
            line = line[1:]
            codes = self.interpretCode(code) #Each terminology has different interpretation of the codes
            line = codes + line
            dataBuff.append(line)
        return dataBuff

    def loadData(self):
        for structure in self.structures:
            ###Categories Parent
            catDaughter = 0
            for catCurrent in range(len(structure['categories'])-1):
                data = self.fileToMatrix(self.pathFolder + structure['categories'][catCurrent]['nameFile'])
                for i in range(catCurrent+1):
                    data = self.filter(data,structure['categories'][i]['rank'])
                #dataMap = {}
                for line in data:
                    code = ""
                    position = 0
                    for position in range(catCurrent+1):
                        code = code + line[position]
                    newLine = line[position+1:]
                    #dataMap[code] = newLine
                    if self.classNamesBuffer.has_key(newLine[0]):
                        buff=self.classNamesBuffer[newLine[0]]
                        self.classNamesBuffer[newLine[0]]=buff+1
                    else:
                        self.classNamesBuffer[newLine[0]]=1
                    self.classNames.append(newLine[0])
                    self.allCategoriesParent[code] = newLine
                catDaughter = catCurrent
            ###Categorie Child
            catDaughter += 1
            data = self.fileToMatrix(self.pathFolder + structure['categories'][catDaughter]['nameFile'])
            data = self.interpret(data)
            for i in range(catDaughter):
                data = self.filter(data,structure['categories'][i]['rank'])
            self.allCategoriesChild.append(data)


    def __str__(self):
        return "Name of the Terminology: %s" % (getName())
