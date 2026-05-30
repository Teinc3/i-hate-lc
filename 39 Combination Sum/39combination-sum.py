class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        outputs = []

        def candidate_nest(c_idx: int, prev_combins: list[int]):
            no = candidates[c_idx]
            prev_val = sum(prev_combins)
            for curr_combins in range(150 - len(prev_combins)):
                curr_val = no * curr_combins

                if prev_val + curr_val == target:
                    # Correct match - add
                    prev_combins.extend([no] * curr_combins)
                    outputs.append(prev_combins)
                    return 

                elif prev_val + curr_val > target:
                    return
                
                else: # still possible for a match
                    if c_idx == len(candidates) - 1:
                        continue # final candidate - so needs further bumping
                    else:
                        # Start exploring combins for the next candidate
                        combins = prev_combins.copy()
                        combins.extend(curr_combins * [no])
                        candidate_nest(c_idx + 1, combins)
        
        candidate_nest(0, list())
        return outputs

                
                