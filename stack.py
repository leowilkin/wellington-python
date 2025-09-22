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
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
	        
#main
s = Stack()
myString = input("Please enter a word or phrase to be tested: ")
list1 = list(myString)
print(list1)
numChars = len(list1)
s = Stack()
#push the characters from the list onto the stack
for char in list1:
    s.push(char)

list2 = []
#now pop the items from the stack
for char in range(numChars):
    list2.append(s.pop())
if list1 == list2:
    print("This is a palindrome")
else:
    print("This is not a palindrome")