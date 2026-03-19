// Reverse_Nodes_In_K-Group.cpp
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
    ListNode *reverseKGroup(ListNode *head, int k)
    {
        ListNode dummy(0);
        dummy.next = head;
        ListNode *ptr = &dummy;

        // if an empty list, just return it
        if (dummy.next == nullptr)
        {
            return head;
        }
        // attempt to move ptr forward 3 times
        int cnt = 0;
        for (int i = 0; i < k; i++)
        {
            ptr = ptr->next;
            if (ptr == nullptr)
            {
                break;
            }
            cnt++;
        }
        // if couldn't get to the end, then the list is too short, return the head
        if (cnt != k)
        {
            return head;
        }

        // if the cnt reached 3, then we can process
        ListNode *tmp1 = ptr->next;
        ListNode *tmp2 = dummy.next;
        ptr->next = nullptr;
        dummy.next = reverseList(dummy.next);
        tmp2->next = reverseKGroup(tmp1, k);

        return dummy.next;
    }

    ListNode *reverseList(ListNode *head)
    {

        ListNode *curr = head;
        ListNode *prev = nullptr;
        ListNode *next = nullptr;

        while (curr != nullptr)
        {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
};
