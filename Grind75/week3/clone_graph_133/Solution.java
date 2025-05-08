package Grind75.week3.clone_graph_133;

import common.Node;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public Node cloneGraph(Node node) {
        bfs(node);
        return seen.get(node);
    }

    public Map<Node, Node> seen = new HashMap<>();

    public void bfs(Node node){
        if(!seen.containsKey(node) && node != null){
            seen.put(node, new Node(node.val));
            for(Node tmp: node.neighbors){
                if(!seen.containsKey(tmp)){
                    bfs(tmp);
                }
                Node newTmp = seen.get(tmp);
                seen.get(node).neighbors.add(newTmp);
            }
        }
    }

    public static void main(String[] args) {
        Node a = new Node(1);
        Node b = new Node(2);
        Node c = new Node(3);
        Node d = new Node(4);


        a.neighbors.add(b);
        a.neighbors.add(d);
        b.neighbors.add(a);
        b.neighbors.add(c);
        c.neighbors.add(b);
        c.neighbors.add(d);
        d.neighbors.add(a);
        d.neighbors.add(c);

        Solution s = new Solution();

        Node newNode = s.cloneGraph(a);



        System.out.println("Running clone_graph_133...");
    }
}
