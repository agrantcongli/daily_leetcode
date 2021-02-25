#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
#暴力解法，O(n^2)的复杂度，贼烂的代码还写了10分钟太菜
# class Solution(object):
#     def twoSum(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """
#         for idx,num in enumerate(nums):
#             minus = target - num
#             j = idx + 1
#             while j < len(nums):
#                 if nums[j] == minus:
#                     return idx,j
#                 j += 1
#         return "no answer"

#使用字典将值存储起来保证时间复杂度是n
#正确解法 点赞
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_value = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in dict_value:
                # i应该放在后面的位置，因为i其实是第二个数的索引，第一个数的索引在dict_value内
                return [dict_value[diff], i] 
            dict_value[value] = i 

# @lc code=end

