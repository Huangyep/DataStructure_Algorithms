# c(n,k)表示在n个中选k个，有多少种选法，无顺序的

# 递归实现
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def cnk(n,k):
    if k == 0: return 1 # k,n的顺序不能改变，cnk(1,1)=cnk(0,1)+cnk(0,0),k在前保证cnk(0,0)=1,n在前等于0，返回错误结果
    if n == 0: return 0
    else:
        return cnk(n-1,k-1) + cnk(n-1,k)


# 迭代实现
from collections import defaultdict
def cnk2(n,k):
    C = defaultdict(int)
    for row in range(n+1):
        C[row,0] = 1  # 相当于k=0时，返回1
        for col in range(1,k+1):
            C[row,col] = C[row-1,col-1] + C[row-1,col] # defaultdict当C中值不存在时，返回默认值0
    return C[n,k]
