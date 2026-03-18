// Remove_Node_from_End_of_List.cpp
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
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode dummy(0);
        dummy.next = head;
        ListNode *first = &dummy, *second = &dummy;

        for (int i = 0; i < n + 1; i++)
        {
            second = second->next;
        }

        while (second)
        {
            first = first->next;
            second = second->next;
        }

        first->next = first->next->next;

        return dummy.next;
    }
};
