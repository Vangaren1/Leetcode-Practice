// Compliment_Of_Base_10_Int.cpp
//
// Compile locally with:
// clang++ Compliment_Of_Base_10_Int.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int bitwiseComplement(int n)
    {
        int result = 0;
        int bitLen = 32 - __builtin_clz(n);
        int mask = (1 << bitLen) - 1;

        return mask ^ n;
    }
};

int main()
{
    cout << "Running Compliment_Of_Base_10_Int.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
