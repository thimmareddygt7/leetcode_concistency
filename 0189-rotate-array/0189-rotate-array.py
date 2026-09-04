class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = k % len(nums)
        arr=[ ]
        for _ in range(n):
            res = nums.pop()
            arr.insert(0,res)
        nums[:] = arr+nums