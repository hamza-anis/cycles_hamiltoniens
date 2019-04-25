import Hamilton_data as hd
import os
import sys
class HamiltonSolver():
    global aList
    aList = []
    def __init__(self,name):
        """
        """
        self.name = name
        self.sommets_dic = hd.sommets_depuis_un_point(name)
        self.sommetsPersistants = hd.sommets_depuis_un_point(name)
        self.dic_pour_dessin = hd.sommets_unilateral(name)

    def getSommets(self):
         return self.sommets_dic
    def getSommetsPersistants(self):
        return self.sommetsPersistants
    def get_dic_pour_dessin(self):
        return self.dic_pour_dessin

    def solve(self,nodes,current=0,lenpath = 0):
        """
        fonction de recherche d'un cycle hamiltonien.
        """
        reacheable_nodes = nodes[current]
        nodes[current] = None
        for i in reacheable_nodes:
            if (lenpath == len(nodes)-1 and i == 0) or (nodes[i] != None \
                and HamiltonSolver.solve(self,nodes,i,lenpath+1)):
                    aList.append(current)
                    return True
        nodes[current] = reacheable_nodes
        return False

    def draw_graph(self):
        """
        crée une image représentant le polyedre.
        """
        if aList:
            aList.append(aList[0])
        f = open(self.name.split('.')[0]+".dot","w")
        f.write("strict graph G1{\n"+self.name.split('.')[0]+"[shape=plaintext]\nedge[len=6;edgesep=10];\noverlap = false;\n")
        for i in self.dic_pour_dessin:
            for k in self.dic_pour_dessin[i]:
                f.write(str(i)+"--"+str(k)+"\n")
        for i in range(max(self.dic_pour_dessin)+2):
            f.write(str(i)+"[color=green,style=filled]\n")
        if aList:
            p = aList
            for i in range(len(p)-1):
                f.write(str(p[i])+"--"+str(p[i+1])+"[color=blue,penwidth=3]\n")
        f.write('}')
        f.close()
        os.system('neato -Tjpeg '+self.name.split('.')[0]+'.dot  -o  image_'+self.name.split('.')[0]+'.jpg')
        os.system('rm -f '+self.name.split('.')[0]+'.dot')

if __name__ == '__main__':
    name= sys.argv[1]+".off"
    k = HamiltonSolver(name)
    k.solve(k.getSommets())
    k.draw_graph()
