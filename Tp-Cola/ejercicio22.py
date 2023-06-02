from colaClass import Cola

MCU = [
    {'nombre':'Tony Stark', 'superheroe':'Iron Man', 'genero':'Masc'},
    {'nombre':'Steve Rogers', 'superheroe':'Capitan América', 'genero':'Masc'},
    {'nombre':'Natasha Romanoff', 'superheroe':'Black Widow', 'genero':'Fem'},
    {'nombre':'Peter Parker', 'superheroe':'Spiderman', 'genero':'Masc'},
    {'nombre':'Profesor Hulk', 'superheroe':'Hulk', 'genero':'Masc'},
    {'nombre':'Carol Danvers', 'superheroe':'Capitana Marvel', 'genero':'Fem'},
]

cola = Cola()

for i in range(len(MCU)):
    value = MCU[i]
    cola.arrive(value)


def puntoA(datos):
    cont = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['superheroe'] == 'Capitana Marvel':
            print('el nombre de la capitana marvel es: ', value['nombre'])
        cont +=1

def puntoB(datos):
    cont = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['genero'] == 'Fem':
            print('Nombre: ',value['nombre'], 'Superheroina: ',value['superheroe'])
        cont += 1
        
def puntoC(datos):
    cont = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['genero'] == 'Masc':
            print('Nombre: ',value['nombre'])
        cont += 1

def puntoD(datos):
    cont = 0
    cont2 = 0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['nombre'] == 'Scott Lang':
            cont2 +=1
            print('el nombre del superheroe es: ', value['superheroe'])
        
        cont +=1
    
    if cont2 == 0:
        print('no se encontro el personaje')

def puntoE(datos):
    cont = 0
    total = cola.size()
    print('Personajes o Superheroes que su nombre comienza con S')
    while cont < total:
        value = datos.move_to_end()
        nombre = value['nombre']
        personaje = value['superheroe']
        genero = value['genero']
        if (nombre[0] == 'S') or (personaje[0] == 'S'):
            print()
            print(f'Nombre: {nombre} | Personaje: {personaje} | Genero: {genero}') 
        cont +=1

def puntoF(datos):
    cont = 0
    total = cola.size()
    while cont < total:
        value = datos.move_to_end()
        if value['nombre'] == 'Carol Danvers':
            print('se encontro el personaje que interpreta Carol Danvers y es: ', value['superheroe'])
        cont +=1


print('--punto A--')
puntoA(cola)
print()
print('--punto B--')
puntoB(cola)
print()
print('--punto C--')
puntoC(cola)
print()
print('--punto D--')
puntoD(cola)
print()
print('--Punto E--')
puntoE(cola)
print()
print('--Punto F--')
puntoF(cola)
print()
