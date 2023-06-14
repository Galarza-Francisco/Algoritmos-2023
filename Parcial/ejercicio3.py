from pilaClass import Pila

stack = Pila()



stack.push({
        "planeta": "Bespin",
        "capturado": "Lando Calrissian",
        "recompensa": 50000
})

stack.push({
        "planeta": "Tatooine",
        "capturado": "Han Solo",
        "recompensa": 100000
})

stack.push({
        "planeta": "Endor",
        "capturado": "nadie",
        "recompensa": 0
})


def puntoA(data):
    stackAux = Pila()
    while data.size() > 0:
        value = data.pop()
        stackAux.push(value)
    
    while stackAux.size() > 0:
            dato = stackAux.pop()
            print(f'Mision al planeta {dato}')
            stack.push(dato)

def puntoB(data):
    cont = 1
    stackAux = Pila()
    while data.size()>0:
        value = data.pop()
        cont += value['recompensa']
        stackAux.push(value)
    
    while stackAux.size() > 0:
        dato = stackAux.pop()
        print(f'Mision al planeta {dato}')
        stack.push(dato)

    print(f'la cantidad recaudada en las misiuones es de {cont}')


def puntoC(data):
    for i in range(data.size()):
         cont = 3
         value = data.pop()
         if value['capturado'] == 'Han Solo':
              print('se capturo a han solo en el pklaneta ', value['planeta'],'en la segunda mision', cont-i)
   

       

             
print('punto A')
print()
puntoA(stack)
print()
print('punto B')
print()
puntoB(stack)
print()
print('punto C')
print()
puntoC(stack)

