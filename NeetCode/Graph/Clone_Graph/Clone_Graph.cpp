// Clone_Graph.cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;
class Node
{
public:
    int val;
    vector<Node *> neighbors;
    Node()
    {
        val = 0;
        neighbors = vector<Node *>();
    }
    Node(int _val)
    {
        val = _val;
        neighbors = vector<Node *>();
    }
    Node(int _val, vector<Node *> _neighbors)
    {
        val = _val;
        neighbors = _neighbors;
    }
};

class Solution
{
public:
    Node *cloneGraph(Node *node)
    {
        unordered_map<Node *, Node *> nodemap;

        return dfs(node, nodemap);
    }

    Node *dfs(Node *node, unordered_map<Node *, Node *> &nmap)
    {
        if (node == nullptr)
        {
            return nullptr;
        }
        if (nmap.count(node) > 0)
        {
            return nmap[node];
        }
        nmap[node] = new Node(node->val);
        for (Node *tmp : node->neighbors)
        {
            Node *neighbor = dfs(tmp, nmap);
            nmap[node]->neighbors.push_back(neighbor);
        }

        return nmap[node];
    }
};
