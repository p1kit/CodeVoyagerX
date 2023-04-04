"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

"""


from typing import List


class Solution:
    def dfs(self, grid: List[List[str]], row: int, column: int) -> None:
        """
        Helper function to traverse the grid and mark the visited cells as '0'.
        """

        rows = len(grid)
        columns = len(grid[0])
        if (
            row < 0
            or row >= rows
            or column < 0
            or column >= columns
            or grid[row][column] == "0"
        ):
            return
        grid[row][column] = "0"
        self.dfs(grid, row + 1, column)
        self.dfs(grid, row - 1, column)
        self.dfs(grid, row, column + 1)
        self.dfs(grid, row, column - 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Intuition: We traverse the grid and we count the number of islands.
        We use a helper function to traverse the grid and we mark the visited cells as '0'.
        We do this because we don't want to count the same island twice.

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Parameters
        ----------
        grid: List[List[str]]

        Returns
        -------
        int - number of islands

        Examples
        --------
        >>> solution = Solution()
        >>> grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
        >>> solution.numIslands(grid)
        1
        >>> grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
        >>> solution.numIslands(grid)
        3

        """
        islands = 0
        rows = len(grid)
        columns = len(grid[0])
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == "1":
                    islands += 1
                    self.dfs(grid, row, column)
        return islands


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    solution = Solution()
    print(solution.numIslands(grid))
    assert solution.numIslands(grid) == 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(solution.numIslands(grid))
    assert solution.numIslands(grid) == 3
