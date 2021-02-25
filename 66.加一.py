#
# @lc app=leetcode.cn id=66 lang=python
#
# [66] 加一
#

# @lc code=start
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 利用python的列表转化
        digitsstr = "".join([str(i) for i in digits])
        digitsint = int(digitsstr)
        outint = digitsint + 1
        outlist = [int(i) for i in str(outint)]
        return outlist
        #根据最原始的思路遍历一遍所有的数字如果9
        #则上一位加1 如果不是9则正常返回
        # for i in range(len(digits)-1,0,-1):
        #     print(i)
        #     if digits[i] < 9:
        #         digits[i] += 1
        #         return digits
        #     else :
        #         digits[i] = 0
        #         if i == 0:
        #             digits.insert(1)
        #             return digits
                    
            


# @lc code=end

