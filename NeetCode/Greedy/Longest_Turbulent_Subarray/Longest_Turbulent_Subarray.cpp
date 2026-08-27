// Longest_Turbulent_Subarray.cpp
//
// Compile locally with:
// clang++ Longest_Turbulent_Subarray.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int maxTurbulenceSize(vector<int> &arr)
    {
        int n = arr.size();
        int best = 1;
        int count = 1;

        vector<int> compare;
        for (int index = 1; index < n; index++)
        {
            if (arr[index] > arr[index - 1])
            {
                compare.push_back(1);
            }
            else if (arr[index] < arr[index - 1])
            {
                compare.push_back(-1);
            }
            else
            {
                compare.push_back(0);
            }
        }

        for (int i = 0; i < compare.size(); i++)
        {
            if (compare[i] == 0)
            {
                count = 1;
            }
            else if (i > 0 && compare[i] == -compare[i - 1])
            {
                count++;
            }
            else
            {
                count = 2;
            }
            best = max(best, count);
        }
        return best;
    }
};

int main()
{
    cout << "Running Longest_Turbulent_Subarray.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
