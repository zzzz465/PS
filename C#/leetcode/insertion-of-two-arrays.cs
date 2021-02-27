public class Solution {
    public int[] Intersect(int[] nums1, int[] nums2) {
        if (nums1.Length < nums2.Length)
            return Intersect(nums2, nums1);
        
        // nums1 length > nums2 length
        // solve 1
        /*
        var num1Dict = new Dictionary<int,int>();
        
        foreach(var num in nums1) {
            if (!num1Dict.ContainsKey(num))
                num1Dict.Add(num, 0);
            
            num1Dict[num] += 1;
        }
        
        var result = new List<int>();
        
        foreach(var num in nums2) {
            if (num1Dict.TryGetValue(num, out var value)) {
                if (value > 0) {
                    result.Add(num);
                    num1Dict[num] -= 1;
                }
            }
        }
        
        return result.ToArray();
        */
        
        
    }
}