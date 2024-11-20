import java.util.Collections;
import java.util.PriorityQueue;

class Main {
    public static void main(String[] args) {
        int[] nums = { 4, 5, 8, 2 };
        KthLargest kthLargest = new KthLargest(3, nums);
    }
}

class KthLargest {

    private final PriorityQueue<Integer> minHeap;
    private final int k;
    private int heapSize;

    public KthLargest(int k, int[] nums) {
        this.minHeap = new PriorityQueue<Integer>(k); //
        this.k = k;
        this.heapSize = 0;

        for (int n : nums) {
            this.add(n);
        }

    }

    public int add(int val) {
        this.minHeap.offer(val);
        if (this.minHeap.size() > this.k) {
            this.minHeap.poll();
        }
        return this.minHeap.peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
