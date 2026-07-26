class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s_word, l_word = (word1, word2) if len(word1) <= len(word2) else (word2, word1)
        dp = [x for x in range(1, len(s_word) + 1)]
        dp.append(0)

        for j, l_char in enumerate(l_word):
            dp[-1] = last_char = j
            for i, s_char in enumerate(s_word):
                if l_char == s_char:
                    # Take from TL
                    dp[i], last_char = last_char, dp[i]
                else:
                    # One plus either Top, TL, or Left
                    dp[i], last_char = 1 + min(dp[i], dp[i-1], last_char), dp[i]
        
        return dp[-2] if len(dp) >= 2 else len(l_word)