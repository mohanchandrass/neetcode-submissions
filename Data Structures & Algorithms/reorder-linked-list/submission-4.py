# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left,right = head,head

        while right and right.next:
            left = left.next
            right = right.next.next
        
        start = left

        prev = None
        curr = start.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        sec = prev
        start.next = None
        
        curr = head
        
        while curr and sec:
            
            nxt = curr.next
            snxt = sec.next
            
            curr.next = sec
            sec.next  = nxt

            curr = nxt
            sec = snxt

            
            
    


            
        