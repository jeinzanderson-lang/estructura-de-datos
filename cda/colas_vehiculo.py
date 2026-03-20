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