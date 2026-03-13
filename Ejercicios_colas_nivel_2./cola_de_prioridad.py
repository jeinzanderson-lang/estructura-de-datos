class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None   # nodo de mayor prioridad
        self.rear = None    # nodo de menor prioridad

    def is_empty(self):
        return self.front is None

    def enqueue(self, data, priority):
        new_node = Node(data, priority)
        # Caso vacío
        if self.is_empty():
            self.front = self.rear = new_node
            return

        # Insertar al inicio (prioridad más alta)
        if priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            return

        # Buscar posición intermedia o final
        prev, cur = None, self.front
        while cur and cur.priority <= priority:
            prev, cur = cur, cur.next
        prev.next = new_node
        new_node.next = cur

        # Actualizar rear si se insertó al final
        if new_node.next is None:
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        node = self.front
        self.front = self.front.next
        if self.front is None:          # quedó vacía
            self.rear = None
        return node.data
pq = PriorityQueue()
pq.enqueue('A', 3)
pq.enqueue('B', 1)
pq.enqueue('C', 2)
pq.enqueue('D', 5)

while not pq.is_empty():
    print(pq.dequeue())
# Salida esperada: B, C, A, D