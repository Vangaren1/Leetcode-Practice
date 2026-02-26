// Minimum_Stack.cpp
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

class MinStack
{
private:
    vector<pair<int, int>> stk;

public:
    MinStack()
    {
    }

    void push(int val)
    {
        if (stk.size() > 0)
        {
            int t = getMin();
            stk.push_back({val, min(val, t)});
        }
        else
        {
            stk.push_back({val, val});
        }
    }

    void pop()
    {
        if (stk.size() > 0)
        {
            stk.pop_back();
        }
    }

    int top()
    {
        pair<int, int> tmp = stk.back();
        return tmp.first;
    }

    int getMin()
    {
        pair<int, int> tmp = stk.back();
        return tmp.second;
    }
};
