// Tribonaci.cpp
//
// Compile locally with:
// clang++ Tribonaci.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int tribonacci(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        if (n == 1 || n == 2)
        {
            return 1;
        }

        vector<int> tri(n + 1, 0);
        tri[1] = 1;
        tri[2] = 1;
        for (int index = 3; index < n + 1; index++)
        {
            tri[index] = tri[index - 1] + tri[index - 2] + tri[index - 3];
        }
        return tri[n];
    }
};

int main()
{
    cout << "Running Tribonaci.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
