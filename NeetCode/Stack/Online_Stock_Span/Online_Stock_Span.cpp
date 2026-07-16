// Online_Stock_Span.cpp
//
// Compile locally with:
// clang++ Online_Stock_Span.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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

class StockSpanner
{
private:
    vector<pair<int, int>> stk;

public:
    StockSpanner()
    {
    }

    int next(int price)
    {
        int span = 1;
        while (!stk.empty() && stk.back().first <= price)
        {
            auto tmp = stk.back();
            stk.pop_back();
            span += tmp.second;
        }
        stk.push_back({price, span});
        return span;
    }
};

int main()
{
    cout << "Running Online_Stock_Span.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
