from database.DAO import DAO
import networkx as nx
import geopy
from geopy.distance import geodesic

class Model:
    def __init__(self):
        self.getAnni=DAO.getAnni()
        self.grafo=nx.Graph()

    def creaGrafo(self, anno):
        self.nodi = DAO.getNodi(anno)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges()
        return self.grafo

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)

    def addEdges(self):
        self.grafo.clear_edges()
        for nodo1 in self.grafo:
            for nodo2 in self.grafo:
                if nodo1 != nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                    posizione1 = (nodo1.lat, nodo1.lon)
                    posizione2 = (nodo2.lat, nodo2.lon)
                    distanzaCalcolata = geodesic(posizione1, posizione2).kilometers
                    self.grafo.add_edge(nodo1, nodo2, weight=abs(distanzaCalcolata))

    def analisi(self):
        dizio={}
        for nodo in self.grafo.nodes:
            lista=[]
            for vicino in self.grafo.neighbors(nodo):
                lista.append((vicino.id,self.grafo[nodo][vicino]["weight"]))
            listaOrdinata=sorted(lista, key=lambda x:x[1],reverse=True)
            dizio[nodo.id]=lista
        return dizio