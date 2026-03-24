// Lowest_Common_Ancestor_In_A_Binary_Search_Tree.cpp
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
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        TreeNode *ptr = root;

        while (ptr)
        {
            if (ptr->val > p->val && ptr->val > q->val)
            {
                ptr = ptr->left;
            }
            else if (ptr->val < p->val && ptr->val < q->val)
            {
                ptr = ptr->right;
            }
            else
            {
                return ptr;
            }
        }

        return root;
    }
};
