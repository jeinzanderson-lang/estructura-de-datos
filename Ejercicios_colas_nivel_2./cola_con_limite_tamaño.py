class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class BoundedQueue:
    def __init__(self, max_size):
        self.front = self.rear = None
        self.max_size = max_size
        self.size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        # Si está llena, descartamos el más viejo
        if self.size == self.max_size:
            self.dequeue()               # reduce size en 1

        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        val = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return val

bq = BoundedQueue(max_size=3)
for i in range(1, 6):   # encola 1..5
    bq.enqueue(i)

while not bq.is_empty():
    print(bq.dequeue())
