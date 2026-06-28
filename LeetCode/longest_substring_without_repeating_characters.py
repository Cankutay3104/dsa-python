# LeetCode "3. Longest Substring Without Repeating Characters" Solution

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        chars = {}
        left = 0
        size = 0
        max_size = 0

        for i, ch in enumerate(s):
            chars[ch] = chars.get(ch, 0) + 1

            while chars[ch] > 1:
                chars[s[left]] -= 1
                if chars[s[left]] == 0:
                    del chars[s[left]]
                left += 1
            size = i - left + 1
            if size > max_size:
                max_size = size
        return max_size