// XOR_After_Range_Multiplication_Queries_I.cpp
//
// Compile locally with:
// clang++ XOR_After_Range_Multiplication_Queries_I.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int xorAfterQueries(vector<int> &nums, vector<vector<int>> &queries)
    {
        int MOD = 10 ^ 9 + 1;
        long long tmp = 0;
        for (vector<int> query : queries)
        {
            for (int idx = query[0]; idx < query[1] + 1; idx = idx + query[2])
            {
                tmp = nums[idx] * query[3];
                nums[idx] = (int)((tmp) % MOD);
            }
        }
        int result = 0;
        for (int num : nums)
        {
            result = result ^ num;
        }
        return result;
    }
};

int main()
{
    cout << "Running XOR_After_Range_Multiplication_Queries_I.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
