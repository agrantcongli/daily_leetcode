#
# @lc app=leetcode.cn id=11 lang=python
#
# [11] 盛最多水的容器
#
#暴力解法，将所有的可能性列出选择最大的
#时间溢出悲剧
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         Area = 0
#         lenght = len(height) 
#         if lenght<=1:
#             return Area
#         # dict_value = {}
#         for idx,num in enumerate(height):
#             idx_right = idx + 1
#             while idx_right < lenght:
#                 res = (idx_right - idx) * min(height[idx_right],num)
#                 if res > Area:
#                     Area = res
#                 idx_right += 1
#         return Area   
#从中间向两边找，如果左边的边比较矮则往左边找一个，
# 如果右边的边比较矮，那向右边找一个，直到找完所有的板子
# 时间复杂度O(n) 干掉了86%的时间
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        Area = 0
        length = len(height) - 1

        left = 0
        right = length

        while left <= right:
            res = (right - left) * min(height[left],height[right ])
            if res > Area:
                Area = res
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return Area



