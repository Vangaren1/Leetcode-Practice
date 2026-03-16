// Copy_Linked_List_with_Random_Pointer.cpp
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
class Node
{
public:
    int val;
    Node *next;
    Node *random;

    Node(int _val)
    {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
class Solution
{
public:
    Node *copyRandomList(Node *head)
    {
        unordered_map<Node *, Node *> oldToNew;

        Node *ptr = head, *tmp;
        while (ptr)
        {
            tmp = new Node(ptr->val);
            oldToNew[ptr] = tmp;
            ptr = ptr->next;
        }

        ptr = head;

        while (ptr)
        {
            oldToNew[ptr]->next = oldToNew[ptr->next];
            oldToNew[ptr]->random = oldToNew[ptr->random];
            ptr = ptr->next;
        }
        return oldToNew[head];
    }
};
