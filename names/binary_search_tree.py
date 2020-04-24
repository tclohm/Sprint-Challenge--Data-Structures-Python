class BinarySearchTree:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	# Insert the given value into the tree
	def insert(self, value):
	# check the value against the node's value
	# if value is less than value, go left
		if value < self.value:
			if self.left:
				self.left.insert(value)
			else:
				self.left = BinarySearchTree(value)
		# if value is greater, go right
		else:
			# if the node.right is true, recurse
			if self.right:
				self.right.insert(value)
			else:
			# if the node.right is empty, store our node
				self.right = BinarySearchTree(value)
	
	# Return True if the tree contains the value
	# False if it does not
	def contains(self, target):
		if target == self.value:
			return True
		elif target < self.value:
			if self.left:
				return self.left.contains(target)
		else:
			if self.right:
				return self.right.contains(target)