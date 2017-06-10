#
# Copyright Pamela Revuelta 2017
#

from Terminology import Terminology

class TUSS(Terminology):
    def __init__(self,nameFolder):
        structures = {}
        Terminology.__init__(self, "Tuss", nameFolder,structures)

    def execute(self):
        self.loadData()
