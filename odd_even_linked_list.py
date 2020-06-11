# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next ==None:
            return head
        head1=head
        head2,head2_beg= head.next,head.next
        while head2.next!= None and head2.next.next!= None:
            head1.next = head2.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next
        if head2.next!=None:
            head1.next = head2.next
            head1 = head1.next
        head1.next = head2_beg
        head2.next = None
        return head