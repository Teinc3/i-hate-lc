class WordDictionary:

    def __init__(self):
        self.chars = {}
        self.can_terminate = False

    def addWord(self, word: str) -> None:
        first_char = word[0]
        if first_char not in self.chars:
            self.chars[first_char] = WordDictionary()
        
        if len(word) > 1:
            self.chars[first_char].addWord(word[1:])
        else:
            self.chars[first_char].can_terminate = True

    def search(self, word: str) -> bool:
        first_char = word[0]
        if first_char == ".":
            if len(word) == 1:
                return any(node.can_terminate for node in self.chars.values())
            else:
                return any(node.search(word[1:]) for node in self.chars.values())
        
        elif first_char not in self.chars:
            return False

        if len(word) > 1:
            return self.chars[first_char].search(word[1:])
        else:
            return self.chars[first_char].can_terminate


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)