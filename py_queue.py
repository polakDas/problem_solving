class MyQueue:
    def __init__(self):
        self._data = []
        self.p_start = 0
    
    def enQueue(self, x: int) -> bool:
        self._data.append(x)
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.p_start += 1
        return True
    
    def front(self) -> int:
        return self._data[self.p_start]

    def isEmpty(self) -> bool:
        return self.p_start >= len(self._data)

if __name__ == "__main__":
    q = MyQueue()
    q.enQueue(8)
    q.enQueue(5)
    q.enQueue(3)
    if not q.isEmpty():
        print(q.front())
    q.deQueue()
    if not q.isEmpty():
        print(q.front())
    q.deQueue()
    if not q.isEmpty():
        print(q.front())
    else:
        print("Nothing found")