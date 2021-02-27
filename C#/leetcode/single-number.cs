public class Solution {
    public int SingleNumber(int[] nums) {
        // solve 1
        /*
        var record = new Dictionary<int, int>();
        foreach(var num in nums) {
            if (!record.ContainsKey(num)) {
                record.Add(num, 0);
            }
            
            record[num] += 1;
        }
        
        foreach(var num in nums) {
            if (record[num] == 1)
                return num;
        }
        
        return -1;
        */
        
        // solve 2 with O(N) time, O(1) space complexity
        int unique = 0;
        foreach(var num in nums)
            unique ^= num;
        
        return unique;
        
    }
}