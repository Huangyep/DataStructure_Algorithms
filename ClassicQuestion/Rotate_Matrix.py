# 问题：N*N的矩阵逆时针旋转90度
# 解决方法：先沿着主对角线翻，再上下翻

def Print_Matrix(Matrix):
	"""直观地打印矩阵"""
	row = len(Matrix)
	columns = len(Matrix[0])
	print("Matrix now:")
	for i in range(row):
		for j in Matrix[i]:
			print(j,end=' ')
		print()

def Rotate_Matrix(Matrix):
	"""矩阵逆时针旋转90度"""
	row = len(Matrix)
	columns = len(Matrix[0])
	if row != columns:
		return
	# 将矩阵沿着主对角线翻转
	for i in range(row):
		for j in range(i): # 这里为i,对角线下与对角线上数据交换
			Matrix[i][j],Matrix[j][i] = Matrix[j][i],Matrix[i][j]
	Print_Matrix(Matrix)
	# 将矩阵上下翻转，两步后效果为逆时针旋转90度
	for i in range(int(row/2)):
		Matrix[i],Matrix[row-1-i] = Matrix[row-1-i],Matrix[i]
	Print_Matrix(Matrix)


if __name__ == '__main__':
	Matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	Print_Matrix(Matrix1)
	Rotate_Matrix(Matrix1)