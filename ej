# con while
def busqueda_binaria(arr, objetivo):
    izq = 0
    der = len(arr) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        
        if arr[medio] == objetivo:
            return medio
        
        elif objetivo < arr[medio]:
            der = medio - 1
        
        else:
            izq = medio + 1
    return -1
print(busqueda_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9],9))


# con For
def busqueda_binaria(arr, objetivo):
    izq = 0
    der = len(arr) - 1
    for _ in range(len(arr)):  
        if izq > der:
            return -1
        
        medio = (izq + der) // 2
        
        if arr[medio] == objetivo:
            return medio
        elif objetivo < arr[medio]:
            der = medio - 1
        else:
            izq = medio + 1
    return -1
print(busqueda_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))

# con recursividad
def busqueda_binaria_recursiva(arr, objetivo, izq, der):
    # Caso base 1: no se encontró
    if izq > der:
        return -1
    
    medio = (izq + der) // 2
    
    # Caso base 2: encontrado
    if arr[medio] == objetivo:
        return medio
    
    # Caso recursivo
    if objetivo < arr[medio]:
        return busqueda_binaria_recursiva(arr, objetivo, izq, medio - 1)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, der)
print(busqueda_binaria_recursiva([1, 2, 3, 4, 5, 6, 7, 8, 9], 7, 0, len([1, 2, 3, 4, 5, 6, 7, 8, 9]) - 1))