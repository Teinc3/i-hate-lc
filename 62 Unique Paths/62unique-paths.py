class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Instantiate array
        combinations = [] # access through m*n

        for row in range(m):
            for col in range(n):
                local_combs = 0
                # Access LEFT if col > 1, access top if row > 1
                if col > 0:
                    local_combs += combinations[row*n + col - 1]
                if row > 0:
                    local_combs += combinations[(row-1)*n + col]
                
                local_combs = max(1, local_combs)
                combinations.append(local_combs)
        
        return combinations[-1]
