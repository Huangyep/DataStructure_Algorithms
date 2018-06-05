import time
import random
from functools import wraps


def decorator(fn):
	"""打印运行时间，数据量小的时候为0是正常情况"""
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


if __name__ == '__main__':
	relist = [1,5,2,6,6,9,3]
	# relist = [random.randint(1,1000) for i in range(1000)]
	# print(bubble_sort(relist))
	# print(selection_sort(relist))
	# print(quick_sort(relist))
	# print(insert_sort1(relist))
	# print(insert_sort2(relist))
	# print(shell_sort(relist))
	# print(merge_sort(relist))
	print(heap_sort(relist))