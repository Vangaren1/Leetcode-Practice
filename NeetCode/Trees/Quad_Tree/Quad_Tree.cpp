// Quad_Tree.cpp
//
// Compile locally with:
// clang++ Quad_Tree.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
//
// NOTE:
// - Remove main() before submitting to LeetCode.
// - Keep only the class Solution definition.
//

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
    bool val;
    bool isLeaf;
    Node *topLeft;
    Node *topRight;
    Node *bottomLeft;
    Node *bottomRight;

    Node()
    {
        val = false;
        isLeaf = false;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }

    Node(bool _val, bool _isLeaf)
    {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = NULL;
        topRight = NULL;
        bottomLeft = NULL;
        bottomRight = NULL;
    }

    Node(bool _val, bool _isLeaf, Node *_topLeft, Node *_topRight, Node *_bottomLeft, Node *_bottomRight)
    {
        val = _val;
        isLeaf = _isLeaf;
        topLeft = _topLeft;
        topRight = _topRight;
        bottomLeft = _bottomLeft;
        bottomRight = _bottomRight;
    }
};

class Solution
{
public:
    Node *construct(vector<vector<int>> &grid)
    {
        return recursive(grid.size(), 0, 0, grid);
    }

    Node *recursive(int n, int offsetY, int offsetX, vector<vector<int>> &grid)
    {
        if (n == 1)
        {
            return new Node(grid[offsetY][offsetX], true, nullptr, nullptr, nullptr, nullptr);
        }

        int newN = n / 2;
        Node *topleft = recursive(newN, offsetY, offsetX, grid);
        Node *topright = recursive(newN, offsetY, offsetX + newN, grid);
        Node *bottomleft = recursive(newN, offsetY + newN, offsetX, grid);
        Node *bottomright = recursive(newN, offsetY + newN, offsetX + newN, grid);

        if (topleft->isLeaf && topright->isLeaf && bottomleft->isLeaf && bottomright->isLeaf && topleft->val == topright->val && topleft->val == bottomleft->val && topleft->val == bottomright->val)
        {
            bool val = topleft->val;
            delete topleft;
            delete topright;
            delete bottomleft;
            delete bottomright;
            return new Node(val, true, nullptr, nullptr, nullptr, nullptr);
        }

        return new Node(true, false, topleft, topright, bottomleft, bottomright);
    }
};

int main()
{
    cout << "Running Quad_Tree.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
