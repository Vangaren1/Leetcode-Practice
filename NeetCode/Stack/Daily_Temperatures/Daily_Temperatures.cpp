// Daily_Temperatures.cpp
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
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        int n = temperatures.size();
        vector<int> results(n, 0);
        vector<pair<int, int>> stk;
        int tmp, index;
        pair<int, int> tmpPair;
        for (int idx = 0; idx < n; idx++)
        {
            tmp = temperatures[idx];
            if (stk.size() == 0 || stk.back().second > tmp)
            {
                stk.push_back({idx, tmp});
            }
            else
            {
                while (stk.back().second > tmp)
                {
                    tmpPair = stk.back();
                    stk.pop_back();

                    results[tmpPair.first] = idx - tmpPair.first + 1;
                }
            }
            return results;
        }

        return results;
    }
};

int main()
{
    Solution sol;

    vector<int> temperatures = {73, 74, 75, 71, 69, 72, 76, 73};

    vector<int> results = sol.dailyTemperatures(temperatures);

    for (int n : results)
    {
        cout << n << " ";
    }

    return 0;
}
