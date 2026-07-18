# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        # now slow is at mid
        # disconnect the two halves of the list
        second_head = slow.next
        slow.next = None
        # reverse every node from slow to fast (end of list)
        # HOW TO REVERSE A LINKED LIST 
        curr = second_head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # alternate nodes from front half and back half (one each)
        left = head
        right = prev
        while left and right:
            tempLeft = left.next
            tempRight = right.next
            left.next = right
            left = tempLeft
            right.next = left
            right = tempRight

            # 1->2->None
            # 5->4->3->None
    
        return


        
        #find middle (with slow pointer)
        #slow = 6
        #fast = 10
        #reverse the second half
        #[2,4] and [10, 8, 6]
        #merge (start from left half)
        #normally left half will finish faster -> add the rest of right
