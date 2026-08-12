# LeetCode "211. Design Add and Search Words Data Structure" Solution

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

    def search(self, word):
        def dfs(index, node):
            curr = node

            for i in range(index, len(word)):
                char = word[i]

                if char == '.':
                    for value in curr.children.values():
                        if dfs(i + 1, value):
                            return True
                    return False

                if char not in curr.children:
                    return False
                curr = curr.children[char]

            return curr.is_end

        return dfs(0, self.root)