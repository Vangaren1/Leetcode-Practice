// Diameter_Of_A_Binary_Tree.cpp
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
private:
    int maxFound;

public:
    int diameterOfBinaryTree(TreeNode *root)
    {
        maxFound = 0;
        dfs(root);
        return maxFound;
    }
    int dfs(TreeNode *node)
    {
        if (!node)
        {
            return 0;
        }
        int left = dfs(node->left);
        int right = dfs(node->right);

        maxFound = max(maxFound, left + right);

        return max(left, right) + 1;
    }
};
