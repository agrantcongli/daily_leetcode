#
# @lc app=leetcode.cn id=9 lang=python
#
# [9] 回文数
#
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if len(str(x)) == 1:
            return True
        length = int(len(str(x)) / 2)
        for i in range(length):
            # print(i)
            if str(x)[i] == str(x)[-i-1]:
                continue
            else:
                return False
        return True



