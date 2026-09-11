# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative in order traversal, stopping as soon as the result is found

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr) # adding to the stack so that we can backtrack to it
                curr = curr.left
            
            # processing the node
            node = stack.pop()

            k -= 1
            if k == 0:
                return node.val
            
            curr = node.right

