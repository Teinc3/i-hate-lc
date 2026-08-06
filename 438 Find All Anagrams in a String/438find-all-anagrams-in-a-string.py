from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        anagram_counter = Counter(p)
        curr_counter = Counter(s[:len(p)])
        perf = sum(
            1 if v == curr_counter[k] else 0 for k, v in anagram_counter.items()
        )
        p_len = len(p)
        ac_len = len(anagram_counter)
        indices = []

        if ac_len == perf:
            indices.append(0)
        for ptr in range(1, len(s) - p_len + 1):
            new_el = s[ptr + p_len - 1]
            old_el = s[ptr - 1]
            if new_el != old_el:
                curr_counter[new_el] += 1
                perf += (
                    1 if curr_counter[new_el] == anagram_counter[new_el]
                    else -1 if curr_counter[new_el] - 1 == anagram_counter[new_el] and curr_counter[new_el] - 1 != 0
                    else 0
                )
                curr_counter[old_el] -= 1
                perf += (
                    1 if curr_counter[old_el] == anagram_counter[old_el] and curr_counter[old_el] != 0
                    else -1 if curr_counter[old_el] + 1 == anagram_counter[old_el]
                    else 0
                )
            
            if perf == ac_len:
                indices.append(ptr)

        return indices
