# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev= None
        curr = head
        temp = head
        length=0

        while temp.next!=None:
            length+=1
            temp=temp.next
        
        if length==0:
            return None
        
        front = (length+1)-n
        if front==0:
            head=head.next
            return head

        while front>0:
            prev=curr
            curr=curr.next
            front-=1
        
        prev.next=curr.next
        curr.next=None
    
        return head
