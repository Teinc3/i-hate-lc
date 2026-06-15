class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = set()

        def searchPossibilities(curr_word):
            for word in wordDict:
                new_word = curr_word + word
                if new_word in cache:
                    continue
                if len(new_word) > len(s):
                    continue
                if new_word == s:
                    return True
                if s[:len(new_word)] == curr_word + word:
                    res = searchPossibilities(new_word)
                    if res:
                        return True

            cache.add(curr_word)
            return False
        
        return searchPossibilities("")