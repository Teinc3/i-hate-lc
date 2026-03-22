class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        buckets: dict[int, set[int]] = {}

        for edge in edges:
            a, b = edge[0], edge[1]

            a_in_b = a in buckets
            b_in_b = b in buckets
            
            # If either of a/b is not in a bucket, add to the other bucket
            if a_in_b and not b_in_b:
                buckets[a].add(b)
                buckets[b] = buckets[a]
            elif b_in_b and not a_in_b:
                buckets[b].add(a)
                buckets[a] = buckets[b]

            # If neither of them are in a bucket, create a new bucket
            elif not a_in_b and not b_in_b:
                buckets[a] = buckets[b] = {a, b}

            else:
                # If both of them are in the same bucket
                # Then return
                if buckets[a] is buckets[b]:
                    return edge
                
                # As both are in different buckets, merge b's bucket into a
                # And update references for every item in b
                buckets[a].update(buckets[b])
                for node in buckets[b]:
                    buckets[node] = buckets[a]
            