from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Intuition: For each island we assume the perimeter is 4.
        Then we check if the island has a neighbor on the left or on the top.
        If it has, we subtract 2 from the perimeter for each of them.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Parameters
        ----------
        grid: List[List[int]]

        Returns
        -------
        int - perimeter of the island

        Examples
        --------
        >>> solution = Solution()
        >>> grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
        >>> solution.islandPerimeter(grid)
        16
        >>> grid = [[1]]
        >>> solution.islandPerimeter(grid)
        4
        >>> grid = [[1, 0]]
        >>> solution.islandPerimeter(grid)
        4
        """
        perimeter = 0
        rows = len(grid)
        columns = len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 1:
                    perimeter += 4
                    if row > 0 and grid[row - 1][column] == 1:
                        perimeter -= 2
                    if column > 0 and grid[row][column - 1] == 1:
                        perimeter -= 2

        return perimeter


if __name__ == "__main__":
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    solution = Solution()
    print(solution.islandPerimeter(grid))
    assert solution.islandPerimeter(grid) == 16
