# LeetCode "1876. Substrings of Size Three with Distinct Characters" Solution

class Solution(object):
    def countGoodSubstrings(self, s):
        if len(s) < 3:
            return 0
        
        window_counts = {}
        good_substrings = 0

        for i in range(3):
            window_counts[s[i]] = window_counts.get(s[i], 0) + 1

        if len(window_counts) == 3:
            good_substrings += 1
        
        for i in range(3, len(s)):
            window_counts[s[i]] = window_counts.get(s[i], 0) + 1
            
            ch = s[i-3]
            window_counts[ch] -= 1
            if window_counts[ch] == 0:
                del window_counts[ch]

            if len(window_counts) == 3:
                good_substrings += 1

        return good_substrings