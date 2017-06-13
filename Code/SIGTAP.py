#
# Copyright Pamela Revuelta 2017
#


from Terminology import Terminology

class SIGTAP(Terminology):

    def __init__(self,nameFolder):
        structures = [{
                       'rank':['02','03','04'], # Rank the structure One
                       # Number the categories the class hierarchy is len(structures[0]['categories'])
                       'categories': {0:{'rank':['02','03','04'],'nameFile':'tb_grupo.txt','nameCategorie':'Grupo'}, ## Categorie More Generic
                                      1:{'rank':[],'nameFile':'tb_sub_grupo.txt','nameCategorie':'Sub Grupo'},
                                      2:{'rank':[],'nameFile':'tb_forma_organizacao.txt','nameCategorie':'Forma de Organizacao'},
                                      3:{'rank':[],'nameFile':'tb_procedimento.txt','nameCategorie':'Procedmientos'}} ## Categorie More Specific
                                      #If rank is empty [] consider all items that fall within the previous category
                      }]
        Terminology.__init__(self, "Sigtap", nameFolder,structures)

    def interpretCode(self,code):
        return [code[0:2], code[2:4], code[4:6],code[6:9],code[9:]]

    def execute(self):
        self.loadData()
        for categoriesChild in self.allCategoriesChild:
            for child in categoriesChild:
                self.classNames.append(child[5])
                self.relationship.append([self.allCategoriesParent[child[0]][0], self.allCategoriesParent[child[0]+child[1]][0]])
                self.relationship.append([self.allCategoriesParent[child[0]+child[1]][0], self.allCategoriesParent[child[0]+child[1]+child[2]][0]])
                self.relationship.append([self.allCategoriesParent[child[0]+child[1]+child[2]][0],child[5]])
        dataTerminological = {}
        dataTerminological["class"] = self.classNames
        dataTerminological["relationship"] = self.relationship
        return dataTerminological
