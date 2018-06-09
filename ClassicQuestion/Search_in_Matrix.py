# 问题：搜索二维数组1、2
# 问题1思路：先对行进行二分，再对列进行二分
# 问题2思路：从左下角往右上角比较进行查找

def Search_Matrix1(Matrix,target):
	"""二维数组每行递增，而且下一行第一个数大于上一行最后一个数"""
	row = len(Matrix)
	columns = len(Matrix[0])
	i_up = 0
	i_down = row-1
	# 先对行进行二分，这里是当i_up和i_down相邻为1时结束循环
	while i_down-i_up > 1:
		i_half = int((i_up+i_down)/2)
		if target == Matrix[i_half][0]:
			return True
		if target > Matrix[i_half][0]:
			i_up = i_half
		if target < Matrix[i_half][0]:
			i_down = i_half
	# 确定targer在哪一行，即是i值
	if target == Matrix[i_up][0] or target == Matrix[i_down][0]:
		return True
	else:
		if target < Matrix[i_down][0]:
			i = i_up
		else:
			i = i_down
	j_left = 0
	j_right = columns-1
	# 对第i行进行二分，存在targer则返回True
	while j_right-j_left > 1:
		j_half = int((j_left+j_right)/2)
		if target == Matrix[i][j_half]:
			return True
		if target > Matrix[i][j_half]:
			j_left = j_half
		if target < Matrix[i][j_half]:
			j_right = j_half
	if target == Matrix[i][j_left] or target == Matrix[i][j_right]:
		return True
	else:
		return False 


def Search_Matrix2(Matrix,target):
	"""二维数组每行递增，每列递增，每行每列无重复数值"""
	row = len(Matrix)
	columns = len(Matrix[0])
	i = row-1 # 这里注意-1，数组中是从0开始的下标
	j = 0
	while i >= 0 and j < columns:
		# 注意if-if和if-elif的区别
		if target == Matrix[i][j]:
			return True
		elif target > Matrix[i][j]:
			j += 1
		elif target < Matrix[i][j]:
			i -= 1
	return False


if __name__ == '__main__':
	Matrix1 = [ [1,3,5,6],[7,10,16,20],[23,30,34,50] ] 
	print(Search_Matrix1(Matrix1,16))
	Matrix2 = [ [1,3,5,7],[2,4,7,8],[3,5,9,10] ]
	print(Search_Matrix2(Matrix2,7))