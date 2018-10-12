# 题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import math
# 解法1：先顺序获取链表的数据，然后返回逆序数组
class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return []
        values = []
        while listNode:
            values.append(listNode.val)
            listNode = listNode.next
        reverse_list = []
        # 逆序表获得1，用python的range逆序保存在reverse_list中
        # for i in range(len(values)-1,-1,-1):
        #     reverse_list.append(values[i])
        # return reverse_list
        # 逆序列表获得2，交换values首尾的元素位置
        length = len(values)
        index = int(math.ceil(length/2))
        for i in range(0,index):
            values[i],values[length-1-i] = values[length-1-i],values[i]
        return values


# 解法2：运用栈的先进后出
class Solution2:
    def printListFromTailToHead(self,listNode):
        if listNode == None:
            return []
        values = []
        while listNode:
            values.append(listNode.val) # 入栈
            listNode = listNode.next
        reversed_list = []
        while values:
            value = values.pop()  # 出栈
            reversed_list.append(value)
        return reversed_list


# 解法3：递归实现
class Solution3:
    def printListFromTailToHead(self,listNode):
        if listNode == None: # 递归到链表为空，返回
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]