package Grind75.week7.contains_most_water_11;

class Solution {
    public int maxArea(int[] height) {
        int currVol = 0;

        int ptr1 = 0;
        int ptr2 = height.length -1;

        while( ptr1 < ptr2){
            int left = height[ptr1];
            int right = height[ptr2];

            int volume = Integer.min(left, right) * (ptr2 - ptr1);

            currVol = Integer.max(currVol, volume);
            
            if ( right < left) {
                ptr2--;
            }else{
                ptr1++;
            }
        
        }

        
        return currVol;
    }

    public static void main(String[] args) {
        System.out.println("Running contains_most_water_11...");
    }
}
