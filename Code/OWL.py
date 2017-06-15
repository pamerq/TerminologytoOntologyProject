#
# Copyright Pamela Revuelta 2017
#

from OntologyFormat import OntologyFormat

from Utils import *

class OWL(OntologyFormat):
    def __init__(self):
        self.head = '<?xml version="1.0"?>\n<Ontology xmlns="http://www.w3.org/2002/07/owl#"\n\txml:base="http://www.semanticweb.org/ontologies/'
        self.xmlns = '\n\txmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n\txmlns:xml="http://www.w3.org/XML/1998/namespace"\n\txmlns:xsd="http://www.w3.org/2001/XMLSchema#"\n\txmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"\n\tontologyIRI="http://www.semanticweb.org/ontologies/'
        self.prefixsname =  '\n\t<Prefix name="" IRI="http://www.semanticweb.org/ontologies/'
        self.prefixs = '\n\t<Prefix name="owl" IRI="http://www.w3.org/2002/07/owl#"/>\n\t<Prefix name="rdf" IRI="http://www.w3.org/1999/02/22-rdf-syntax-ns#"/>\n\t<Prefix name="xml" IRI="http://www.w3.org/XML/1998/namespace"/>\n\t<Prefix name="xsd" IRI="http://www.w3.org/2001/XMLSchema#"/>\n\t<Prefix name="rdfs" IRI="http://www.w3.org/2000/01/rdf-schema#"/>\n'
        OntologyFormat.__init__(self, "Owl")

    def execute(self,dataTerminological):
        self.loadData(dataTerminological)
        self.dataOntology = self.head + self.name + '"' + self.xmlns +  self.name + '">' + self.prefixsname + self.name + '"/>' + self.prefixs
        clases = ""
        for nameCurrent in self.className:
            clases = clases + '\t<Declaration>\n\t\t<Class IRI="#' + nameCurrent.replace(' ','_') + '"/>\n\t</Declaration>\n'
        relations = ""
        for nameRelations in self.relationship:
            relations = relations + '\t<SubClassOf>\n\t\t<Class IRI="#' + nameRelations[1].replace(' ','_') + '"/>\n\t\t<Class IRI="#'+ nameRelations[0].replace(' ','_') + '"/>\n\t</SubClassOf>\n'
        writeFile(self.name+".owl", self.dataOntology + clases + relations +'</Ontology>')
