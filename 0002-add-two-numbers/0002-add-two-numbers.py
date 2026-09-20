# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 != None or l2!= None or carry!=0:
            val1 = l1.val if l1 != None  else 0
            val2 = l2.val if l2 != None else 0
            total = val1 + val2+carry

            digits = total % 10 
            carry = total //10

            curr.next = ListNode(digits)
            curr = curr.next 

            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        return dummy.next