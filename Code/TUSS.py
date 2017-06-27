#
# Copyright Pamela Revuelta 2017
#

from Terminology import Terminology

class TUSS(Terminology):
    def __init__(self,nameFolder):
        structures = [{
                       'rank':['10','20','30','31','40','41'], # Rank the structure One
                       # Number the categories the class hierarchy is len(structures[0]['categories'])
                       'categories': {0:{'rank':['10','20','30','31','40','41'],'nameFile':'Capitulos.txt','nameCategorie':'Capitulo'}, ## Categorie More Generic
                                      1:{'rank':[],'nameFile':'Grupos.txt','nameCategorie':'Grupo'},
                                      2:{'rank':[],'nameFile':'Subgrupos.txt','nameCategorie':'SubGrupos'},
                                      3:{'rank':[],'nameFile':'Procedimientos.txt','nameCategorie':'Procedimientos'}} ## Categorie More Specific
                                      #If rank is empty [] consider all items that fall within the previous category
                      }]
        numberPosition = 4
        Terminology.__init__(self, "Tuss", nameFolder, structures,numberPosition)

    #def interpretCode(self,code):
    #    return [code[0:2], code[2:4], code[4:6],code[6:9],code[9:]]

    def interpretCode(self,code):
            return [code[0:2], code[2:4], code[4:6],code[6:9]]

    def execute(self):
        self.loadData()
        for categoriesChild in self.allCategoriesChild:
            for child in categoriesChild:
                self.classNamesBuffer[child[self.numberPosition]]=1
                self.relationship.append([self.allCategoriesParent[child[0]][0], self.allCategoriesParent[child[0]+child[1]][0]])
                self.relationship.append([self.allCategoriesParent[child[0]+child[1]][0], self.allCategoriesParent[child[0]+child[1]+child[2]][0]])
                self.relationship.append([self.allCategoriesParent[child[0]+child[1]+child[2]][0],child[self.numberPosition]])

        dataTerminological = {}
        dataTerminological["name"] = self.name
        dataTerminological["class"] = self.classNamesBuffer
        dataTerminological["relationship"] = self.relationship
        return dataTerminological
