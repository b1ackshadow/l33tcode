from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1); n = len(nums2)
        total = m + n

        lo = 0; hi = m - 1
        while lo <= hi:
            partition_x = (lo + hi) // 2
            partition_y = ((m + n + 1) // 2) - partition_x

            if (partition_x == 0 or (nums1[partition_x] < nums2[partition_y + 1])) and (partition_x == m or (nums2[partition_y]) < nums1[partition_x + 1]):
                if total % 2 == 0:
                    return (max(nums1[partition_x], nums1[partition_y]) + min(nums1[partition_x + 1], nums2[partition_y + 1])) // 2
                else:
                    return min(nums1[partition_x], nums2[partition_y])
            elif 
       


        


sol = Solution()

tests = [
    ([1,3], [2], 2),
    ([1,2],[3,4], 2.5)
]

for i, (a, b, wanted) in enumerate(tests):
    try:
        got = sol.findMedianSortedArrays(a, b)
        assert got == wanted, f"Case {a}, {b}: wanted {wanted} != got {got}"
        print(f"Test case {i} passed")
    except Exception as e:
        print(str(e))
        break
