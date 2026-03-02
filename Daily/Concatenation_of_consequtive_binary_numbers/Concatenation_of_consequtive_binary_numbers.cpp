// Concatenation_of_consequtive_binary_numbers.cpp
//
// Compile locally with:
// clang++ Concatenation_of_consequtive_binary_numbers.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int concatenatedBinary(int n)
    {
        const int MOD = 1000000007;
        long long ans = 0;
        int bits = 0;
        for (int i = 1; i <= n; i++)
        {
            if ((i & (i - 1)) == 0)
            {
                bits++;
            }
            ans = ((ans << bits) + i) % MOD;
        }
        return (int)ans;
    }
};

int main()
{
    cout << "Running Concatenation_of_consequtive_binary_numbers.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
