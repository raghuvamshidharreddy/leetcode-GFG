# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        def inorder(root,res):
            if root is None:
                return 
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
        res=[]
        inorder(root,res)
        n=len(res)
        sufixSum=[0]*(n)
        sufixSum[n-1]=res[n-1]
        for i in range(len(res)-2,-1,-1):
            sufixSum[i]=sufixSum[i+1]+res[i]
        dic={}
        for i in range(n):
            dic[res[i]]=sufixSum[i]
        def changer(root,dic):
            if root is None:
                return 
            root.val=dic[root.val]
            changer(root.left,dic)
            changer(root.right,dic)
        changer(root,dic)
        return root