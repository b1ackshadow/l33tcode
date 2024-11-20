from typing import List


class Job:
    def __init__(self, name, schedule):
        self.name = name
        self.schedule = schedule

    def __lt__(self, other):
        return self.schedule < other.schedule

    def __str__(self) -> str:
        return f"Job {self.name} with {self.schedule}"

    def cycle(self):
        if self.schedule > 0:
            self.schedule -= 1

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        self.queue = []
        self.job_last_run = {}
        self.cpu_cycle = 0

    def queue_job(self, job: str):

        # we are trying to get the last time this job ran so that we wait 'n' cycles before 
        last_run_job = self.job_last_run.get(job, None)
        new_schedule = 0
        if last_run_job:
            new_schedule = last_run + 2





s= Solution()

print(s.leastInterval(["A","A","A","B","B","B"], 2))
        
