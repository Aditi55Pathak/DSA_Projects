class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot add more items.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Sushi Bowls on the Conveyor Belt:")
        i = self.front
        count = 0
        while count < self.size:
            print(self.queue[i], end=" ")
            i = (i + 1) % self.capacity
            count += 1
        print()


conveyor_belt = CircularQueue(5)
conveyor_belt.enqueue("Sushi A")
conveyor_belt.enqueue("Sushi B")
conveyor_belt.enqueue("Sushi C")
conveyor_belt.enqueue("Sushi D")
conveyor_belt.enqueue("Sushi E")
conveyor_belt.display()

# Rotation
conveyor_belt.dequeue()
conveyor_belt.enqueue("Sushi F")
conveyor_belt.display()
