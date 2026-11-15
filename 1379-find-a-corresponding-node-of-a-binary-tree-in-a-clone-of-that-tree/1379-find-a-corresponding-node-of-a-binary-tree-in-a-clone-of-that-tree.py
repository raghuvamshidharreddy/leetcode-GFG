# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        from collections import deque
        q=deque()
        q.append(cloned)
        while q:
            p=q.popleft()
            if p.val==target.val:
                return p
            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)