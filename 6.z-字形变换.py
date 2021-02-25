#
# @lc app=leetcode.cn id=6 lang=python
#
# [6] Z 字形变换
#

# @lc code=start
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        import collections
        if numRows == 1 or numRows >= len(s):
            return s
        else:
            string_idx_base = [i for i in range(0,numRows)] + [i for i in range(numRows-2,0,-1)]
            len_idx_base = len(string_idx_base)
            loop_count = int(len(s) / len_idx_base) + 1
            string_idx = string_idx_base * loop_count
            dict_return = collections.OrderedDict()
            for i in range(len(s)):
                if string_idx[i] in dict_return.keys():
                    dict_return[string_idx[i]] += s[i]
                else:
                    dict_return[string_idx[i]] = s[i]
            s_return = ""
            for value in dict_return.values():
                s_return += value
            return  s_return
            
        
# @lc code=end

