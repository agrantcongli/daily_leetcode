#
# @lc app=leetcode.cn id=67 lang=python
#
# [67] 二进制求和
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_max = max(len(a),len(b))
        a = "0" * (len_max - len(a)) + a
        a = a[::-1]
        b = "0" * (len_max - len(b)) + b
        b = b[::-1]
        result = ""
        flag = 0
        for idx in range(len_max):
            if flag == 0:
                flag = (int(a[idx]) + int(b[idx])) / 2
                result += str((int(a[idx]) + int(b[idx])) % 2)
            else:
                flag = (int(a[idx]) + int(b[idx]) + 1) / 2
                result += str((int(a[idx]) + int(b[idx]) + 1) % 2)

        if flag == 1:
            result += "1"
        return result[::-1]
               

# @lc code=end

