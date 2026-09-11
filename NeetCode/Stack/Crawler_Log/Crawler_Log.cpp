// Crawler_Log.cpp
//
// Compile locally with:
// clang++ Crawler_Log.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int minOperations(vector<string> &logs)
    {
        int stk = 0;
        for (string &log : logs)
        {
            if (log == "../")
            {
                if (stk)
                {
                    stk--;
                }
                else
                {
                    continue;
                }
            }
            else if (log == "./")
            {
                continue;
            }
            else
            {
                stk++;
            }
        }
        return stk;
    }
};

int main()
{
    cout << "Running Crawler_Log.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
