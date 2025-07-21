package Extra.fizz_buzz_412;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> array = new ArrayList<>();

        for (int index = 1; index < n + 1; index++) {
            String tmp = "";
            if (index % 3 == 0) {
                tmp = "Fizz";
            }
            if (index % 5 == 0) {
                tmp = tmp + "Buzz";
            }
            if (tmp.length() != 0) {
                array.add(tmp);
            } else {
                array.add(Integer.toString(index));
            }
        }
        return array;
    }

    public static void main(String[] args) {
        System.out.println("Running fizz_buzz_412...");
    }
}
