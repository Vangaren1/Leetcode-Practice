// Merge_Sorted_Arrays.cpp
//
// Compile locally with:
// clang++ Merge_Sorted_Arrays.cpp -std=c++17 -Wall -Wextra -O2 -o run && ./run
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
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        m--;
        n--;
        for (int index = nums1.size(); index >= 0; index--)
        {
            if (m >= 0 && n >= 0)
            {
                if (nums1[m] >= nums2[n])
                {
                    nums1[index] = nums1[m];
                    m--;
                }
                else
                {
                    nums1[index] = nums2[n];
                    n--;
                }
            }
            else
            {
                if (n >= 0)
                {
                    nums1[index] = nums2[n];
                    n--;
                }
            }
        }
    }
};

int main()
{
    cout << "Running Merge_Sorted_Arrays.cpp..." << endl;

    Solution sol;

    // TODO:
    // Add local test calls here

    return 0;
}
