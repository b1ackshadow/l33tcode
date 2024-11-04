from types import SimpleNamespace


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        i = 0 
        current = ""
        prev = None
        while i < len(path):
            if path[i] == "/":
                if prev == "/":
                    continue
                prev = "/"
                if current == "..":
                    stack.pop()
                    stack.pop()
                    stack.append("/")
                elif current == ".":
                    i += 1

            else:
                current += path[i]
            i += 1


        return "".join(stack)

# sol = Solution()
# print(sol.simplifyPath("/home/"))

#             /home/

def simplifyPath(path: str) -> str:
    stack = []

    p = path.split("/")

    for token in p:
        if token == ".." and len(stack) > 0:
            stack.pop()
        elif token not in [".", "..", ""]:
            stack.append(token)

    return "/" + "/".join(stack)



print(simplifyPath("/home//foo/"))
print(simplifyPath(r"/home/"))
print(simplifyPath("/home/user/Documents/../Pictures"))
print(simplifyPath( "/../"))
print(simplifyPath("/.../a/../b/c/../d/./"))
