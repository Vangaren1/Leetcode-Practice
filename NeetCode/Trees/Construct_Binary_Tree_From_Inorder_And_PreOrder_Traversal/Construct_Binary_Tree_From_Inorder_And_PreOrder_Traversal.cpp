// Construct_Binary_Tree_From_Inorder_And_PreOrder_Traversal.cpp
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
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder)
    {
        unordered_map<int, int> inPos;
        for (int idx = 0; idx < inorder.size(); idx++)
        {
            inPos[inorder[idx]] = idx;
        }
        int prePos = 0;
        return dfs(preorder, inorder, inPos, 0, preorder.size(), prePos);
    }

    TreeNode *dfs(vector<int> &preorder, vector<int> &inorder, unordered_map<int, int> &inpos, int left, int right, int &prePos)
    {
        if (left == right)
        {
            return nullptr;
        }
        TreeNode *tmp = new TreeNode(preorder[prePos]);
        int mid = inpos.at(preorder[prePos]);
        prePos++;

        tmp->left = dfs(preorder, inorder, inpos, left, mid, prePos);
        tmp->right = dfs(preorder, inorder, inpos, mid + 1, right, prePos);

        return tmp;

        return nullptr;
    }
};
