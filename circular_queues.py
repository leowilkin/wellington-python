# Topic 1 Queues
# circularQueue.py demonstrates enqueuing and dequeuing items
# from a circular queue

#constructing a Queue ADT
class CircularQueue:
    def __init__(self,maxItems):
        self.items = [None]*maxItems
        self.front = 0
        self.rear = -1
        self.size = 0
        self.maxSize = maxItems
              
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self):
        print("self.size, self.maxSize",self.size, self.maxSize)
        return self.size == self.maxSize
    
    def size(self):
        # return the size of the queue
        return self.size
    
    def show(self):
        # show all pointers
        print("list and pointers",self.items, self.front,self.rear, "size =",self.size)
     
    def peek(self):
        #  show the item at the front of the Queue
        print(self.items[self.front])
     
    def enqueue(self, item):
        if self.size < self.maxSize:
            self.items[self.rear+1] = item
            self.rear = (self.rear+1) % self.maxSize
            self.size += 1
        else:
            print("Queue is full")

    def dequeue(self):
        return_item = None
        if self.size > 0:
            return_item = self.items[self.front]
            self.front = (self.front+1)%self.maxSize
            self.size = self.size-1
        else:
            print("Nothing to remove from queue")
        return return_item

#Instantiate a Queue of size 5 elements
task2Queue = CircularQueue(5)
task2Queue.show()

# use input to force user to hit an enter key to progress through

# task steps
input("\nAdding J45, task2Queue using task2Queue.enqueue() ")
task2Queue.enqueue("J45")
task2Queue.show()

input("Adding J38 to task2Queue using task2Queue.enqueue()")
task2Queue.enqueue("J38")
task2Queue.show()

input("Adding J92 to task2Queue using task2Queue.enqueue()")
task2Queue.show()
task2Queue.enqueue("J92")

input("Removing item from task2Queue using task2Queue.dequeue()")
print(f'Removed queue item is {task2Queue.dequeue()}')
task2Queue.show()

input("Removing item from task2Queue using task2Queue.dequeue()")
print(f'Removed queue item is {task2Queue.dequeue()}')
task2Queue.show()

input("Adding J44 to task2Queue using task2Queue.enqueue()")
task2Queue.show()
task2Queue.enqueue("J44")