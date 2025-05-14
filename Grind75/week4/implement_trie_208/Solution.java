package Grind75.week4.implement_trie_208;

import java.util.*;


class Solution {
    class Trie {
    Map<Character, Trie> letterMap = new HashMap<>();
    boolean wordEnd = false;

    public Trie() {   
    }
    
    public void insert(String word) {
        Trie ptr = this;
        for(char w: word.toCharArray()){
            ptr.letterMap.putIfAbsent(w, new Trie());
            ptr = ptr.letterMap.get(w);
        }
        ptr.wordEnd = true;
    }
    
    public boolean search(String word) {
        Trie ptr = this;
        for(char w: word.toCharArray()){
            ptr = ptr.letterMap.get(w);
            if(ptr == null){
                return false;
            }                
        }
        return ptr.wordEnd;
    }
    
    public boolean startsWith(String prefix) {
        Trie ptr = this;
        for(char p: prefix.toCharArray()){
            ptr = ptr.letterMap.get(p);
            if(ptr == null){
                return false;
            } 
        }
        return true;            
    }
}

/**
* Your Trie object will be instantiated and called as such:
* Trie obj = new Trie();
* obj.insert(word);
* boolean param_2 = obj.search(word);
* boolean param_3 = obj.startsWith(prefix);
*/
    public static void main(String[] args) {
        System.out.println("Running implement_trie_208...");
    }
}
