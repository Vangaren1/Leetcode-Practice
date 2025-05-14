package Grind75.week4.min_stack_155;

import java.util.Stack;

class Solution {
    class MinStack {

        Stack<int[]> numStack;
        public MinStack() {
            numStack = new Stack<>();
        }
        
        public void push(int val) {
            if ( numStack.size() == 0){
                numStack.add( new int[] { val, val });
            }else{
                int currMin = getMin();
                if(val < currMin){
                    currMin = val;
                }
                numStack.add( new int[] {val, currMin});
            }
        }
        
        public void pop() {
            numStack.pop();
        }
        
        public int top() {
            return numStack.peek()[0];
        }
        
        public int getMin() {
            return numStack.peek()[1];
        }
    }
    public static void main(String[] args) {
        System.out.println("Running min_stack_155...");
    }
}
