# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        dummy=TreeNode(0)
        self.curr=dummy
        res=[]
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.curr.right=TreeNode(root.val)
            self.curr=self.curr.right
            inorder(root.right)
        inorder(root)
        print(res)
        
        return dummy.right
