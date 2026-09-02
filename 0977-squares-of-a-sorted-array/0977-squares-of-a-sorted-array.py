class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr= []
        for i in range (len(nums)):
            s=nums[i]**2
            arr.append(s)
            arr.sort()
        return arr