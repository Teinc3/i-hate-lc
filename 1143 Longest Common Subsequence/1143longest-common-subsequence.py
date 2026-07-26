class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s_text, l_text = (text1, text2) if len(text1) <= len(text2) else (text2, text1)

        dp = [0] * (len(s_text) + 1)
        for l_char in l_text:
            last_val = 0
            for i in range(len(s_text)):
                s_char = s_text[i]
                if l_char == s_char:
                    curr_val = dp[i]
                    dp[i] = last_val + 1
                    last_val = curr_val
                else:
                    last_val = dp[i]
                    dp[i] = max(dp[i-1], dp[i])
        
        return dp[-2]