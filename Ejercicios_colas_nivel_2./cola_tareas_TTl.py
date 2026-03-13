import time

class TaskNode:
    def __init__(self, name, ttl_seconds):
        self.name = name
        self.expiry = time.time() + ttl_seconds
        self.next = None


class TaskQueue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, name, ttl_seconds):
        node = TaskNode(name, ttl_seconds)
        if self.is_empty():
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue_valid(self):
        now = time.time()
        # Eliminar todas las tareas expiradas
        while self.front and self.front.expiry <= now:
            self.front = self.front.next
        if self.front is None:           # nada válido
            raise IndexError("no valid tasks left")
        # Sacar la primera tarea válida
        node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return node.name
tq = TaskQueue()
tq.enqueue('A', ttl_seconds=2)   # expira en 2 s
tq.enqueue('B', ttl_seconds=5)   # expira en 5 s

time.sleep(3)                     # esperar 3 s
print(tq.dequeue_valid())        # -> 'B' (A ya expiró)