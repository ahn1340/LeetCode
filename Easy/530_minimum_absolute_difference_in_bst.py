# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_sorted_list(node, arr):
            if node is not None:
                get_sorted_list(node.left, arr)
                arr.append(node.val)
                get_sorted_list(node.right, arr)

        array = []
        get_sorted_list(root, array)
        best = float('inf')
        for i in range(len(array) - 1):
            best = min(best, abs(array[i] - array[i+1]))
        
        return best
        
"""
Simple DFS to get sorted array + one traversal to find minimum difference. Time & Space: O(n)
"""
