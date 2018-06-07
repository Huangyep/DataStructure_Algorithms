# 无序数组在排序后相邻数的最大差值问题，要求时间复杂度为O(n)
import random

def MaxGap_in_SortedArray(relist):
	length = len(relist)
	if length < 2:
		return 
	maxnum = max(relist)
	minnum = min(relist)
	# 桶的长度为relist的长度
	temp = [[]]*length
	# 将minnum放在第一个桶，maxnum放在最后一个桶，然后均匀的划分
	per = (maxnum-minnum+1)/length
	for i in range(length):
		# 算出在relist[i]在哪一个桶，数学很重要啊！
		index = int((relist[i]-minnum)/per)
		if len(temp[index]) == 0:
			min_max_list = [relist[i],relist[i]]
			temp[index] = min_max_list
		elif len(temp[index]) > 0:
			# temp[index][1]记录桶中最大值
			if relist[i] > temp[index][1]:
				temp[index][1] = relist[i]
			# temp[index][0]记录桶中最小值	
			if relist[i] < temp[index][0]:
				temp[index][0] = relist[i] 
	maxgap = 0
	# 先找出第一个有数据的桶，记录桶中最大值
	for j in range(length):
		if len(temp[j]) != 0:
			forntnum = temp[j][1]
			k = j
			break
	# 然后从后面开始遍历，gap为后一个有数据的桶的最小值-forntnum.
	for j in range(k+1,length):
		if len(temp[j]) != 0:
			if temp[j][0]-forntnum > maxgap:
				maxgap = temp[j][0]-forntnum
			# 如果找到了有数据的桶，那么forntnum就要更新为temp[j][1]
			forntnum = temp[j][1]
		else:
			continue
	print(maxgap)


if __name__ == '__main__':
	relist = [random.randint(1,500) for i in range(200)]
	# relist = [1,8,3,1]
	# relist = [1,2,23,46,44,20,8]
	MaxGap_in_SortedArray(relist)