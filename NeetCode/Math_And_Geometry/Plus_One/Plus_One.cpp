// Plus_One.cpp
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
    vector<int> plusOne(vector<int> &digits)
    {
        int ptr = digits.size() - 1;
        bool carry = true;
        while (ptr >= 0)
        {
            if (carry)
            {
                digits[ptr]++;
                carry = false;
            }
            if (digits[ptr] == 10)
            {
                digits[ptr] = 0;
                carry = true;
            }
            ptr--;
        }
        if (carry && digits.size() > 0)
        {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
