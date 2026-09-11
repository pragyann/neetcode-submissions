# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs_goodNodes(root: Optional[TreeNode], max_seen: int) -> int:
            if not root:
                return 0

            res = 0
            if root.val >= max_seen:
                res = 1

            max_seen = max(max_seen, root.val)

            return res + dfs_goodNodes(root.left, max_seen) + dfs_goodNodes(root.right, max_seen)

        return dfs_goodNodes(root, root.val)