class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        leftover=0
        for i in range(k):
            if(blocks[i]=="W"):
                leftover+=1
        first=0
        last=k
        ans=leftover
        while last<len(blocks):
            if(blocks[first]=="W"):
                leftover-=1
            if(blocks[last]=="W"):
                leftover+=1
            if(leftover<ans):
                ans=leftover
            last+=1
            first+=1
        return ans

            