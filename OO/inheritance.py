class Tree(object):
	def __init__(self, kind, height):
		self.kind = kind
		self.age = 0
		self.height = height

	def info(self):
		print("{} years old {}. {} meters high.".format(self.age, self.kind, 
														self.height))

	def grow(self):
		self.age += 1
		self.height += 0.5

class FruitTree(Tree):
	def __init__(self, kind, height):
		super().__init__(kind, height)

	def give_fruits(self):
		print("Collected 20kg of {}s".format(self.kind))

tree_1 = Tree("oak", 0.5)
tree_1.info()
tree_1.grow()
tree_1.info()

tree_2=FruitTree("apple", 0.7)
tree_2.info()
tree_2.grow()
tree_2.give_fruits()