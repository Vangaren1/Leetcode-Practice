// Valid_Parantheses.cpp
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
    bool isValid(string s)
    {
        unordered_map<char, char> parans = {
            {')', '('},
            {'}', '{'},
            {']', '['}};

        unordered_set<char> opn = {'(', '[', '{'};
        vector<char> stk;
        for (char ch : s)
        {
            if (opn.count(ch) > 0)
            {
                stk.push_back(ch);
            }
            else
            {
                if (stk.size() == 0 || parans[ch] != stk.back())
                {
                    return false;
                }
                stk.pop_back();
            }
        }

        return stk.size() == 0;
    }
};
