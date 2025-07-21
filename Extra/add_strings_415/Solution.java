package Extra.add_strings_415;

class Solution {
    public String addStrings(String num1, String num2) {
        String num1r = new StringBuilder(num1).reverse().toString();
        String num2r = new StringBuilder(num2).reverse().toString();

        char[] n1 = num1r.toCharArray();
        char[] n2 = num2r.toCharArray();

        int ptr1 = 0;
        int ptr2 = 0;
        int c1, c2;

        String tmp = "";
        Boolean carry = false;
        while (ptr1 < num1.length() && ptr2 < num2.length()) {
            c1 = num1r.charAt(ptr1) - '0';
            c2 = num2r.charAt(ptr2) - '0';

            int val = c1 + c2;
            if (carry)
                val++;

            carry = val > 9;

            tmp = tmp + Integer.toString(val % 10);
            ptr1++;
            ptr2++;
        }

        while (ptr1 < num1.length()) {
            c1 = num1r.charAt(ptr1) - '0';
            if (carry)
                c1++;
            carry = c1 > 9;
            tmp = tmp + Integer.toString(c1 % 10);
            ptr1++;
        }

        while (ptr2 < num2.length()) {
            c2 = num2r.charAt(ptr2) - '0';
            if (carry)
                c2++;
            carry = c2 > 9;
            tmp = tmp + Integer.toString(c2 % 10);
            ptr2++;
        }

        if (carry) {
            tmp = tmp + "1";
        }

        return new StringBuilder(tmp).reverse().toString();

    }

    public static void main(String[] args) {
        System.out.println("Running add_strings_415...");
    }
}
