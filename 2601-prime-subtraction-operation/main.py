from typing import List
import math
class Solution:
    def __init__(self):
        n = 1000
        self.primes = { k: True for k in range(2, n + 1)}

        p = 2
        end = math.sqrt(n)
        while p <= end:
            if self.primes[p]:
                # mark mulitples as not prime - False
                i = 2
                while (multiple := p * i ) <= n:
                    self.primes[multiple] = False
                    i += 1
            p += 1
            while not self.primes[p]:
                p += 1

    def primeSubOperation(self, nums: List[int]) -> bool:
        for i, e in enumerate(nums):
        # for each number we need to make sure use the larget prime < e such that res > prev
            prime = e - 1





tests = [
    ([4,9,6,10], True),
    ([6,8,11,12], True),
    ([5,8,3], False)
]

sol = Solution()

for i, (nums, wanted) in enumerate(tests):
    try:
        got = sol.primeSubOperation(nums)
        assert wanted == got, f"{nums} :  Wanted {wanted} but got {got}"
        print(f"Test case {i + 1} passed")
    except Exception as e:
        print(str(e))
        break
