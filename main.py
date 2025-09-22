class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node('A')

print(node1.data)

node1.data ='B'

print(node1.data)

node2 = Node('C')

node1.next = node2

print(node1.data, node1.next.data)

print(f'Contents of node1 is {node1.data} and node2 is {node2.data}')