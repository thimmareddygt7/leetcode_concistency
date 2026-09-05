class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        numZeros = []
        ans = []
        for i in range (n):
            if nums[i] == 0:
                numZeros.append(nums[i])
                
            elif nums[i] != 0:
                ans.append(nums[i])
                
        nums[:] = ans+numZeros

                    
