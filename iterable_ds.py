class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.size = 0
        self.rear = 0
        self.front = 0
        self.maxSize = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.size

    def enqueue(self, item):
        if self.size == self.maxSize:
            print("queue is full, size = ",self.size)
        else:
            self.rear = (self.rear + 1) % self.maxSize

def build_ds(char_seq):
    start = None
    n = None
    for member in char_seq:
        if start is None:
            start = Node(member)
            n = start
        else:
            n.next = Node(member)
            n = n.next
    return start

def concat_ds(ds1, ds2):
    new_concat = Node(ds1.data)
    current_old = ds1.next
    current_new = new_concat
    while current_old:
        current_new.next = Node(current_old.data)
        # iterate onto the next node
        current_new = current_new.next
        current_old = current_old.next
    # when it reaches the end, link the last node to ds2
    current_new.next = ds2
    return new_concat

def append_ds(ds1, append_message):
    new_append = Node(ds1.data)
    current_old = ds1.next
    current_new = new_append
    while current_old:
        current_new.next = Node(current_old.data)
        # iterate onto the next node
        current_new = current_new.next
        current_old = current_old.next
    # when it reaches the end, link the last node to ds2
    current_new.next = append_message
    return new_append

def print_ds(message_input):
    current = message_input
    while current:
        print(current.data, end="")
        current = current.next
    print("\n")

def find_ds(ds,pos):
    current = ds
    for i in range(0,(pos+1)):
        if i == pos:
            if current is None:
                print("Out of range")
            else:
                print(current.data, end="")
        else:
                current = current.next

message = build_ds('Hello')
message2 = build_ds('World')

concat_message = concat_ds(message, message2)

print_ds(message)

print_ds(concat_message)

find_ds(concat_message,5)