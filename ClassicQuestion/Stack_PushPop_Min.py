# 问题：实现一个栈，要求Push,Pop,Min(返回最小值的操作)的时间复杂度为O(1)
# 解决方法：一个栈stack1来进行push,pop操作，另一个stackmin来保存min值

class StackReturnMin:
	def __init__(self):
		self.stack1 = []
		self.stackmin = []

	def push(self,item):
		# 第一次插入，min=item
		if len(self.stack1) == 0:
			self.stack1.append(item)
			self.stackmin.append(item)
		# 后面插入，如果有更小的就push入stackmin，此时栈顶为更stack1中的最小值
		else:
			self.stack1.append(item)
			# 注意是小于等于，可能多个相同的min
			if item <= self.stackmin[-1]:
				self.stackmin.append(item)
		print(str(item)+" Push Succeed!")


	def pop(self):
		temp = self.stack1.pop()
		print(str(temp)+" Pop Succeed!")
		# 如果最小值已经出栈，那么stackmin中也跟着pop出来
		if temp == self.stackmin[-1]:
			self.stackmin.pop()

	def returnmin(self,isReturn):
		if len(self.stackmin) > 0:
			print("Min in Stack now:",self.stackmin[-1])
		else:
			print("Min is empty!")
		if isReturn:
			return self.stackmin[-1]


if __name__ == '__main__':
	s = StackReturnMin()
	testlist = [5,2,3,2,4,1]
	for i in range(len(testlist)):
		s.push(testlist[i])
		s.returnmin(isReturn=False)
	for j in range(len(testlist)):
		s.pop()
		s.returnmin(isReturn=False)
