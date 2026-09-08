class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        l = 0
        c = 0

        for i in range(len(s)):
            while s[i] in a:
                a.remove(s[l])
                l += 1

            a.add(s[i])
            c = max(c, i - l + 1)

        return c