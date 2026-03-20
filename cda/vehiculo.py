class Vehiculo:
    def __init__(self, marca: str, modelo: str, año: int, tipo: str):
        self.marca = marca
        self.modelo = modelo
        self.anio = año
        self.tipo = tipo 

    def mostrar_informacion(self) -> str:
        return f"{self.marca} {self.modelo} ({self.anio})"