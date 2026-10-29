class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums.sort()
        res = len(nums)//2
        return nums[res]