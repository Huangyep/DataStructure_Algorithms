# 题目描述
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.l1 = []
        self.l2 = []

    def push(self, node):
        # write code here
        self.l1.append(node)

    def pop(self):
        # return xx
        while self.l1:
            temp = self.l1.pop()
            self.l2.append(temp)
        xx = self.l2.pop()
        while self.l2:
            temp = self.l2.pop()
            self.l1.append(temp)
        return xx