#Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
#resuelva las siguientes consultas:
#a. listado inorden de las criaturas y quienes la derrotaron;
#b. se debe permitir cargar una breve descripción sobre cada criatura;
#c. mostrar toda la información de la criatura Talos;
#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
#e. listar las criaturas derrotadas por Heracles;
#f. listar las criaturas que no han sido derrotadas;
#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
#o dios que la capturo;
#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;
#i. se debe permitir búsquedas por coincidencia;
#j. eliminar al Basilisco y a las Sirenas;
#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias;
#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#m. realizar un listado por nivel del árbol;
#n. muestre las criaturas capturadas por Heracles.


from arbol_ejercicios import BinaryTree
from lista import Lista

criaturas = [    {'nombre' : "Ceto", 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Tifon', 'derrotadoPor' : 'Zeus', 'descripcion' : '', 'capturadoPor' : ''},
                 {'nombre' : 'Equidna', 'derrotadoPor' : 'Argos Panoptes', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Dino', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Pefredo', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Enio', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Escila', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Medusa', 'derrotadoPor' : 'Perseo', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Ladon', 'derrotadoPor' : 'Heracles', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre': 'Ortro', 'derrotadoPor': 'Heracles', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Talos', 'derrotadoPor' : 'Medea', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Cerbero', 'derrotadoPor' : 'Teseo', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Toro de Creta', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Jabali de Erimanto', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Cierva Cerinea', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Aves de Estinfalo', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Basilisco', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''},
                 {'nombre' : 'Sirenas', 'derrotadoPor' : '', 'descripcion': '', 'capturadoPor' : ''}
]
arbol = BinaryTree()

for criatura in criaturas:
    arbol.insert_node(criatura['nombre'], criatura)

#A
#arbol.inordenDerrotados()

#B
#arbol.inorden_add_field_descripcion()
#arbol.inorden()

#C
#pos = arbol.search('Talos')
#if pos:
#    print(pos.other_values)


#D. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

# Crear el árbol de derrotas
#arbolDerrota = BinaryTree()
#for i in criaturas:
#    if i['derrotadoPor']:
#        arbolDerrota.insert_node(i['derrotadoPor'], i)


# Contar las derrotas para los tres principales
#derrotas = arbolDerrota.contar_derrotas()

# Obtener los tres principales
#top_tres = sorted(derrotas.items(), key=lambda x: x[1], reverse=True)[:3]

# Mostrar los resultados
#print("Los tres héroes o dioses que derrotaron a la mayor cantidad de criaturas son:")
#for heroe, cantidad in top_tres:
#    print(f"{heroe}: {cantidad} criaturas derrotadas")



#e. listar las criaturas derrotadas por Heracles;
#arbol.inordenDerrotaHeracles()

#f. listar las criaturas que no han sido derrotadas;
#arbol.inordenNoDerrotados()

#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
#Erimanto indicando que Heracles las atrapó;

#arbol.modificarCriaturas()

#i. se debe permitir búsquedas por coincidencia;

#aux = input('ingresar nombre para buscar ')
#arbol.search_by_coincidence(aux)


#j. eliminar al Basilisco y a las Sirenas;
#arbol.delete_node('Basilisco')
#arbol.delete_node('Sirenas')


#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
#derroto a varias;
#arbol.agregarAves()


#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
#aux = input('ingresar el nomnre por el cual queres cambiar ')
#pos = arbol.search('Ladon')
#if pos:
#    valores = pos.other_values
#    arbol.delete_node('Ladon')
#    arbol.insert_node(aux, valores)


#m. realizar un listado por nivel del árbol;
#arbol.by_level()

#n. muestre las criaturas capturadas por Heracles.

#arbol.capturadasPorHeracles()