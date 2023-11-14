# Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, 
# para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
# uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
# e. determinar si algún país tiene más de una dato del mismo tipo;
# f. deberá utilizar un grafo no dirigido.

from grafo import Grafo
from random import randint

miGrafo = Grafo(dirigido=False)

class Maravilla:
    def __init__(self, nombre, pais, tipo, distancia):
            self.nombre = nombre
            self.pais = pais
            self.tipo = tipo
            self.distancia = distancia

    def __str__(self):
            return f'{self.nombre}-{self.pais}-{self.tipo}-{self.distancia}'


datos = [
    {
        "Nombre": "Gran Muralla China",
        "Tipo": "arquitectonica",
        "Pais": { "China"},
        "Distancias": {
            "Machu Picchu": 500,
            "Cristo Redentor": 2000,
            "Chichén Itzá": 1500,
            "Petra": 3000,
            "Estudio Sagrada Familia": 6000,
            "Coliseo Romano": 7000
        }
    },
    {
        "Nombre": "Machu Picchu",
        "Tipo": "arquitectonica",
        "Pais": { "Perú"}, #Perú
        "Distancias": {
            "Gran Muralla China": 500,
            "Cristo Redentor": 1800,
            "Chichén Itzá": 1200,
            "Petra": 2500,
            "Estudio Sagrada Familia": 5500,
            "Coliseo Romano": 6500
        }
    },
    {
        "Nombre": "Cristo Redentor",
        "Tipo": "arquitectonica",
        "Pais": { "Brasil"},
        "Distancias": {
            "Gran Muralla China": 2000,
            "Machu Picchu": 1800,
            "Chichén Itzá": 2200,
            "Petra": 3200,
            "Estudio Sagrada Familia": 4000,
            "Coliseo Romano": 5500
        }
    },
    {
        "Nombre": "Chichén Itzá",
        "Tipo": "arquitectonica",
        "Pais": { "México"},
        "Distancias": {
            "Gran Muralla China": 1500,
            "Machu Picchu": 1200,
            "Cristo Redentor": 2200,
            "Petra": 2000,
            "Estudio Sagrada Familia": 5000,
            "Coliseo Romano": 6000
        }
    },
    {
        "Nombre": "Petra",
        "Tipo": "arquitectonica",
        "Pais": { "Jordania"},
        "Distancias": {
            "Gran Muralla China": 3000,
            "Machu Picchu": 2500,
            "Cristo Redentor": 3200,
            "Chichén Itzá": 2000,
            "Estudio Sagrada Familia": 4500,
            "Coliseo Romano": 5500
        }
    },
    {
        "Nombre": "Parque Nacional de Komodo",
        "Tipo": "natural",
        "Pais": { "Argentina"}, #Indonesia
        "Distancias": {
            "Montaña de la Mesa": 4500,
            "Cataratas del Iguazú": 5500,
            "Monte Everest": 12000,
            "Bahía de Ha Long": 3000,
            "Parque Nacional de Yellowstone": 15000,
            "Gran Muralla China": 12000
        }
    },
    {
        "Nombre": "Montaña de la Mesa",
        "Tipo": "natural",
        "Pais": { "Sudáfrica","Argentina"}, #sudafrica
        "Distancias": {
            "Parque Nacional de Komodo": 4500,
            "Cataratas del Iguazú": 6000,
            "Monte Everest": 11000,
            "Bahía de Ha Long": 3500,
            "Parque Nacional de Yellowstone": 14000,
            "Gran Muralla China": 13000
        }
    },
    {
        "Nombre": "Estudio Sagrada Familia",
        "Tipo": "arquitectonica",
        "Pais": { "España"},
        "Distancias": {
            "Gran Muralla China": 6000,
            "Machu Picchu": 5500,
            "Cristo Redentor": 4000,
            "Chichén Itzá": 5000,
            "Petra": 4500,
            "Coliseo Romano": 800
        }
    },
    {
        "Nombre": "Coliseo Romano",
        "Tipo": "arquitectonica",
        "Pais": { "Italia"},
        "Distancias": {
            "Gran Muralla China": 7000,
            "Machu Picchu": 6500,
            "Cristo Redentor": 5500,
            "Chichén Itzá": 6000,
            "Petra": 5500,
            "Estudio Sagrada Familia": 800
        }
    },
    {
        "Nombre": "Taj Mahal",
        "Tipo": "arquitectonica",
        "Pais": { "India"},
        "Distancias": {
            "Bahía de Ha Long": 4500,
            "Parque Nacional de Yellowstone": 11000,
            "Parque Nacional de Komodo": 12000,
            "Cataratas del Iguazú": 9000,
            "Montaña de la Mesa": 11000,
            "Monte Everest": 14000
        }
    },
    {
        "Nombre": "Cataratas del Iguazú",
        "Tipo": "natural",
        "Pais": {"Argentina", "Brasil"},
        "Distancias": {
            "Parque Nacional de Komodo": 5500,
            "Montaña de la Mesa": 6000,
            "Monte Everest": 13000,
            "Bahía de Ha Long": 4000,
            "Parque Nacional de Yellowstone": 12000,
            "Gran Muralla China": 10000
        }
    },
    {
        "Nombre": "Monte Everest",
        "Tipo": "natural",
        "Pais": { "Nepal"},
        "Distancias": {
            "Parque Nacional de Komodo": 12000,
            "Montaña de la Mesa": 11000,
            "Cataratas del Iguazú": 13000,
            "Bahía de Ha Long": 11000,
            "Parque Nacional de Yellowstone": 9000,
            "Gran Muralla China": 13000
        }
    },
    {
        "Nombre": "Bahía de Ha Long",
        "Tipo": "natural",
        "Pais": { "Vietnam"},
        "Distancias": {
            "Parque Nacional de Komodo": 3000,
            "Montaña de la Mesa": 3500,
            "Cataratas del Iguazú": 4000,
            "Monte Everest": 11000,
            "Parque Nacional de Yellowstone": 9000,
            "Gran Muralla China": 9000
        }
    },
    {
        "Nombre": "Parque Nacional de Yellowstone",
        "Tipo": "natural",
        "Pais": { "Estados Unidos"},
        "Distancias": {
            "Parque Nacional de Komodo": 15000,
            "Montaña de la Mesa": 14000,
            "Cataratas del Iguazú": 12000,
            "Monte Everest": 9000,
            "Bahía de Ha Long": 9000,
            "Gran Muralla China": 11000
        }
    }
]

print()
print('Punto A B')

#se agregan lso vertices

for dato in datos:
        miGrafo.insert_vertice(Maravilla(dato["Nombre"], dato["Pais"], dato["Tipo"], dato["Distancias"]), criterio='nombre')

#aristas

for i in range(miGrafo.size() -1): #se resta para ecitar el fuera de rango
       origen = miGrafo.get_element_by_index(i)[0].nombre
       destino = miGrafo.get_element_by_index(i+1)[0].nombre
       km = randint(1000,2000)#peso en km
       miGrafo.insert_arist(origen,destino,km,criterio_vertice='nombre')

print()
print('Punto C')

#C
arquitectonicas = miGrafo.kruskal_por_tipo('arquitectonica')
naturales = miGrafo.kruskal_por_tipo('naturales')
#print(arquitectonicas)
print()
print('Punto D')

#D determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
for a in arquitectonicas:
       value = a.split(';') #[0] origen y destino [1]peso [2]tipo
       print(f'{datos[0]}-{datos[1]} km')

for a in naturales:
       value = a.split(';') #[0] origen y destino [1]peso [2]tipo
       print(f'{datos[0]}-{datos[1]} km')

#armar dos lustas para naturales o arquitec por paises
arquitectonicasxPais=[]
naturalesxPais=[]

for i in range(miGrafo.size()):
       paises = miGrafo.get_element_by_index(i)[0].pais
       tipo = miGrafo.get_element_by_index(i)[0].tipo
       for pais in paises:
              if tipo == 'natural':
                     naturalesxPais.append(pais)
              else:
                     arquitectonicasxPais.append(pais)


existe = False
for pais in naturalesxPais:
       if pais in arquitectonicasxPais:
              existe = True
              print(f'{pais} tiene maravillas nat y arq')

if not existe:
       print('ningun pais tiene maravillas nat o arq')
print()
print('Punto E')

