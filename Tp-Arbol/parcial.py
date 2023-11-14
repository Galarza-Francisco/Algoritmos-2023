from arbolBinario import BinaryTree


def ejercicioArbol():
    
    pokemones = [
        {'nombre':'Bulbasaur', 'numero':1, 'tipo':'Planta'},
        {'nombre':'Bulivysaur', 'numero':2, 'tipo':'Planta'},
        {'nombre':'Charmander', 'numero':5, 'tipo':'Fuego'},
        {'nombre':'Jolteon,', 'numero':6, 'tipo':'Electrico'},
        {'nombre':'Lycanroc', 'numero':8, 'tipo':'Roca'},
        {'nombre':'Tyrantrum;', 'numero':10 , 'tipo':'Roca'},
    ]

    arbol = BinaryTree()
    arbolNombre = BinaryTree()
    arbolNumero = BinaryTree()
    arbolTipo = BinaryTree()

    for pokemon in pokemones:
        nombre = pokemon['nombre']
        numero = pokemon['numero']
        tipo = pokemon['tipo']

        arbolNombre.insert_node(pokemon['nombre'], pokemon)
        arbolNumero.insert_node(pokemon['numero'], pokemon)
        arbolTipo.insert_node(pokemon['tipo'], pokemon)


    #punto b
    #primera parte
    """pos = arbolNumero.search_pokemon_num(5)"""

    #segunda parte
    """if pos:
        print(pos.other_values)

    poke = input('ingresar indicios de nombre ')
    arbolNombre.search_by_coincidence(poke)
    nombrePoke = input('Elegir uno de los nombres posibles ')
    arbolNombre.search_by_coincidence_pokemon(nombrePoke)"""

    #punto C
    """tipoPokemon = input('ingresar el tipo de pokemon que desea buscar [Agua/Fuego/Planta/Electrico]')
    arbolNombre.search_by_tipo_pokemon(tipoPokemon)"""
    
    #punto D
    """arbolNumero.postorden_Nombre()
    arbolNombre.inorden()"""

    #punto E
     
"""    value = input('ingresar el nombre que desea Buscar ') # waler lo dejo variable pero es cuestion de cargar el nombre del pokemon
    pos = arbolNombre.search(value)
    if pos:
        pokemon = pos.other_values
        print(pokemon)
    else:
        print('no se encuentra ')"""


    #punto F
"""    cantidadPoke = arbolTipo.contar_Pokemon()
    print(cantidadPoke)
"""
ejercicioArbol()

