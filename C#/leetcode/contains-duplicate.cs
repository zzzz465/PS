public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        var memo = new HashSet<int>();
        foreach(var num in nums) {
            if (memo.Contains(num)) {
                return true;
            } else {
                memo.Add(num);
            }
        }
        
        return false;
    }
}