# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        start=None
        temp=None

        if head1==None:
            return head2
        elif head2 == None:
            return head1

        if head1.val < head2.val:
            temp = head1
            head1=head1.next
        else:
            temp = head2
            head2=head2.next
        
        start = temp

        while head1 is not None and head2 is not None:
            if head1.val >= head2.val:
                temp.next = head2
                head2 = head2.next
            else:
                temp.next = head1
                head1 = head1.next
            temp=temp.next
        if head1 is not None:
            temp.next = head1
        elif head2 is not None:
            temp.next = head2
        return start
        