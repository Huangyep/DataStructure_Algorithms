# 问题：一个数组array,超过一半为某一元素a,求a。
# 解决方法：火拼方法

import random

def AppearMoreThanHalf(array):
	length = len(array)
	temp = array[0]
	count = 1
	for i in range(1,length):
		if count > 0:
			if array[i] == temp:
				count += 1
			else:
				count -= 1
		elif count == 0:
			temp = array[i]
			count += 1
	if count > 0 and temp:
		return temp

if __name__ == '__main__':
	array1 = [random.randint(1,20)]*50+[random.randint(1,50) for i in range(40)]
	print("More than Half in array1:",array1[0])
	print(AppearMoreThanHalf(array1))

	array2 = [5,50,7,5,1,5,3,5,5,6,5]
	print(AppearMoreThanHalf(array2))