class Pila():
    """Stack class"""

    def __init__(self):
        self.__elements = []

    def __eq__(self, stack_aux):
        if isinstance(stack_aux, Pila):
            return self.__elements == stack_aux.__elements
        else:
            return False

    def push(self, value):
        self.__elements.append(value)

    def pop(self):
        if self.size() > 0:
            dato = self.__elements.pop()
            return dato

    def size(self):
        return len(self.__elements)

    def on_top(self):
        if self.size() > 0:
            return self.__elements[-1]

    def __iter__(self):
        return iter(self.__elements)


class Pelicula():
    """Movie class"""

    def __init__(self, titulo, estudio, anio):
        self.titulo = titulo
        self.estudio = estudio
        self.anio = anio

pila_peliculas = Pila()
pila_peliculas.push(Pelicula("Avengers: Age of Ultron", "Marvel Studios", 2015))
pila_peliculas.push(Pelicula("Iron Man 3", "Marvel Studios", 2013))
pila_peliculas.push(Pelicula("Guardians of the Galaxy", "Marvel Studios", 2014))
pila_peliculas.push(Pelicula("Black Panther", "Marvel Studios", 2018))
pila_peliculas.push(Pelicula("Captain America: Civil War", "Marvel Studios", 2016))

def mostrar_peliculas_por_anio(pila, anio):
    for pelicula in pila:
        if pelicula.anio == anio:
            print(pelicula.titulo)


def contar_peliculas_por_anio(pila, anio):
    contador = 0
    for pelicula in pila:
        if pelicula.anio == anio:
            contador += 1
    return contador

def mostrar_peliculas_marvel_por_anio(pila, anio):
    for pelicula in pila:
        if pelicula.anio == anio and pelicula.estudio == "Marvel Studios":
            print(pelicula.titulo)




print("Películas estrenadas en el año 2014:")
mostrar_peliculas_por_anio(pila_peliculas, 2014)

anio_2018 = 2018
cantidad_peliculas_2018 = contar_peliculas_por_anio(pila_peliculas, anio_2018)
print(f"Cantidad de películas estrenadas en el año {anio_2018}: {cantidad_peliculas_2018}")

print("Películas de Marvel Studios estrenadas en el año 2016:")
mostrar_peliculas_marvel_por_anio(pila_peliculas, 2016)
