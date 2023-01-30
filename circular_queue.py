class MyCircularQueue:

    def __init__(self, k: int):
        self._data = [-1 for _ in range(k)]
        self.front = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % len(self._data)
        self._data[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            return True
        self.front = (self.front + 1) % len(self._data)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self.rear]

    def isEmpty(self) -> bool:
        return self.rear == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self._data) == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()