// Graph_Valid_Tree.cpp
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

class Solution
{
private:
    unordered_map<int, vector<int>> adj;
    unordered_set<int> visited;

public:
    bool validTree(int n, vector<vector<int>> &edges)
    {
        if (edges.size() != (n - 1))
        {
            return false;
        }
        for (vector<int> uv : edges)
        {
            adj[uv[0]].push_back(uv[1]);
            adj[uv[1]].push_back(uv[0]);
        }
        bool check = dfs(0, -1);

        return check && visited.size() == n;
    }

    bool dfs(int v, int parent)
    {
        if (visited.count(v))
        {
            return false;
        }
        visited.insert(v);
        for (int neighbor : adj[v])
        {
            if (neighbor == parent)
            {
                continue;
            }
            if (!dfs(neighbor, v))
            {
                return false;
            }
        }
        return true;
    }
};
