from listaClass import Lista
from colaClass import Cola

lista = Lista()
listaAux = Lista()

class Personaje():
    def __init__(self, superheroe, personaje, grupo, año):

        self.superheroe = superheroe
        self.personaje = personaje
        self.grupo = grupo
        self.año = año
    
    def __str__(self):
        print()
        return (f'superheroe: {self.superheroe} | personaje: {self.personaje} | grupo: {self.grupo} | año: {self.año}')

datosAux = [
    {
        "superheroe": "Black Cat",
        "personaje": "Felicia Hardy",
        "grupo": "Spider Man",
        "año": 1979
    },
    {
        "superheroe": "Hulk",
        "personaje": "Bruce Banner",
        "grupo": "Avengers",
        "año": 1962
    },
    {
        "superheroe": "Rocket Racoonn",
        "personaje": "Rocket",
        "grupo": "Guardians of the Galaxy",
        "año": 1976
    },
    {
        "superheroe": "Loki",
        "personaje": "Loki Laufeyson",
        "grupo": "Avengers",
        "año": 1949
    },
]
datos = [
    {
        "superheroe": "Vlanck Widow",
        "personaje": "Natasha Romanoff",
        "grupo": "Avengers",
        "año": 2010
    },
    {
        "superheroe": "Capitan America",
        "personaje": "Steve Rogers",
        "grupo": "Avengers",
        "año": 1941
    },
    {
        "superheroe": "Falcon",
        "personaje": "Sam Wilson",
        "grupo": "Avengers",
        "año": 1969
    },
    {
        "superheroe": "Hawkeye",
        "personaje": "Clint Barton",
        "grupo": "Avengers",
        "año": 1964
    },
    {
        "superheroe": "Hulk",
        "personaje": "Bruce Banner",
        "grupo": "Avengers",
        "año": 1962
    },
    {
        "superheroe": "Iron Man",
        "personaje": "Tony Stark",
        "grupo": "Avengers",
        "año": 1963
    },
    {
        "superheroe": "Scarlet Witch",
        "personaje": "Wanda Maximoff",
        "grupo": "Avengers",
        "año": 1964
    },
    {
        "superheroe": "Thor",
        "personaje": "Thor Odinson",
        "grupo": "Avengers",
        "año": 1963
    },
    {
        "superheroe": "Vision",
        "personaje": "Vision",
        "grupo": "Avengers",
        "año": 1968
    },
    {
        "superheroe": "War Machine",
        "personaje": "James Rhodes",
        "grupo": "Avengers",
        "año": 1979
    },
    {
        "superheroe": "Ant-Man",
        "personaje": "Scott Lang",
        "grupo": "Avengers",
        "año": 1979
    },
    {
        "superheroe": "Wasp",
        "personaje": "Janet Van Dyne",
        "grupo": "Avengers",
        "año": 1963
    },
    {
        "superheroe": "Black Panther",
        "personaje": "T'Challa",
        "grupo": "Avengers",
        "año": 1966
    },
    {
        "superheroe": "Doctor Strange",
        "personaje": "Stephen Strange",
        "grupo": "Masters of the Mystic Arts",
        "año": 1963
    },
     {
        "superheroe": "Vision",
        "personaje": "Vision",
        "grupo": "Avengers",
        "año": 1968
    },
    {
        "superheroe": "Spider-Man",
        "personaje": "Peter Parker",
        "grupo": "Spider-Man",
        "año": 1962
    },
    {
        "superheroe": "Star-Lord",
        "personaje": "Peter Quill",
        "grupo": "Guardianes de las galaxias",
        "año": 1976
    }
]

for i in datos:
    value = Personaje(i['superheroe'], i['personaje'], i['grupo'], i['año'])
    lista.insert(value, 'superheroe')

for i in datosAux:
    value = Personaje(i['superheroe'], i['personaje'], i['grupo'], i['año'])
    listaAux.insert(value, 'superheroe')


def puntoA(data):
    aux = False
    
    for i in range(data.size()):
        value = data.get_element_by_index(i) #se podria hacer con get_element_by_value (revisar)
        if (value.superheroe == 'Capitana Marvel'):
            aux = True
            print(f'se encontro el personaje de capitana marvel, su nomre es {value.personaje}')
        
    if aux == False:
        print('No se encontro capitana marvel en la lista de superheroes')

def puntoB(data):
    cola = Cola()
    aux = False
    for i in range(data.size()):
        value = data.get_element_by_index(i)
        if (value.grupo == 'Guardianes de las galaxias'):
            aux = True
            cola.arrive(value)
    
    print(f'los superheroes que pertenecen a el grupo Guardianes de las galaxias son: {cola.size()}')

    if aux == False:
        print('no se encontraron personajes del grupo Guardianes de las galaxias')

def puntoC(data):
    fantasticos = Lista()
    guardianes = Lista()
    for i in range(data.size()):
        value = data.get_element_by_index(i)
        if (value.grupo == 'Los Cuatro Fantasticos'):
            fantasticos.insert(value, 'superheroe')
        elif (value.grupo == 'Guardianes de las galaxias'):
            guardianes.insert(value, 'superheroe')
    
    if fantasticos.size() > 0:
        print('Lista de los cuatro fantasticos')
        fantasticos.order_by('superheroe', True)
        fantasticos.barrido()
    else:
        print('no se contraron personajes del grupo los cuatro fantasticos')
    if guardianes.size() > 0:
        print()
        print('lista Guardianes de las galaxias')
        guardianes.order_by('superheroe', True)
        guardianes.barrido()
    else:
        print('no se encontraton personajes de las guerras de las galaxias')


def puntoD(data):
    aux = False
    for i in range(data.size()):
        value = data.get_element_by_index(i)
        if (value.personaje != '') and (value.año > 1960):
            print(value)

def puntoE(data):
    value = data.get_element_by_value('Vlanck Widow', 'superheroe')
    # data.set_value('Vlanck Widow','Black Widow','superheroe') tengo un error de que no se puede ordenar por este criterio, tiene conflicto con la funcion criterio de compracion
    value.superheroe = 'Black Widow'


def puntoF(data,dataAux):
    for i in range(dataAux.size()):
        nuevo = dataAux.get_element_by_index(i)
        if (data.get_element_by_value(nuevo.superheroe, 'superheroe' )):
            print(f'El personaje {nuevo.superheroe} ya se encuentra cargado en la lista original')
        else:
            print(f'Cargando a {nuevo.superheroe}')
            data.insert(nuevo, 'superheroe')


def puntoG(data):
    for i in range(data.size()):
        value = data.get_element_by_index(i)
        
        if (value.personaje[0] == 'C'):
            print(f'Personaje con inicial C: {value.personaje}')
        elif (value.personaje[0] == 'P'):
            print(f'Personaje con inicial P: {value.personaje}')
        elif (value.personaje[0] == 'S'):
            print(f'Personaje con inicial S: {value.personaje}')

print('punto a')
puntoA(lista)
print()
print('punto b')
puntoB(lista)
print()
print('punto C')
puntoC(lista)
print()
print('punto D')
puntoD(lista)
print()
print('punto E')
puntoE(lista)
print()
print('punto F')
puntoF(lista, listaAux)
print()
print('punto G')
print()
puntoG(lista)

