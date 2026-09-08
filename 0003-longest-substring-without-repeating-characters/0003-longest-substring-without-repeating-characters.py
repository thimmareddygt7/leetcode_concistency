class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        left = 0
        count = 0

        for i in range(len(s)):
            while s[i] in ans:
                ans.remove(s[left])
                left += 1

            ans.add(s[i])
            count = max(count, i - left + 1)

        return count