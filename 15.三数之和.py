#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#

# @lc code=start
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_nums = []
        nums.sort()
        if len(nums) < 3:
            return res_nums
        if nums[0] > 0:
            return res_nums
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i -1] :
                continue
            target = abs(nums[i])
            # dict_target = {}
            left_index = i + 1
            right_index = len(nums) - 1
            while left_index < right_index:
                if nums[left_index] + nums[right_index] > target:
                    while left_index < right_index:
                        if nums[right_index - 1] == nums[right_index]:
                            right_index -= 1
                        else:
                            break
                    right_index -= 1
                elif nums[left_index] + nums[right_index] < target:
                    while left_index < right_index:
                        if nums[left_index + 1] == nums[left_index]:
                            left_index += 1
                        else:
                            break
                    left_index += 1
                else:
                    res_nums.append([nums[i], nums[left_index], nums[right_index]])
                    while left_index < right_index:
                        if nums[left_index + 1] == nums[left_index]:
                            left_index += 1
                        else:
                            break
                    while left_index < right_index:
                        if nums[right_index - 1] == nums[right_index]:
                            right_index -= 1
                        else:
                            break
                    left_index += 1
                    right_index -= 1
        return res_nums
# @lc code=end

