# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0)
        curr = dummy 
        dummy.next = head
        temp = head
        while curr.next !=None :
            if curr.next.val == val:
                #temp = temp.next.next
                curr.next = curr.next.next
                #temp = temp.next
            else:
                #temp = temp.next 
                curr = curr.next
                #temp = temp.next
        return dummy.next