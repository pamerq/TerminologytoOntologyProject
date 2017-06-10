#
# Copyright Pamela Revuelta 2017
#

from ConvertTerminologytoOntology import ConvertTerminologytoOntology
from TUSS import TUSS
from SIGTAP import SIGTAP
from OWL import OWL


## Terminologies
sigtap = SIGTAP("SigtapResource")
#tuss = TUSS("TussResource")

## Ontology Format
owl = OWL()

convert = ConvertTerminologytoOntology(sigtap,owl)
convert.execute()
