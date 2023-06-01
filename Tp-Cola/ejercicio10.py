from colaClass import Cola
from pilaClass import Pila


notificaciones = [
    {'hora:':'11:45', 'aplicacion:': 'Facebook', 'mensaje:': 'notifiacion de facebook'},
    {'hora:':'14:00', 'aplicacion:': 'Instagram', 'mensaje:': 'notifiacion de  instagram'},
    {'hora:':'9:40', 'aplicacion:': 'Twitter', 'mensaje:': 'notifiacion de twitter'},
    {'hora:':'17:55', 'aplicacion:': 'Linkedin', 'mensaje:': 'notifiacion de  linkedin'},
    {'hora:':'15:30', 'aplicacion:': 'Telegram', 'mensaje:': 'notifiacion de telegram'},
    {'hora:':'9:40', 'aplicacion:': 'Twitter', 'mensaje:': 'notifiacion de twitter desde python'},
]

cola = Cola()

for i in range(len(notificaciones)):
    cola.arrive(notificaciones[i])

def eliminarFacebook(notif):
    colaAux = Cola()
    cont = 0
    while cont < notif.size():
        value = notif.move_to_end()
        if value['aplicacion:'] != 'Facebook':
            colaAux.arrive(value)
        
        cont +=1

    return colaAux




def notifiTwitter(datos):  
    colaTwitter = Cola()

    cont = 0
    total = datos.size()
    while cont < total:
        value = datos.move_to_end()
        app = value['aplicacion:']
        msj = value['mensaje:']
        if (app == 'Twitter') and ('python' in msj):
            colaTwitter.arrive(value)
        cont += 1

    print('---------notificaciones que contienen python en el mensaje desde la app twitter----------')
    contAux = 0
    while contAux < colaTwitter.size():
        aux = colaTwitter.move_to_end()
        print(aux['mensaje:'])
        print(aux['hora:'])
        print(aux['aplicacion:'])
        contAux += 1
        

def pilaTemporal(notificaciones):
    pila = Pila()
    colaTemporal = Cola()

    cont = 0
    while cont < notificaciones.size():

        data = notificaciones.move_to_end()
        hora = data['hora:']

        if (hora >= '11:43') and (hora <= '15:57'):
            
            pila.push(data)

        cont +=1

    cantidadNotif = pila.size()
    print(f'la cantidad de nofiticaciones son {cantidadNotif}')



#llamada a funciones

cola_sin_facebook = eliminarFacebook(cola)

cont = 0
while cont < cola_sin_facebook.size() > 0:
    value = cola_sin_facebook.move_to_end()
    print(value)
    cont +=1


notifiTwitter(cola)
pilaTemporal(cola)