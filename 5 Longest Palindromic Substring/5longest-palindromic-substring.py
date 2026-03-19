class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)

        max_pal_len = 0
        max_pal_idx = 0
        max_pal_mode = -1
        max_pal_offset = 0

        for mode in range(2): # Odd (0), Even (1) Mode
            for i in range(len_s):
                offset = 0
                while True:
                    l_idx = i - offset
                    r_idx = i + mode + offset
                    
                    if l_idx < 0 or r_idx >= len_s or s[l_idx] != s[r_idx]:
                        break
                    offset += 1

                offset -= 1
                pal_len = 2 * offset + mode + 1
                if pal_len > max_pal_len:
                    max_pal_len = pal_len
                    max_pal_idx = i
                    max_pal_mode = mode
                    max_pal_offset = offset
        
        start_idx = max_pal_idx - max_pal_offset
        end_idx = max_pal_idx + max_pal_offset + max_pal_mode
        return s[start_idx:end_idx+1]