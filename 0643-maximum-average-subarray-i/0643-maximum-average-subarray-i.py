class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    # Compute sum of the first window
        w = sum(nums[:k])
        s = w
        for i in range (k , len(nums)):
            w += nums[i] - nums[i-k]
            s = max(w,s)
        return s/k