# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        t = head 
        values = []
        while t != None :
            values.append(t.val)
            t=t.next
        if values == values[::-1]:
            return True
        return False 
