// Generate_Paranthese.cpp
//
// Compile locally with:
// clang++ Generate_Paranthese.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<string> generateParenthesis(int n)
    {
        string s = "";
        vector<string> results;
        dfs(s, 0, 0, results, n);
        return results;
    }

    void dfs(string s, int left, int right, vector<string> &results, int n)
    {
        if (s.size() == 2 * n)
        {
            results.push_back(s);
        }

        if (left < n)
        {
            dfs(s + "(", left + 1, right, results, n);
        }
        if (right < left)
        {
            dfs(s + ")", left, right + 1, results, n);
        }
    }
};

int main()
{
    cout << "Running Generate_Paranthese.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
