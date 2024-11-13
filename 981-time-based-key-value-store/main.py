class TimeMap:

    def __init__(self):
        self.cache = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_value = [timestamp, value]
        current_arr = self.cache.get(key,[])
        current_arr.append(new_value)
        self.cache[key] = current_arr

    def get(self, key: str, timestamp: int) -> str:
        if key in self.cache:
            return self.bin_search(key, timestamp)
        return ""

    def bin_search(self, key, target) -> str:
        nums = self.cache[key]
        lo = 0; hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            mid_time = nums[mid][0]
            if mid_time <= target and ((mid == len(nums)-1) or (nums[mid + 1][0] > target)):
                return nums[mid][1] # value
            elif mid_time > target:
                hi = mid  - 1
            else:
                lo = mid + 1
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

 # Initialize the TimeMap object
timeMap = TimeMap()

# Test case input and expected output
inputs = [
    ("set", "foo", "bar", 1),
    ("get", "foo", 1),
    ("get", "foo", 3),
    ("set", "foo", "bar2", 4),
    ("get", "foo", 4),
    ("get", "foo", 5)
]
expected_outputs = [None, "bar", "bar", None, "bar2", "bar2"]

# Running the test
outputs = []
for command, *args in inputs:
    if command == "set":
        outputs.append(timeMap.set(*args))
    elif command == "get":
        outputs.append(timeMap.get(*args))

# Compare expected outputs with actual outputs
assert outputs == expected_outputs, f"Expected {expected_outputs} but got {outputs}"
print("All test cases passed!")
