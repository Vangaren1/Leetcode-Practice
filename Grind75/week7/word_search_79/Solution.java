package Grind75.week7.word_search_79;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;

import common.Node;

class Solution {

    public class Pair {
        public final int first;
        public final int second;

        public Pair(int first, int second) {
            this.first = first;
            this.second = second;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Pair)) return false;
            Pair p = (Pair) o;
            return this.first == p.first && this.second == p.second;
        }

        @Override
        public int hashCode() {
            return Objects.hash(first, second);
        }
    }

    Map<Character, Set<Pair>> charMap;
    List<Pair> directions = new ArrayList<>();
    Set<Pair> seen;
    int height, width;
    char[][] Board;


    public boolean exist(char[][] board, String word) {
        height = board.length;
        width = board[0].length;
        Board = board.clone();
        charMap = new HashMap<>();
        seen = new HashSet<>();

        directions.add(new Pair(0,1));
        directions.add(new Pair(0,-1));
        directions.add(new Pair(1,0));
        directions.add(new Pair(-1,0));

        for (int y=0; y < height; y++) {
            for ( int x = 0; x < width; x++) {
                char thisChar = board[y][x];
                Pair thisPair = new Pair(y,x);
                if ( charMap.containsKey(thisChar)) {
                    charMap.get(thisChar).add(thisPair);
                } else{
                    Set<Pair> tmpSet = new HashSet<>();
                    tmpSet.add(thisPair);
                    charMap.put(thisChar, tmpSet);
                }
            }
        }
 
        Set<Boolean> exist = new HashSet<>();
        char firstLetter = word.charAt(0);
        char[] restOfTheLetters = word.toCharArray();
        if ( charMap.containsKey(firstLetter)) {
            for ( Pair tmpPair : charMap.get(firstLetter)) {
                seen.add(tmpPair);
                exist.add( bfs(Arrays.copyOfRange(restOfTheLetters, 1, word.length()), tmpPair));
                seen = new HashSet<>();
            }
        }


        return exist.contains(true);
    }

    public boolean bfs(char[] letters, Pair pos ) {

        if ( letters.length == 0){
            return true;
        }

        Set<Boolean> found = new HashSet<>();
        for ( Pair tmp: directions) {
            int ny = pos.first + tmp.first;
            int nx = pos.second + tmp.second;
            Pair newPair = new Pair(ny,nx);
            if (    0 <= ny && 
                    0 <= nx && 
                    ny < height && 
                    nx < width && 
                    Board[ny][nx] == letters[0] && 
                    !seen.contains(newPair)
            ){
                seen.add(newPair);
                boolean result = bfs(Arrays.copyOfRange(letters, 1, letters.length), newPair);
                if ( !result ) {
                    seen.remove(newPair);
                }
                found.add(result);
            }
        }

        return found.contains(true);
    }

    public static void main(String[] args) {
        System.out.println("Running word_search_79...");
    }
}
