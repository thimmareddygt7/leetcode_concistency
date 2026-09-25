class Solution:
    def reorderList(self, head: ListNode | None) -> None:

        if head is None or head.next is None:
            return

        # Step 1: Find middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        second = prev

        # Step 3: Merge two halves
        first = head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2