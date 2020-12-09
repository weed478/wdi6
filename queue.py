class Block:
    def __init__(self, value, next_block):
        self.value = value
        self.next = next_block


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def collect(self):
        t = []
        q = self.first
        while q is not None:
            t.append(q.value)
            q = q.next

        return t

    def push(self, x):
        block = Block(x, None)

        if self.first is None:
            self.first = block
        else:
            self.last.next = block

        self.last = block

    def pop(self):
        if self.first is None:
            return None

        val = self.first.value

        self.first = self.first.next
        if self.first is None:
            self.last = None

        return val


q = Queue()
print(q.collect())

q.push(1)
print(q.collect())

print(q.pop())
print(q.collect())

q.push(1)
q.push(2)
q.push(3)
print(q.collect())

print(q.pop())
print(q.collect())

print(q.pop())
print(q.collect())

q.push(4)
q.push(5)
print(q.collect())

print(q.pop())
print(q.collect())
