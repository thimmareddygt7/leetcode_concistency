# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        t =head
        p = None
        while t != None:

            next_node = t.next

            t.next = p

            p = t

            t = next_node
        return p