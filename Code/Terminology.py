#
# Copyright Pamela Revuelta 2017
#

from Utils import *

class Terminology(object):
    def __init__(self,name,nameFolder):
        self.name = name
        self.pathFolder = OriginalPath + nameFolder
        self.data = []

    def getName(self):
        return self.name

    def execute(self):
        print "Execute read the terminology"
        return self.data

    def __str__(self):
        return "Name of the Terminology: %s" % (getName())
