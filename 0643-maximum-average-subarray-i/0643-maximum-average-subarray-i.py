class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    # Compute sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window: add new element, remove old element
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k
        