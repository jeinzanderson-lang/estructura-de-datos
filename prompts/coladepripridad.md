# Cola de Prioridad con Inserción Ordenada

Implementación de una **cola de prioridad usando una lista enlazada en Python**, donde los elementos se insertan en la posición correcta según su prioridad.

## 📌 Objetivo

Insertar elementos en una cola de forma que siempre se mantenga **ordenada por prioridad numérica**.

* **Menor número = mayor prioridad**
* La ordenación ocurre **durante el `enqueue`**

---

## ⚙️ Características

* Cada nodo contiene:

  * `data`
  * `priority`
* `enqueue()` recorre la lista y coloca el nodo en la posición correcta.
* `dequeue()` elimina siempre el nodo del frente (el de mayor prioridad).

---

## 🧠 Estructura del Nodo

```python
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None
```

---

## 🏗️ Implementación de la Cola de Prioridad

```python
class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, data, priority):
        new_node = Node(data, priority)

        # Insertar al inicio si la cola está vacía
        # o si tiene mayor prioridad
        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            current = self.front

            while current.next is not None and current.next.priority <= priority:
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.front is None:
            print("La cola está vacía")
            return None

        removed = self.front
        self.front = self.front.next
        return removed.data

    def display(self):
        current = self.front
        while current:
            print(f"Data: {current.data}, Priority: {current.priority}")
            current = current.next
```

---

## ▶️ Ejemplo de Uso

```python
pq = PriorityQueue()

pq.enqueue("Tarea A", 3)
pq.enqueue("Tarea B", 1)
pq.enqueue("Tarea C", 2)
pq.enqueue("Tarea D", 4)

print("Cola de prioridad:")
pq.display()

print("\nElemento eliminado:", pq.dequeue())

print("\nCola después de dequeue:")
pq.display()
```

---

## 📊 Ejemplo de Salida

```
Cola de prioridad:
Data: Tarea B, Priority: 1
Data: Tarea C, Priority: 2
Data: Tarea A, Priority: 3
Data: Tarea D, Priority: 4

Elemento eliminado: Tarea B
```

---

## 📚 Conceptos utilizados

* Estructuras de datos
* Listas enlazadas
* Colas de prioridad
* Algoritmos de inserción ordenada

---

## 👨‍💻 Autor

Proyecto académico de **Estructuras de Datos**.
