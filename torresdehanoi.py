# con while
def hanoi(n, origen, destino, auxiliar):
    movimientos = []
    
    def mover(n, origen, destino, auxiliar):
        # Caso base
        if n == 0:
            return
        
        
        mover(n - 1, origen, auxiliar, destino)
        
        
        movimientos.append(f"Mover disco {n} de {origen} a {destino}")
        
        
        mover(n - 1, auxiliar, destino, origen)
    
    mover(n, origen, destino, auxiliar)
    
   
    i = 0
    while i < len(movimientos):
        print(movimientos[i])
        i += 1
    
    
    if n == 3:
        print(f"\nTotal de movimientos: {len(movimientos)}")
        if len(movimientos) == 7:
            print("✔ Se generaron exactamente 7 movimientos.")
        else:
            print("✘ Error en la cantidad de movimientos.")


hanoi(3, "A", "C", "B")

#con for
def hanoi(n, origen, destino, auxiliar):
    movimientos = []
    
    def mover(n, origen, destino, auxiliar):
        # Caso base
        if n == 0:
            return
        
       
        mover(n - 1, origen, auxiliar, destino)
        
       
        movimientos.append(f"Mover disco {n} de {origen} a {destino}")
        
        
        mover(n - 1, auxiliar, destino, origen)
    
    mover(n, origen, destino, auxiliar)
    

    for movimiento in movimientos:
        print(movimiento)
    
    if n == 3:
        print(f"\nTotal de movimientos: {len(movimientos)}")
        if len(movimientos) == 7:
            print("✔ Se generaron exactamente 7 movimientos.")
        else:
            print("✘ Error en la cantidad de movimientos.")



hanoi(3, "A", "C", "B")