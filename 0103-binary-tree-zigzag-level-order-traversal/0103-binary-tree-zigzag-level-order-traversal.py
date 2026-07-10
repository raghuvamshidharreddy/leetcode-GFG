# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # here i am useing bfs
        # For Bfs 
        '''
        1. use a deque for storing node values
        2. level value for adding a another list inside it
        3. now take a boolean value for reversing the values
        '''
        q=deque()
        if root is None:
            return []
        level=0
        q.append(root)
        res=[]
        while q:
            len_q=len(q)
            res.append([])
            for i in range(len_q):
                node=q.popleft()
                res[level].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        for i in range(len(res)):
            if i%2!=0:
                res[i]=res[i][::-1]
        return res
