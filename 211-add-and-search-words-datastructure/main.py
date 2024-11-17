class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()

    def __str__(self, level=0):
        # Visual representation with indentation for each level
        result = " " * (level * 2) + f"{self.val}\n"
        for child in self.children.values():
            result += child.__str__(level + 1)
        return result

class Trie:

    def __init__(self):
        self.trie = Node("")

    def addWord(self, word: str) -> None:
        # Ex: cat 
        current = self.trie
        for c in word:
            if c not in current.children:
                current.children[c] = Node(c)
            current = current.children[c]
        else:
            current.children['#'] = Node("#")

    def search(self, word: str) -> bool:
        return self.dfs(self.trie, word + '#', 0)

    def dfs(self, root, word, index):
        current = root
        print(f"Search for {word[index]}")
        if word[index] == "#" and '#' in root.children:
            return True


        if word[index] == ".":
            # we need to try for every child of current
            for child in current.children:
                print(f"child {current.children[child].val}")
                if self.dfs(current.children[child], word, index + 1):
                    return True
        if not (word[index] in current.children):
            print(f"{word[index]} not in tree")
            return False

        # print(f"consumed  {word[index]} == {current.children[word[index]].val} next -> i = {index + 1} {word[index + 1]}")
        return self.dfs(current.children[word[index]], word, index + 1)
    
    def __str__(self):
        return str(self.trie)
        

trie = Trie()
# trie.addWord("cat")
# trie.addWord("car")
# trie.addWord("bat")
# print(trie)
#
# print(trie.search("cat"))
# print(trie.search("car"))
# print(trie.search("x"))
# # print(trie.search("c"))
# print(trie.search(".at"))
# print(trie.search('.ar'))
# print(trie.search("cat"))
# print(trie.search(".at"))
# print(trie.search(".a."))
# print(trie.search("..x"))


