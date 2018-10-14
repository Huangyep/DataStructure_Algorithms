# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

# -*- coding:utf-8 -*-
class Solution:
    def tenTotwo(self,n):
        # n > 0
        result = ""
        while n > 0:
            temp = n % 2
            n = int(n / 2)
            result = str(temp) + result
        return result

    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0
        if n < 0:
            n = 2**32 + n # 负数转换为对应的正数，测试机器为32位
        count = 0
        while n > 0:
            if n%2 == 1:
                count += 1 # 统计1的个数
            n = int(n/2)
        return count

