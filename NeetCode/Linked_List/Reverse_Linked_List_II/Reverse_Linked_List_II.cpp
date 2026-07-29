// Reverse_Linked_List_II.cpp
//
// Compile locally with:
// clang++ Reverse_Linked_List_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        ListNode *front = new ListNode(0);
        front->next = head;

        ListNode *first = front;
        for (int i = 0; i < left - 1; i++)
        {
            first = first->next;
        }

        ListNode *second = first;
        for (int j = 0; j < right - left + 1; j++)
        {
            second = second->next;
        }

        ListNode *end = second->next;
        ListNode *ptr1 = first->next;
        ListNode *ptr2 = ptr1->next;
        ListNode *tmp;
        ptr1->next = end;

        while (ptr2 != end)
        {
            tmp = ptr2->next;
            ptr2->next = ptr1;
            ptr1 = ptr2;
            ptr2 = tmp;
        }
        first->next = ptr1;
        return front->next;
    }
};

int main()
{
    cout << "Running Reverse_Linked_List_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
