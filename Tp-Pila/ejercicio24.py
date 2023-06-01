class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def push(self, dato):
        self.__elements.append(dato)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]

pila_mcu = Pila()
pila_mcu.push({'nombre': 'Iron Man', 'peliculas': 3})
pila_mcu.push({'nombre': 'Groot', 'peliculas': 4})
pila_mcu.push({'nombre': 'Captain America', 'peliculas': 9})
pila_mcu.push({'nombre': 'Thor', 'peliculas': 5})
pila_mcu.push({'nombre': 'Hulk', 'peliculas': 3})
pila_mcu.push({'nombre': 'Black Widow', 'peliculas': 6})
pila_mcu.push({'nombre': 'Hawkeye', 'peliculas': 4})
pila_mcu.push({'nombre': 'Rocket Raccoon', 'peliculas': 5})

letras = ['C', 'D', 'G']

#punto1

def pos_RocketRaccoon_Groot(pila):
    pos_Rocket = None
    pos_Groot = None
    pila_aux = Pila()

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['nombre'] == 'Rocket Raccoon':
            pos_Rocket = pila.size() + 1
        if personaje['nombre'] == 'Groot':
            pos_Groot = pila.size() + 1 
        pila_aux.push(personaje)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return pos_Rocket, pos_Groot

#punto 2

def mas_5_pelis(pila):
    personajes=[]

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['peliculas'] > 5:
            personajes.append((personaje['nombre'], personaje['peliculas']))
    return personajes

#punto 3

def black_widow_peli(pila):
    pila_aux = Pila()
    contador_peli = 0

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)
        if personaje['nombre'] == "Black Widow":
            contador_peli = personaje['peliculas']
        
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())
    
    return contador_peli

contador_peli = black_widow_peli(pila_mcu)
print('peliculas que participo Black Widow:', contador_peli)


#punto4

def buscados_iniciales(pila):
    pila_aux = Pila()
    iniciales = []

    while pila.size() > 0:
        personaje = pila.pop()
        pila_aux.push(personaje)
        nombre = personaje['nombre']
        if nombre.startswith('C') or nombre.startswith('D') or nombre.startswith('G'):
            iniciales.append(personaje)
    
    while pila_aux.size() > 0:
        pila.push(pila_aux.pop())

    return iniciales


#4

iniciales = buscados_iniciales(pila_mcu)
print('personajes que inician con c - d - g')
for personaje in iniciales:
    print(personaje['nombre'])


#respuestas


#1

pos_Rocket, pos_Groot = pos_RocketRaccoon_Groot(pila_mcu)
print('posicion Rocket: ',pos_Rocket,'posicion Groot: ', pos_Groot)

#2

personajes_mas_cinco = mas_5_pelis(pila_mcu)
print('personajes con mas de 5 peliculas:')
for personaje, peliculas in personajes_mas_cinco:
    print(personaje,'cant. peliculas: ', peliculas)
