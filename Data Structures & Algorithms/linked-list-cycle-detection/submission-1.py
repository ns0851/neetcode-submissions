# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        while temp!=None and temp.next!=None:
            temp = temp.next.next
            head=head.next
            if temp==head:
                return True
        return False