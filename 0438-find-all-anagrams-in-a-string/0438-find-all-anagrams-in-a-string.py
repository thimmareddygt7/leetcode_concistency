class Solution:
    def findAnagrams(self, s: str, p: str):

        if len(p) > len(s):
            return []

        p_count = {}
        s_count = {}
        ans = []

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        for i in range(len(p)):
            s_count[s[i]] = s_count.get(s[i], 0) + 1

        if s_count == p_count:
            ans.append(0)

        for i in range(len(p), len(s)):

            # add new character
            s_count[s[i]] = s_count.get(s[i], 0) + 1

            # remove old character
            old = s[i - len(p)]
            s_count[old] -= 1

            if s_count[old] == 0:
                del s_count[old]

            if s_count == p_count:
                ans.append(i - len(p) + 1)

        return ans