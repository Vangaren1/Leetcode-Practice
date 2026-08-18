// Find_The_Judge.cpp
//
// Compile locally with:
// clang++ Find_The_Judge.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int findJudge(int n, vector<vector<int>> &trust)
    {
        vector<int> trusts(n, 0);

        for (auto tmp : trust)
        {
            trusts[tmp[0] - 1]--;
            trusts[tmp[1] - 1]++;
        }
        for (int index = 0; index < n; index++)
        {
            if (trusts[index] == n - 1)
            {
                return index + 1;
            }
        }
        return -1;
    }
};

int main()
{
    cout << "Running Find_The_Judge.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
