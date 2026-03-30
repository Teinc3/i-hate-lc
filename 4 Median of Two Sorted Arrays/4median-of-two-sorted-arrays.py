class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # set m as longer and n as shorter
        if len(nums1) >= len(nums2):
            m = nums1
            n = nums2
        else:
            m = nums2
            n = nums1

        m_parts = len(m)
        n_parts = len(n)

        # We do binary search on n
        # Number of possible partitions: len(n) + 1 [-1:0 to len(n)-1:len(n)]
        # So let part be the partition on the LEFT side of the index
        n_part_lo = 0
        n_part_hi = len(n)

        while True:
            # Partition n to divide into two halves
            # If partition count is even - allow left side to have less elements
            n_part_mid = n_part_lo + (n_part_hi - n_part_lo) // 2

            # Calculate how many partitions in m we need to compensate for
            m_part_idx = (len(m) + len(n))//2 - n_part_mid

            # Look at the bounds of m and n at their partition indices
            # NOTE: IDX left is lower bound with part_idx-1
            m_left = m[m_part_idx-1] if m_part_idx >= 1 else -9999999
            m_right = m[m_part_idx] if m_part_idx < len(m) else 9999999
            n_left = n[n_part_mid-1] if n_part_mid >= 1 else -9999999
            n_right = n[n_part_mid] if n_part_mid < len(n) else 9999999

            # IF Upper bound of m < lower bound of n, n part need to move left
            # IF lower bound of m > upper bound of n, n part to be moved right
            # Otherwise the partitions are correct!

            if m_right < n_left:
                n_part_hi = n_part_mid - 1 # Check part to the left
            elif n_right < m_left:
                n_part_lo = n_part_mid + 1 # Check partition to the right
            else:
                # Correct partitions
                # Search for median
                # If m+n is even then the partition is exactly in the middle
                # So take max of lower and min of upper parts and average them
                # If m+n is odd then the partition is on the left of the midpt
                # So take the min value of the upper partition
                max_lower = max(m_left, n_left)
                min_upper = min(m_right, n_right)
                if (len(m) + len(n)) % 2 == 1:
                    return min_upper
                else:
                    return (max_lower + min_upper)/2
