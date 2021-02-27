public class Solution {
    public void Rotate(int[] nums, int k) {
        // solve 1
        /*
        int[] newArray = new int[nums.Length];
        for (int i = 0; i < nums.Length; i++) {
            newArray[(i + k) % nums.Length] = nums[i];
        }
        
        for (int i = 0; i < nums.Length; i++)
            nums[i] = newArray[i];
        */
        
        // solve 2
        /*
        int length = nums.Length;
        if (length > 1) {
            for (int c = 0; c < k; c++) {
                int last = nums[length-1];
                for (int i = length - 2; i >= 0; i--)
                    nums[i+1] = nums[i];
                
                nums[0] = last;
            }
        }
        */
        
        // solve 3???
    }
}