# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = dummy
        second = dummy
        while n != 0:
            first = first.next
            n -= 1
        # now we've created the distance
        while first.next:
            first = first.next
            second = second.next
        # first is at the end and second is the node before the nth from the end
        second.next = second.next.next
        return dummy.next