// Baseball_Game.cpp
//
// Compile locally with:
// clang++ Baseball_Game.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int calPoints(vector<string> &operations)
    {
        stack<int> stk;
        for (auto &op : operations)
        {
            if (op == "C")
            {
                stk.pop();
            }
            else if (op == "D")
            {
                stk.push(2 * stk.top());
            }
            else if (op == "+")
            {
                int tmp = stk.top();
                stk.pop();
                int tmp2 = tmp + stk.top();
                stk.push(tmp);
                stk.push(tmp2);
            }
            else
            {
                stk.push(stoi(op));
            }
        }
        int total = 0;
        while (!stk.empty())
        {
            total += stk.top();
            stk.pop();
        }
        return total;
    }
};

int main()
{
    cout << "Running Baseball_Game.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
