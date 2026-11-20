# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        def path(head, val, temp):
            if not head:
                return
            val += head.val
            temp.append(head.val)
            # Leaf node
            if not head.left and not head.right:
                if val == targetSum:
                    res.append(temp[:])   # copy the path
                temp.pop()
                return
            path(head.left, val, temp)
            path(head.right, val, temp)
            temp.pop()  # backtrack
        res=[]
        path(root,0,[])
        print(res)
        return res