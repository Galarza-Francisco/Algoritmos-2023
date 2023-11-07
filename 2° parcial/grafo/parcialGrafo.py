from grafo import Grafo
from random import randint

mi_grafo = Grafo(dirigido=False) 

personajes = [ "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]

#Punto A
for personaje in personajes:
    cap = randint(1,12)
    mi_grafo.insert_vertice(personaje)
    mi_grafo.insert_arist(personaje, personajes[cap-1], cap)


#Punto B
Aux = mi_grafo.kruskal()
if 'Yoda' in Aux:
    print('si se encuentra yoda')
else:
    print('no se encuentra')

print(Aux)

#Punto C

def maximosCapitulos(grafo):
    pers = None
    max = 0
    
    for a in range(grafo.size()):
        for b in range(a+1, grafo.size()):
            persona1=grafo.get_element_by_index(a)
            persona2=grafo.get_element_by_index(b)
            
#PUNTO D se cumple cuando se cargan los personajes

    