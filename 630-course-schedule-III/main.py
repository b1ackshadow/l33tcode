from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        n = len(courses)
        completed = 0
        total_duration = 0

        queue = []

        # first we need to process the courses in ascending order of deadline with this we can 
        # ensure courses that have lower deadlines are processed first 

        # if we find a course that will go past deadline we can remove the longest duration from 
        # heap and swap this 
        courses.sort(key = lambda each: each[1])
        # print(courses)
        for c in courses:
            # print(f"processing course {c}")
            heapq.heappush(queue, -c[0])
            total_duration += c[0]
            # print(f"total_duration {total_duration}")
            if total_duration > c[1]:
                # if it exceeds the deadline remove the course with the longest duration
                removed_duration = -heapq.heappop(queue)
                total_duration -= removed_duration
                # print(f"reducing duration {removed_duration}")



        return len(queue)


s = Solution()

tests = [
    ([[100,200],[200,1300],[1000,1250],[2000,3200]], 3),
    ([[1,2]], 1),
    ([[3,2],[4,3]], 0),
    ([[5,15],[3,19],[6,7],[2,10],[5,16],[8,14],[10,11],[2,19]], 5)
]

for i, test in enumerate(tests):
    courses, want = test

    got = s.scheduleCourse(courses)
    assert got == want, f"{i}: want {want} != {got} got"
