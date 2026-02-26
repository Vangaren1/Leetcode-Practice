// Binary_Gap.cpp
//
// Compile locally with:
// clang++ Binary_Gap.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int binaryGap(int n)
    {
        int count = 0;
        int tmp = 0;
        bool found = false;
        int step = 0;
        for (int i = 0; i < 32; i++)
        {
            tmp = n % 2;
            if (tmp == 1 && !found)
            {
                found = true;
                step++;
            }
            else if (found && tmp == 1)
            {
                count = max(count, step);
                step = 1;
            }
            else if (found)
            {
                step++;
            }
            n >>= 1;
        }

        return count;
    }
};

int main()
{
    cout << "Running Binary_Gap.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
