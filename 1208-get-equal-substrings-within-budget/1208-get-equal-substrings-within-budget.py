class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cc = 0
        l = 0
        res = 0
        for r in range (len(s)):
            cc += abs(ord(s[r]) - ord(t[r]))
            while cc > maxCost :
                cc -= abs(ord(s[l]) - ord(t[l]))
                l +=1
            res = max(res,r - l + 1)
        return res