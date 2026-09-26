# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None :
            return head
        slow = head 
        fast = head.next

        while fast is not None and fast.next is not None :
            slow = slow.next 
            fast = fast.next.next 
        mid = slow.next 
        slow.next = None 
        
        left = self.sortList(head)
        right = self.sortList(mid)

        return self.merge(left,right)
    def merge(self, left, right):
        
        dummy = ListNode(0)
        curr= dummy 
        while left and right :
                if left.val < right.val :

                    curr.next = left
                    left = left.next
                else:
                    curr.next = right 
                    right = right.next
                curr = curr.next 
        if left :
            curr.next = left
        else :
            curr.next = right
        return dummy.next
