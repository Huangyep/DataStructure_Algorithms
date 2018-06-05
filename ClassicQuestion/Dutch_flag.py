# 荷兰国旗问题，将红白蓝分别记为0，1，2。解决方法是将0全部放前面，1全部放后面。
import random

def Dutch_Flag(relist):
	length = len(relist)
	begin = 0
	end = -1
	current = 0
	while True:
		# 如果为0，那么要放到前面，注意begin和current的值要互换，因为begin处的值可能为1。
		# 然后begin、current都向右移
		if str(relist[current]) == "0":
			relist[begin],relist[current] = relist[current],relist[begin]
			begin += 1
			current += 1
		# 如果为1，那么在中间，不影响begin和end,current右移即可
		if str(relist[current]) == "1":
			current += 1
		# 如果为2，那么放在最后，end和current的值互换，end左移，
		# 但是current不能右移，因为此刻换后relist[current]的值未知，需要重新判断。
		if str(relist[current]) == "2":
			relist[end],relist[current] = relist[current],relist[end]
			end -= 1
		if int(current)-int(end) == length:
			break
	return relist


if __name__ == '__main__':
	relist = [random.randint(0,2) for i in range(20)]
	print(relist)
	print(Dutch_Flag(relist))

		