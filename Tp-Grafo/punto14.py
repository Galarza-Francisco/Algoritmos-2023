# Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las si-
# guientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la aris-
# ta es la distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el smart Tv.

from grafo import Grafo
from random import randint

ambientes = [
    ['cocina', ['comedor', 'cochera', 'quincho', 'sala de estar', 'patio']],
    ['comedor', ['cochera', 'quincho', 'baño 1']],
    ['cochera', ['quincho', 'baño 1', 'baño 2']],
    ['quincho', ['comedor', 'baño 2', 'habitación 1']],
    ['baño 1', ['terraza', 'habitación 1', 'habitación 2']],
    ['baño 2', ['habitación 1', 'habitación 2', 'sala de estar']],
    ['habitacion 1', ['habitación 2', 'sala de estar', 'terraza']],
    ['habitacion 2', ['sala de estar', 'terraza', 'patio']],
    ['sala de estar', ['terraza', 'patio', 'cocina', 'baño 1','habitación 2']],
    ['terraza', ['patio', 'cocina', 'comedor']],
    ['patio', ['cocina', 'comedor', 'cochera']]
]

casa = Grafo(dirigido=False)

for ambiente in ambientes:
    casa.insert_vertice(ambiente[0])

#no se puede insertar vertices y aristas al mismo tiempo, uando se insertan las aristas tiene que tener origen y destino

#B

for ambiente in ambientes:
    origen = ambiente[0]
    adyacente = ambiente[1]
    for destino in adyacente:
        metros = randint(1,10)
        casa.insert_arist(origen,destino,metros)

casa.barrido()

#C obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
# para conectar todos los ambientes;
arbolMinima = casa.kruskal()
totMetros = 0
#print(arbolMinima)

for arbol in arbolMinima: #separando el arbol de expresion minima
    for nodo in arbol.split(';'):#en cada nodo le saco el ; y el - para tener los datos desde donde sale hasta donde va y el peso
        data = nodo.split('-')
        print('datos: ',data)
        totMetros += int(data[2])

print('total de metros: ', totMetros)

# D. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el smart Tv.

origen = 'habitacion 1'
destino = 'sala de estar'
posOrigen = casa.search_vertice(origen, criterio='nombre')
posDestino = casa.search_vertice(destino, criterio='nombre')

if posOrigen and posDestino:
    if casa.has_path(origen, destino, criterio='nombre'):
        caminoCorto = casa.dijkstra(origen, destino)  
        while caminoCorto.size() > 0:
            value = caminoCorto.pop() #los valores que saca de la pila sin [0]veritce destino [1]peso [2]origen
            if destino == value[0]:
                total = value[1]



print(f'la cantidad de cable que se necesita son', total,'mts')