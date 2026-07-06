# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        prev=None
        c=0
        head=None
        while l1!=None or l2!=None:
            if l1!=None and l2!=None:
                addi = l1.val+l2.val+carry
            elif l1==None:
                addi = l2.val+carry
            else:
                addi = l1.val+carry
            carry=0

            newNode = ListNode(addi)
            if c==0:
                head=newNode
                prev=newNode
            if addi > 9:
                curr=newNode.val
                newNode.val=int(str(curr)[1])
                carry = int(str(curr)[0])
            if c==0:            
                prev.next=None
                c=1
            else:
                prev.next=newNode
                prev=prev.next
            if l1!=None and l2!=None:
                l1=l1.next
                l2=l2.next
            elif l1==None:
                l2=l2.next
            else:
                l1=l1.next
        if carry>0:
            newNode = ListNode(carry)
            newNode.next=None
            prev.next = newNode
        else:
            prev.next=None


        return head
