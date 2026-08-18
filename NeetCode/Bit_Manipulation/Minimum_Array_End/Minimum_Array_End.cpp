// Minimum_Array_End.cpp
//
// Compile locally with:
// clang++ Minimum_Array_End.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    long long minEnd(int n, int x)
    {
        long long k = static_cast<long long>(n) - 1;
        long long xmask(1), kmask(1), result(0), currX(0), currK(0);
        int xBits(0), tmpX(x), kBits(0), tmpK(k);
        while (tmpX)
        {
            xBits++;
            tmpX = tmpX >> 1;
        }
        while (tmpK)
        {
            kBits++;
            tmpK = tmpK >> 1;
        }
        int totalbits = xBits + kBits;
        for (int bit = 0; bit < totalbits; bit++)
        {
            currX = x & xmask;
            currK = k & kmask;

            if (currX == 0)
            {
                result = result | currK;
            }
            else
            {
                result = result | currX;
                k = k << 1;
            }
            kmask = kmask << 1;
            xmask = xmask << 1;
        }
        return result;
    }
};

int main()
{
    cout << "Running Minimum_Array_End.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
