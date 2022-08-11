# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(node, low, high):
            if not low < node.val < high:
                return False
            else:
                if node.left is not None:
                    left = recursion(node.left, low, node.val)
                else:
                    left = True
                if node.right is not None:
                    right = recursion(node.right, node.val, high)
                else:
                    right = True
                return left and right

        return recursion(root, -float('inf'), float('inf'))

"""
Simple Recursive DFS.
"""
