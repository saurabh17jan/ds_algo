# 1. Two Sum
# Leet
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

# python3

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        ans = []
        # print(l)
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                # print(x, y)
                if  nums[x] + nums[y] == target:
                    ans.append(x)
                    ans.append(y)
                    return ans
