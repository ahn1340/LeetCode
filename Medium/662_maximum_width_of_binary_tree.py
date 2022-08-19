from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # bfs solution
        queue = deque()
        start = (root, 1, 1)  # node, level, idx
        queue.append(start)
        widths = []
        curr_level = 1
        w_max = -float('inf')
        w_min = float('inf')
        while queue:
            node, level, idx = queue.popleft()
            if level == curr_level + 1:
                widths.append(w_max - w_min + 1)
                w_max = -float('inf')
                w_min = float('inf')
                curr_level += 1
            
            w_max = max(w_max, idx)
            w_min = min(w_min, idx)
            if node.left:
                queue.append((node.left, level + 1, 2 * idx))
            if node.right:
                queue.append((node.right, level + 1, 2 * idx + 1))
        
        widths.append(w_max - w_min + 1)
        
        return max(widths)
    
"""
Simple BFS.
Time: O(n), Space: O(n) where n: number of nodes
"""
