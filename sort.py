import time
import random
from functools import wraps


def decorator(fn):
	"""打印运行时间，数据量小的时候为0是正常情况,有迭代的不可用"""
	@wraps(fn)
	def wrapped(*args,**kwargs):
		st = time.time()
		l = fn(*args,**kwargs)
		et = time.time()
		runtime = et-st
		print("Runtime:%.3f%s" %(runtime,"s"))
		return l
	return wrapped

@decorator
def bubble_sort(relist):
	"""冒泡排序"""
	length = len(relist)
	for i in range(length):
		for j in range(0,length-1-i):
			if relist[j]>relist[j+1]:
				bridge = relist[j]
				relist[j] = relist[j+1]
				relist[j+1] = bridge
	return relist

def selection_sort(relist):
	"""选择排序"""
	length = len(relist)
	for i in range(length):
		minnum = relist[i]
		index = i
		for j in range(i+1,length):
			if relist[j] < minnum:
				minnum = relist[j]
				index = j
		relist[index] = relist[i]
		relist[i] = minnum
	return relist

def quick_sort(array):
	"""快速排序，分片+递归"""
	if len(array) < 2:
		return array
	else:
		# 这里取了列表第一个数来进行分片
		pivot = array[0]
		less = [i for i in array[1:] if i <= pivot]
		greater = [j for j in array[1:] if j > pivot]
		return quick_sort(less) + [pivot] + quick_sort(greater)

def random_quick_sort(array):
	"""随机快速排序，分片+递归，随机的下标用randint方法产生"""
	length = len(array)
	if length < 2:
		return array
	else:
		index = random.randint(0,length-1)
		pivot = array[index]
		a = array[:index]+array[index+1:]
		left = [i for i in a if i <= pivot]
		right = [j for j in a if j > pivot]
		return random_quick_sort(left)+[pivot]+random_quick_sort(right)

def insert_sort1(relist):
	"""插入排序,用python的insert和pop方法"""
	length = len(relist)
	for i in range(1,length):
		for j in range(i):
			if relist[i] < relist[j]:
				# 找到左边有序数组中比自己大的数时，在此位置插入
				relist.insert(j,relist[i])
				# 因为前面insert操作，所有后面的位数+1了，该数已经插入前面数组，所以pop
				relist.pop(i+1)
	return relist

def insert_sort2(relist):
	"""插入排序，对已排序的列表从后往前插入数据"""
	length = len(relist)
	for i in range(1,length):
		# 将要插入的数据暂存
		temp = relist[i]
		j = i
		# while循环，从左边有序序列的后面开始，如果j的前一位值比temp值大，
		# 那么relist[j-1]值后移一位，然后继续向前查找。
		while j>0 and relist[j-1]>temp:
			relist[j] = relist[j-1]
			j -= 1
		# 当找到前一位relist[j-1]小于等于temp时，此刻直接插入即可，后面数都已经后移了
		relist[j] = temp
		# 插入后，排序完成
	return relist


def shell_sort(relist):
	"""希尔排序，插入排序一种"""
	length = len(relist)
	gap = int(length/2)
	while gap>0:
		# 错开，进行插入排序
		for i in range(gap,length):
			temp = relist[i]
			j = i 
			# 对于前面已经排序好的列表，从后进行插入排序
			while j>=gap and relist[j-gap]>temp:
				relist[j] = relist[j-gap]
				j -= gap
			relist[j] = temp
		# 缩小gap
		gap = int(gap/2)
	return relist


def merge(left,right):
	"""左右列表进行归并操作"""
	result = []
	while left and right:
		if left[0] <= right[0]:
			temp = left.pop(0)
			result.append(temp)
		else:
			temp = right.pop(0)
			result.append(temp)
	while left:
		temp = left.pop(0)
		result.append(temp)
	while right:
		temp = right.pop(0)
		result.append(temp)
	return result
def merge_sort(relist):
	"""归并排序"""
	if len(relist) <= 1:
		return relist
	mid_index = int(len(relist)/2)
	# 递归拆解过程
	left = merge_sort(relist[:mid_index])
	right = merge_sort(relist[mid_index:])
	# 合并过程
	return merge(left,right)

def Max_Heapify(heap,HeapSize,root):
	"""在堆中做结构调整使得父节点大于子节点"""
	# 如果要用最小堆方法只要改成取三个点中最小的作为根节点
	left = 2*root + 1
	right = left + 1
	larger = root
	# 找出父节点和两个子节点中，最大的值
	if left<HeapSize and heap[larger]<heap[left]:
		larger = left
	if right<HeapSize and heap[larger]<heap[right]:
		larger = right
	# 如果找到子节点值比父节点大，进行调换
	if larger != root:
		bridge = heap[larger]
		heap[larger] = heap[root]
		heap[root] = bridge
		# 迭代往下调整
		Max_Heapify(heap,HeapSize,larger)
def Build_MaxHeap(heap):
	"""构造一个堆，构造完成后使根节点0的值为最大的，而且它是一个最大堆"""
	HeapSize = len(heap)
	# (HeapSize-2)//2是指树的最后一个值的父节点
	for i in range((HeapSize-2)//2,-1,-1):
		Max_Heapify(heap,HeapSize,i)
def heap_sort(heap):
	"""堆排序，最大堆"""
	Build_MaxHeap(heap)
	# 从后往前开始调整，由于构造完成后heap[0]为最大值
	# 所以将根节点取出与最后一位做对调，对前面(len-1)个节点继续进行调整
	for i in range(len(heap)-1,-1,-1):
		bridge = heap[0]
		heap[0] = heap[i]
		heap[i] = bridge
		# 继续调查，此时HeapSize=i，所以后面已经排好序的值不会受到影响
		Max_Heapify(heap,i,0)
	return heap

@decorator
def bucket_sort1(relist):
	"""桶排序,桶的数量小于(maxnum-minnum+1)的情况"""
	length = len(relist)
	maxnum = max(relist)
	minnum = min(relist)
	# 这里取最大最小值差的一半作为桶的数量，+1是因为差可能为奇数
	buckets_num = int((maxnum-minnum)/2)+1 
	buckets = []
	result = []
	# 先创建buckets_num个空桶
	for i in range(buckets_num):
		bucket = []
		buckets.append(bucket)
	for j in range(length):
		index = int((relist[j]-minnum)/2)
		if len(buckets[index]) == 0:
			buckets[index].append(relist[j])
		# 注意这里是elif或者直接为else,开始是if被自己坑了，前面append后len肯定为1了。
		elif len(buckets[index]) > 0:
			buckets[index].append(relist[j])
			# 桶内的排序直接用其他的了~
			buckets[index] = insert_sort2(buckets[index])
	# 遍历所有桶，输出有序数组
	for bucket in buckets:
		if len(bucket) > 0:
			for hapi in bucket:
				result.append(hapi)
		if len(bucket) == 0:
			continue
	return result

@decorator
def bucket_sort2(relist):
	"""桶排序，桶的数量刚好为(maxnum-minnum+1)的情况"""
	length = len(relist)
	# 求出relist数组中的最大、最小值，来构建temp数组
	maxnum = max(relist)
	minnum = min(relist)
	result = []
	temp = [0]*(maxnum-minnum+1)
	# 遍历relist进行计数
	for i in range(length):
		temp[relist[i]-minnum] += 1
	# 读取每个桶中数值的数量，输出有序数组
	for j in range(len(temp)):
		if temp[j] == 0:
			continue
		if temp[j] > 0:
			while temp[j]>0:
				result.append(j+minnum)
				temp[j] -= 1
	return result

def count_sort(relist):
	"""计数排序，输入relist数据为(0-maxmun)的正整数"""
	maxnum = max(relist)
	length = len(relist)
	result = [0]*(length)
	# temp先保存relist每个数据的计数，然后再转换成在result中的位置
	temp = [0]*(maxnum+1)
	# 遍历relist进行计数
	for num in relist:
		temp[num] += 1
	# 对所有计数累加，这样变成了result中的位置
	for i in range(1,maxnum+1):
		temp[i] = temp[i-1]+temp[i]
	# 遍历读取relist,输出有序数组
	for j in relist:
		# 读取位置，放入result中
		result[temp[j]-1] = j
		# 只能说想出这个算法的人很流弊，relist中有重复数据时，第一次读在temp在其位置上
		# 第二次又是一样的读temp中的位置，已经-1推前了，不会覆盖掉第一次存的
		temp[j] -= 1
	return result

def radix_sort(relist):
	"""基数排序，k为relist中的最高数位"""
	maxnum = max(relist)
	d = len(str(maxnum))
	# 每一个数位都进行一轮排序，从低位到高位
	for k in range(d):
		# 每一位都是0-9的数字，所以每一轮给10个桶进行排序
		s = [[] for j in range(10)]
		for i in relist:
			s[int(i/(10**k))%10].append(i)
			# 重新排序relist,这样低位排好序的结果在每次循环中可以保存下来
		relist = [a for b in s for a in b]
	return relist


if __name__ == '__main__':
	# relist = [1,5,2,6,6,9,3]
	# relist = [random.randint(1,1000) for i in range(2000)]
	# print(bubble_sort(relist))
	# print(selection_sort(relist))
	# print(quick_sort(relist))
	# print(random_quick_sort(relist))
	# print(insert_sort1(relist))
	# print(insert_sort2(relist))
	# print(shell_sort(relist))
	# print(merge_sort(relist))
	# print(heap_sort(relist))
	# print(bucket_sort1(relist))
	# print(bucket_sort2(relist))
	# print(count_sort(relist))
	print(radix_sort(relist))