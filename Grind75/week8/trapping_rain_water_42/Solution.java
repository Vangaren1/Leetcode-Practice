package Grind75.week8.trapping_rain_water_42;

class Solution {
    public int trap(int[] height) {

        int total = 0;
        int leftPtr = 0;
        int rightPtr = height.length - 1;
        int maxLeft = height[0];
        int maxRight = height[rightPtr];
        int tmp = 0;
        while (leftPtr < rightPtr) {

            if (maxLeft <= maxRight) {
                leftPtr++;
                tmp = maxLeft - height[leftPtr];
                maxLeft = Math.max(maxLeft, height[leftPtr]);
            } else {
                rightPtr--;
                tmp = maxRight - height[rightPtr];
                maxRight = Math.max(maxRight, height[rightPtr]);
            }
            if (tmp > 0)
                total = total + tmp;
        }

        return total;

    }

    public static void main(String[] args) {
        System.out.println("Running trapping_rain_water_42...");
    }
}
