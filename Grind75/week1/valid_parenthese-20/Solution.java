import java.util.HashMap;
import java.util.Map;
import java.util.Stack;


class Solution {
    public boolean isValid(String s) {
        Stack<Character> parans = new Stack<>();
        char top = '_';
        for(char c : s.toCharArray()){
            if(pairs.containsKey(c)){
                parans.push(c);
            }else{
                if(parans.isEmpty()){
                    return false;
                }
                top = parans.pop();
                if( c != pairs.get(top)){
                    return false;
                }
            }
        }
        
        return parans.isEmpty();
    }

    private static final Map<Character, Character> pairs = new HashMap<>();

    static{
        pairs.put('[',']' );
        pairs.put('{','}');
        pairs.put('(',')');
    }

    public static void main(String[] args){
        Solution s = new Solution();

        String str1 = "()[]{}";
        String str2 = "(]";

        assert s.isValid(str1) == true;
        assert s.isValid(str2) == false;
        System.out.println("All tests pass");
    }
}