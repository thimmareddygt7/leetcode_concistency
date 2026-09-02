class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''arr= []
        for i in range (len(nums)):
            s=nums[i]**2
            arr.append(s)
            arr.sort()
        return arr'''

        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):

            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1

        return result