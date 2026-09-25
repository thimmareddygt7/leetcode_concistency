class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            # 1. Find the kth node
            kth = group_prev

            for _ in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            # 2. Save the node after the group
            group_next = kth.next

            # 3. Reverse the k nodes
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # 4. Reconnect the reversed group
            old_group_start = group_prev.next

            group_prev.next = kth

            # 5. Move group_prev to the end of reversed group
            group_prev = old_group_start