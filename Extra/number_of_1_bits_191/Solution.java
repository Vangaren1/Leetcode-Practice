package Extra.number_of_1_bits_191;

class Solution {
    public int hammingWeight(int n) {
        int total = 0;
        String s = Integer.toBinaryString(n);
        for (char c : s.toCharArray()){
            if (c == '1') total++;
        }    
        return total;
    }
    public static void main(String[] args) {
        System.out.println("Running number_of_1_bits_191...");
    }
}
