public class Solution {
    public int RemoveDuplicates(int[] nums) {
        void swap(int index1, int index2) {
            int temp = nums[index1];
            nums[index1] = nums[index2];
            nums[index2] = temp;
        }
        
        if (nums.Length == 0)
            return 0;
        
        int i = 0;
        
        for (i = 1; i < nums.Length; i++) {
            if (nums[i] <= nums[i-1]) {
                bool found = false;
                for (int j = i+1; j < nums.Length; j++) {
                    if (nums[j] > nums[i-1]) {
                        swap(i, j);
                        found = true;
                        break;
                    }
                }
                
                if (!found) // 더 큰 숫자가 없음 -> minimum만 가지고 배열 완성함
                    break;
            }
        }
        
        return i;
    }
}