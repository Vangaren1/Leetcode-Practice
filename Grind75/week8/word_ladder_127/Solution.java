package Grind75.week8.word_ladder_127;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.HashSet;
import java.util.List;
import java.util.Queue;
import java.util.Set;

class Solution {
    class Node {
        String w;
        int step;

        public Node(String w, int step) {
            this.w = w;
            this.step = step;
        }
    }

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordSet = new HashSet<>(wordList);

        if (!wordSet.contains(endWord))
            return 0;

        if (beginWord.compareTo(endWord) == 0)
            return 0;

        String letters = "abcdefghijklmnopqrstuvwxyz";

        Queue<Node> queue = new ArrayDeque<>();

        queue.add(new Node(beginWord, 1));

        while (!queue.isEmpty()) {
            Node curr = queue.poll();
            int step = curr.step;
            for (int index = 0; index < curr.w.length(); index++) {
                for (char c : letters.toCharArray()) {
                    String tmp = curr.w;
                    tmp = tmp.substring(0, index) + c + tmp.substring(index + 1);
                    if (wordSet.contains(tmp)) {
                        if (tmp.compareTo(endWord) == 0)
                            return step + 1;

                        queue.add(new Node(tmp, step + 1));
                        wordSet.remove(tmp);
                    }

                }
            }
        }

        return 0;
    }

    public static void main(String[] args) {
        System.out.println("Running word_ladder_127...");
    }
}
