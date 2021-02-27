public class Solution {
    public int MaxProfit(int[] prices) {
        bool hodl = false;
        int totalProfit = 0;
        int priceAtBought = 0;
        
        for (int i = 0; i < prices.Length - 1; i++) {
            int price = prices[i];
            int nextPrice = prices[i+1];
            
            if (hodl) {
                if (nextPrice < price) {
                    totalProfit += price - priceAtBought;
                    hodl = false;
                }
            } else {
                if (!hodl && nextPrice > price) {
                    priceAtBought = price;
                    hodl = true;
                }
            }
        }
        
        if (hodl) {
            totalProfit += prices[prices.Length - 1] - priceAtBought;
        }
        
        return totalProfit;
    }
}