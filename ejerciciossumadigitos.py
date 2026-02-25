# usando el ciclo while
def suma_digitos(n):
    suma = 0
    while n > 0:
        ultimo_digito = n % 10   
        suma += ultimo_digito    
        n = n // 10              
    return suma
print(suma_digitos(2345))

# usando ciclo for
def suma_digitos_for(n):
    suma = 0  
    for i in range(len(str(n))):
        ultimo_digito = n % 10
        suma += ultimo_digito
        n = n // 10
    return suma
print(suma_digitos_for(1234))

#recursiva
def suma_digitos_recursiva(n):
    if n==0:
        return 0
    else:
        ultimo_digito = n%10
        return ultimo_digito + suma_digitos_recursiva(n//10)
print(suma_digitos_recursiva(5678))
