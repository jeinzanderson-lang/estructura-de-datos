# Sistema de Gestión de Tickets con Lista Doblemente Enlazada

## 🌍 Contexto
Una empresa de tecnología en Bogotá necesita un sistema de gestión de tickets de soporte para su área de TI.  
Los técnicos atienden tickets en **orden de prioridad**, y los de **alta prioridad se ubican al inicio de la lista**.

El sistema debe permitir **consultar, reasignar y recorrer los tickets en ambas direcciones**.

---

## 🎯 Objetivo
Implementar un **sistema de gestión de tickets usando una lista doblemente enlazada ordenada por prioridad**.

La lista mantiene siempre el orden:

ALTA → MEDIA → BAJA

Además, permite **navegación bidireccional** para que los técnicos recorran los tickets hacia adelante y hacia atrás.

---

## 📋 Requerimientos funcionales

### Clase Ticket
Debe contener:

- ID único
- Descripción
- Prioridad (ALTA / MEDIA / BAJA)
- Técnico asignado
- Timestamp (fecha y hora de creación)
- Puntero siguiente
- Puntero anterior

---

### Clase ListaTickets
Implementa una **lista doblemente enlazada** con:

- cabeza (primer ticket)
- extremo (último ticket)

---

## ⚙️ Métodos requeridos

### agregar_ticket(ticket)
- Inserta el ticket en la **posición correcta según prioridad**
- Complejidad: **O(n)**
- Mantiene el orden:

ALTA → MEDIA → BAJA

---

### atender_primero()
- Retira y retorna el **ticket en la cabeza**
- Ajusta el puntero **anterior** del nuevo primer nodo
- Complejidad: **O(1)**

---

### buscar_ticket(id)
- Realiza un **recorrido lineal**
- Complejidad: **O(n)**
- Retorna el nodo encontrado **sin eliminarlo**

---

### reasignar(id_ticket, nuevo_tecnico)
- Busca el ticket por ID
- Actualiza el **técnico asignado**

---

### listar_adelante()
Recorre la lista desde:

cabeza → extremo

usando el puntero `.siguiente`.

---

### listar_atras()
Recorre la lista desde:

extremo → cabeza

usando el puntero `.anterior`.

---

### estadisticas()

Debe calcular:

- Conteo de tickets por prioridad:
  - ALTA
  - MEDIA
  - BAJA
- Tiempo promedio desde la creación del ticket.

---

## 📊 Estructura esperada
