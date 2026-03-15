class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slen = len(s)

        if (slen <= 1):
            return slen
        
        i, j = 0, 1
        a = s[0]
        max_len = 0

        dictmap: list[str, int] = { a: 0 }

        while j < slen:
            # Check if char already exists in map
            curr_char = s[j]
            last_idx = dictmap.get(curr_char, None)
            if last_idx != None and last_idx >= i: # Exists
                # Save streak
                max_len = max(max_len, j - i)
                # Move pointer 1 to last occurence + 1
                i = last_idx + 1
                
                # Wipe all keys with values < 0
                dictmap.pop(curr_char)

            # Save the current character as well as our current position
            dictmap[curr_char] = j
            j += 1

        return max(max_len, j - i)