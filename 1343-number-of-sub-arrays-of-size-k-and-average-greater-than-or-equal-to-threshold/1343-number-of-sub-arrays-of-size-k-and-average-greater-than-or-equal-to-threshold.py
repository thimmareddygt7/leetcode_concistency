class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s = sum(arr[:k])
        w = s
        count = 0
        if w >= k*threshold:
            count +=1

        for i in range (k , len(arr)):
            w = w-arr[i-k] +arr[i]
            if w >= k*threshold:
                count+=1
        return count
