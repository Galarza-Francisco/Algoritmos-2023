from lista_de_lista import Lista
from listaClass import Lista as listaSimple
from random import randint


class Entrenador():

    def __init__(self, nombre, ct_ganados=0, cb_perdidas=0, cb_ganadas=0):
        self.nombre = nombre
        self.ct_ganados = ct_ganados
        self.cb_perdidas = cb_perdidas
        self.cb_ganadas = cb_ganadas

    def __str__(self):
        return f'{self.nombre} --> ctg:{self.ct_ganados}-cbg{self.cb_ganadas}-cbp{self.cb_perdidas}'

class Pokemon():

    def __init__(self, nombre, tipo, nivel=1, subtipo=None):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre}-{self.nivel}-{self.tipo}-{self.subtipo}'


e1 = Entrenador('Juan', ct_ganados=randint(1, 10), cb_perdidas=randint(1,10), cb_ganadas=randint(1,10))
e2 = Entrenador('Maria', ct_ganados=randint(1, 10), cb_perdidas=randint(1,10), cb_ganadas=randint(1,10))
e3 = Entrenador('Ana', ct_ganados=randint(1, 10), cb_perdidas=randint(1,10), cb_ganadas=randint(1,10))

entrenadores = [e1, e2, e3]

lista_entrenadores = Lista()
    
p1 = Pokemon('pikachu', 'electrico', randint(1, 20))
p2 = Pokemon('jolteon', 'electrico', randint(1, 20))
p3 = Pokemon('vaporeon', 'agua', randint(1, 20))
p4 = Pokemon('flareon', 'fuego', randint(1, 20))
p5 = Pokemon('leafeon', 'planta', randint(1, 20))
p6 = Pokemon('jolteon', 'electrico', randint(1, 20))

pokemons = [p1, p2, p3, p4, p5]

#! lista principal
for entrenador in entrenadores:
    lista_entrenadores.insert(entrenador, 'nombre')

#! lista secundaria
for pokemon in pokemons:
    numero_entrenador = randint(0, lista_entrenadores.size()-1)
    entrenador = lista_entrenadores.get_element_by_index(numero_entrenador)
    entrenador[1].insert(pokemon, 'nombre')


lista_entrenadores.barrido_entrenadores()
print()
print('punto A')

#!A
pos = lista_entrenadores.search('Juan', 'nombre')
if pos is not None:
    valor = lista_entrenadores.get_element_by_index(pos)
    entrenador, sublista = valor[0], valor[1]
    print(f'{entrenador.nombre} tiene {sublista.size()} pokemons')

print()
print('punto B')
#!B
lista_entrenadores.barrido_cantidad_torneos_ganados(9)

print()
print('punto C')
# ! C
mayor_cantidad = lista_entrenadores.get_element_by_index(0)[0].ct_ganados
pos_mayor = 0

for pos in range(1, lista_entrenadores.size()):
    entrenador = lista_entrenadores.get_element_by_index(pos)[0]
    if entrenador.ct_ganados > mayor_cantidad:
        pos_mayor = pos
        mayor_cantidad = entrenador.ct_ganados

valor = lista_entrenadores.get_element_by_index(pos_mayor)
entrenador, sublista = valor[0], valor[1]

if sublista.size() > 0:
    pokemon_mayor = sublista.get_element_by_index(0)
    for pos in range(1, sublista.size()):
        pokemon = sublista.get_element_by_index(pos)
        if pokemon.nivel > pokemon_mayor.nivel:
            pokemon_mayor = pokemon

print(f'El pokemon de mayor nivel del entrenador {entrenador.nombre} es {pokemon_mayor.nombre} {pokemon_mayor.nivel} ')

print()
print('punto D')

# ! D

def mostrar_datos_entrenador_y_pokemons(entrenador_nombre, lista_entrenadores):
    pos = lista_entrenadores.search(entrenador_nombre, 'nombre')
    if pos is not None:
        valor = lista_entrenadores.get_element_by_index(pos)
        entrenador, sublista_pokemons = valor[0], valor[1]

        print(f'Datos del entrenador {entrenador.nombre}:')
        print(f'Cantidad de torneos ganados: {entrenador.ct_ganados}')
        print(f'Cantidad de batallas perdidas: {entrenador.cb_perdidas}')
        print(f'Cantidad de batallas ganadas: {entrenador.cb_ganadas}')
        print('Pokémons:')
        sublista_pokemons.barrido()
    else:
        print(f'El entrenador {entrenador_nombre} no se encontró en la lista.')

nombre_entrenador = 'Juan'  
mostrar_datos_entrenador_y_pokemons(nombre_entrenador, lista_entrenadores)


print()
print('punto E')

# ! E

def calcular_porcentaje_batallas_ganadas(entrenador):
    if entrenador.cb_ganadas == 0:
        return 0
    total_batallas = entrenador.cb_ganadas + entrenador.cb_perdidas
    porcentaje = (entrenador.cb_ganadas / total_batallas) * 100
    return porcentaje

def listar_entrenadores_porcentaje_batallas_ganadas(lista_entrenadores):
    for pos in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(pos)[0]
        porcentaje = calcular_porcentaje_batallas_ganadas(entrenador)
        if porcentaje > 79:
            print(f'{entrenador.nombre} tiene un porcentaje de batallas ganadas del {porcentaje}%.')
        else: 
            print(f'el entrenador {entrenador.nombre} esta por debajo del 79%')

listar_entrenadores_porcentaje_batallas_ganadas(lista_entrenadores)

# print()
# print('punto F')

def mostrar_datos_entrenador_y_pokemons(entrenador_nombre, lista_entrenadores):
    pos = lista_entrenadores.search(entrenador_nombre, 'nombre')
    if pos is not None:
        valor = lista_entrenadores.get_element_by_index(pos)
        entrenador, sublista_pokemons = valor[0], valor[1]

        print(f'Datos del entrenador {entrenador.nombre}:')
        print(f'Cantidad de torneos ganados: {entrenador.ct_ganados}')
        print(f'Cantidad de batallas perdidas: {entrenador.cb_perdidas}')
        print(f'Cantidad de batallas ganadas: {entrenador.cb_ganadas}')
        print('Pokémons:')
        sublista_pokemons.barrido()
    else:
        print(f'El entrenador {entrenador_nombre} no se encontró en la lista.')

nombre_entrenador = 'Juan'  
mostrar_datos_entrenador_y_pokemons(nombre_entrenador, lista_entrenadores)


print()
print('punto F')

#! F

def entrenadores_con_tipos_pokemon(lista_entrenadores):
    
    for pos in range(lista_entrenadores.size()):
        value = lista_entrenadores.get_element_by_index(pos)
        entrenador, sublista_pokemons = value[0], value[1]
        
        for pos_pokemon in range(sublista_pokemons.size()):
            pokemon = sublista_pokemons.get_element_by_index(pos_pokemon)
            if pokemon.tipo == 'fuego' and 'planta':
                print(f'{entrenador.nombre} tiene pokemon de fuego y planta ')
            if pokemon.tipo == 'agua' and 'volador':
                print(f'{entrenador.nombre} tiene pokemon de tipo volador/agua')

entrenadores_con_tipos_pokemon(lista_entrenadores)


print()
print('punto G')

#! G
def promedioPokemonEntrenador(entrenador_nombre, lista_entrenadores):
    pos = lista_entrenadores.search(entrenador_nombre, 'nombre')
    if pos is not None:
        valor = lista_entrenadores.get_element_by_index(pos)
        entrenador, sublista_pokemons = valor[0], valor[1]
        if sublista_pokemons.size() > 0:
            suma_niveles = 0
            for i in range(sublista_pokemons.size()):
                poke = sublista_pokemons.get_element_by_index(i)
                suma_niveles += poke.nivel
            promedio = suma_niveles / sublista_pokemons.size()
            print(f'El promedio de nivel de los Pokémon de {entrenador.nombre} es {promedio}%')
        else:
            print(f'El entrenador {entrenador.nombre} no tiene Pokémon.')

promedioPokemonEntrenador('Maria', lista_entrenadores)


print()
print('punto H')

#! H

def determinadoPokemon(nombre_poke, lista_entrenadores):
    for i in range(lista_entrenadores.size()):
        value = lista_entrenadores.get_element_by_index(i)
        entrenador, sublista_pokemons = value[0], value[1]

        for a in range(sublista_pokemons.size()):
            pokemon = sublista_pokemons.get_element_by_index(a)
            if pokemon.nombre == nombre_poke:
                print(f'{entrenador} tiene en sus pokemones a {nombre_poke}')


determinadoPokemon('pikachu', lista_entrenadores)



print()
print('punto I')

#! I

def mostrar_entrenadores_con_pokemons_repetidos(lista_entrenadores):
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        sublista_pokemons = entrenador[1]
        nombres_pokemons = set()
        tiene_repetidos = False
        
        for j in range(sublista_pokemons.size()):
            pokemon = sublista_pokemons.get_element_by_index(j)
            if pokemon.nombre in nombres_pokemons:
                tiene_repetidos = True
                break
            nombres_pokemons.add(pokemon.nombre)
        
        if tiene_repetidos:
            print(f'El entrenador {entrenador[0].nombre} tiene Pokémon repetidos.')

mostrar_entrenadores_con_pokemons_repetidos(lista_entrenadores)

print()
print('punto J')

#! J
def entrenadores_con_pokemons_especificos(lista_entrenadores, nombres_pokemons):
    entrenadores_encontrados = []
    
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        sublista_pokemons = entrenador[1]
        
        for j in range(sublista_pokemons.size()):
            pokemon = sublista_pokemons.get_element_by_index(j)
            if pokemon.nombre in nombres_pokemons:
                entrenadores_encontrados.append(entrenador[0])
                break
    
    return entrenadores_encontrados


nombres_pokemons_buscar = ['Tyrantrum', 'Terrakion', 'Wingull']

entrenadores_encontrados = entrenadores_con_pokemons_especificos(lista_entrenadores, nombres_pokemons_buscar)
if len(entrenadores_encontrados) > 0:
    print('Entrenadores con Pokémon específicos encontrados:')
    for entrenador in entrenadores_encontrados:
        print(entrenador.nombre)
else:
    print('No se encontraron entrenadores con los Pokémon especificados.')


print()
print('punto k')

#! k
def buscar_entrenador_y_pokemon(lista_entrenadores, nombre_entrenador, nombre_pokemon):
    for i in range(lista_entrenadores.size()):
        entrenador = lista_entrenadores.get_element_by_index(i)
        if entrenador[0].nombre == nombre_entrenador:
            sublista_pokemons = entrenador[1]
            
            for j in range(sublista_pokemons.size()):
                pokemon = sublista_pokemons.get_element_by_index(j)
                if pokemon.nombre == nombre_pokemon:
                    return entrenador[0], pokemon
    
    return None, None

nombre_entrenador_buscar = input('Ingrese el nombre del entrenador: ')
nombre_pokemon_buscar = input('Ingrese el nombre del Pokémon: ')

entrenador_encontrado, pokemon_encontrado = buscar_entrenador_y_pokemon(lista_entrenadores, nombre_entrenador_buscar, nombre_pokemon_buscar)

if entrenador_encontrado is not None and pokemon_encontrado is not None:
    print(f'Datos del entrenador {entrenador_encontrado.nombre}:')
    print(f'Cantidad de torneos ganados: {entrenador_encontrado.ct_ganados}')
    print(f'Cantidad de batallas perdidas: {entrenador_encontrado.cb_perdidas}')
    print(f'Cantidad de batallas ganadas: {entrenador_encontrado.cb_ganadas}')
    
    print(f'Datos del Pokémon {pokemon_encontrado.nombre}:')
    print(f'Nivel: {pokemon_encontrado.nivel}')
    print(f'Tipo: {pokemon_encontrado.tipo}')
    print(f'Subtipo: {pokemon_encontrado.subtipo}')
else:
    print('No se encontró al entrenador o al Pokémon especificado.')
