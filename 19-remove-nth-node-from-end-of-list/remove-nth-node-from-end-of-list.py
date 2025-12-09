from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to simplify edge cases (removing the head)
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Move fast n+1 steps ahead so that when fast reaches the end,
        # slow is just before the node to remove
        for _ in range(n + 1):
            if fast is not None:
                fast = fast.next
            else:
                # If n is larger than the length, just return head (defensive)
                return head

        # Move both pointers until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        # Remove the target node
        to_remove = slow.next
        slow.next = to_remove.next
        # Optional: explicitly free memory if needed (not required in Python)
        # del to_remove

        return dummy.next