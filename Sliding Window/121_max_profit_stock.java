class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;

        int n = prices.length;

        for(int i = 1; i < n; i++){
            if(prices[i] < minPrice){
                minPrice = prices[i];
                continue;
            }

            maxProfit = Math.max(maxProfit, prices[i] - minPrice);
        }

        return maxProfit;
    }
}