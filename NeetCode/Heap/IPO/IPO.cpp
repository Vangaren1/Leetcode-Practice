// IPO.cpp
//
// Compile locally with:
// clang++ IPO.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int findMaximizedCapital(int k, int w, vector<int> &profits, vector<int> &capital)
    {
        int n = profits.size();
        int currCapital = w;
        vector<pair<int, int>> capProf;

        for (int index = 0; index < n; index++)
        {
            capProf.push_back({capital[index], profits[index]});
        }
        sort(capProf.begin(), capProf.end(), greater<pair<int, int>>());

        priority_queue<int> available;

        for (int i = 0; i < k; i++)
        {
            while (!capProf.empty() && capProf.back().first <= currCapital)
            {
                available.push(capProf.back().second);
                capProf.pop_back();
            }
            if (!available.empty())
            {
                currCapital += available.top();
                available.pop();
            }
        }
        return currCapital;
    }
};

int main()
{
    cout << "Running IPO.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
