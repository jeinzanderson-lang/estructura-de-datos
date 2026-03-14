from .vehiculo import Vehículo
class automovil(Vehículo):
    tipo = "automovil"
    def __init__(self, marca: str, modelo: str, año: int):
        super().__init__(marca, modelo, año, self.tipo)

    def mostrar_informacion(self) -> str:
        return f"{super().mostrar_informacion()}"  