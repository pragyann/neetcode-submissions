# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], left: int, right: int) -> bool:
            if not root:
                return True
            
            res = left < root.val and root.val < right
            left_valid = dfs(root.left, left, root.val)
            right_valid = dfs(root.right, root.val, right)
            
            return res and left_valid and right_valid
        
        return dfs(root, float('-inf'), float('inf'))
        


