// Delete_Leaves_With_Given_Value.cpp
//
// Compile locally with:
// clang++ Delete_Leaves_With_Given_Value.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    TreeNode *removeLeafNodes(TreeNode *root, int target)
    {
        if (root == nullptr)
        {
            return nullptr;
        }

        root->left = removeLeafNodes(root->left, target);
        root->right = removeLeafNodes(root->right, target);

        if (root->val != target)
        {
            return root;
        }
        if (root->val == target && root->left == nullptr && root->right == nullptr)
        {
            return nullptr;
        }

        return root;
    }
};

int main()
{
    cout << "Running Delete_Leaves_With_Given_Value.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
