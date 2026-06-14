import heapq
from collections import Counter

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # l_heap uses maxheap
        # r_heap uses minheap
        # median = r_heap root for odd k, otherwise average of roots of l and r_heap

        # 0. fuck k = 1
        if k == 1:
            return nums

        # 1. Sort the initial window and populate heaps
        i_window = sorted(nums[:k])
        div = k//2
        l_heap, r_heap = i_window[:div], i_window[div:]
        medians = []

        heapq.heapify_max(l_heap)
        heapq.heapify(r_heap)

        l_lazy, r_lazy = Counter(), Counter()

        # 2. Iterate through 
        for i in range(len(nums) - k + 1):
            if i != 0:
                # Because this only runs during 2nd cycle (i = 1)
                # any lazily deleted elements should not appear on heap root
                e_rm = nums[i - 1] # Element to remove:
                e_add = nums[i + k - 1] # El to add
                left_rm = False

                # Check current median to determine where to delete from
                if e_rm <= l_heap[0]: # If it's on the left heap
                    # Mark the existing element as lazy
                    l_lazy[e_rm] += 1
                    left_rm = True
                else: # We know it must be on the right heap
                    r_lazy[e_rm] += 1

                # Identify where the new element should be added to.
                # if left removed and e_add <= r_heap[0] then add to left
                # if left removed and e_add > r_heap[0] then add to right, pop r_heap[0] to left
                # Similarly if not left removed and e_add >= l_heap[0] add right
                # And if not left removed and e_add < l_heap[0] then add to left and pop l_heap[0] and move it to the right
                # This is run only after the lazy deletion logic below makes all heap roots safe for deletion
                if left_rm:
                    if e_add <= r_heap[0]:
                        heapq.heappush_max(l_heap, e_add)
                    else:
                        old = heapq.heappop(r_heap)
                        heapq.heappush(r_heap, e_add)
                        heapq.heappush_max(l_heap, old)
                else:
                    if e_add >= l_heap[0]:
                        heapq.heappush(r_heap, e_add)
                    else:
                        old = heapq.heappop_max(l_heap)
                        heapq.heappush_max(l_heap, e_add)
                        heapq.heappush(r_heap, old)

            # If we find a lazy deleted item we pop heap and decrement counter
            while True:
                if l_lazy[l_heap[0]] >= 1:
                    val = heapq.heappop_max(l_heap)
                    l_lazy[val] -= 1
                elif r_lazy[r_heap[0]] >= 1:
                    val = heapq.heappop(r_heap)
                    r_lazy[val] -= 1
                else:
                    break

            # Do the median calculations
            medians.append(
                r_heap[0] if k % 2 == 1 else (l_heap[0] + r_heap[0])/2
            )
            
        return medians