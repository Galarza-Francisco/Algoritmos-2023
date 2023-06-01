mochila = ['comida', 'agua','sable de luz', 'mapa']


def usar_la_fuerza(mochila, objetos_sacados=0):
    if len(mochila) == 0:
        print("La mochila está vacía, no se encontró el sable de luz")
        return objetos_sacados
    elif mochila[0] == "sable de luz":
        print(f"Se encontró el sable de luz ")
        return objetos_sacados+1
    else:
        return usar_la_fuerza(mochila[1:], objetos_sacados+1)

objetos_sacados = usar_la_fuerza(mochila)
print(f"Se sacaron {objetos_sacados} objetos de la mochila")
