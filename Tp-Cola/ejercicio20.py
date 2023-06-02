from colaClass import Cola
from random import choice

data = [
    {'vehiculo':'automoviles', 'tarifa':47},
    {'vehiculo':'camionetas', 'tarifa':59},
    {'vehiculo':'camiones', 'tarifa':71},
    {'vehiculo':'colectivos', 'tarifa':64},
]

cabina1 = Cola()
cabina2 = Cola()
cabina3 = Cola()

for i in range(30):
    value = choice(data)
    cabina1.arrive(value)
    value2 = choice(data)
    cabina2.arrive(value2)
    value3 = choice(data)
    cabina3.arrive(value3)

def Listar(dato):
    cont = 0
    total = dato.size()
    while cont < total:
        value = dato.move_to_end()
        print('| vehiculo:', value['vehiculo'])
        print('| Tarifa  :', value['tarifa'])
        print()
        cont +=1

def TotalRecaudo(data):
    cont = 0
    total = data.size()
    recaudo = 0

    while cont < total:
        value = data.atention()
        vehiculo = value['vehiculo']
        tarifa = value['tarifa']
        if vehiculo == 'automoviles':
            recaudo += tarifa
        elif vehiculo == 'camionetas':
            recaudo += tarifa
        elif vehiculo == 'camiones':
            recaudo += tarifa
        elif vehiculo == 'colectivos':
            recaudo += tarifa
        else:
            print('el vehiculo no esta dentro de la lista del peaje')
        cont +=1

    return recaudo

def mayorRecaudo(data1, data2, data3):
    
    if (data1 > data2) and (data1 > data3):
        print('la mayor recaudacion la tiene la cabina 1')
    elif (data2 > data1) and (data2 > data3):
        print('la mayor recaudacion la tiene la cabina 2')
    elif (data3 > data1) and (data3 > data2):
        print('la mayor recaudacion la tiene la cabina 3')
    else:
        print('las cabinas 3 tienen la misma recaudacion')    

def cantidadVehiculos(data):
    cont = 0
    total = data.size()
    autos = 0
    camionetas = 0
    camiones = 0
    colectivos = 0

    while cont < total:
        
        value = data.move_to_end()
        vehiculo = value['vehiculo']
        if vehiculo == 'automoviles':
            autos +=1
        elif vehiculo == 'camionetas':
            camionetas += 1
        elif vehiculo == 'camiones':
            camiones += 1
        elif vehiculo == 'colectivos':
            colectivos +=1
        else:
            print('no se encontro el vechiulo en la lista de precios')

        cont += 1

    print(f'cantidad de vehiculos que pasaron por esta cabina: ')
    print(f'Autos:      {autos}')
    print(f'Camionetas: {camionetas}')
    print(f'Camiones:   {camiones}')
    print(f'Colectivos: {colectivos}')


#----------ejercicio a----------

# print('--- cabina 1---')
# Listar(cabina1)
# print()
# print('--- cabina 2---')
# Listar(cabina2)
# print()
# print('--- cabina 3---')
# Listar(cabina3)

#----------ejercicio b----------

# print('--cabina 1--')
# recaudoCabina1 = TotalRecaudo(cabina1)
# print(f'recaudo total cabina: ${recaudoCabina1}')
# print('--cabina 2--')
# recaudoCabina2 = TotalRecaudo(cabina2)
# print(f'recaudo total cabina: ${recaudoCabina2}')
# print('--cabina 3--')
# recaudoCabina3 = TotalRecaudo(cabina3)
# print(f'recaudo total cabina: ${recaudoCabina3}')
# print()
# print()

#----------ejercicio c----------

# mayorRecaudo(recaudoCabina1,recaudoCabina2,recaudoCabina3)


#----------ejercicio d----------

print('--- cabina 1---')
cantidadVehiculos(cabina1)
print()
print('--- cabina 2---')
cantidadVehiculos(cabina2)
print()
print('--- cabina 3---')
cantidadVehiculos(cabina3)