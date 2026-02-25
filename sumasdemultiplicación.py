#con while
def multiplicar(a, b):
    resultado = 0
    contador = 0
    while contador < b:
        resultado += a
        contador += 1
    return resultado
print(multiplicar(5, 3))  

#con for
def multiplicar(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado
print(multiplicar(5, 4))

# recursiva
def multiplicar(a, b):
    if a == 0 or b == 0:
        return 0
    
    return a + multiplicar(a, b - 1)
print(multiplicar(2, 6))