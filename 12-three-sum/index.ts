function threeSum(nums: number[]): number[][] {
  const triplets = [];
  const duplicateSet = new Set<number>();
  for (let i = 0; i < nums.length; i++) {
    const x = -nums[i]; // a + b + c = 0 or a + b = -c 

    const res = twoSum(nums.slice(i + 1), x, duplicateSet);
    for (const double of res) {
      const [y, z] = double;
      triplets.push([-x, y, z]);
    }

    duplicateSet.add(-x);
  }

  return triplets;
};

function twoSum(nums: number[], target: number, dupl: Set<number>): number[][] {
  const set = new Set();
  console.log(dupl);

  const multipleSoltuion = [];
  for (const num of nums) {
    const z = target - num;
    console.log(target, num, z);
    console.log(`z ${z} ${set}`);
    if (set.has(z) && !dupl.has(z)) {
      multipleSoltuion.push([num, target - num]);
    }
    set.add(num);
  }

  return multipleSoltuion;
}

console.log(threeSum([-1, 0, 1, 2, -1, -4]));

