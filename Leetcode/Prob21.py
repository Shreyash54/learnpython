You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

code:
from typing import List
class Solution:
    def maxareaisland(self,grid:List[List[int]])->int:
        def dfs(i:int,j:int)->int:
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)

        area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    area=max(area,dfs(i,j))
        return area
sol=Solution()
print(sol.maxareaisland([[0,0,1,0,0,0,0,1,0,0,0,0,0],
                         [0,0,0,0,0,0,0,1,0,1,0,0,0],
                         [0,1,1,0,1,0,0,0,0,0,0,0,0],
                         [0,1,0,0,1,1,0,0,1,0,0,0,0],
                         [0,1,0,0,1,1,0,0,1,1,1,0,0],
                         [0,0,0,0,0,0,0,0,0,0,1,0,0],
                         [0,0,0,0,0,0,0,1,1,1,0,0,0],
                         [0,0,0,0,0,0,0,1,1,0,0,0,0]]))
