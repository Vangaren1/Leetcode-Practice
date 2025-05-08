package Grind75.week3.evaluate_reverse_polish_notation_150;

import java.util.Arrays;
import java.util.List;
import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        
        Stack<String> numStack = new Stack<>();

        List<String> operators = Arrays.asList("+", "-", "*", "/");

        String first, second;
        int tmp=0;
        for(String tok: tokens){
            if( operators.contains(tok)){
                first = numStack.pop();
                second = numStack.pop();
                switch(tok){
                    case "+":
                        tmp = Integer.parseInt(second) + Integer.parseInt(first);
                        break;
                    case "-":
                        tmp = Integer.parseInt(second) - Integer.parseInt(first);
                        break;
                    case "*":
                        tmp = Integer.parseInt(second) * Integer.parseInt(first);
                        break;
                    case "/":
                        tmp = Integer.parseInt(second) / Integer.parseInt(first);
                        break;
                }
                numStack.push( Integer.toString(tmp));
            }else{
                numStack.push(tok);
            }

        }

        return Integer.parseInt(numStack.pop());
    }
    
    public static void main(String[] args) {
        System.out.println("Running evaluate_reverse_polish_notation_150...");
    }
}
