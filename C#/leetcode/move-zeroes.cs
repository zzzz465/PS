public class Solution {
    public void MoveZeroes(int[] nums) {
        void swap(int index1, int index2) {
            var temp = nums[index1];
            nums[index1] = nums[index2];
            nums[index2] = temp;
        }
        
        // solution 1
        /*
        for (int i = 0; i < nums.Length; i++) {
            var num = nums[i];
            
            if (num == 0) {
                bool found = false;
                for (int j = i + 1; j < nums.Length; j++) {
                    if (nums[j] != 0) {
                        swap(i, j);
                        found = true;
                        break;
                    }
                }
                
                if (!found)
                    break;
            }
        }
        */

        // solution 2
        int lastNonZeroFoundAt = 0;
        for (int i = 0; i < nums.Length; i++) {
            var num = nums[i];
            
            if (num == 0) {
                bool found = false;
                for (int j = lastNonZeroFoundAt; j < nums.Length; j++) {
                    if (nums[j] != 0) {
                        swap(i, j);
                        found = true;
                        lastNonZeroFoundAt = j;
                        break;
                    }
                }
                
                if (!found)
                    break;
            }
        }
    }
}