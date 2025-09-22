class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self, maxItems):
        self.items = [None] * maxItems
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = maxItems

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        print("self.size, self.maxSize", self.size, self.maxSize)
        return self.size == self.maxSize

    def size(self):
        # return the size of the queue
        return self.size

    def show(self):
        # show all pointers
        print("list and pointers", self.items, self.front, self.rear, "size =", self.size)

    def peek(self):
        #  show the item at the front of the Queue
        print(self.items[self.front])

    def enqueue(self, item):
        if self.size < self.maxSize:
            self.items[self.rear + 1] = item
            self.rear = (self.rear + 1) % self.maxSize
            self.size += 1
        else:
            print("Queue is full")

    def dequeue(self):
        return_item = None
        if self.size > 0:
            return_item = self.items[self.front]
            self.front = (self.front + 1) % self.maxSize
            self.size = self.size - 1
        else:
            print("Nothing to remove from queue")
        return return_item

s = Stack()
myString = input("Please enter a word or phrase to be reversed: ")
list1 = list(myString)
print(list1)
numChars = len(list1)
s = Stack()
#push the characters from the list onto the stack
for char in list1:
    s.push(char)

task2Queue = CircularQueue(5)
task2Queue.show()
