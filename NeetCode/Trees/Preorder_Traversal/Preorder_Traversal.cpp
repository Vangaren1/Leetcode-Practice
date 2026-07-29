// Preorder_Traversal.cpp
//
// Compile locally with:
// clang++ Preorder_Traversal.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    vector<int> preorderTraversal(TreeNode *root)
    {
        vector<int> results;
        dfs(root, results);
        return results;
    }

    void dfs(TreeNode *node, vector<int> &arr)
    {
        if (node)
        {
            arr.push_back(node->val);
            dfs(node->left, arr);
            dfs(node->right, arr);
        }
    }
};

int main()
{
    cout << "Running Preorder_Traversal.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
