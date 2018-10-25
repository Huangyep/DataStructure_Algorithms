# 抢红包：
# 1.所有人抢到金额之和等于红包金额，不能超过，也不能少于。
# 2.每个人至少抢到一分钱。
# 3.要保证所有人抢到金额的几率相等。

# 二倍均值法
# 剩余红包金额为M，剩余人数为N，那么有如下公式：
# 每次抢到的金额 = 随机区间 （0， (M/N) X 2）
# import random
# m = int(input("红包金额:"))
# n = int(input("红包总数:"))
# def s1(m,n):
#     if n == 1:
#         return m
#     low = 1
#     high = int(m/n) * 2
#     money = random.randint(low,high)
#     return money
# while m>0 and n>0:
#     x = s1(m,n)
#     print(x)
#     m = m-x
#     n = n-1


# 线段切割法
# 当N个人一起抢红包的时候，就需要确定N-1个切割点。
# 做N-1次随机运算，以此确定N-1个切割点。随机的范围区间是（1， M）
# 当所有切割点确定以后，子线段的长度也随之确定。
# 这样每个人来抢红包的时候，只需要顺次领取与子线段长度等价的红包金额即可。
# import random
# m = int(input("红包金额:"))
# n = int(input("红包总数:"))
# l = [0,m]
# for i in range(n-1):
#     temp = random.randint(1,m)
#     while temp in l:
#         temp = random.randint(1,m)
#     l.append(temp)
# l = sorted(l)
# print(l)
# for j in range(1,len(l)):
#     print(l[j]-l[j-1])