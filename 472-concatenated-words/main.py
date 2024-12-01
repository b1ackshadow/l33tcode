from typing import Dict, List

#
# class Node:
#     def __init__(self, ch):
#         self.val = ch
#         self.children = {}

class Solution:
    
    def __init__(self):
        self.root  = {}


    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []

        for word in words:
            self.build_dict(word)

        print(self.root)
        for word in words:
            self.dfs(self.root, word, 0)
        return res

    def dfs(self, node, word, count):

        if len(word) == 0:
            return count

        if "#" in node
    #

    def build_dict(self, word):
        root = self.root
        i = 0
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
            if i == len(word) - 1:
                root['#'] = True

            i += 1





s = Solution()

print(s.findAllConcatenatedWordsInADict(["a","b","ab","abc"]))
