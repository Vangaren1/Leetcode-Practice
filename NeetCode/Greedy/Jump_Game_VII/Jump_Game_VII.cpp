// Jump_Game_VII.cpp
//
// Compile locally with:
// clang++ Jump_Game_VII.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    bool canReach(string s, int minJump, int maxJump)
    {
        int n = s.size();
        if (s[n - 1] == '1')
        {
            return false;
        }

        deque<int> dq;
        dq.push_back(0);
        int farthest(0), curr(0), start(0), end(0);

        while (!dq.empty())
        {
            curr = dq.front();
            dq.pop_front();
            start = max(curr + minJump, farthest + 1);
            end = min(curr + maxJump, n - 1);
            for (int jump = start; jump < end + 1; jump++)
            {
                if (s[jump] == '0')
                {
                    if (jump == n - 1)
                    {
                        return true;
                    }
                    dq.push_back(jump);
                }
            }
            farthest = max(farthest, end);
        }
        return n == 1;
    }
};

int main()
{
    cout << "Running Jump_Game_VII.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
