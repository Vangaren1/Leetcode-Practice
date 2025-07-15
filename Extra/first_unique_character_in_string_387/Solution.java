package Extra.first_unique_character_in_string_387;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int firstUniqChar(String s) {
     
        Map<Character, Integer> count = new HashMap<>();
        Map<Character, Integer> firstPos = new HashMap<>();

        for ( int index = 0; index < s.length(); index++) {
            char curr = s.charAt(index);
            count.merge(curr, 1, Integer::sum);
            if ( !firstPos.containsKey(curr)) {
                firstPos.put(curr, index);
            }
        }

        List<Character> single = new ArrayList<>();
        for ( char c : count.keySet() ) {
            if ( count.get(c) == 1){
                single.add(c);
            }
        }

        if ( single.size() == 0) return -1;

        List<Integer> pos = new ArrayList<>();
        for ( char tmp : single ){
            pos.add(firstPos.get(tmp));
        }

        Collections.sort(pos);

        return pos.get(0);
    }

    public static void main(String[] args) {
        System.out.println("Running first_unique_character_in_string_387...");
    }
}
