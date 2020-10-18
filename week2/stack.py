class Stack:
	def __init__(self):
		self.internalArray = []

	def push(self, item):
		self.internalArray.append(item)

	def pop(self):
		if len(self.internalArray) == 0:
			print("Error: Stack empty")
		else:
			print("Popping stack: ",self.internalArray[-1])
			del self.internalArray[-1]

	def peek(self):
		print("Top item on stack:",self.internalArray[-1])

	def __str__(self):
		return self.internalArray.__str__()

stack1 = Stack()
stack1.push(1)
stack1.push(4)
stack1.push(9)
stack1.peek()
print(stack1)
stack1.pop()
stack1.pop()
stack1.pop()
stack1.pop()
print(stack1)


stack2 = Stack()
stack2.push("Linux")
stack2.push("Windows")
stack2.push("Mac OS X")
print(stack2)
stack2.pop()
stack2.pop()
print(stack2)