from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # lptr, rptr = 0, n
        # element_counters + number of matching pairs (perf)
        # Bump n until matching pair equal and perf equal
        # Constrict l appropriately until violation
        # etc.
        lptr = 0
        min_window = (float('inf'), 0) # length, start
        m, n = len(s), len(t)
        target_counter = Counter(t)
        window_counter = Counter(s[:n])
        matches = sum(
            1 if window_counter[char] >= freq else 0
            for char, freq in target_counter.items()
        )
        match_total = len(target_counter)
        if matches == match_total: # For first match
            min_window = (n, lptr)

        for rptr in range(n, m):
            r_el = s[rptr]
            # Add new r_rel
            window_counter[r_el] += 1
            matches += (
                1 if window_counter[r_el] == target_counter[r_el] else 0
            )

            # Constrict lptr until violation
            while matches == match_total and rptr >= lptr + n - 1:
                min_window = min(min_window, (rptr - lptr + 1, lptr))
                old_el = s[lptr]
                lptr += 1
                # Evaluate the new match
                matches -= (
                    # window can't be 0 here, since we subtract later
                    1 if window_counter[old_el] == target_counter[old_el] else 0
                )
                window_counter[old_el] -= 1
                        
        if isinstance(min_window[0], float):
            return ""
        else:
            return s[min_window[1]:min_window[1] + min_window[0]]
