# import time
# start_time = time.time()
# # for a in range(0,1001):
# #     for b in range(0,1001):
# #         for c in range(0,1001):
# #             if a+b+c== 1000 and a**2 + b**2 == c**2:
# #                 print("a:",a,"b:",b,"c:",c)
# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000 - a - b
#         if a**2 + b**2 == c**2:
#             print("a:",a,"b:",b,"c:",c)
#
# end_time = time.time()
# print("cost_time",end_time - start_time)

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         Area = 0
#         length = len(height) - 1
#
#         left = 0
#         right = length
#
#         while left <= right:
#             left_value = height[left]
#             right_value = height[right ]
#             res = (right - left) * min(height[left],height[right ])
#             if res > Area:
#                 Area = res
#             if min(height[left],height[right]) == height[left]:
#                 left += 1
#             else:
#                 right -= 1
#         return Area

# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
# #先用暴力解法，从第一个数字开始遍历所有子序
#         lenght = len(nums)
#         if lenght == 1:
#             return sum(nums)
#         maxSub = max(nums)
#         lenght = len(nums)
#         if lenght == 1:
#             return sum(nums)
#         maxSub = nums[0]
#         for i in range(lenght - 1):
#             for j in range(i,lenght):
#                 SumSub = sum(nums[i:j])
#                 if SumSub >= maxSub:
#                     maxSub = SumSub
#         return maxSub


# class Solution(object):
#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#
#         # digitsstr = "".join([str(i) for i in digits])
#         # digitsint = int(digitsstr)
#         # outint = digitsint + 1
#         # outlist = [int(i) for i in str(outint)]
#         # return outlist
#         for i in range(len(digits)-1,0,-1):
#             print(i)
#             if digits[i] < 9:
#                 digits[i] += 1
#                 return digits
#             else :
#                 digits[i] = 0
#                 if i == 0:
#                     digits.insert(1)
#                     return digits
#
# class Solution(object):
#     def judge(self,a,b):
#         if (a == "{") and (b == "}"):
#             return True
#         elif (a == "[" and b == "]"):
#             return True
#         elif (a == "(" and b == ")"):
#             return True
#         else:
#             return False
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         dict_para = {
#             "(" : 1,
#             ")" : 19,
#             "[" : 2,
#             "]" : 18,
#             "{" : 3,
#             "}" : 17
#         }
#         length = len(s)
#         lst = [string for string in s]
#         if length % 2 != 0:
#             return False
#         lst_res = []
#         for i in range(len(lst)):
#             para = lst[i]
#             if dict_para[para] <= 10:
#                 lst_res.append(para)
#                 i += 1
#                 para_2 = lst_res[-1]
#
#             else:
#                 if len(lst_res) == 0:
#                     return False
#                 elif dict_para[para] + dict_para[lst_res[-1]] == 20:
#                     i += 1
#                     del lst_res[-1]
#                 else:
#                     return False
#         return len(lst_res) == 0

# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res_nums = []
#         nums.sort()
#         if len(nums) < 3:
#             return res_nums
#         if nums[0] > 0:
#             return res_nums
#         for i in range(len(nums) - 2):
#             if i > 0 and nums[i] == nums[i -1] :
#                 continue
#             target = abs(nums[i])
#             # dict_target = {}
#             left_index = i + 1
#             right_index = len(nums) - 1
#             while left_index < right_index:
#                 if nums[left_index] + nums[right_index] > target:
#                     while left_index < right_index:
#                         if nums[right_index - 1] == nums[right_index]:
#                             right_index -= 1
#                         else:
#                             break
#                     right_index -= 1
#                 elif nums[left_index] + nums[right_index] < target:
#                     while left_index < right_index:
#                         if nums[left_index + 1] == nums[left_index]:
#                             left_index += 1
#                         else:
#                             break
#                     left_index += 1
#                 else:
#                     res_nums.append([nums[i], nums[left_index], nums[right_index]])
#                     while left_index < right_index:
#                         if nums[left_index + 1] == nums[left_index]:
#                             left_index += 1
#                         else:
#                             break
#                     while left_index < right_index:
#                         if nums[right_index - 1] == nums[right_index]:
#                             right_index -= 1
#                         else:
#                             break
#                     break
#         return res_nums


# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         len_max = max(len(a),len(b))
#         a = "0" * (len_max - len(a)) + a
#         a = a[::-1]
#         b = "0" * (len_max - len(b)) + b
#         b = b[::-1]
#         result = ""
#         flag = 0
#         for idx in range(len_max):
#             if flag == 0:
#                 flag = (int(a[idx]) + int(b[idx])) / 2
#                 result += str((int(a[idx]) + int(b[idx])) % 2)
#             else:
#                 flag = (int(a[idx]) + int(b[idx]) + 1) / 2
#                 result += str((int(a[idx]) + int(b[idx]) + 1) % 2)
#
#         if flag == 1:
#             result += "1"
#         return result[::-1]

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

if __name__ == "__main__":

    solution = Solution()
    print(solution.convert("PAYPALISHIRING",3))