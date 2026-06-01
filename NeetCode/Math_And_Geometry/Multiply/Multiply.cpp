// Multiply.cpp
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
    string multiply(string num1, string num2)
    {
        long long one = convert(num1);
        long long two = convert(num2);
        long long product = one * two;

        string result = "";
        if (product == 0)
        {
            return "0";
        }
        while (product)
        {
            result = result + (char)(product % 10 + '0');
            product = product / 10;
        }
        reverse(result.begin(), result.end());
        return result;
    }
    long long convert(string num)
    {
        long long total = 0;
        int tens = 1;
        for (int ptr = num.size() - 1; ptr >= 0; ptr--)
        {
            int digit = (char)num[ptr] - '0';
            total = total + (digit * tens);
            tens = tens * 10;
        }
        return total;
    }
};
