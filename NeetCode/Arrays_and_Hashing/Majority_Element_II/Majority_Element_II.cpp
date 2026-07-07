// Majority_Element_II.cpp
//
// Compile locally with:
// clang++ Majority_Element_II.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    vector<int> majorityElement(vector<int> &nums)
    {
        int cand1(INT32_MIN);
        int cand2(INT32_MIN);
        int count1(0), count2(0);
        for (auto &num : nums)
        {
            if (num == cand1)
            {
                count1++;
            }
            else if (num == cand2)
            {
                count2++;
            }
            else if (count1 == 0)
            {
                cand1 = num;
                count1 = 1;
            }
            else if (count2 == 0)
            {
                cand2 = num;
                count2 = 1;
            }
            else
            {
                count1--;
                count2--;
            }
        }
        vector<int> results;
        int n = nums.size();

        if (cand1 != INT32_MAX)
        {
            int cand1Count = count(nums.begin(), nums.end(), cand1);
            if (cand1Count * 3 > n)
            {
                results.push_back(cand1);
            }
        }

        if (cand2 != INT32_MAX)
        {
            int cand2Count = count(nums.begin(), nums.end(), cand2);
            if (cand2Count * 3 > n)
            {
                results.push_back(cand2);
            }
        }
        return results;
    }
};

int main()
{
    cout << "Running Majority_Element_II.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
