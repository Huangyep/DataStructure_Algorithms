# 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # 递归实现
        if n < 2:
            return n
        a,b = 0,1
        while n >= 2:
            c = a+b
            a = b
            b = c
            n -= 1
        return c

