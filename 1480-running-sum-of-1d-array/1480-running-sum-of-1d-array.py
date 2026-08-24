class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        res = 0
        n = len(nums)
        for i in range (n ):

            res = res + nums[i]
            result.append(res)
        return result