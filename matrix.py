
def MatrixAdd(Matrix1,Matrix2):
	"""矩阵加法"""
	m1row = len(Matrix1)
	m1columns = len(Matrix1[0])
	m2row = len(Matrix2)
	m2columns = len(Matrix2[0])
	if m1row!=m2row and m1columns!=m2columns:
		return
	result = []
	for i in range(m1row):
		eachrow = []
		for j in range(m1columns):
			eachrow.append(Matrix1[i][j]+Matrix2[i][j])
		result.append(eachrow)
	return result

def MatrixMinus(Matrix1,Matrix2):
	"""矩阵减法，和加法一个，改个符号就行"""
	m1row = len(Matrix1)
	m1columns = len(Matrix1[0])
	m2row = len(Matrix2)
	m2columns = len(Matrix2[0])
	if m1row!=m2row and m1columns!=m2columns:
		return
	result = []
	for i in range(m1row):
		eachrow = []
		for j in range(m1columns):
			eachrow.append(Matrix1[i][j]-Matrix2[i][j])
		result.append(eachrow)
	return result

def MatrixMultiply(Matrix1,Matrix2):
	"""矩阵乘法，一个矩阵的每一行乘以另一个的每一列"""
	m1row = len(Matrix1)
	m1columns = len(Matrix1[0])
	m2row = len(Matrix2)
	m2columns = len(Matrix2[0])
	if m1row == m2columns or m1columns == m2row:
		result = []
		for i in range(m1row):
			eachrow = []
			count = 0
			while count < m2columns:
				temp = 0
				for j in range(m1columns):
					temp += Matrix1[i][j]*Matrix2[j][count]
				eachrow.append(temp)
				count += 1
			result.append(eachrow)
		return result
	else:
		return

def MatrixTranspose(Matrix):
	"""矩阵转置"""
	row = len(Matrix)
	columns = len(Matrix[0])
	result = []
	for i in range(columns):
		eachrow = []
		for j in range(row):
			eachrow.append(Matrix[j][i])
		result.append(eachrow)
	return result


if __name__ == '__main__':
 	Matrix1 = [[1,2,3],[4,5,6]]
 	Matrix2 = [[7,8,9],[10,11,12]]
 	Matrix3 = [[1,1]]
 	print("MatrixAdd:",MatrixAdd(Matrix1,Matrix2)) 
 	print("MatrixMinus:",MatrixMinus(Matrix2,Matrix1))
 	print("MatrixMultiply:",MatrixMultiply(Matrix3,Matrix1))
 	print("MatrixTranspose:",MatrixTranspose(Matrix1))