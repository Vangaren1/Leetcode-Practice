package Extra.add_digits_258;

class Solution {
    public int addDigits(int num) {
        while ( num > 9){
            num = add_digits(num);
        }
        return num;
    }

    public int add_digits(int num){
        if ( num == 0) return 0;
        int tmp = num % 10;
        return tmp + add_digits(num / 10);
    }
    public static void main(String[] args) {
        System.out.println("Running add_digits_258...");
    }
}
