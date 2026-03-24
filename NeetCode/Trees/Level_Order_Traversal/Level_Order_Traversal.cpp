// Level_Order_Traversal.cpp
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
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        vector<vector<int>> results;

        if (!root)
        {
            return results;
        }

        queue<TreeNode *> nodeQ;

        nodeQ.push(root);

        while (!nodeQ.empty())
        {
            int tmpSize = nodeQ.size();

            vector<int> level;

            for (int i = 0; i < tmpSize; i++)
            {
                TreeNode *tmp = nodeQ.front();
                nodeQ.pop();

                level.push_back(tmp->val);
                if (tmp->left)
                {
                    nodeQ.push(tmp->left);
                }
                if (tmp->right)
                {
                    nodeQ.push(tmp->right);
                }
            }
            results.push_back(level);
        }

        return results;
    }
};

/*
// DFS solution without a member variable
class Solution
{
public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        vector<vector<int>> results;
        traverse(root, results, 0);
        return results;
    }

    void traverse(TreeNode *node, vector<vector<int>> &rList, int level)
    {
        if (!node)
        {
            return;
        }

        if (rList.size() < level + 1)
        {
            rList.push_back({node->val});
        }
        else
        {
            rList[level].push_back(node->val);
        }

        traverse(node->left, rList, level + 1);
        traverse(node->right, rList, level + 1);
    }
};
*/

/*
// DFS solution with results as a member variable

class Solution
{
private:
    vector<vector<int>> results;

public:
    vector<vector<int>> levelOrder(TreeNode *root)
    {
        traverse(root, 0);
    }

    void traverse(TreeNode *node, int level)
    {
        if (!node)
        {
            return;
        }

        if (results.size() < level)
        {
            results.push_back({node->val});
        }
        else
        {
            results[level].push_back(node->val);
        }

        traverse(node->left, level + 1);
        traverse(node->right, level + 1);
    }
};

*/