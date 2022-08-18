class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        coords = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        
        return coords[:k]
"""
Sort the coordinates according to its distance to the origin, and return the first k elements
Time: O(nlogn), Space: O(n), where n: length of points
"""
