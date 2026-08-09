// Matchsticks_To_Square.cpp
//
// Compile locally with:
// clang++ Matchsticks_To_Square.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
private:
    int total;
    int target;
    vector<int> sides;

public:
    bool makesquare(vector<int> &matchsticks)
    {
        total = 0;
        for (auto &sticks : matchsticks)
        {
            total += sticks;
        }
        if (total % 4 != 0)
        {
            return false;
        }
        target = total / 4;
        sides = vector<int>(4, 0);
        sort(matchsticks.begin(), matchsticks.end(), greater<int>());
        if (matchsticks[0] > target)
        {
            return false;
        }
        return backtrack(0, matchsticks);
    }
    bool backtrack(int index, vector<int> &matchsticks)
    {
        if (index == matchsticks.size())
        {
            for (auto side : sides)
            {
                if (side != target)
                {
                    return false;
                }
            }
            return true;
        }

        for (int s = 0; s < 4; s++)
        {
            if (s > 0 && sides[s] == sides[s - 1])
            {
                continue;
            }
            if (sides[s] + matchsticks[index] <= target)
            {
                sides[s] += matchsticks[index];
                if (backtrack(index + 1, matchsticks))
                {
                    return true;
                }
                sides[s] -= matchsticks[index];
            }
        }
        return false;
    }
};

int main()
{
    cout << "Running Matchsticks_To_Square.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
