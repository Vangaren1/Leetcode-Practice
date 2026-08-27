// Candy.cpp
//
// Compile locally with:
// clang++ Candy.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int candy(vector<int> &ratings)
    {
        int n = ratings.size();
        vector<int> results(n, 1);
        for (int index = 1; index < n; index++)
        {
            if (ratings[index] > ratings[index - 1])
            {
                results[index] = results[index - 1] + 1;
            }
        }
        for (int i = n - 2; i > -1; i--)
        {
            if (ratings[i] > ratings[i + 1])
            {
                results[i] = max(results[i], results[i + 1] + 1);
            }
        }
        int total = 0;
        for (int j = 0; j < n; j++)
        {
            total += results[j];
        }
        return total;
    }
};

int main()
{
    cout << "Running Candy.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
