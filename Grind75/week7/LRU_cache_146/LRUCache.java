package Grind75.week7.LRU_cache_146;

import java.util.HashMap;
import java.util.Map;

class LRUCache {

    class Node {
        int key;
        int val;
        Node left;
        Node right;
        public Node(int key, int val){
            this.key = key;
            this.val = val;
            this.left = null;
            this.right = null;
        }
    }

    int capacity;
    int size;
    Map<Integer, Node> keymap;
    Node LRU; 
    Node MRU;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        size = 0;
        keymap = new HashMap<>();
        LRU = new Node(0, 0);
        MRU = new Node(0,0);
        LRU.right = MRU;
        MRU.left = LRU;
    }
    
    public void insert(Node newVal) {
        keymap.put(newVal.key, newVal);
        newVal.left = MRU.left;
        newVal.right = MRU;
        newVal.left.right = newVal;
        MRU.left = newVal; 
    }

    public void removeLRU() {
        Node tmp = LRU.right;
        keymap.remove(tmp.key);
        if ( LRU.right.right != null ) {
            LRU.right.right.left = LRU;
            LRU.right = LRU.right.right;
            size--;
        }
    }

    public int get(int key) {
        if ( !keymap.containsKey(key) ) {
            return -1;
        }
        Node tmp = keymap.get(key);
        tmp.left.right = tmp.right;
        tmp.right.left = tmp.left;
        insert(tmp);
        return tmp.val;
    }
    
    public void put(int key, int value) {
        if ( keymap.containsKey(key) ) {
            Node tmp = keymap.get(key);
            get(key);
            tmp.val = value;
            return;
        }
        Node tmp = new Node(key, value);
        size++;
        if (size <= capacity) {
            insert(tmp);
        }else {
            removeLRU();
            insert(tmp);
        }
    }

    public static void main(String[] args) {
        LRUCache test = new LRUCache(2);

        test.put(1,2);
        test.put(2,2);
        System.out.println(test.get(2));
        test.put(3,3);
        System.out.println(test.get(1));
        test.put(3,4);
        System.out.println(test.get(3));
    }
}
