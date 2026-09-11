# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root: Optional[TreeNode], left: int, right: int) -> bool:
            if not root:
                return True

            if not (left < root.val and root.val < right):
                return False

            left_valid = valid(root.left, left, root.val)
            right_valid = valid(root.right, root.val, right)

            return left_valid and right_valid
        
        return valid(root, float('-inf'), float('inf'))
        


