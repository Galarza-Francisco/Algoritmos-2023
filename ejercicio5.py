# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic 
# Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# A. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
# que indica si es un héroe o un villano, True y False respectivamente;
# B. listar los villanos ordenados alfabéticamente;
# C. mostrar todos los superhéroes que empiezan con C;
# D. determinar cuántos superhéroes hay el árbol;
# E. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
# encontrarlo en el árbol y modificar su nombre;
# F. listar los superhéroes ordenados de manera descendente;
# G. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
# los villanos, luego resolver las siguiente tareas:
# I. determinar cuántos nodos tiene cada árbol;
# II. realizar un barrido ordenado alfabéticamente de cada árbol

from arbol_ejercicios import BinaryTree
heroes = [
    {'name': 'iron man', 'heroe': True},
    {'name': 'thanos', 'heroe': False},
    {'name': 'capitan america', 'heroe': True},
    {'name': 'red skull', 'heroe': False},
    {'name': 'hulk', 'heroe': True},
    {'name': 'black widow', 'heroe': True},
    {'name': 'rocket raccon', 'heroe': False},
    {'name': 'dotor strage', 'heroe': True},
    {'name': 'doctor octopus', 'heroe': False},
    {'name': 'deadpool', 'heroe': True},
]

arbol = BinaryTree()

#A
for heroe in heroes:
    arbol.insert_node(heroe['name'], heroe['heroe'],)
    
#B
#arbol.inordenVillanos()

#C
#arbol.search_by_coincidence_Superheroes('c')

#D
#como es contar, esta funcion me devuelve el valor del contador, tengo que meter en una variable y despues mostrarla
#cantHeroes = arbol.contar_heroes()
#print(f'La cantidad de Heroes es: {cantHeroes}')

#E
"""arbol.search_by_coincidence(input('ingresar algun dato para mostrar personajes cargados con esos nombres '))
value = input('ingrese el nombre que desea modificar ')
pos = arbol.search(value)
if pos:
     is_hero = pos.other_values
     arbol.delete_node(value)
     print('modificar')
     new_value = input('ingrese en nuevo nombre ')
     arbol.insert_node(new_value, is_hero)
else:
   print('no esta')
    """

#F
#arbol.postorden_supers()

#G
Supers = BinaryTree()
Villanos = BinaryTree()

for h in heroes:
    if h['heroe'] is True:
        Supers.insert_node(h['name'],h['heroe'])
    else:
        Villanos.insert_node(h['name'],h['heroe'])


Supers.inorden()
Villanos.inorden()

#1
cantSupers = Supers.contar_heroes()
cantVillanos = Villanos.contar_villanos()

print(f'cantidad de supers: {cantSupers} | cantidad de villanos: {cantVillanos}')


#2
print('SUPERHEROES')
print()
Supers.inorden()
print()
print('VILLANOS')
print()
Villanos.inorden()