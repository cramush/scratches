# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
# A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.
#
# Example 1:
# Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
# Output: true
# Explanation:
# In the above grid, the diagonals are:
# "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
# In each diagonal all elements are the same, so the answer is True.
#
# Example 2:
# Input: matrix = [[1,2],[2,2]]
# Output: false
# Explanation:
# The diagonal "[1, 2]" has different elements.

# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:


class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:

        for i in range(len(matrix) - 1):
            for j in range(i, len(matrix[0]) - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False

        for i in range(len(matrix[0]) - 1):
            for j in range(i, len(matrix) - 1):
                if matrix[j][i] != matrix[j + 1][i + 1]:
                    return False

        return True


my_sol = Solution()
print(my_sol.isToeplitzMatrix(matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]))