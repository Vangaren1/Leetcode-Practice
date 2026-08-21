// Dota2_Senate.cpp
//
// Compile locally with:
// clang++ Dota2_Senate.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    string predictPartyVictory(string senate)
    {
        deque<int> rq;
        deque<int> dq;
        int n = senate.size();

        for (int i = 0; i < n; i++)
        {
            if (senate[i] == 'R')
            {
                rq.push_back(i);
            }
            else
            {
                dq.push_back(i);
            }
        }

        while (!rq.empty() && !dq.empty())
        {
            int r = rq.front();
            rq.pop_front();
            int d = dq.front();
            dq.pop_front();

            if (r < d)
            {
                rq.push_back(r + n);
            }
            else
            {
                dq.push_back(d + n);
            }
        }
        if (!rq.empty())
        {
            return "Radiant";
        }
        return "Dire";
    }
};

int main()
{
    cout << "Running Dota2_Senate.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
