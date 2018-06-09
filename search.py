
def sequence_search(array,target):
	"""顺序查找"""
	length = len(array)
	for i in range(length):
		if target == array[i]:
			return i
	return False

def binary_search1(array,target):
	"""二分查找，用while循环"""
	length = len(array)
	left = 0
	right = length-1
	while right-left > 1:
		middle = int((left+right)/2)
		if target == array[middle]:
			return middle
		if target > array[middle]:
			left = middle
		if target < array[middle]:
			right = middle
	if target == array[left]:
		return left
	if target == array[right]:
		return right
	return False

def binary_search2(array,target):
	"""二分查找，递归。由于通过列表切片的方法，所以不好返回在array的具体位置"""
	length = len(array)
	if length == 1:
		if target == array[0]:
			return True
		else:
			return False
	left = 0
	right = length - 1
	middle = int((left+right)/2)
	if target == array[middle]:
		return True
	if target > array[middle]: 
		# 注意切片，后面的是不包括的。从middle+1到right,后面要写成right+1
		return binary_search2(array[middle+1:right+1],target)
	if target < array[middle]:
		#　这里也一样的道理，开始被坑了
		return binary_search2(array[left:middle],target)

def binary_search3(array,target,left,right):
	"""二分查找，递归。为了返回在array中的具体位置，用left，right来切割数组"""
	if right-left == 0:
		if target == array[left]:
			return left
		return False
	middle = int((left+(right-left)/2))
	if target == array[middle]:
		return middle
	if target > array[middle]:
		return binary_search3(array,target,middle+1,right)
	if target < array[middle]:
		return binary_search3(array,target,left,middle-1)

def insert_search(array,target,left,right):
	"""插值查找,递归"""
	# 这个判断真的非常重要，原因可能array[middle] < target < array[middle+1]时，
	# 那么下一次递归的target-array[left]为负数，可能导致求middle出现万劫不复的循环迭代当中
	# 例子array2=[1,3,5,7,8,10],查找4，如果没有这一个判断，将是不断的迭代
	if target < array[left] or target > array[right]:
		return False
	if right-left == 0:
		if target == array[left]:
			return left
		return False
	# 按比例不断趋近于target，对于分布均匀的array效果好
	middle = int(left + ((target-array[left])/(array[right]-array[left]))*(right-left))
	if target == array[middle]:
		return middle
	if target > array[middle]:
		return insert_search(array,target,middle+1,right)
	if target < array[middle]:
		return insert_search(array,target,left,middle-1)



if __name__ == '__main__':
	array1 = [3,13,2,1,5,8]
	array2 = [1,3,5,7,8,10]
	# print("SequenceSearch: i =",sequence_search(array1,1))
	# print("BinarySearch1: i =",binary_search1(array2,10))
	# print("BnarySearch2:",binary_search2(array2,15))
	# print("BinarySearch3: i =",binary_search3(array2,8,0,len(array2)-1))
	print("InsertSearch: i =",insert_search(array2,4,0,len(array2)-1))