package Grind75.week6.spiral_order_54;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {

    public class Pair{
        public int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if ( this == o) return true;
            if (! (o instanceof Pair) ) return false;
            Pair p = (Pair) o;
            return x == p.x && y == p.y;
        }

        @Override
        public int hashCode() {
            return 31 * x + y;
        }

    }


    public List<Integer> spiralOrder(int[][] matrix) {
        int x = 0;
        int y = 0;
        int dx = 0;
        int dy = 0;
        int height = matrix.length;
        int width = matrix[0].length;
        int remaining = height * width;

        Set<Pair> seen = new HashSet<>();
        List<Pair> directions = new ArrayList<>();
        directions.add(new Pair(1,0));
        directions.add(new Pair(0,1));
        directions.add(new Pair(-1,0));
        directions.add(new Pair(0,-1));
        int dirPos = 0;
        List<Integer> results = new ArrayList<>();

        Pair dir = directions.get(dirPos);

        while (remaining > 0) {
            Pair coord = new Pair(x, y);
            seen.add(coord);
            results.add(matrix[y][x]);
            remaining--;

            dir = directions.get(dirPos);
            x = x + dir.x;
            y = y + dir.y;

            Pair tmp = new Pair(x,y);
            if (seen.contains(tmp) || y == height || y < 0 || x == width || x < 0) {
                x = x - dir.x;
                y = y - dir.y;
                dirPos = dirPos + 1;
                dirPos = dirPos % 4;
                dir = directions.get(dirPos);
                x = x + dir.x;
                y = y + dir.y;
            }

        }

        return results;
    }
    public static void main(String[] args) {
        System.out.println("Running spiral_order_54...");
    }
}
