class Node():
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None

	#link prev and next nodes
	def link(self, otherNode):
		self.next = otherNode
		otherNode.prev = self

	#print node
	def __str__(self):
		return self.data.__str__()

class LinkedList():
	def __init__(self):
		self.first = None
		self.last = None

	
llist = LinkedList()

llist.first = Node(1)
second = Node(2)
third = Node(3)

llist.first.next(second)
second.next = third