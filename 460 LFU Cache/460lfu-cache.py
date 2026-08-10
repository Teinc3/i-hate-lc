class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.left = self.right = None

class FreqNode:
    def __init__(self, freq):
        self.freq = freq
        self.head = self.tail = Node(-1, -1)
        self.head.right = self.tail.left = self.head
        self.left = self.right = None

class LFUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.head = self.tail = FreqNode(0)
        self.head.right = self.tail.left = self.head
        self.freqs = { 0: self.head }
        self.curr_cap = 0
        self.max_cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Obtain the frequency of this node
        # then move it over to the tail of the neighboring bucket.
        node = self.cache[key]
        node.freq += 1
        freq = node.freq

        # Disassociate this node from the Previous FreqNode DLL
        node.left.right, node.right.left = node.right, node.left

        # Add this to the next frequency bucket (create if not exists)
        old_freq = self.freqs[freq - 1]
        next_freq = old_freq.right
        if freq not in self.freqs:
            curr_freq = self.freqs[freq] = FreqNode(freq)
            old_freq.right = next_freq.left = curr_freq
            curr_freq.left = old_freq
            curr_freq.right = next_freq
        else:
            curr_freq = self.freqs[freq]
        
        # If old_freq's dll is now empty, remove it
        if old_freq.head.right is old_freq.tail:
            self.freqs.pop(freq - 1)
            old_freq.left.right, curr_freq.left = curr_freq, old_freq.left

        # Embed on the RIGHT (tail end) of the DLL within the Current FreqNode
        left_node = curr_freq.tail.left
        left_node.right, node.left = node, left_node
        node.right, curr_freq.tail.left = curr_freq.tail, node

        # All good now, return.
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.get(key) # Force the frequency update with identical logic
            return

        self.cache[key] = node = Node(key, value)
        self.curr_cap += 1
        if self.curr_cap > self.max_cap:
            self.curr_cap -= 1

            # Evict first
            nearest_freq = self.head.right
            evict = nearest_freq.head.right
            evict.left.right, evict.right.left = evict.right, evict.left
            self.cache.pop(evict.key)

            # Check if nearest_freq is now empty and clean it up
            if nearest_freq.head.right is nearest_freq.tail:
                self.freqs.pop(nearest_freq.freq)
                nearest_freq.left.right, nearest_freq.right.left = nearest_freq.right, nearest_freq.left

        # Here we are sure the new freq must be 1
        # Create one if there isn't any
        old_freq = self.head
        next_freq = self.head.right
        if 1 not in self.freqs:
            curr_freq = self.freqs[1] = FreqNode(1)
            old_freq.right = next_freq.left = curr_freq
            curr_freq.left = old_freq
            curr_freq.right = next_freq
        else:
            curr_freq = self.freqs[1]
        
        # And finally, add the node to the 1-freq (curr)'s tail
        left_node = curr_freq.tail.left
        left_node.right, node.left = node, left_node
        node.right, curr_freq.tail.left = curr_freq.tail, node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)