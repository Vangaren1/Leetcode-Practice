// Valid_Binary_Search_Tree.cpp
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
    bool isValidBST(TreeNode *root)
    {
        return dfs(root, LLONG_MIN, LLONG_MAX);
    }

    bool dfs(TreeNode *node, long long minimum, long long maximum)
    {
        if (!node)
        {
            return true;
        }
        if (node->val >= minimum || node->val >= maximum)
        {
            return false;
        }
        return dfs(node->left, minimum, node->val) && dfs(node->right, node->val, maximum);
    }
};
