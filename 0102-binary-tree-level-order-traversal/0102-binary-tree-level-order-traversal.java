/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        Deque<TreeNode> q= new ArrayDeque<>();
        List<List<Integer>> res=new ArrayList<>();
        if(root==null){
            return new ArrayList<>();
        }
        int level=0;
        q.addFirst(root);
        while(!q.isEmpty()){
            int lenq=q.size();
            res.add(new ArrayList<>());
            for(int i=0;i<lenq;i++){
                TreeNode node=q.removeFirst();
                res.get(level).add(node.val);
                if(node.left!=null){
                    q.addLast(node.left);
                }
                if(node.right!=null){
                    q.addLast(node.right);
                }
            }
            level++;
        }
        return res;
    }
}