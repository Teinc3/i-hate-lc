class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = self.tail = None
        self.current = 0
        self.max_cap = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        # Obtain the node otherwise return -1
        # Rewire the linked list and move the node to the tail
        if key not in self.cache:
            return -1
        node = self.cache[key]

        # If node is tail, all good, no need to bubble anything up.
        if node is self.tail:
            return node.val
        # If node is head, move its neighbor right over as head
        elif node is self.head:
            self.head = node.right
            self.head.left = None # new head
        # Otherwise cross left and right pointers
        else:
            left, right = node.left, node.right
            left.right = right
            right.left = left
        
        # And set node as tail
        if self.tail:
            self.tail.right = node
        node.left = self.tail
        self.tail = node
        
        return node.val

    def put(self, key: int, value: int) -> None:
        update = False
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            update = True
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.current += 1
            if self.current == 1:
                self.head = self.tail = node

        # If node is tail, no need to do anything.
        if node is self.tail:
            return node.val
        # If head, move right over as head
        elif node is self.head:
            self.head = node.right
            self.head.left = None # new head
        # Otherwise cross left and right pointers
        else:
            left, right = node.left, node.right
            if left:
                left.right = right
            if right:
                right.left = left

        # And set node as tail
        if self.tail:
            self.tail.right = node
        node.left = self.tail
        self.tail = node

        if self.current > self.max_cap and not update:
            popped_node = self.head
            self.head = popped_node.right
            self.head.left = None
            self.cache.pop(popped_node.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)