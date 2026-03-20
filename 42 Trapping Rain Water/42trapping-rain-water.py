class Solution:
    """
    Go from Left to Right
    Add all water values in between if equal or higher and save pointer
    If reached right extreme, go back from right to saved pointer
    """
    def trap(self, height: List[int]) -> int:
        len_h = len(height)
        l_ptr = 0
        total = 0
        r_ptr = 0
        while r_ptr < len_h:
            w_lvl = height[l_ptr]
            if height[r_ptr] >= w_lvl:
                for idx in range(l_ptr, r_ptr + 1):
                    total += max(0, w_lvl - height[idx])
                l_ptr = r_ptr
            r_ptr += 1
        
        # Scan back from the other end
        rr_ptr = r_ptr = r_ptr - 1
        while r_ptr >= l_ptr:
            w_lvl = height[rr_ptr]
            if height[r_ptr] >= w_lvl:
                for idx in range(r_ptr, rr_ptr + 1):
                    total += max(0, w_lvl - height[idx])
                rr_ptr = r_ptr
            r_ptr -= 1

        return total
        
            
        