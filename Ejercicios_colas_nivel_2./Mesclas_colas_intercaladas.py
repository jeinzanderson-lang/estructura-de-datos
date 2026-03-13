from queue import Queue

def merge_queues(q1, q2):
    merged = Queue()
    turn_q1 = True

    while not q1.empty() or not q2.empty():
        if turn_q1 and not q1.empty():
            merged.put(q1.get())
        elif not turn_q1 and not q2.empty():
            merged.put(q2.get())
        turn_q1 = not turn_q1

    return merged


q1 = Queue()
q2 = Queue()

for v in [1, 3, 5]:
    q1.put(v)

for v in [2, 4, 6, 8]:
    q2.put(v)

merged = merge_queues(q1, q2)

while not merged.empty():
    print(merged.get(), end=" ")