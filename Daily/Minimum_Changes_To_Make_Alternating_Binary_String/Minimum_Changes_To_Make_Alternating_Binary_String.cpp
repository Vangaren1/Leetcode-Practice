// Minimum_Changes_To_Make_Alternating_Binary_String.cpp
//
// Compile locally with:
// clang++ Minimum_Changes_To_Make_Alternating_Binary_String.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class Solution
{
public:
    int minOperations(string s)
    {
        int total{0}, zeroStart{0}, oneStart{0};
        bool startZero{true};

        for (char ch : s)
        {
            if (startZero)
            {
                if (ch == '0')
                {
                    oneStart++;
                }
                else
                {
                    zeroStart++;
                }
            }
            else
            {
                if (ch == '0')
                {
                    zeroStart++;
                }
                else
                {
                    oneStart++;
                }
            }
            startZero = !startZero;
            total = min(zeroStart, oneStart);
        }

        return total;
    }
};

int main()
{
    cout << "Running Minimum_Changes_To_Make_Alternating_Binary_String.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
