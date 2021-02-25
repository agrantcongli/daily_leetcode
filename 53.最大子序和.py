#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#先用暴力解法，从第一个数字开始遍历所有子序
        lenght = len(nums)
        if lenght == 1:
            return sum(nums)
        maxSub = nums[0]
        for i in range(lenght - 1):
            for j in range(i,lenght):
                SumSub = sum(nums[i:j])
                if SumSub >= maxSub:
                    maxSub = SumSub
        return maxSub

# @lc code=end

