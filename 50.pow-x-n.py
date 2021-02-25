#
# @lc app=leetcode.cn id=50 lang=python
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # res = 1
        # if n == 0:
        #     return 1
        # elif n > 0:
        #     return x * self.myPow(x,n - 1)
        # elif n < 0 :
        #     return 1 / x * self.myPow(x,n + 1)
        # if n == 0:
        #     return 1
        # elif n > 0:
        #     res = 1
        #     sum_ = x 
        #     while res <= n:
        #         sum_ = sum_ * sum_
        #         res = res * 2
        #     delta = res - n
        #     while delta > 0:
        #         x = x * x
        #         delta -= 1
        #     return sum_ / x
        # elif n < 0:
        #     res = 1
        #     x = 1 / x
        #     n = -n
        #     sum_ = x 
        #     while res <= n:
        #         sum_ = sum_ * sum_
        #         res = res * 2
        #     delta = res - n
        #     while delta > 0:
        #         x = x * x
        #         delta -= 1
        #     return sum_ / x
        return x**n




# @lc code=end

