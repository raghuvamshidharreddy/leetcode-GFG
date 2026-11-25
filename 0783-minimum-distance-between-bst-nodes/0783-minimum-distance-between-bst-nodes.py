# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        if not root :
            return 0
        from collections import deque
        q=deque()
        res=[]
        q.append(root)
        while q:
            len_q=len(q)
            for i in range(len_q):
                n=q.popleft()
                res.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        res.sort()
        ans=float('inf')
        for i in range(len(res)-1):
            ans=min(ans,abs(res[i]-res[i+1]))
        return ans