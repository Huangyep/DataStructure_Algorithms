# 题目描述
# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        for i in range(1,len(rotateArray)):
            if rotateArray[i] < rotateArray[i-1]:
                return rotateArray[i]

    def minNumberInRotateArray2(self, rotateArray):
        # 二分查找
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray)-1
        mid = int((right + left)/2)
        while left < right:
            if rotateArray[mid-1] <= rotateArray[mid] and rotateArray[mid] <= rotateArray[mid+1]: # 这里要加等号，不然遇到连续的数据，返回错误的结果
                if rotateArray[mid] >= rotateArray[left]:
                    left = mid
                else:
                    right = mid
                mid = int((right + left)/2)
            elif rotateArray[mid] >= rotateArray[mid-1]:
                return rotateArray[mid+1]
            elif rotateArray[mid] < rotateArray[mid-1]:
                return rotateArray[mid]



x = [1,1,1,1,1,1,1,1,0,1]
s = Solution()
print(s.minNumberInRotateArray2(x))