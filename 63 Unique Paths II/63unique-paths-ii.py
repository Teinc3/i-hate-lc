class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        combinations = []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        for row in range(m):
            for col in range(n):
                local_combs = 0
                # Access LEFT if col > 1, access top if row > 1
                if obstacleGrid[row][col] == 0:
                    if col > 0:
                        local_combs += combinations[row*n + col - 1]
                    if row > 0:
                        local_combs += combinations[(row-1)*n + col]
                    if col == 0 and row == 0:
                        local_combs = 1

                combinations.append(local_combs)
        
        return combinations[-1]