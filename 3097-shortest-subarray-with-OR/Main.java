import java.util.Arrays;

/**
 * Main
 */

public class Main {

  public static void main(String[] args) {
    Main main = new Main();

    // Running test cases
    try {
      testMinimumSubarrayLength(main);
    } catch (Exception e) {
      System.out.println(e.getMessage());
    }
  }

  public int minimumSubarrayLength(int[] nums, int k) {
    System.out.println("=".repeat(20));
    int lo = 0, hi = 0;
    int win_or = 1;
    int minLen = Integer.MAX_VALUE;

    while (hi < nums.length) {
      int temp_or = (win_or | nums[hi]);
      System.out.printf("lo = %d hi = %d\n", lo, hi);
      if (temp_or >= k) {
        System.out.printf("Found temp_or %d\n", temp_or);
        // hit our base case
        // try to find a small window by moving start. everytime we move and it satifies
        while (Main.orAll(nums, lo, hi) >= k && lo <= hi) {
          lo++;
        }
        lo--;
        System.out.printf("updated lo %d\n", lo);

        minLen = Math.min(minLen, hi - lo + 1);
        if (minLen == 1) {
          return 1;
        }
        // update minLen
        hi++;
        lo++;
        win_or = Main.orAll(nums, lo, hi);
      } else {
        win_or = temp_or;
        hi++;
      }
    }

    return minLen != Integer.MAX_VALUE ? minLen : -1;
  }

  public static int orAll(int[] nums, int i, int j) {

    int res = 0;
    while (i <= j) {
      res |= nums[i];
      i++;
    }
    return res;

  }

  public static void testMinimumSubarrayLength(Main main) throws Exception {
    // Test case data (input arrays and k values)
    int[][] testCases = {
        { 1, 2, 3 }, // nums1
        { 2, 1, 8 },
        { 1, 2 },
        { 32, 1, 2, 81, 76, 58 },
    };

    // Corresponding k values for each test case
    int[] kValues = { 2, 10, 0, 125 };

    // Expected results for each test case
    int[] expectedResults = { 1, 3, 1, 2 };

    // Loop through test cases
    for (int i = 0; i < testCases.length; i++) {
      int[] nums = testCases[i];
      int k = kValues[i];
      int expected = expectedResults[i];

      // Calculate the result
      int result = main.minimumSubarrayLength(nums, k);

      // Check if the result matches the expected value
      if (result != expected) {
        throw new Exception("Test case " + (i + 1) + " failed: Expected " + expected + " but got " + result);
      }
    }

    // If all tests pass
    System.out.println("All test cases passed!");
  }
}
