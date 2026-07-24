// Sqrt_X.cpp
//
// Compile locally with:
// clang++ Sqrt_X.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int mySqrt(int x)
    {
        if (x < 2)
        {
            return x;
        }

        int left(1);
        long long curr(0), cnext(0);
        int right = x / 2;
        long long mid = left + (right - left) / 2;
        while (left < right)
        {
            curr = mid * mid;
            if (curr == x)
            {
                return mid;
            }
            cnext = (mid + 1) * (mid + 1);
            if (cnext == x)
            {
                return mid + 1;
            }
            if (curr < x)
            {
                if (cnext > x)
                {
                    return mid;
                }
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
            mid = left + (right - left) / 2;
        }
        return mid;
    }
};

int main()
{
    cout << "Running Sqrt_X.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
