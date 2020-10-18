class Node:
	#init node data
	def __init__(self, data, next):
		self.data = data
		self.prev = None
		self.next = None

	#return printable version of self
	def __repr__(self):
		return repr(self.data)

class LinkedList:
	#init list with no head of list
	def __init__(self):
		self.head = None

	#return printable version of self
	def __repr__(self):
		nodes = []
		currentNode = self.head
		while currentNode:
			nodes.append(repr(currentNode))
			currentNode = currentNode.next
		return'[' + ', '.join(nodes) + ']'

	def add(self, data):
		if not self.head:
			self.head = Node(data = data)
			return
		currentNode = self.head
		while currentNode.next:
			currentNode = currentNode.next
		currentNode.next = Node(data = data, prev = currentNode)

llist = LinkedList()
llist

llist.add(1)
llist.add(2)
llist.add(3)