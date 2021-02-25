#
# @lc app=leetcode.cn id=58 lang=python
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        lis = s.rstrip().split(" ")
        if len(lis) == 0:
            return 0
        else:
            return len(lis[-1])


# @lc code=end

