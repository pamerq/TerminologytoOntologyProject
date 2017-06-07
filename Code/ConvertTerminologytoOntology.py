#
# Copyright Pamela Revuelta 2017
#

import os, sys
from Utils import *

class ConvertTerminologytoOntology(object):
    def __init__(self,ObjectTerminology,ObjectOntologyFormat):
        self.terminology = ObjectTerminology
        self.ontologyFormat = ObjectOntologyFormat
        self.ontologyPath = OntologiesPath + self.terminology.getName();
        self.dataTerminology = ""
        self.dataOntology = ""
        print "Terminology: " + self.terminology.getName()
        print "Ontology Format: " + self.ontologyFormat.getName()

    def execute(self):
        dataTerminology=self.terminology.execute()
        self.dataOntology = self.ontologyFormat.execute(dataTerminology)

    def save(self):
        # Ask if it exists TerminologyPath
        os.mkdir(self.ontologyPath, 0755 );
        # Save self.dataOntology
        print "Saved Ontology"
