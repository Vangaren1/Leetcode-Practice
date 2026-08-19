// Insert_GCD_Linked_List.cpp
//
// Compile locally with:
// clang++ Insert_GCD_Linked_List.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *insertGreatestCommonDivisors(ListNode *head)
    {
        ListNode *ptr = head;
        while (ptr && ptr->next)
        {
            ListNode *tmp = ptr->next;
            ptr->next = new ListNode(gcd(ptr->val, ptr->next->val), tmp);
            ptr = ptr->next->next;
        }
        return head;
    }
};

int main()
{
    cout << "Running Insert_GCD_Linked_List.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
