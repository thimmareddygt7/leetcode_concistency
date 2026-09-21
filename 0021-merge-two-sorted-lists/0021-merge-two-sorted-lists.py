# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy 
        t1 = list1
        t2 = list2

        while t1 != None and t2 != None :
            if t1.val < t2.val :
                curr.next = t1
                curr=curr.next
                t1 = t1.next
            else:
                curr.next = t2
                curr = curr.next
                t2 = t2.next
        if t1!=None :
            curr.next =t1
        if t2!=None:
            curr.next = t2
        return dummy.next 