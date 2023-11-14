from grafo import Grafo
from random import randint

miGrafo = Grafo(dirigido=False)

miGrafo.insert_vertice('T')
miGrafo.insert_vertice('F')
miGrafo.insert_vertice('X')
miGrafo.insert_vertice('R')
miGrafo.insert_vertice('Z')
miGrafo.insert_vertice('P')
miGrafo.insert_vertice('J')

miGrafo.insert_arist('P','J',8)
miGrafo.insert_arist('T', 'R', 8)
miGrafo.insert_arist('T', 'F', 3)
miGrafo.insert_arist('T', 'X', 6)
miGrafo.insert_arist('F', 'R', 2)
miGrafo.insert_arist('F', 'X', 2)
miGrafo.insert_arist('X', 'Z', 9)
miGrafo.insert_arist('X', 'R', 5)
miGrafo.insert_arist('R', 'Z', 4)


origen='F'
destino='R'

verOrigen = miGrafo.search_vertice(origen)
if verOrigen:
   aux =  miGrafo.get_element_by_index(verOrigen)
   posArista = aux[1].search(destino, 'vertice')
   if posArista is not None:
      arista = verOrigen[1].get_element_by_index(posArista)
      print(posArista.vertice, arista.peso)