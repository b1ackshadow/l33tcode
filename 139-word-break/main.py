from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in words_set and dp[j]:
                    dp[i] = True
                    break



        return dp[-1]

        

    # def build_dict(self, word):
    #     node = self.root
    #     for c in word:
    #         node[c] = node.get(c, {})
    #         node = node[c]
        # node['#'] = True



s = Solution()

# print(s.wordBreak("applepenapple", ["apple","pen"]))
print(s.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))


