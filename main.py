import math


class Coordinate:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"X: {self.x}, Y: {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Queue:
    def __init__(self, c):
        self.queue = []
        self.front = self.rear = 0
        self.capacity = c

    def enqueue(self, data):
        if (self.capacity == self.rear):
            print("\nQueue is full")
        else:
            self.queue.append(data)
            self.rear += 1

    def dequeue(self):
        if (self.front == self.rear):
            print("Queue is empty")
        else:
            x = self.queue.pop(0)
            self.rear -= 1

    def print_queue(self):
        if (self.front == self.rear):
            print("Queue is Empty")

        for i in self.queue:
            print(i, "<--", end='')

    def length_between_first_and_last_point(self) -> float:
        a = (self.queue[self.front].x - self.queue[self.rear - 1].x) ** 2
        b = (self.queue[self.front].y - self.queue[self.rear - 1].y) ** 2
        res = math.sqrt(a + b)
        print("\nLength:", res)
        return res

    def size_queue(self) -> int:
        print("Size:", self.rear)
        return self.rear

    def number_of_same_element(self, data: Coordinate):
        if (self.front == self.rear):
            print("\nQueue is Empty")
        count = 0
        for i in self.queue:
            if i == data:
                return count
            count + 1
        return "No node with these coordinates"


if __name__ == '__main__':
    q = Queue(4)
    q.print_queue()
    q.enqueue(Coordinate(1, 2))
    q.enqueue(Coordinate(2, 3))
    q.enqueue(Coordinate(3, 4))
    q.enqueue(Coordinate(4, 5))
    q.print_queue()
    q.length_between_first_and_last_point()
    q.size_queue()
    print("Number of the same coordinate:", q.number_of_same_element(Coordinate(1, 2)))
