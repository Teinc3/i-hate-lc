class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Reverse generate the entries after computation reached shared state
        # Never do fast return when we hit the end. We still need to try all
        # possibilities that have not been tried before.

        # cache: index -> list of possible strings
        # Use length of the other possible strings to chain

        cache = {}

        wd2 = [x for x in wordDict if x in s]

        def explore(prev_word):
            if prev_word in cache:
                return cache[prev_word]

            combins = []

            for word in wd2:
                current_word = prev_word + word
                if len(current_word) > len(s):
                    continue
                elif len(current_word) == len(s) and current_word == s:
                    combins.append(word)
                elif s.startswith(current_word):
                    for possible_combin in explore(current_word):
                        combins.append(word + " " + possible_combin)

            cache[prev_word] = combins

            # Returns a list of combinations that can reach the end
            return combins

        return explore("")