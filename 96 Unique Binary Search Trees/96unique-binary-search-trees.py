class Solution:
    def numTrees(self, n: int) -> int:
        node_count = 1
        combinations = [1] # N(0) = 1

        while node_count <= n:
            # We have node_count nodes (from 1 to node_count)
            # Select any node as root
            # Then count the number of LEFT and RIGHT subtrees
            # And them together.

            count = 0
            for root in range(1, node_count + 1):
                left_node_count = root - 1
                right_node_count = node_count - root
                combins_count = combinations[left_node_count] * combinations[right_node_count]
                count += combins_count

            # Push the current level's combinations 
            combinations.append(count)
            node_count += 1

        return combinations[n]
        