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

    def insert(self, word: str) -> None:
        # Ex: cat 
        current = self.trie
        for c in word:
            if c not in current.children:
                current.children[c] = Node(c)
            current = current.children[c]

    def search(self, word: str) -> bool:
        current = self.trie
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return True

    def startsWith(self, prefix: str) -> bool:
        return self.search(prefix)

    def __str__(self):
        return str(self.trie)
        

trie = Trie()
trie.insert("cat")
trie.insert("bat")
trie.insert("cap")
trie.insert("capa")
print(trie)
# print(trie.search("x"))
# print(trie.search("c"))
# print(trie.search("cat"))
print(trie.startsWith("ca"))


exit(1)
test_cases = [
    (["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
     [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
     [None, None, True, False, True, None, True]),
    
    # Add additional test cases here
    # Example:
    # (["Trie", "insert", "insert", "search", "search", "startsWith"],
    #  [[], ["hello"], ["helium"], ["hello"], ["he"], ["hel"]],
    #  [None, None, None, True, False, True])
]


# Run test cases
for operations, arguments, expected in test_cases:
    results = []
    trie = Trie()
    
    for op, arg in zip(operations, arguments):
        if op == "Trie":
            results.append(None)
        elif op == "insert":
            results.append(trie.insert(arg[0]))
        elif op == "search":
            results.append(trie.search(arg[0]))
        elif op == "startsWith":
            results.append(trie.startsWith(arg[0]))
    
    assert results == expected, f"Failed for operations: {operations}, expected {expected} but got {results}"

print("All test cases passed.")

