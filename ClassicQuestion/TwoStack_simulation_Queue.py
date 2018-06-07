# 问题：两个栈实现队列入队出队操作
# 栈先进后出，队列先进先出。将stack1作为入栈操作，stack2作为出栈操作 

class FakeQueue:
	def __init__(self,maxsize):
		self.maxsize = maxsize
		self.stack1 = []
		self.stack2 = []

	def put(self,item):
		"""入队，对stack1进行入队操作"""
		if len(self.stack1) == self.maxsize:
			print("Queue is full!")
			return
		self.stack1.append(item)

	def get(self):
		"""出队,用stack2来出队"""
		if len(self.stack2) > 0:
			temp = self.stack2.pop()
			return temp
		else:
			if len(self.stack1) == 0:
				print("Queue is empty!")
				return
			# 将stack1中出栈进入stack2,此时为倒序了，stack1最先进入的在stack2的顶部
			while len(self.stack1) > 0:
				temp = self.stack1.pop()
				self.stack2.append(temp)
			return self.stack2.pop()
			# 下面调用后self.get(),要用return返回数值
			# return self.get()


if __name__ == '__main__':
	maxsize = 5
	q = FakeQueue(maxsize)
	q.put(1)
	q.put(2)
	one = q.get()
	two = q.get()
	three = q.get()
	print("Out:",one,two,three)