// House_Robber_III.cpp
//
// Compile locally with:
// clang++ House_Robber_III.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int rob(TreeNode *root)
    {
        pair<int, int> results = dfs(root);
        return max({results.first, results.second});
    }
    pair<int, int> dfs(TreeNode *node)
    {
        if (node == nullptr)
        {
            return {0, 0};
        }

        pair<int, int> left = dfs(node->left);
        pair<int, int> right = dfs(node->right);

        int canRob = node->val + left.second + right.second;
        int cantRob = max({left.first, left.second}) + max({right.first, right.second});
        return {canRob, cantRob};
    }
};

int main()
{
    cout << "Running House_Robber_III.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
