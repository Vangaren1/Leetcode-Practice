// Capacity_To_Ship_Packages_Within_D_Days.cpp
//
// Compile locally with:
// clang++ Capacity_To_Ship_Packages_Within_D_Days.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    int shipWithinDays(vector<int> &weights, int days)
    {
        int left = 0;
        int right = 0;
        for (auto &tmp : weights)
        {
            left = max(left, tmp);
            right += tmp;
        }

        int d(1), mid(0), curr(0);
        while (left < right)
        {
            mid = left + (right - left) / 2;
            curr = 0;
            d = 1;
            for (auto &weight : weights)
            {
                if (curr + weight > mid)
                {
                    curr = weight;
                    d++;
                }
                else
                {
                    curr += weight;
                }
            }
            if (d <= days)
            {
                right = mid;
            }
            else
            {
                left = mid + 1;
            }
        }

        return left;
    }
};

int main()
{
    cout << "Running Capacity_To_Ship_Packages_Within_D_Days.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
