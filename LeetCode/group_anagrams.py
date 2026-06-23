# LeetCode "49. Group Anagrams" Solution
class Solution(object):
    def groupAnagrams(self, strs):
        masterHashmap = {}
        for word in strs:
            sortedStr = "".join(sorted(word))
            
            if sortedStr not in masterHashmap:
                masterHashmap[sortedStr] = []
            masterHashmap[sortedStr].append(word)
    
        return list(masterHashmap.values())