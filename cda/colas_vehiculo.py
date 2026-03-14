class ColasVehiculo: 
    
    def agregar_vehiculo(self, marca: str, modelo: str, año: int, tipo: str):
        vehículo = None
        if tipo == "Motocicleta":
            vehículo = Motocicleta(marca, modelo, año)
        elif tipo == "Automovil":
            vehículo = Automovil(marca, modelo, año)

        # poner su logica maravillosa

    def despachar_vehiculo(self):
        # poner su logica maravillosa
        pass

    def mostrar_vehiculos(self):
        # poner su logica maravillosa
        pass