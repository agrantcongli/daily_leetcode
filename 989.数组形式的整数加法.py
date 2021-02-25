#
# @lc app=leetcode.cn id=989 lang=python
#
# [989] 数组形式的整数加法
#

# @lc code=start
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        num_A = 0
        for idx, num in enumerate(A[::-1]):
            num_A += 10**idx * num
        num_return = num_A + K
        return [i for i in str(num_return)]
        
# @lc code=end

