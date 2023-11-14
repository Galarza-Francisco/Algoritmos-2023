#Dado un archivo con todos los Jedi, de los que se cuenta con: nombre, especie, año de naci-
#miento, color de sable de luz, ranking (Jedi Master, Jedi Knight, Padawan) y maestro, los últimos

#tres campos pueden tener más de un valor. Escribir las funciones necesarias para resolver las
#siguientes consignas:
#a. crear tres árboles de acceso a los datos: por nombre, ranking y especie;
#b. realizar un barrido inorden del árbol por nombre y ranking;
#c. realizar un barrido por nivel de los árboles por ranking y especie;
#d. mostrar toda la información de Yoda y Luke Skywalker;
#e. mostrar todos los Jedi con ranking “Jedi Master”;
#f. listar todos los Jedi que utilizaron sabe de luz color verde;
#g. listar todos los Jedi cuyos maestros están en el archivo;
#h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;
#i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.


from arbol_ejercicios import BinaryTree, get_value_from_file

file_jedi = open('jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

arbolNombre = BinaryTree()
arbolRanking = BinaryTree()
arbolEspecie = BinaryTree()

read_lines.pop(0) #elimina la primera linea que es el encabezado
for index, linea_jedi in enumerate(read_lines):
    jedi = linea_jedi.split(';') #Para cada línea, se divide la línea en campos con ; como separador y se almacena en la var jedi
    jedi.pop() #Elimina el ultimo campo de cada linea que fue separado por la instruccion anterior
    arbolNombre.insert_node(jedi[0], index+2)     #index en Python comienza en 0, pero los datos en el archivo estan 
    arbolRanking.insert_node(jedi[1], index+2)  #a partir de la linea 2 (linea 1 contiene el encabezado)
    arbolEspecie.insert_node(jedi[2], index+2)   #para compensar ese desplazamiento y que las lineas de datos se asocien con la clave correcta de cada arbol se usa el '+2'



#b. realizar un barrido inorden del árbol por nombre y ranking;

#arbolNombre.inorden()
#arbolRanking.inorden()

#c. realizar un barrido por nivel de los árboles por ranking y especie;

#arbolRanking.by_level()
#arbolEspecie.by_level()

#d. mostrar toda la información de Yoda y Luke Skywalker;


#pos = arbolNombre.search('yoda'.swapcase().lower())
#if pos:
#     print(get_value_from_file('jedis.txt', pos.other_values))

#pos2 = arbolNombre.search('luke skywalker'.swapcase().lower())
#if pos2:
#     print(get_value_from_file('jedis.txt', pos2.other_values))



#e. mostrar todos los Jedi con ranking “Jedi Master”;

#arbolRanking.mostrarJediRank('jedis.txt')

#f. listar todos los Jedi que utilizaron sabe de luz color verde;

#arbolNombre.inorden_file_lightsaber('jedis.txt', 'green')

#g. listar todos los Jedi cuyos maestros están en el archivo;
print('los jedis cuyos maestros estan dentro del archivo son:')
arbolNombre.inorden_file2('jedis.txt')

#h. mostrar todos los Jedi de especie “Togruta” o “Cerean”;

#arbolEspecie.jediEspecie('jedis.txt', 'cerean')

#i. listar los Jedi que comienzan con la letra A y los que contienen un “-” en su nombre.

#arbolNombre.listarComienzan('jedis.txt')