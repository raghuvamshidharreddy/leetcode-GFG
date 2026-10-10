# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        while(head):
            l.append(head.val)
            head=head.next
        print(l)
        l=l[::-1]
        dummy=ListNode(0)
        curr=dummy
        for i in l:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next