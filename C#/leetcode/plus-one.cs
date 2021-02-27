public class Solution {
    public int[] PlusOne(int[] digits) {
        // solution 1
        return (BigInteger.Parse(String.Join("", digits)) + 1)
            .ToString()
            .Select(d => int.Parse(d.ToString()))
            .ToArray();
        
        // solution 2?
    }
}