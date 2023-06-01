
numero_romano = 'MMXV'

def romano_a_decimal(numero_romano):
    valores_romanos = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    if len(numero_romano) == 0:
        return 0
    elif len(numero_romano) == 1:
        return valores_romanos[numero_romano[0]]
    else:
        primer_valor = valores_romanos[numero_romano[0]]
        segundo_valor = valores_romanos[numero_romano[1]]
        if primer_valor < segundo_valor:
            return segundo_valor - primer_valor + romano_a_decimal(numero_romano[2:])
        else:
            return primer_valor + romano_a_decimal(numero_romano[1:])
        
numero_decimal = romano_a_decimal(numero_romano)
print(f"El número romano {numero_romano} equivale a {numero_decimal} en decimal")