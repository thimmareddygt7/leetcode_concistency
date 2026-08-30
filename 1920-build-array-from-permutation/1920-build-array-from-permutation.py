class Solution(object):
    def buildArray(self, nums):
        n = len(nums)
        return [nums[nums[_]] for _ in range(n)]