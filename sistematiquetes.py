from datetime import datetime

# Clase Ticket
class Ticket:
    def __init__(self, id, descripcion, prioridad, tecnico):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad  # ALTA / MEDIA / BAJA
        self.tecnico = tecnico
        self.timestamp = datetime.now()
        
        # Punteros de lista doble
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"[{self.id}] {self.descripcion} | Prioridad: {self.prioridad} | Técnico: {self.tecnico}"


# Clase ListaTickets
class ListaTickets:
    def __init__(self):
        self.cabeza = None
        self.extremo = None

    # Valor numérico de prioridad para ordenar
    def _valor_prioridad(self, prioridad):
        valores = {"ALTA": 3, "MEDIA": 2, "BAJA": 1}
        return valores.get(prioridad.upper(), 0)

    # Agregar ticket en orden de prioridad
    def agregar_ticket(self, ticket):
        if self.cabeza is None:
            self.cabeza = self.extremo = ticket
            return

        actual = self.cabeza

        while actual:
            if self._valor_prioridad(ticket.prioridad) > self._valor_prioridad(actual.prioridad):
                ticket.siguiente = actual
                ticket.anterior = actual.anterior

                if actual.anterior:
                    actual.anterior.siguiente = ticket
                else:
                    self.cabeza = ticket

                actual.anterior = ticket
                return

            if actual.siguiente is None:
                actual.siguiente = ticket
                ticket.anterior = actual
                self.extremo = ticket
                return

            actual = actual.siguiente

    # Atender primer ticket (cabeza)
    def atender_primero(self):
        if self.cabeza is None:
            return None

        ticket = self.cabeza
        self.cabeza = self.cabeza.siguiente

        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.extremo = None

        ticket.siguiente = None
        return ticket

    # Buscar ticket por ID
    def buscar_ticket(self, id):
        actual = self.cabeza
        while actual:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None

    # Reasignar técnico
    def reasignar(self, id_ticket, nuevo_tecnico):
        ticket = self.buscar_ticket(id_ticket)
        if ticket:
            ticket.tecnico = nuevo_tecnico
            return True
        return False

    # Listar desde cabeza hacia extremo
    def listar_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual)
            actual = actual.siguiente

    # Listar desde extremo hacia cabeza
    def listar_atras(self):
        actual = self.extremo
        while actual:
            print(actual)
            actual = actual.anterior

    # Estadísticas
    def estadisticas(self):
        actual = self.cabeza
        conteo = {"ALTA": 0, "MEDIA": 0, "BAJA": 0}
        total_tiempo = 0
        cantidad = 0

        ahora = datetime.now()

        while actual:
            conteo[actual.prioridad] += 1
            total_tiempo += (ahora - actual.timestamp).total_seconds()
            cantidad += 1
            actual = actual.siguiente

        promedio = total_tiempo / cantidad if cantidad > 0 else 0

        print("Estadísticas:")
        print("ALTA:", conteo["ALTA"])
        print("MEDIA:", conteo["MEDIA"])
        print("BAJA:", conteo["BAJA"])
        print("Tiempo promedio desde creación (segundos):", promedio)


# Ejemplo de uso
lista = ListaTickets()

t1 = Ticket(1, "Error en servidor", "ALTA", "Carlos")
t2 = Ticket(2, "Actualizar software", "MEDIA", "Ana")
t3 = Ticket(3, "Problema con impresora", "BAJA", "Luis")
t4 = Ticket(4, "Red caída", "ALTA", "Pedro")

lista.agregar_ticket(t1)
lista.agregar_ticket(t2)
lista.agregar_ticket(t3)
lista.agregar_ticket(t4)

print("Tickets adelante:")
lista.listar_adelante()

print("\nAtendiendo primer ticket:")
print(lista.atender_primero())

print("\nLista actual:")
lista.listar_adelante()

print("\nReasignando ticket 2 a Marta")
lista.reasignar(2, "Marta")

print("\nLista hacia atrás:")
lista.listar_atras()

print("\n")
lista.estadisticas()