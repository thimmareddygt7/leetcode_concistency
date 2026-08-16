class Solution(object):
    def longestCommonPrefix(self, strs):
        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0][:min_len]