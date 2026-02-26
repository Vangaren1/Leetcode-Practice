// Evalutate_Reverse_Polish_Notation.cpp
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

class Solution
{
public:
    int evalRPN(vector<string> &tokens)
    {
        unordered_set<string> oprs = {"+", "-", "*", "/"};
        vector<int> stk;
        int a, b;
        for (string tk : tokens)
        {
            if (!oprs.count(tk))
            {
                stk.push_back(stoi(tk));
                continue;
            }
            a = stk.back();
            stk.pop_back();
            b = stk.back();
            stk.pop_back();

            if (tk == "+")
            {
                stk.push_back(a + b);
            }
            else if (tk == "-")
            {
                stk.push_back(b - a);
            }
            else if (tk == "*")
            {
                stk.push_back(b * a);
            }
            else if (tk == "/")
            {
                stk.push_back(b / a);
            }
        }

        return stk.back();
    }
};
