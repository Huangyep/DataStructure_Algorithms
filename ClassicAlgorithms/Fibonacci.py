# 斐波那契实现
# 1 1 2 3 5 8 13 21 34 55……   f(n) = f(n-1) + f(n-2)

# 递归实现，n小的时候可以，n大的时候递归较深运行较久或者得不到结果
def fib1(n):
    if n < 2:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)


# 装饰器实现,如果计算过f(n)，那么保存下来，避免反复计算，这样n较大时候也能运算
from functools import wraps
def memo(func):
    cache = {} # 缓存，保存计算过的fib2(n),像一个备忘录
    @wraps(func)
    def wrap(*args):
        if args not in cache: # 如果没有计算过该n,计算fib2(n),并保存
            print(args,cache)
            cache[args] = func(*args)
        return cache[args] # 返回fib2(n)的结果，计算过了读cache直接返回
    return wrap

@memo
def fib2(n):
    if n < 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


# 递归，不用装饰器实现,这是计算单个f(n)比较适用,如果是多次计算的例如算f(1)到f(100),用装饰器较好，装饰器中cache会保存上一次计算的结果,不用重复计算。
def fib3(n):
    cache = [1,1]
    while len(cache) < n:
        temp = cache[-1] + cache[-2] # 类似平时手算的过程，前两个加得出下一个，从前往后推
        cache.append(temp)
    return cache

# 迭代实现
def fib_iter1(n):
    if n < 2:
        return 1
    a,b = 1,1
    c = 0
    while n >= 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c


