function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const lastSeen = {};

  for (let index = 0; index < nums.length; index++) {
    const i = index;
    const n = nums[i];
    if (lastSeen[n] !== undefined) {
      if (Math.abs(lastSeen[n] - i) <= k) {
        return true;
      }
    }
    lastSeen[n] = i;
  }

  return false;
};

let nums = [1, 2, 3, 1], k = 3;
console.log(containsNearbyDuplicate(nums, k));

nums = [1, 0, 1, 1];
k = 1;
console.log(containsNearbyDuplicate(nums, k));

nums = [1, 2, 3, 1, 2, 3];
k = 2;
console.log(containsNearbyDuplicate(nums, k));

