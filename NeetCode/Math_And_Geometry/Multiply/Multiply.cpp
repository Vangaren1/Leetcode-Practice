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
        // make sure that num1 is shorter than num2
        if (num1.size() > num2.size())
        {
            swap(num1, num2);
        }

        vector<int> result;
        int carry = 0;
        for (int i = 0; i < num1.size(); i++)
        {
            int n1 = (int)(num1[i] - '0');
            carry = 0;
            for (int j = 0; j < num2.size(); j++)
            {
                if (i + j + 1 > result.size())
                {
                    result.push_back(0);
                }
                int n2 = (int)(num2[j] - '0');
                int prod = n1 * n2;
                carry = prod / 10;
                result[i + j] = result[i + j] + carry + (prod % 10);
            }
        }
        reverse(result.begin(), result.end());

        string s = "";
        for (int k : result)
        {
            s = s + (char)(k + '0');
        }
        return s;
    }
};
