#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_para = {
            "(" : 1,
            ")" : 19,
            "[" : 2,
            "]" : 18,
            "{" : 3,
            "}" : 17
        }
        length = len(s)
        lst = [string for string in s]
        if length % 2 != 0:
            return False
        lst_res = []
        for i in range(len(lst)):
            para = lst[i]
            if dict_para[para] <= 10:
                lst_res.append(para)
                i += 1
            else:
                if len(lst_res) == 0:
                    return False
                elif dict_para[para] + dict_para[lst_res[-1]] == 20:
                    i += 1
                    del lst_res[-1]
                else:
                    return False
        return len(lst_res) == 0                



        
# @lc code=end

