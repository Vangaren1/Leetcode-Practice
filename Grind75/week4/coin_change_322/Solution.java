package Grind75.week4.coin_change_322;

class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] coinmap = new int[amount + 2];
        coinmap[0] = 0;

        for ( int j = 1; j < coinmap.length; j++){
            coinmap[j] = amount + 1;
        }

        for (int i = 0; i < amount + 1; i++){
            for (int c: coins){
                if (i - c >= 0){
                    coinmap[i] = Math.min(coinmap[i], coinmap[i-c] + 1);
                }
            } 
        }
        if( coinmap[amount] != coinmap[amount + 1]){
            return coinmap[amount];
        }else{
            return -1;
        }  
    }

    public static void main(String[] args) {
        int[] coins = {1,2,5};
        int amount = 11;

        Solution s= new Solution();

        System.out.println(s.coinChange(coins, amount));

        System.out.println("Running coin_change_322...");
    }
}
