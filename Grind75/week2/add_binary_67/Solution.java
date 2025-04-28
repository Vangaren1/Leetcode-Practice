package Grind75.week2.add_binary_67;

class Solution {
    public String addBinary(String a, String b) {
        String result = "";
        int carry = 0;
        char[] aArray = a.toCharArray();
        char[] bArray = b.toCharArray();
        int aptr = a.length() - 1;
        int bptr = b.length() - 1;
        int[] sumResults;
        char aBit = '0'; 
        char bBit = '0';
        while( aptr >= 0 && bptr >= 0){
            aBit = aArray[aptr];
            bBit = bArray[bptr];
            sumResults = fullAdder((int)(aBit - '0'), (int)(bBit-'0'), carry);
            carry = sumResults[1];
            result = (char)( sumResults[0] + '0') + result;
            aptr --;
            bptr --;
        }  
        while(aptr >= 0){
            aBit = aArray[aptr];
            sumResults = fullAdder((int)(aBit - '0'), 0, carry);
            carry = sumResults[1];
            result = (char)( sumResults[0] + '0') + result;
            aptr --;
        }
        while(bptr >= 0){
            bBit = bArray[bptr];
            sumResults = fullAdder(0, (int)(bBit-'0'), carry);
            carry = sumResults[1];
            result = (char)( sumResults[0] + '0') + result;
            bptr --;
        }
        if( carry == 1){
            result = '1' + result;
        }

        return result;   
    }

    public int[] fullAdder(int a, int b, int carry){
        int sum = a ^ b ^ carry;
        int cout = (a & b) | (carry & (a ^ b) );
        return new int[] {sum,cout};
    }

    public static void main(String[] args) {
        String a = "1010";
        String b = "1011";
        Solution s = new Solution();
        System.out.println(s.addBinary(a, b));
        System.out.println("Running add_binary_67...");
    }
}
