numeros = [3,5,8,12,15]
resultado = 0
for numero in numeros:
    resultado += numero
print(resultado)

#convertido a funcion con for
def suma_numeros(numeros: list)-> int:
    for numero in numeros:
        resultado += numero
    return(resultado)

#usando while
def sumar_numeros_while(numeros: list)->int:
    resultado = 0
    i = 0
    while i< len(numeros):
        resultado += numeros[i]
        i+=1
    return resultado

# con recursión
def sumar_numeros_recursivo(numeros: list) -> int:
    if not numeros:
        return 0
    else:
        return numeros[0] + sumar_numeros_recursivo(numeros[1:])

