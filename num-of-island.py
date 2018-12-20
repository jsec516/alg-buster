class Solution:
    def explore(self, row, col):
        if(self.isNotPartOfIsland(row, col)):
            return
        self.grid[row][col] = 0
        self.explore(row + 1, col)
        self.explore(row - 1, col)
        self.explore(row, col + 1)
        self.explore(row, col - 1)

    def numIslands(self, grid):
        self.grid = grid
        rowIndex = 0
        columnIndex = 0
        numOfIsland = 0
        self.rowLength = len(grid) - 1
        for row in self.grid:
            self.columnLength = len(row) - 1
            for column in row:
                if(self.isNotPartOfIsland(rowIndex, columnIndex) == False):
                    numOfIsland += 1
                    self.explore(rowIndex, columnIndex)
                columnIndex += 1
            columnIndex = 0
            rowIndex += 1
        return numOfIsland

    def isNotPartOfIsland(self, row, col):
        if(self.rowLength < row or row == -1):
            return True
        if(self.columnLength < col or col == -1):
            return True
        if(int(self.grid[row][col]) == 0):
            return True
        return False
  

# grid = [["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]
# soln = Solution()
# print(soln.numIslands(grid))
