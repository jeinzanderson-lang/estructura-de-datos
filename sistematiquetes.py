from datetime import datetime

class Ticket:
    def __init__(self, id, descripcion, prioridad, tecnico):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad  # ALTA, MEDIA, BAJA
        self.tecnico = tecnico
        self.timestamp = datetime.now()

        # punteros de la lista doble
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"[{self.id}] {self.descripcion} | Prioridad: {self.prioridad} | Técnico: {self.tecnico} | Creado: {self.timestamp}"


class ListaTickets:
    def __init__(self):
        self.cabeza = None
        self.extremo = None

    def prioridad_valor(self, prioridad):
        orden = {"ALTA": 1, "MEDIA": 2, "BAJA": 3}
        return orden.get(prioridad, 3)

    # insertar manteniendo orden de prioridad
    def agregar_ticket(self, ticket):

        if self.cabeza is None:
            self.cabeza = ticket
            self.extremo = ticket
            return

        actual = self.cabeza

        while actual and self.prioridad_valor(actual.prioridad) <= self.prioridad_valor(ticket.prioridad):
            actual = actual.siguiente

        # insertar al inicio
        if actual == self.cabeza:
            ticket.siguiente = self.cabeza
            self.cabeza.anterior = ticket
            self.cabeza = ticket

        # insertar al final
        elif actual is None:
            self.extremo.siguiente = ticket
            ticket.anterior = self.extremo
            self.extremo = ticket

        # insertar en medio
        else:
            anterior = actual.anterior
            anterior.siguiente = ticket
            ticket.anterior = anterior

            ticket.siguiente = actual
            actual.anterior = ticket

    # atender primer ticket (O(1))
    def atender_primero(self):
        if self.cabeza is None:
            return None

        atendido = self.cabeza
        self.cabeza = self.cabeza.siguiente

        if self.cabeza:
            self.cabeza.anterior = None
        else:
            self.extremo = None

        atendido.siguiente = None
        return atendido

    # buscar ticket por id
    def buscar_ticket(self, id_ticket):
        actual = self.cabeza
        while actual:
            if actual.id == id_ticket:
                return actual
            actual = actual.siguiente
        return None

    # reasignar técnico
    def reasignar(self, id_ticket, nuevo_tecnico):
        ticket = self.buscar_ticket(id_ticket)
        if ticket:
            ticket.tecnico = nuevo_tecnico
            return True
        return False

    # listar desde cabeza hacia adelante
    def listar_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual)
            actual = actual.siguiente

    # listar desde extremo hacia atrás
    def listar_atras(self):
        actual = self.extremo
        while actual:
            print(actual)
            actual = actual.anterior

    # estadísticas
    def estadisticas(self):
        conteo = {"ALTA": 0, "MEDIA": 0, "BAJA": 0}
        total_tiempo = 0
        cantidad = 0

        actual = self.cabeza
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


# ---------------------------
# Ejemplo de uso
# ---------------------------

sistema = ListaTickets()

t1 = Ticket(1, "Servidor caído", "ALTA", "Carlos")
t2 = Ticket(2, "Error en impresora", "BAJA", "Ana")
t3 = Ticket(3, "Problema de red", "MEDIA", "Luis")
t4 = Ticket(4, "Base de datos lenta", "ALTA", "Maria")

sistema.agregar_ticket(t1)
sistema.agregar_ticket(t2)
sistema.agregar_ticket(t3)
sistema.agregar_ticket(t4)

print("\nLista adelante:")
sistema.listar_adelante()

print("\nLista atrás:")
sistema.listar_atras()

print("\nAtendiendo primer ticket:")
print(sistema.atender_primero())

print("\nReasignando ticket 3 a Pedro")
sistema.reasignar(3, "Pedro")

print("\nLista actualizada:")
sistema.listar_adelante()

print()
sistema.estadisticas()