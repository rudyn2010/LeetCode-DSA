# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #est. a dummy node to help manage edge cases (first element being removed)
        dummy = ListNode(0, next=head)
        prev, curr = dummy, head
        
        #while there is a head, or something there we will continue to iterate through 
        while curr:
            next = curr.next
            
            if curr.val == val:
                prev.next = next
                
            else:
                prev = curr
                
            curr = next
            
        return dummy.next