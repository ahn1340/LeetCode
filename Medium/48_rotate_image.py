import math

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def rotate(vector):
            return (0 * vector[0] + 1 * vector[1], -1 * vector[0] + 0 * vector[1])
        
        def center_coordinate(vector, center):
            return (vector[0] - center + 1, vector[1] - center + 1)
            
        def revert_to_index(vector, center, odd):
            val = 1 if odd else 0
            return (vector[0] + center - 1, vector[1] + center - val)
        
        def get_new_coord(vector):
            center = math.ceil(len(matrix[0]) / 2)
            if len(matrix[0]) % 2 == 1:
                odd = True
            else:
                odd = False
            idx = revert_to_index(rotate(center_coordinate(vector, center)), center, odd)
            
            return idx
            
        for i in range(len(matrix[0]) // 2):
            for j in range(i, len(matrix[i]) - (i + 1)):
                x, y = i, j
                val = matrix[x][y]
                for k in range(4):
                    x, y = get_new_coord((x, y))
                    nval = matrix[x][y]
                    matrix[x][y] = val
                    val = nval

"""
Convert indices to centered coordinates on a 2d plane and apply rotation to get the updated index.
Update the value at the new index iteratively until we are done.
Time: O(n), Space: O(1), where n is the number of elements in the matrix
"""
                    
