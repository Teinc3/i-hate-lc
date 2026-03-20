class Solution:
    def jump(self, nums: List[int]) -> int:
        jmps = 0
        curr_pos = 0
        last_pos = 0 # Optimisation
        fin_pos = len(nums)-1
        while curr_pos < fin_pos:
            r_ptr = curr_pos + nums[curr_pos]
            if r_ptr >= fin_pos:
                return jmps + 1

            max_ptr = r_ptr
            max_val = nums[r_ptr]
            # We only search until we reach last_pos
            # Which is the maximum of all searches we had
            # continuing will just yield lower jmp values
            while r_ptr > last_pos: 
                if nums[r_ptr] > max_val + (max_ptr - r_ptr):
                    max_ptr = r_ptr
                    max_val = nums[r_ptr]
                r_ptr -= 1

            # Update lastpos to shortcut
            last_pos = curr_pos + nums[curr_pos]
            
            # Jump to max_ptr (This allows the maximum reach)
            curr_pos = max_ptr
            jmps += 1

        return jmps 
