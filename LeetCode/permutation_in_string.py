# LeetCode "567. Permutation in String" Solution

class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s2) < len(s1):
            return False

        window = {}
        s1_counts = {}

        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
            s1_counts[s1[i]] = s1_counts.get(s1[i], 0) + 1
        
        if window == s1_counts:
            return True

        k = len(s1)
        for i in range(len(s1), len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1
            window[s2[i-k]] -= 1
            if window[s2[i-k]] == 0:
                del window[s2[i-k]]
            
            if s1_counts == window:
                return True
        return False