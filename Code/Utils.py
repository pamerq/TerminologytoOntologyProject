#
# Copyright Pamela Revuelta 2017
#

import codecs

Path = "/Users/Pamela/Repositories/Git/TerminologytoOntologyProject/"
OriginalPath = Path + "Resources/"
OntologiesPath = Path + "Ontologies/"

def loadFile(file):
	document = codecs.open(file, encoding="utf-8", errors='ignore') # Para archivo con codificacion utf-8
	#document =  codecs.open(file, 'r', 'iso-8859-1')
	return document
