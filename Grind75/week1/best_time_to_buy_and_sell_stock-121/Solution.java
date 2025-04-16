package Grind75.week1.best_time_to_buy_and_sell_stock;

class Solution {
    public int maxProfit(int[] prices) {

        int curr = 0;
        int lowest = prices[0];

        for(int p : prices){
            if(p < lowest){
                lowest = p;
            }
            int tmp = p - lowest;
            if(tmp > curr){
                curr = tmp;
            }
        }

        return curr;
    }
}