# 问题：用两个队列实现一个栈
# 解决方法：一个队列queue1用来入栈，出栈的话将queue1全部搬到queue2暂存，输出queue1最后一个
import queue

class FakeStack:
	"""栈，先进后出，用两个队列来实现"""
	def __init__(self,length):
		self.queue1 = []
		self.queue2 = []
		self.length = length

	def push(self,item):
		if len(self.queue1) == self.length:
			print("Stack is full!")
			return
		self.queue1.append(item)

	def pop(self):
		while True:
			# 用pop(0)方法模拟队列先进先出
			temp = self.queue1.pop(0)
			if len(self.queue1) > 0:
				self.queue2.append(temp)
			else:
				# 将queue2剩下的转移回queue1
				self.queue1 = self.queue2
				self.queue2 = []
				return temp
		

if __name__ == '__main__':
	maxsize = 5
	stack = FakeStack(maxsize)
	stack.push(1)
	stack.push(2)
	stack.push(3)
	one = stack.pop()
	two = stack.pop()
	three = stack.pop()
	print("Out:",one,two,three)