class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next != None and prev.next.next != None:
            first = prev.next
            second = first.next

            temp = second.next

            prev.next = second
            second.next = first
            first.next = temp

            prev = first

        return dummy.next