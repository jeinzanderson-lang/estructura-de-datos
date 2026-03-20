# Historial de Conversación

## Mensaje Inicial del Usuario
en este archivo hay errores con "motocicleta" y "automovil", corrigelos para que coincidan con los archivos de esta carpeta, y proporcona un codigo para el apartado de despachar vehiculo, y otro para mostrar vehiculo

## Respuesta del Asistente
He corregido los errores en el archivo `colas_vehiculo.py`. Los cambios principales fueron:

- Agregué las importaciones necesarias para las clases `Motocicleta` y `automovil` desde los archivos correspondientes en la carpeta.
- Cambié "Automovil" a "automovil" para que coincida con el nombre de la clase en `automovil.py`.
- Agregué un constructor `__init__` para inicializar una lista de vehículos.
- Implementé la lógica en `agregar_vehiculo` para añadir vehículos a la lista.
- Implementé `despachar_vehiculo` para remover y devolver el primer vehículo de la cola (si existe).
- Implementé `mostrar_vehiculos` para imprimir la información de todos los vehículos en la cola.

También corregí un error menor en `vehiculo.py` donde se usaba `self.año` en lugar de `self.anio` para mantener consistencia.

El código actualizado en `colas_vehiculo.py` es:

```python
from .motocicleta import Motocicleta
from .automovil import automovil

class ColasVehiculo:
    
    def __init__(self):
        self.vehiculos = []
    
    def agregar_vehiculo(self, marca: str, modelo: str, año: int, tipo: str):
        vehículo = None
        if tipo == "Motocicleta":
            vehículo = Motocicleta(marca, modelo, año)
        elif tipo == "automovil":
            vehículo = automovil(marca, modelo, año)
        
        if vehículo:
            self.vehiculos.append(vehículo)

    def despachar_vehiculo(self):
        if self.vehiculos:
            return self.vehiculos.pop(0)
        return None

    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(vehiculo.mostrar_informacion())
```

No se encontraron errores de sintaxis en el archivo.

## Mensaje Actual del Usuario
por favor crea un nuevo archivo .md con el historial de esta conversacion

## Respuesta del Asistente
He creado el archivo `historial_conversacion.md` con el historial completo de esta conversación.