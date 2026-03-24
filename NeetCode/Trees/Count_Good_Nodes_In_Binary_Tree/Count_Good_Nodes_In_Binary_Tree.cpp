// Count_Good_Nodes_In_Binary_Tree.cpp
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
    int goodNodes(TreeNode *root)
    {
        int count = 0;

        pair<TreeNode *, int> tmp = {root, INT_MIN};
        queue<pair<TreeNode *, int>> que;
        que.push(tmp);

        while (!que.empty())
        {
            auto [curr, pathMax] = que.front();
            que.pop();
            if (pathMax <= curr->val)
            {
                count++;
            }
            if (curr->left)
            {
                que.push({curr->left, max(curr->val, pathMax)});
            }
            if (curr->right)
            {
                que.push({curr->right, max(curr->val, pathMax)});
            }
        }
        return count;
    }
};
