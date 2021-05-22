# Clase para definir un vertice

class Vertice:
    def __init__(self, i):
        self.id = i
        self.vecinos = []

    def agregaVecino(self, id_vecino):
        if not id_vecino in self.vecinos:
            self.vecinos.append(id_vecino)


class Grafica:
    def __init__(self):
        self.vertices = {}

    def agregaVertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = Vertice(vertice)

    def agregaArista(self, a, b):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregaVecino(b)
            self.vertices[b].agregaVecino(a)


def main():
    g = Grafica()

    listaVertice = [0, 1, 2, 3, 4, 5, 6]

    for vertice in listaVertice:
        g.agregaVertice(vertice)

    listaArista = [2, 0, 0, 6, 6, 3, 0, 5, 6, 5, 0, 1, 6, 4, 1, 4]

    for i in range(0, len(listaArista) -1, 2):
        g.agregaArista(listaArista[i] ,listaArista[i + 1])

    for v in g.vertices:
        print(v, g.vertices[v].vecinos)

main()