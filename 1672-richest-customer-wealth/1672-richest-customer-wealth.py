class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        result = [] 
        for i in range (len(accounts)):
            add = sum(accounts[i])
            result.append(add)
            i+1
        return max(result)