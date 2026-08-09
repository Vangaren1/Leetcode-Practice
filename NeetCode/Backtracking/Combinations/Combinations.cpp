// Combinations.cpp
//
// Compile locally with:
// clang++ Combinations.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<vector<int>> combine(int n, int k)
    {
        vector<vector<int>> results;
        vector<int> curr;
        dfs(curr, n, k, 1, results);
        return results;
    }

    void dfs(vector<int> &curr, int n, int k, int index, vector<vector<int>> &results)
    {
        if (curr.size() == k)
        {
            results.push_back(curr);
            return;
        }

        if (index > n)
        {
            return;
        }

        curr.push_back(index);
        dfs(curr, n, k, index + 1, results);
        curr.pop_back();
        dfs(curr, n, k, index + 1, results);
        return;
    }
};

int main()
{
    cout << "Running Combinations.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
