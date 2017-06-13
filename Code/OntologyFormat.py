#
# Copyright Pamela Revuelta 2017
#

class OntologyFormat(object):
    def __init__(self,name):
        self.name = name
        self.className = []
        self.relationship = []
        self.dataOntology = ""

    def getName(self):
        return self.name

    def execute(self,dataTerminological):
        self.className = dataTerminological["class"]
        self.relationship = dataTerminological["relationship"]
        print "Execute Ontology Format"

    def __str__(self):
        return "Name of the Format is: %s" % (self.name)
