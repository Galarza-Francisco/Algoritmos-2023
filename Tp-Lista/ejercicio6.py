from listaClass import Lista as ListaSimple

def criterio_comparacion(value, criterio):
    if isinstance(value, (int, str, bool)):
        return value
    elif isinstance(value, list):
        return value[0]  # Comparar usando el primer elemento de la lista
    else:
        dic_atributos = value.__dict__
        if criterio in dic_atributos:
            return dic_atributos[criterio]
        else:
            print('no se puede ordenar por este criterio')


class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia


# Crear una lista de superhéroes
lista_superheroes = ListaSimple()

# Insertar superhéroes en la lista
lista_superheroes.insert(Superheroe("Linterna Verde", 1940, "DC", "Biografía de Linterna Verde."),criterio="anio_aparicion")
lista_superheroes.insert(Superheroe("Wolverine", 1974, "Marvel", "Biografía de Wolverine con traje."), criterio="anio_aparicion")
lista_superheroes.insert(Superheroe("Dr. Strange", 1963, "Marvel", "Biografía del Dr. Strange."),criterio="anio_aparicion")
# Agregar más superhéroes aquí...

# a. Eliminar el nodo que contiene la información de Linterna Verde
lista_superheroes.delete("Linterna Verde", "nombre")

# b. Mostrar el año de aparición de Wolverine
wolverine = lista_superheroes.get_element_by_value("Wolverine", "nombre")
if wolverine:
    print("Año de aparición de Wolverine:", wolverine.anio_aparicion)
else:
    print("Wolverine no encontrado en la lista.")

# c. Cambiar la casa de Dr. Strange a Marvel
dr_strange = lista_superheroes.get_element_by_value("Dr. Strange", "nombre")
if dr_strange:
    dr_strange.casa = "Marvel"
    print("La casa de Dr. Strange se ha cambiado a Marvel.")
else:
    print("Dr. Strange no encontrado en la lista.")

# d. Mostrar el nombre de aquellos superhéroes que mencionan "traje" o "armadura" en su biografía
print("Superhéroes con 'traje' o 'armadura' en su biografía:")
for i in range(lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value and ("traje" in value.biografia or "armadura" in value.biografia):
        print(value.nombre)

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
print("Superhéroes con fecha de aparición anterior a 1963:")
for i in range(lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value.anio_aparicion < 1963:
        print("Nombre:", value.nombre)
        print("Casa:", value.casa)

# f. Mostrar la casa a la que pertenecen Capitana Marvel y Mujer Maravilla
capitana_marvel = lista_superheroes.get_element_by_value("Capitana Marvel", "nombre")
mujer_maravilla = lista_superheroes.get_element_by_value("Mujer Maravilla", "nombre")

if capitana_marvel:
    print("Casa de Capitana Marvel:", capitana_marvel[0].casa)
else:
    print("Capitana Marvel no encontrada en la lista.")

if mujer_maravilla:
    print("Casa de Mujer Maravilla:", mujer_maravilla[0].casa)
else:
    print("Mujer Maravilla no encontrada en la lista.")

# g. Mostrar toda la información de Flash y Star-Lord
superheroes_a_mostrar = ["Flash", "Star-Lord"]
for nombre_superheroe in superheroes_a_mostrar:
    superheroe = lista_superheroes.get_element_by_value(nombre_superheroe, criterio="nombre")
    if superheroe:
        print(f"Información de {nombre_superheroe}:")
        print("Nombre:", superheroe.nombre)
        print("Año de aparición:", superheroe.anio_aparicion)
        print("Casa:", superheroe.casa)
        print("Biografía:", superheroe.biografia)

# h. Listar los superhéroes que comienzan con la letra B, M y S
letras_iniciales = ["B", "M", "S"]
print("Superhéroes que comienzan con B, M o S:")
for i in range(lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value.nombre  in letras_iniciales:
        print(superheroe.nombre)

# i. Determinar cuántos superhéroes hay de cada casa de cómic
cont_marvel = 0
cont_DC = 0

for i in range(lista_superheroes.size()):
    value = lista_superheroes.get_element_by_index(i)
    if value.casa == "Marvel":
        cont_marvel += 1
    elif value.casa == "DC":
        cont_DC += 1

print("Número de superhéroes de Marvel:", cont_marvel)
print("Número de superhéroes de DC:", cont_DC)
