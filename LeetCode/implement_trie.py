# LeetCode "208. Implement Trie (Prefix Tree)" Solution

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True
            
    def search(self, word):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.is_end

    def startsWith(self, prefix):
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True