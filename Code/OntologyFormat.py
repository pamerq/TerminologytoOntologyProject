#
# Copyright Pamela Revuelta 2017
#

from Utils import *

class OntologyFormat(object):
    def __init__(self,name):
        self.name = name
        self.className = []
        self.relationship = []
        self.name = ""
        self.dataOntology = ""

    def getName(self):
        return self.name

    def loadData(self,dataTerminological):
        self.className = dataTerminological["class"]
        self.relationship = dataTerminological["relationship"]
        self.name = dataTerminological["name"]

    def __str__(self):
        return "Name of the Format is: %s" % (self.name)
