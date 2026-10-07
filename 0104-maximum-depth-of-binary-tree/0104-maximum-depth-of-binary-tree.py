# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if not root:
            return 0
        q=deque([root])
        level=0
        while(q):
            ql=len(q)
            for i in range(ql):
                t=q.popleft()
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            level+=1
        return level
