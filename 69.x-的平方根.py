#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#

# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        for i in range(1,x+1):
            if (i * i > x) and((i - 1)*(i - 1) <=x) :
                return i -1
# @lc code=end

