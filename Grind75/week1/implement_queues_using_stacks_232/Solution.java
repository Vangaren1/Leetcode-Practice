package Grind75.week1.implement_queues_using_stacks_232;

import java.util.Stack;

class Solution {
    class MyQueue {

        private Stack<Integer> queueStack;
        private Stack<Integer> tempStack;

        public MyQueue() {
            this.queueStack = new Stack<>();
        }
        
        public void push(int x) {
            int tmp;
            while(!this.queueStack.isEmpty()){
                tmp = queueStack.pop();
                tempStack.push(tmp);
            }
            this.queueStack.push(x);
            while(!this.tempStack.isEmpty()){
                tmp = tempStack.pop();
                this.queueStack.push(tmp);
            }
        }
        
        public int pop() {
            return this.queueStack.pop();
        }
        
        public int peek() {
            return this.queueStack.peek();
        }
        
        public boolean empty() {
            return this.queueStack.isEmpty();
        }
    }


    public static void main(String[] args) {
        System.out.println("Running implement_queues_using_stacks_232...");
    }
}
