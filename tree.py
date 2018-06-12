# 完全二叉树的递归和非递归遍历

class Node:
	"""节点类"""
	def __init__(self, elem=-1, lchild=None, rchild=None):
		# 确定一个节点对象，如果有左右节点，那么它们的值也可以确定
		self.elem = elem
		self.lchild = lchild
		self.rchild = rchild


class Tree:
	"""树类"""
	def __init__(self):
		self.root = Node() # 树的根节点
		self.myQueue = [] # 用来赋值或者遍历用，并不是说myQueue中保存了树的所有信息

	def add(self,elem):
		"""为树添加节点"""
		# 构造节点对象
		node = Node(elem)
		# 第一次空根节点是Node类，它的elem=-1,第一个值先赋给根节点保存下来
		if self.root.elem == -1:
			self.root = node
			self.myQueue.append(self.root)
		else:
			# treeNode现在add的节点便是myQueue[0] 
			treeNode = self.myQueue[0]
			if treeNode.lchild == None:
				treeNode.lchild = node
				self.myQueue.append(treeNode.lchild)
			else:
				treeNode.rchild = node
				self.myQueue.append(treeNode.rchild)
				# 右节点赋值完成后，treeNode左右子节点都有了，pop(0)后对下一个节点赋值
				self.myQueue.pop(0)

	def front_digui(self,root):
		"""利用递归实现树的先序遍历"""
		if root == None:
			return
		print(root.elem,end=' ')
		self.front_digui(root.lchild)
		self.front_digui(root.rchild)

	def middle_digui(self,root):
		"""使用递归实现树的中序遍历"""
		if root == None:
			return
		self.middle_digui(root.lchild)
		print(root.elem,end=' ')
		self.middle_digui(root.rchild)

	def later_digui(self,root):
		"""利用递归实现树的后序遍历"""
		if root == None:
			return
		self.later_digui(root.lchild)
		self.later_digui(root.rchild)
		print(root.elem,end=' ')

	def front_stack(self,root):
		"""利用堆栈实现树的先序遍历"""
		if root == None:
			return
		myStack = []
		node = root
		while node or myStack:
			while node:                     #从根节点开始，一直找它的左子树
				print(node.elem,end=' ')
				myStack.append(node)
				node = node.lchild
			node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
			node = node.rchild 

	def middle_stack(self,root):
		"""利用堆栈实现树的中序遍历"""
		if root == Node:
			return
		myStack = []
		node = root
		while node or myStack:
			while node:
				myStack.append(node)
				node = node.lchild
			node = myStack.pop()
			print(node.elem,end=' ')
			node = node.rchild

	def later_stack(self,root):
		"""利用堆栈实现树的后序遍历"""
		if root == None:
			return
		myStack1 = []
		myStack2 = []
		node = root
		myStack1.append(node)
		# 第一个while循环的功能是找出后序遍历的逆序，存在myStack2里
		while myStack1:
			node = myStack1.pop()
			if node.lchild:
				myStack1.append(node.lchild)
			if node.rchild:
				myStack1.append(node.rchild)
			myStack2.append(node)
		# 第二个while循环将myStack2中的元素出栈，即为后序遍历次序
		while myStack2:
			print(myStack2.pop().elem,end=' ') 

	def level_queue(self,root,isReturn=False):
		"""利用队列实现树的层次遍历"""
		if root == -1 or root == None:
			return 
		temp = []
		result = []
		temp.append(self.root)
		while temp:
			treeNode = temp.pop(0)
			if not isReturn:
				print(treeNode.elem,end=' ')
			result.append(treeNode.elem)
			if treeNode.lchild:
				temp.append(treeNode.lchild)
			if treeNode.rchild:
				temp.append(treeNode.rchild)
		if isReturn:
			return result

	def height(self,root):
		"""获取二叉树的高度"""
		if root == None or root.elem == -1:
			return
		treenode = root
		height = 1
		while treenode.lchild:
			height += 1
			treenode = treenode.lchild
		return height

	def length(self,root):
		"""获取二叉树的长度,用左右子数的高度来比较,递归实现"""
		if root == None:
			return
		if root.lchild == None:
			return 1
		if root.rchild == None:
			return 2
		treenode = root
		lchildtree_height = self.height(treenode.lchild)
		rchildtree_height = self.height(treenode.rchild)
		# 如果左子树的高度等于右子树的高度，那么左子树是满的
		if lchildtree_height == rchildtree_height:
			left = 2**lchildtree_height - 1
			right = self.length(treenode.rchild)# 递归求不满的右子树高度
		else:
			# 如果右子树高度小于左子树，那么右子树是满的
			right = 2**rchildtree_height - 1
			left = self.length(treenode.lchild)# 递归求不满的左子树高度
		# 二叉树的长度为左子树节点数+根节点+右子树节点数
		return left + 1 + right



if __name__ == '__main__':
	tree = Tree()
	for elem in range(0,10):
		tree.add(elem)

	# print("Recursive",end='')
	# print("\nFrontTraverse")
	# tree.front_digui(tree.root)
	# print("\nMiddleTraverse")
	# tree.middle_digui(tree.root)
	# print("\nLaterTraverse")
	# tree.later_digui(tree.root)
	# print()

	# print("\nStack",end='')
	# print("\nFrontTraverse")
	# tree.front_stack(tree.root)
	# print("\nMiddleTraverse")
	# tree.middle_stack(tree.root)
	# print("\nLaterTraverse")
	# tree.later_stack(tree.root)
	# print()

	# print("\nQueue",end=' ')
	# print("\nLevelTraverse")
	# tree.level_queue(tree.root)
	# print()

	print("TreeHeight:",tree.height(tree.root))
	print("TreeLength:",tree.length(tree.root))


	