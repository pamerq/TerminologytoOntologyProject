#
# Copyright Pamela Revuelta 2017
#

from ConvertTerminologytoOntology import ConvertTerminologytoOntology
from TUSS import TUSS
from SIGTAP import SIGTAP
from OWL import OWL


#Terminologies
sigtap = SIGTAP("SigtapSource")
tuss = TUSS("TussSource")

#Ontology Format
owl = OWL()

convert = ConvertTerminologytoOntology(tuss,owl)
convert.execute()
convert.save()
