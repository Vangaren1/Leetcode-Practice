package Extra.reverse_bits_190;

class Solution {
    public int reverseBits(int n) {
        String binaryStr = Integer.toBinaryString(n);   
        String padded = String.format("%32s", binaryStr).replace(' ', '0');
        String reversed = new StringBuilder(padded).reverse().toString();
        long tmp = Long.parseLong(reversed,2);
        return (int) tmp;
    }
    public static void main(String[] args) {
        int nums = 41;

        Solution s = new Solution();
        System.out.println(s.reverseBits(nums));

        System.out.println("Running reverse_bits_190...");
    }
}
