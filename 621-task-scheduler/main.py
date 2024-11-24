from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0

        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1
        task_heap = []
        for freq in task_freq.values():
            heapq.heappush(task_heap, -freq) # max heap

        queue = []
        while task_heap or queue:
        # get the most freq task so we that can minimize the idle time

            # one unit of cycle is done whether a task is processed or not (basically idle time)
            time += 1

            if task_heap:
                task = heapq.heappop(task_heap)
                task += 1  # we need to reduce the unit but its -(task) so just add to decrement

                # schedule current task if needed 
                if task != 0:
                    queue.append((task, time + n)) # remaining units of work, current_time + gap

            # check if any task is ready to be on heap at this time 
            while queue and queue[0][1] == time:
                schedule_task = queue.pop(0)
                heapq.heappush(task_heap, schedule_task[0])

        return time

#    ____                   _                 _                   _
#  / ___|_ __ ___  ___  __| |_   _          | |__   __ _ _ __ __| |
# | |  _| '__/ _ \/ _ \/ _` | | | |  _____  | '_ \ / _` | '__/ _` |
# | |_| | | |  __/  __/ (_| | |_| | |_____| | | | | (_| | | | (_| |
#  \____|_|  \___|\___|\__,_|\__, |         |_| |_|\__,_|_|  \__,_|

class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        most_freq = 0
        for task in tasks:

            new_count = counter.get(task, 0) + 1
            counter[task] = new_count

            most_freq = max(most_freq, new_count)

        most_freq_count = 0 # how many tasks have the same most_freq
        for key in counter:
            if counter[key] == most_freq:
                most_freq_count += 1

        
        # total slots caluclation
        # 1. we need the most frequence elements sepearted by n gasp
        # (most_freq - 1) * (n + 1) 
        # Ex - 3A, n = 1 which means we need (3 - 1) * (1 + 1) = 4 total slots
        # we obviously need (freq-1) gaps between each element and its size is 'n'
        # to calcuale the total tasks we also need to include task itself. each group will have gap + letter


        # we also need to add the most freq later at the end since it is not present in the group
        # multiple tasks with same most frequene could be present so track and add it


        total_slots = (most_freq - 1) * (n + 1) + most_freq_count

        # edge case if n < unique tasks in the queue this means that other tasks can easily fill the gap and no need to accomodate idle time which was done previously by assuming most freq needed the gaps 

        return max(total_slots, len(tasks))



s= Solution()

print(s.leastInterval(["A","A","A","B","B","B"], 2))
# print(s.leastInterval(["A","A","A","B","B","B", "C", "D", "E"], 2))
        

#
# When n is smaller than the number of unique tasks, the reason the total number of tasks becomes the minimum required intervals lies in how the gaps are distributed:
#
# Key Points:
# When n < tasks:
#
# The n interval constraint between identical tasks becomes less restrictive because there are enough other tasks to "fill the gaps" naturally.
# The scheduler doesn't need to leave idle slots since tasks can occupy all intervals.
# Why This Works:
#
# The core formula (f_max - 1) * (n + 1) assumes that there aren’t enough tasks to fill gaps created by the most frequent task.
# However, when the number of unique tasks is large enough, the gaps are filled by other tasks, making idle slots unnecessary.
# Example to Explain:
# Input:
# plaintext
# Copy code
# tasks = ["A", "A", "A", "B", "C", "D", "E", "F", "G"], n = 1
# Step 1: Analyze Frequencies:
# A: 3, B: 1, C: 1, D: 1, E: 1, F: 1, G: 1.
# Step 2: Calculate Using (f_max - 1) * (n + 1):
# f_max = 3 for A.
# Total slots = (f_max - 1) * (n + 1) + count_max = (3 - 1) * (1 + 1) + 1 = 5.
# Step 3: Compare Slots and Tasks:
# Total tasks = 9. Calculated slots = 5.
# Since n is small and there are many tasks, the gaps from A can easily be filled by other tasks (B, C, D, E, F, G).
