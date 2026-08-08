class TrieNode:
    def __init__(self):
        self.chars = {}
        self.is_terminate = False


class Trie:
    def __init__(self):
        self.child = TrieNode() 

    def insert(self, word: str) -> None:
        curr_node = self.child
        for char in word:
            if char not in curr_node.chars:
                curr_node.chars[char] = TrieNode()
            curr_node = curr_node.chars[char]
        curr_node.is_terminate = True

    def search(self, word: str) -> bool:
        curr_node = self.child
        for char in word:
            if char not in curr_node.chars:
                return False
            curr_node = curr_node.chars[char]
        return curr_node.is_terminate

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.child
        for char in prefix:
            if char not in curr_node.chars:
                return False
            curr_node = curr_node.chars[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)