# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        first = head.next
        temp = head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        
        second = slow.next
        slow.next=None
        second = self.reverseList(second)

        chance=0
        while first!=None and second !=None:
            if(chance%2!=0):
                temp.next=first
                first = first.next
            else:
                temp.next=second
                second=second.next
            temp=temp.next
            chance+=1
        
        if first!=None:
            temp.next=first
        elif second!=None:
            temp.next=second
        

    
    def reverseList(self, head: Optional[ListNode]):
        curr = head
        temp = head
        prev = None

        while temp!=None:
            temp=temp.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
    

