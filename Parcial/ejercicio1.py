vector_palabras = ["parcial", "python", "algoritmos", "facultad"]

def contar_palabra(vector, palabra):
    if not vector:
        return 0
    elif vector[0] == palabra:  
        return 1 + contar_palabra(vector[1:], palabra)  
    else:
        return contar_palabra(vector[1:], palabra) 
    
palabra_buscar = str(input('ingresar la palabra que quiere buscar: '))
resultado = contar_palabra(vector_palabras, palabra_buscar)
print(f'la palabra {palabra_buscar} aparece {resultado} veces')