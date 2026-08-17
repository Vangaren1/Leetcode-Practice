// Bitwise_AND_of_Number_Range.cpp
//
// Compile locally with:
// clang++ Bitwise_AND_of_Number_Range.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int rangeBitwiseAnd(int left, int right)
    {
        int tmp1(left), tmp2(right);
        int lbits = 0;
        while (left > 0)
        {
            lbits++;
            left >>= 1;
        }
        int rbits = 0;
        while (right > 0)
        {
            rbits++;
            right >>= 1;
        }
        left = tmp1;
        right = tmp2;

        int total(0);

        while (lbits >= 0)
        {
            int mask = 1 << rbits;
            rbits--;
            lbits--;
            int lmask = left & mask;
            int rmask = right & mask;
            if (lmask != rmask)
            {
                break;
            }
            total = total | lmask;
        }
        return total;
    }
};

int main()
{
    cout << "Running Bitwise_AND_of_Number_Range.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
