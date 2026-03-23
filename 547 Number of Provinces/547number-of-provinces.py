class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        buckets: dict[int, set[int]] = {
            x: None for x in range(0, n)
        }
        bucket_count = 0

        for i in range(0, n):
            for j in range(0, i+1): # Symmetric, no need to include i=j
                i_in_b = buckets[i] != None
                j_in_b = buckets[j] != None

                if isConnected[i][j] == 1:
                    if i_in_b and not j_in_b:
                        buckets[i].add(j)
                        buckets[j] = buckets[i]
                    elif j_in_b and not i_in_b:
                        buckets[j].add(i)
                        buckets[i] = buckets[j]
                    elif i_in_b and j_in_b:
                        if buckets[i] is buckets[j]:
                            continue
                        # Merge j's bucket into i and update all references
                        buckets[i].update(buckets[j])
                        for j_items in buckets[j]:
                            buckets[j_items] = buckets[i]
                        bucket_count -= 1
                    else:
                        # Create common bucket
                        buckets[i] = buckets[j] = {i, j}
                        bucket_count += 1
                else:
                    # Create new buckets if necessary
                    if not i_in_b:
                        buckets[i] = {i}
                        bucket_count += 1
                    if not j_in_b:
                        buckets[j] = {j}
                        bucket_count += 1
        
        return bucket_count
