from cola import Cola
from lista import Lista
import linecache

def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split

class NodeTree():

    def __init__(self, value, other_values=None):
        self.value = value
        self.other_values = other_values
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:

    #depende del get_value_form_file
    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)

    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height > right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root
    

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)


    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values['derrotado'] is not None:
                    if root.other_values['derrotado'] not in ranking:
                        ranking[root.other_values['derrotado']] = 1
                    else:
                        ranking[root.other_values['derrotado']] += 1
                __inorden_ranking(root.right, ranking)

        __inorden_ranking(self.root, ranking)

    def inorden_add_field(self):
        def __inorden_add_field(root):
            if root is not None:
                __inorden_add_field(root.left)
                root.other_values['capturado'] = None
                __inorden_add_field(root.right)

        __inorden_add_field(self.root)


    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)

    def inorden_start_with(self, cadena):
        def __inorden_start_with(root, cadena):
            if root is not None:
                __inorden_start_with(root.left, cadena)
                if root.other_values is True and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena)

    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)

        __inorden_start_with_jedi(self.root, cadena)

    """ U T I L I D A D E S"""


    #INSERTAR

    def insert_node(self, value, other_values=None):

        def __insertar(root, value, other_values):
            if root is None:
                return NodeTree(value, other_values)
            elif value < root.value:
                root.left = __insertar(root.left, value, other_values)
            else:
                root.right = __insertar(root.right, value, other_values)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(self.root, value, other_values)


    #BORRAR NODO

    def delete_node(self, key):
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value


    #BARRIDOS

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)


    #reversa

    def postorden(self): 
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    #ordenados alfabeticamente

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)


    #BUSQUEDA


    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)
    
    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)


    #CONTADORES

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count

        return __contar_heroes(self.root)
    
    
    #usadas en el parcial
    
    def search_pokemon_num(self, key):
        def __search_pokemon_num(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search_pokemon_num(root.left, key)
                else:
                    return __search_pokemon_num(root.right, key)

        return __search_pokemon_num(self.root, key)
    
    def search_by_coincidence_pokemon(self, value):
        def __search_by_coincidence_pokemon(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.other_values)
                __search_by_coincidence_pokemon(root.left, value)
                __search_by_coincidence_pokemon(root.right, value)

        __search_by_coincidence_pokemon(self.root, value)


        
       
    
    def search_by_tipo_pokemon(self, tipo):
        print(f'nombre de los pokemones tipo {tipo}')
        def __search_by_tipo_pokemon(root, tipo):
            if root is not None:
                if root.other_values['tipo'] == tipo:
                    print(root.value)
                __search_by_tipo_pokemon(root.left, tipo)
                __search_by_tipo_pokemon(root.right, tipo)

        __search_by_tipo_pokemon(self.root, tipo)

    def inorden_Tipo(self):
        def __inorden_tipo(root):
            if root is not None:
                __inorden_tipo(root.left)
                print(root.other_values)
                __inorden_tipo(root.right)

        __inorden_tipo(self.root)

    def postorden_Nombre(self): 
        def __postorden_Nombre(root):
            if root is not None:
                __postorden_Nombre(root.right)
                print(root.value, root.other_values['nombre'])
                __postorden_Nombre(root.left)

        __postorden_Nombre(self.root)
    
    def contar_Pokemon(self):
        def __contar_Pokemon(root):
            count = 0
            if root is not None:
                if root.value == 'Electrico' or root.value == 'Acero':
                    count = 1
                count += __contar_Pokemon(root.left)
                count += __contar_Pokemon(root.right)
            return count

        return __contar_Pokemon(self.root)
    
    def inordenVillanos(self):
        def __inordenVillanos(root):
            if root is not None:
                __inordenVillanos(root.left)
                if (root.other_values is False):
                    print(root.value)
                __inordenVillanos(root.right)

        __inordenVillanos(self.root)

    def search_by_coincidence_Superheroes(self, value):
        def __search_by_coincidence_Superheroes(root, value):
            if root is not None:
                if root.value.startswith(value):
                    if root.other_values is True:
                        print(root.value)
                __search_by_coincidence_Superheroes(root.left, value)
                __search_by_coincidence_Superheroes(root.right, value)

        __search_by_coincidence_Superheroes(self.root, value)

    def contar_heroes_villanos(self,arbol1,arbo2):
        def __contar_heroes_villanos(root,arbol1,arbo2):
            
            if root is not None:
                if root.other_values is True:
                    arbol1.insert_node(root.value,root.other_values)

                if root.other_values is False:
                    arbo2.insert_node(root.value,root.other_values)
                __contar_heroes_villanos(root.left,arbol1,arbo2)
                __contar_heroes_villanos(root.right,arbol1,arbo2)
           

        return __contar_heroes_villanos(self.root,arbol1,arbo2)
    
    def contar_heroes(self):
        def __contar_heroes(root):
            count = 0
            if root is not None:
                if root.other_values is True:
                    count = 1
                count += __contar_heroes(root.left)
                count += __contar_heroes(root.right)
            return count

        return __contar_heroes(self.root)
    
    def contar_villanos(self):
        def __contar_villanos(root):
            count = 0
            if root is not None:
                if root.other_values is False:
                    count = 1
                count += __contar_villanos(root.left)
                count += __contar_villanos(root.right)
            return count

        return __contar_villanos(self.root)
    
    #ejercicio 6

    def jedisRanking(self):
        def __jedisRanking(root):
            if root is not None:
                __jedisRanking(root.left)
                if root.value == 'Jedi Master':
                    print(root.other_values)
                __jedisRanking(root.right)

        __jedisRanking(self.root)
    
    def search_by_coincidence_sableLuz(self, value):
        def __search_by_coincidence_sableLuz(root, value):
            if root is not None:
                if root.other_values['color_sable'].startswith(value):
                    print(root.value)
                __search_by_coincidence_sableLuz(root.left, value)
                __search_by_coincidence_sableLuz(root.right, value)

        __search_by_coincidence_sableLuz(self.root, value)

    #ejercicio 23
    def inordenDerrotados(self):
        def __inordenDerrotados(root):
            if root is not None:
                __inordenDerrotados(root.left)
                if root.other_values['derrotadoPor']:
                    print(f'{root.value} Derrotado por: {root.other_values["derrotadoPor"]}')
                __inordenDerrotados(root.right)

        __inordenDerrotados(self.root)

    def inorden_add_field_descripcion(self):
        def __inorden_add_field_descripcion(root):
            if root is not None:
                __inorden_add_field_descripcion(root.left)
                desc = input(f'ingresar una descripcion ')
                root.other_values['descripcion'] = desc
                __inorden_add_field_descripcion(root.right)

        __inorden_add_field_descripcion(self.root)

    

    def contar_derrotas(self):
        def __contar_derrotas(root, derrotas):
            if root is not None:
                __contar_derrotas(root.left, derrotas)
                derrotado_por = root.other_values.get('derrotadoPor')
                if derrotado_por:
                    derrotas[derrotado_por] = derrotas.get(derrotado_por, 0) + 1
                __contar_derrotas(root.right, derrotas)

        derrotas = {}
        __contar_derrotas(self.root, derrotas)
        return derrotas
    
    def inordenDerrotaHeracles(self):
        def __inordenDerrotaHeracles(root):
            if root is not None:
                __inordenDerrotaHeracles(root.left)
                if root.other_values['derrotadoPor'] == 'Heracles':
                    print(f'{root.value}')
                __inordenDerrotaHeracles(root.right)

        __inordenDerrotaHeracles(self.root)

    def inordenNoDerrotados(self):
        def __inordenNoDerrotados(root):
            if root is not None:
                __inordenNoDerrotados(root.left)
                if root.other_values['derrotadoPor'] == '':
                    print(f'{root.value}')
                __inordenNoDerrotados(root.right)

        __inordenNoDerrotados(self.root)

    def modificarCriaturas(self):
        def __modificarCriaturas(root):
            if root is not None:
                __modificarCriaturas(root.left)
                if root.value == 'Cerbero':
                    root.other_values['capturadoPor'] = 'Heracles'
                if root.value == 'Toro de Creta':
                    root.other_values['capturadoPor'] = 'Heracles'
                if root.value == 'Cierva Cerinea':
                    root.other_values['capturadoPor'] = 'Heracles'
                if root.value == 'Jabali de Erimanto':
                    root.other_values['capturadoPor'] = 'Heracles'
                
                print(root.other_values)
                __modificarCriaturas(root.right)

        __modificarCriaturas(self.root)
    
    def agregarAves(self):
        def __agregarAves(root):
            if root is not None:
                __agregarAves(root.left)
                if root.value == 'Aves de Estinfalo':
                    root.other_values['derrotadoPor'] = 'Heracles derroto a varias'
                __agregarAves(root.right)

        __agregarAves(self.root)

    def capturadasPorHeracles(self):
        def __capturadasPorHeracles(root):
            if root is not None:
                __capturadasPorHeracles(root.left)
                if root.other_values['capturadoPor'] == 'Heracles':
                    print(root.value)
                __capturadasPorHeracles(root.right)

        __capturadasPorHeracles(self.root)

    #ejercicio 6
    def mostrarJediRank(self, file_name):
        def __mostrarJediRank(root, file_name):
            if root is not None:
                __mostrarJediRank(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if root.value == 'jedi master':
                    print(root.value, value[0])
                __mostrarJediRank(root.right, file_name)

        __mostrarJediRank(self.root, file_name)
    
    def jediEspecie(self, file_name, especie):
        def __jediEspecie(root, file_name, especie):
            if root is not None:
                __jediEspecie(root.left, file_name, especie)
                value = get_value_from_file(file_name, root.other_values)
                if especie in root.value:
                    print(value[0], value[1])
                __jediEspecie(root.right, file_name, especie)

        __jediEspecie(self.root, file_name, especie)

    def listarComienzan(self, file_name):
        def __listarComienzan(root, file_name):
            if root is not None:
                __listarComienzan(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if value[0].startswith('a') or '-' in value[0]:
                    print(root.value, value[0])
                __listarComienzan(root.right, file_name)

        __listarComienzan(self.root, file_name)

        
    def inorden_file2(self, file_name):
        def __inorden_file2(root, file_name):
            if root is not None:
                __inorden_file2(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                if value[3] != '-':
                  if value[3] in value:
                      print(root.value)
                __inorden_file2(root.right, file_name)

        __inorden_file2(self.root, file_name)

            
            
        
        


        



    




    
   

       
       

