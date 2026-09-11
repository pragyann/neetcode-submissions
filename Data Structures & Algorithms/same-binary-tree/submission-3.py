# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not self.are_nodes_same(p, q):
            return False
        
        left = self.isSameTree(p.left, q.left)
        if not left:
            return False

        right = self.isSameTree(p.right, q.right)
        if not right:
            return False
        
        return True
        
    def are_nodes_same(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val
        elif not p and not q:
            return True
        
        return False
        