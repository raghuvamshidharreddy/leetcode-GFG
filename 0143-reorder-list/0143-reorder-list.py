# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        # Step 1: Put all nodes in a list
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        # Step 2: Reorder using two pointers
        i, j = 0, len(nodes) - 1
        while i < j:
            # link i → j
            nodes[i].next = nodes[j]
            i += 1
            if i == j:
                break
            # link j → i
            nodes[j].next = nodes[i]
            j -= 1

        # Step 3: terminate the list
        nodes[i].next = None
