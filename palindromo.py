# con while
def palindromo_while(texto):
    # Si no hay texto o tiene una sola letra
    if len(texto) <= 1:
        return True
    
    izq = 0
    der = len(texto) - 1
    
    while izq < der:
        if texto[izq] != texto[der]:
            return False
        izq += 1
        der -= 1
    return True

print(palindromo_while("radar"))

# con for
def palindromo_for(texto):
    if len(texto) <= 1:
        return True
    
    for i in range(len(texto) // 2):
        if texto[i] != texto[-(i + 1)]:
            return False
    return True
print(palindromo_for("radam"))

# con recursividad
def palindromo_recursivo(texto):
    if len(texto) <= 1:
        return True
    if texto[0] != texto[-1]:
        return False
    return palindromo_recursivo(texto[1:-1])
print(palindromo_recursivo("reconocer"))